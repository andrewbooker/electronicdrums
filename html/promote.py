#!/usr/bin/env python3

import sys
import os
import json
import shutil
import serial
import time


def config():
    with open("../py/config.json") as conf:
        return json.load(conf)


class Remote:
    def __init__(self, serialLoc, toDir):
        self.sp = None
        self.connected = False
        self.toDir = toDir
        self.sp = serial.Serial(serialLoc)

    def __del__(self):
        if self.connected:
            print("disconnecting")
            os.system("umount %s" % self.toDir)
            while os.path.exists(self.toDir):
                time.sleep(0.1)
            self.sp.setDTR(False)
        self.connected = False
        print("done")

    def connect(self):
        if not self.connected:
            print("connecting")
            self.sp.setDTR(True)
            while not os.path.exists(self.toDir):
                time.sleep(0.1)
            self.connected = True

    def cp(self, what, to):
        self.connect()
        td = os.path.dirname(to)
        if not os.path.exists(td):
            print("creating", td)
            os.makedirs(td)
        shutil.copy(what, to)


conf = config()
fromDir = sys.argv[1]
centile = sys.argv[2]
toDir = os.path.join(conf["mediaLoc"], "Roland", "SPD-SX", "WAVE")
serialLoc = conf["serialLoc"]
if not os.path.exists(serialLoc):
    print("no serial port specified")
    exit(1)

blocks = ["DATA", "PRM"]
remote = Remote(serialLoc, toDir)
print("writing to", toDir)

for b in blocks:
    d = os.path.join(fromDir, b, centile)
    print("in", d)
    for f in os.listdir(d):
        nf = os.path.join(d, f)
        tf = f"{toDir}/{b}/{centile}/{f}"
        print("copying", nf, "to", tf)
        remote.cp(nf, tf)
