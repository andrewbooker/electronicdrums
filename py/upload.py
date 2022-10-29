#!/usr/bin/env python

import sys
from utils import any, DelayTimes
from kit import Kit
from iZgenKits import generate, modeNames, Notes, roots, modes, GenericNotes
from sysConfig import SystemConfig
from effects import *
from random import randint

import os



master = 0
sub = 1

if (len(sys.argv) < 2):
    print("upload.py <key> [<tempo>] [<apply-master-fx-to>] [<delay-subdivision>] [<allow-fx-mod>]")
    print("eg upload.py F# 83 kit")
    print("or upload.py C 110 in intra")
    print("or upload.py Bb 150 in poly 1")
    print("or upload.py A")
    print("or upload.py gen 101 in poly")
    exit()

class FxIn():
    inputAssign = master
    allowedFx = [Slicer, TapeEcho, TouchWah]

class FxKit():
    inputAssign = sub
    allowedFx = [RingMod, Phaser, FilterPlusDrive, Distortion, TouchWah, PitchShift, Vibrato, Reverb, Slicer]


effModes = {"kit": FxKit, "in": FxIn}

key = sys.argv[1]
tempo = randint(46, 119) if (len(sys.argv) < 3) else int(sys.argv[2])
mode = FxIn if len(sys.argv) < 4 else effModes[sys.argv[3]]
delaySubdivision = "intra" if len(sys.argv) < 5 else sys.argv[4]
allowFxMod = 1 if len(sys.argv) < 6 else int(sys.argv[5])



dt = DelayTimes(tempo, delaySubdivision == "intra")
print("tempo %d bpm" % tempo)
print("%s ms %s%%" % (dt.time, dt.leftTap))


class Generic():
    def applySysConfigTo(self, c):
        self.c = c
        masterFx = any(mode.allowedFx)

        c.inAssign = mode.inputAssign
        c.fxModOn = allowFxMod
        c.masterFx = masterFx.createRandom()
        self.kitFx1 = Thru
        self.kitFx2 = any(FxKit.allowedFx, [masterFx])
        if (c.fx1On() == 1):
            self.kitFx1 = any(FxKit.allowedFx, [masterFx, self.kitFx2])

        print("master %s %s%s" % (mode.__name__, masterFx.__name__, " allowing FX mod" if allowFxMod == 1 else ""))
        print("FX1 %s" % self.kitFx1.__name__)
        print("FX2 %s" % self.kitFx2.__name__)

    def _createKit(self, name, notes, kitFx1, kitFx2, sysConfig):
        kitDef = generate(name, tempo, notes)
        kitDef.pan = 0

        kitDef.fx1 = kitFx1.createRandom() if sysConfig.fx1On() == 1 else kitFx1()
        kitDef.fx2 = kitFx2.createRandom()

        # assign all sounds using c.kitAssign() and c.fx1On()
        padOutMaster = 0
        padOutFx1 = 1
        padOutFx2 = 2
        padOutSub = 3

        topKitOut = padOutFx1 if (sysConfig.fx1On() == 1) else padOutFx2
        tunedMidiPercOut = padOutMaster if (sysConfig.inAssign == sub) else topKitOut
        midKitOut = padOutFx2
        bdOut = padOutSub # allow padOutFx2 if not RingMod

        kitDef.pads[0]["outAssign"] = tunedMidiPercOut
        kitDef.pads[1]["outAssign"] = tunedMidiPercOut
        kitDef.pads[2]["outAssign"] = tunedMidiPercOut
        kitDef.pads[3]["outAssign"] = topKitOut
        kitDef.pads[4]["outAssign"] = tunedMidiPercOut
        kitDef.pads[5]["outAssign"] = tunedMidiPercOut
        kitDef.pads[6]["outAssign"] = midKitOut
        kitDef.pads[7]["outAssign"] = tunedMidiPercOut
        kitDef.pads[8]["outAssign"] = tunedMidiPercOut
        kitDef.pads[9]["outAssign"] = midKitOut
        kitDef.pads[10]["outAssign"] = midKitOut
        kitDef.pads[11]["outAssign"] = midKitOut
        kitDef.pads[12]["outAssign"] = topKitOut
        return kitDef

    def createIn(self, loc, idxStart):
        pass

class Generic_2019(Generic):
    def createIn(self, loc, idxStart):
        idx = idxStart
        for modeName in modeNames:
            notes = Notes(7, roots[key], modes[modeName])
            name = "%s_%s" % (key, modeName)
            kitDef = self._createKit(name, notes, self.kitFx1, self.kitFx2, self.c)
            Kit().buildNamed(kitDef, os.path.join(loc, "KIT"), idx)
            idx += 1

class Generic_2022(Generic):
    def createIn(self, loc, idxStart):
        for i in range(10):
            kitDef = self._createKit("gen_%02d" % i, GenericNotes(), self.kitFx1, self.kitFx2, self.c)
            Kit().buildNamed(kitDef, os.path.join(loc, "KIT"), idxStart + i)


import json
import serial ## sudo pip install pyserial
import time

class Uploader():
    @staticmethod
    def config():
        with open("config.json") as conf:
            return json.load(conf)

    def __init__(self):
        self.mediaLoc = Uploader.config()["mediaLoc"]
        self.loc = os.path.join(self.mediaLoc, "Roland", "SPD-SX")

    def upload(self, kits, idxStart):
        sp = serial.Serial("/dev/ttyUSB0")
        sp.setDTR(True)
        while not os.path.exists(self.loc):
            time.sleep(0.1)

        c = SystemConfig(dt)
        kits.applySysConfigTo(c)
        c.createIn(os.path.join(self.loc, "SYSTEM", "sysparam.spd"))
        kits.createIn(self.loc, idxStart)

        os.system("umount %s" % self.mediaLoc)
        sp.setDTR(False)


uploader = Uploader()
if key == "gen":
    uploader.upload(Generic_2022(), 69)
else:
    uploader.upload(Generic_2019(), 69)

