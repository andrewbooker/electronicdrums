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


now = time.time()    
fqp = "%s/recording/%s" % (sys.argv[1], datetime.datetime.fromtimestamp(now).strftime("%Y-%m-%d/%Y-%m-%d_%H%M%S"))
if not os.path.exists(fqp):
    os.makedirs(fqp)
    
shouldStop = threading.Event()

audio0 = RecordAudio(fqp, 3) #3 : mic on linux box headphones
ta0 = threading.Thread(target=audio0.start, args=(shouldStop,), daemon=True)

print("starting recording to %s" % fqp)
ta0.start()

keyboard.wait("q")
print ("stopping...")
shouldStop.set()
ta0.join()
print("done")
