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
    def __init__(self, size):
        self.size = size
        self.clear()
        
    def clear(self):
        self.values = []
        self.avg = 0.0

    def add(self, v):
        self.avg += (abs(v) * 1.0 / self.size)
        self.values.append(v)
        if (len(self.values) > self.size):
            p = self.values.pop(0)
            self.avg -= (abs(p) * 1.0 / self.size)

    def first(self):
        return self.values[0]

    
class ReadAudio():

    def __init__(self, dirOut):
        self.movingAvg5 = RMSn(5)
        self.movingAvg30 = RMSn(30)
        self.state = 0
        self.out = None
        self.fn = 0
        self.dirOut = dirOut
        
    def readOneSample(self, i, v):
        self.movingAvg5.add(v)
        self.movingAvg30.add(v)
        
        if (self.state == 2):
            self.movingAvg5.clear()
            self.movingAvg30.clear()
            self.state = 0
        
        if (self.state == 1 and self.movingAvg30.avg < 0.003):
            print("ending sample at %d at %d" % (self.fn, i))
            self.state = 2
            self.out.close()
            self.out = None
            self.fn += 1

        if (self.state == 0 and abs(v - self.movingAvg5.avg) > 0.25):
            print("beginning sample %d at %d" % (self.fn, i))
            self.out = sf.SoundFile("%s/shortSample%03d.wav" % (self.dirOut, self.fn), mode="x", samplerate=44100, channels=1, subtype="PCM_16")
            self.state = 1
            
        if (self.state == 1): 
            self.out.write(self.movingAvg5.first())
        

    def read(self, fqfn):
        with sf.SoundFile(fqfn, "r+") as f:
            print("%d frames" % f.frames)
            i = 0
            while (f.tell() < f.frames):
                v = f.read(1)[0]
                self.readOneSample(i, v)

                i += 1
            
            f.close()
            
if (True):
    ReadAudio(sys.argv[2]).read(sys.argv[1])
