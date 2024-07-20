#!/usr/bin/env python3

import sys
from utils import DelayTimes
from kit import Kit
from iZgenKits import modeNames, Notes, roots, modes, GenericNotes
from kits.generic import Generic
from sysConfig import SystemConfig
import os
import json
import serial  # sudo pip install pyserial
import time
from random import randint


if len(sys.argv) < 2:
    print("upload.py <key> [<tempo>] [<apply-master-fx-to>] [<delay-subdivision>] [<allow-fx-mod>]")
    print("eg upload.py F# 83 kit")
    print("or upload.py C 110 in intra")
    print("or upload.py Bb 150 in poly 1")
    print("or upload.py A")
    print("or upload.py gen 101 in poly")
    print("or upload.py tbb")
    exit()

key = sys.argv[1]


class Generic2019(Generic):
    def createIn(self, loc, idxStart):
        idx = idxStart
        for modeName in modeNames:
            notes = Notes(7, roots[key], modes[modeName])
            name = "%s_%s" % (key, modeName)
            kitDef = self._createKit(name, notes, self.kitFx1, self.kitFx2, self.c)
            Kit().buildNamed(kitDef, os.path.join(loc, "KIT"), idx)
            idx += 1


class Generic2024(Generic):
    def createIn(self, loc, idxStart):
        for i in range(10):
            kitDef = self._createKit("gen_%02d" % i, GenericNotes(), self.kitFx1, self.kitFx2, self.c)
            Kit().buildNamed(kitDef, os.path.join(loc, "KIT"), idxStart + i)


class Uploader:
    @staticmethod
    def config():
        with open("config.json") as conf:
            return json.load(conf)

    def __init__(self):
        self.mediaLoc = Uploader.config()["mediaLoc"]
        self.serialLoc = Uploader.config()["serialLoc"]
        self.loc = os.path.join(self.mediaLoc, "Roland", "SPD-SX")
        self.sp = None
        if os.path.exists(self.serialLoc):
            self.sp = serial.Serial(self.serialLoc)

    def upload(self, kits, idxStart, delayTimes = None):
        isSpdSx = "/media" in self.mediaLoc
        if isSpdSx and self.sp is not None:
            self.sp.setDTR(True)
            while not os.path.exists(self.loc):
                time.sleep(0.1)

        c = SystemConfig(delayTimes)
        kits.applySysConfigTo(c)
        c.createIn(os.path.join(self.loc, "SYSTEM", "sysparam.spd"))
        kits.createIn(self.loc, idxStart)

        if isSpdSx and self.sp is not None:
            os.system("umount %s" % self.mediaLoc)
            self.sp.setDTR(False)


uploader = Uploader()

if key == "tbb":
    from kits.bandSet import Tbb
    uploader.upload(Tbb(), 49)

elif key == "mab":
    from kits.bandSet import BandSet
    uploader.upload(BandSet("mab_2022.json", key), 65)

elif ".json" in key:
    from kits.bandSet import BandSet
    actName = key.split("_")[0]
    uploader.upload(BandSet(key, actName), 69)

else:
    tempo = int(sys.argv[2]) if len(sys.argv) > 2 else randint(46, 119)
    delaySubdivision = sys.argv[4] if len(sys.argv) > 4 else "intra"
    dt = DelayTimes(tempo, delaySubdivision == "intra")
    print("tempo %d bpm" % tempo)
    print("%s ms %s%%" % (dt.time, dt.leftTap))
    if key == "gen":
        uploader.upload(Generic2024(tempo), 49, dt)
    else:
        uploader.upload(Generic2019(tempo), 69, dt)

