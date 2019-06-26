#!/usr/bin/env python

#pip install soundfile
#pip install sounddevice
#pip install numpy

import queue
import sounddevice as sd
import soundfile as sf
import numpy

import datetime
import time
import sys
import os
import threading
import keyboard
import math



class Callback():
    def __init__(self):
        self.q = queue.Queue()
    
    def make(self):
        def handle(indata, frames, time, status):
            #This is called (from a separate thread) for each audio block.
            if status:
                print(status, sys.stderr)
            self.q.put(indata.copy())
        return handle

class RecordAudio():

    def __init__(self, loc, dev):
        self.loc = loc
        self.dev = dev
        self.cb = Callback()
    
    def start(self, shouldStop):
        with sf.SoundFile("%s/audio_%s.wav" % (self.loc, self.dev), mode="x", samplerate=44100, channels=1, subtype="PCM_24") as file:
            with sd.InputStream(samplerate=44100.0, device=self.dev, channels=1, callback=self.cb.make()):
                while not shouldStop.is_set():
                    file.write(self.cb.q.get())
                    
                print("stopping audio %s" % self.dev)


if (False):
    now = time.time()    
    fqp = "%s/recording/%s" % (sys.argv[1], datetime.datetime.fromtimestamp(now).strftime("%Y-%m-%d/%Y-%m-%d_%H%M%S"))
    if not os.path.exists(fqp):
        os.makedirs(fqp)
        
    shouldStop = threading.Event()

    audio0 = RecordAudio(fqp, 1) #3 : mic on linux box headphones
    ta0 = threading.Thread(target=audio0.start, args=(shouldStop,), daemon=True)

    print("starting recording to %s" % fqp)
    ta0.start()

    keyboard.wait("q")
    print ("stopping...")
    shouldStop.set()
    ta0.join()
    print("done")
    
    

class RMSn():
    size = 10

    def __init__(self):
        self.values = []
        self.avg = 0.0

    def add(self, v):
        self.avg += (abs(v) * 1.0 / RMSn.size)
        self.values.append(v)
        if (len(self.values) > 5):
            p = self.values.pop(0)
            self.avg -= (abs(p) * 1.0 / RMSn.size)

    def first(self):
        return self.values[0]

    
class ReadAudio():

    def __init__(self):
        self.movingAvg = RMSn()
        self.state = 0

    def read(self, fqfn, dirOut):
        with sf.SoundFile(fqfn, "r+") as f:
            with sf.SoundFile("%s/sample_e.wav" % dirOut, mode="x", samplerate=44100, channels=1, subtype="PCM_16") as out:
                print("%d frames" % f.frames)
                i = 0
                while (f.tell() < f.frames and self.state < 2):
                    data = f.read(1)
                    self.movingAvg.add(data[0])
                    if (self.movingAvg.avg > (0.1 if self.state == 0 else 0.005)):
                        if self.state == 0:
                            print("beginning sample at %d" % i)
                        self.state = 1
                        v = self.movingAvg.first()
                        out.write(v)
                    else:
                        if self.state == 1:
                            print("ending sample at %d" % i)
                        self.state = 2 if self.state == 1 else 0
                    i += 1
                out.close()
            f.close()
            
if (True):
    ReadAudio().read(sys.argv[1], sys.argv[2])
