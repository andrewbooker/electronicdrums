#!/usr/bin/env python3

import sys
import time
import threading
import random
import readchar
import math
import mido


portNames = mido.get_output_names()
portName = portNames[1]
outport = mido.open_output(portName)


width = 20


class HorizBar:
    def __init__(self):
        self.matrix = [[" "] * width for _ in range(4)]

    def start(self, shouldStop):
        while not shouldStop.is_set():
            sys.stdout.write("\x1b[A" * (len(self.matrix) + 1))
            sys.stdout.flush()
            for m in self.matrix:
                s = "".join(m)
                sys.stdout.write(f"{s}")
                print()

            
            time.sleep(0.02)

    def write(self, idx, valZeroToOne):
        p = math.floor(width * valZeroToOne)
        self.matrix[idx] = [" "] * width
        self.matrix[idx][p] = "|"


class ControlChangeSender:
    def __init__(self, channel, number, midiOut, freq, renderer, idx):
        self.channel = channel
        self.number = number
        self.midiOut = midiOut
        self.freq = freq
        self.renderer = renderer
        self.idx = idx

    def start(self, shouldStop):
        start_time = time.monotonic()
        interval = 0.2
        while not shouldStop.is_set():
            elapsed = time.monotonic() - start_time
            v = math.sin(2 * math.pi * self.freq * elapsed)
            outport.send(mido.Message("control_change", channel=self.channel, control=self.number, value=math.floor(56 * (1.0 + v))))
            self.renderer.write(self.idx, v)
            next_time = start_time + (int(elapsed / interval) + 1) * interval
            time.sleep(max(0, next_time - time.monotonic()))


hb = HorizBar()
procs = [
    ControlChangeSender(0, 12, outport, 0.2, hb, 0),
    ControlChangeSender(0, 13, outport, 1.8, hb, 1),
    ControlChangeSender(13, 12, outport, 0.5, hb, 2),
    ControlChangeSender(13, 13, outport, 2.7, hb, 3),
    hb
]

shouldStop = threading.Event()
threads = [threading.Thread(target=p.start, args=(shouldStop,), daemon=True) for p in procs]
[t.start() for t in threads]
done = False

print("Started. Press 'q' to exit")
while not done:
    c = readchar.readchar()
    if c == "q":
        done = True
        shouldStop.set()
        [t.join() for t in threads]

print()
