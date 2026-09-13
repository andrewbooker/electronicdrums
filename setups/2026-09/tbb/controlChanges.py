import sys
import time
import threading
import random
import readchar
import math


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


class Writer:
    def __init__(self, writeTo):
        self.writeTo = writeTo

    def start(self, shouldStop):
        while not shouldStop.is_set():
            for i in range(4):
                self.writeTo.write(i, random.random());
                time.sleep(random.random())

hb = HorizBar()
procs = [
    hb,
    Writer(hb)
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
