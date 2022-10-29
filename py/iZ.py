#!/usr/bin/env python

import sys
from utils import any, DelayTimes
from kit import Kit
from iZgenKits import generate, modeNames, Notes, roots, modes, GenericNotes
from sysConfig import SystemConfig
from effects import *
from random import randint
import json
import os
import serial
import time

def config():
    with open("config.json") as conf:
        return json.load(conf)

mediaLoc = config()["mediaLoc"]
loc = os.path.join(mediaLoc, "Roland", "SPD-SX")
master = 0
sub = 1

if (len(sys.argv) < 2):
    print("iZ <key> [<tempo>] [<apply-master-fx-to>] [<delay-subdivision>] [<allow-fx-mod>]")
    print("eg iZ.py F# 83 kit")
    print("or iZ.py C 110 korg intra")
    print("or iZ.py Bb 150 korg poly 1")
    print("or iZ.py A")
    print("or iZ.py gen 101 korg poly")
    exit()

class FxKorg():
    korgAssign = master
    allowedFx = [Slicer, TapeEcho, TouchWah]

class FxKit():
    korgAssign = sub
    allowedFx = [RingMod, Phaser, FilterPlusDrive, Distortion, TouchWah, PitchShift, Vibrato, Reverb, Slicer]

def createKit(idx, name, notes, kitFx1, kitFx2):
    kitDef = generate(name, tempo, notes)
    kitDef.pan = 0

    kitDef.fx1 = kitFx1.createRandom() if c.fx1On() == 1 else kitFx1()
    kitDef.fx2 = kitFx2.createRandom()

    # assign all sounds using c.kitAssign() and c.fx1On()
    padOutMaster = 0
    padOutFx1 = 1
    padOutFx2 = 2
    padOutSub = 3

    topKitOut = padOutFx1 if (c.fx1On() == 1) else padOutFx2
    korgPercOut = padOutMaster if (c.inAssign == sub) else topKitOut
    midKitOut = padOutFx2
    bdOut = padOutSub # allow padOutFx2 if not RingMod

    kitDef.pads[0]["outAssign"] = korgPercOut
    kitDef.pads[1]["outAssign"] = korgPercOut
    kitDef.pads[2]["outAssign"] = korgPercOut
    kitDef.pads[3]["outAssign"] = topKitOut
    kitDef.pads[4]["outAssign"] = korgPercOut
    kitDef.pads[5]["outAssign"] = korgPercOut
    kitDef.pads[6]["outAssign"] = midKitOut
    kitDef.pads[7]["outAssign"] = korgPercOut
    kitDef.pads[8]["outAssign"] = korgPercOut
    kitDef.pads[9]["outAssign"] = midKitOut
    kitDef.pads[10]["outAssign"] = midKitOut
    kitDef.pads[11]["outAssign"] = midKitOut
    kitDef.pads[12]["outAssign"] = topKitOut

    Kit().buildNamed(kitDef, os.path.join(loc, "KIT"), idx)


effModes = {"kit": FxKit, "korg": FxKorg}

key = sys.argv[1]
tempo = randint(46, 119) if (len(sys.argv) < 3) else int(sys.argv[2])
mode = FxKorg if len(sys.argv) < 4 else effModes[sys.argv[3]]
delaySubdivision = "intra" if len(sys.argv) < 5 else sys.argv[4]
allowFxMod = 1 if len(sys.argv) < 6 else int(sys.argv[5])

masterFx = any(mode.allowedFx)

dt = DelayTimes(tempo, delaySubdivision == "intra")
print("tempo %d bpm" % tempo)
print("%s ms %s%%" % (dt.time, dt.leftTap))
print("master %s %s%s" % (mode.__name__, masterFx.__name__, " allowing FX mod" if allowFxMod == 1 else ""))

sp = serial.Serial("/dev/ttyUSB0")
sp.setDTR(True)
while not os.path.exists(loc):
    time.sleep(0.1)

c = SystemConfig(dt)

c.inAssign = mode.korgAssign
c.fxModOn = allowFxMod
c.masterFx = masterFx.createRandom()

c.createIn(os.path.join(loc, "SYSTEM", "sysparam.spd"))

kitFx1 = Thru
kitFx2 = any(FxKit.allowedFx, [masterFx])
if (c.fx1On() == 1):
    kitFx1 = any(FxKit.allowedFx, [masterFx, kitFx2])
    print("FX1 %s" % kitFx1.__name__)

print("FX2 %s" % kitFx2.__name__)

idx = 70
if key == "gen":
    for i in range(10):
        createKit(idx + i, "gen_%02d" % i, GenericNotes(), kitFx1, kitFx2)
else:
    for modeName in modeNames:
        notes = Notes(7, roots[key], modes[modeName])
        name = "%s_%s" % (key, modeName)
        createKit(idx, name, notes, kitFx1, kitFx2)
        idx += 1

os.system("umount %s" % mediaLoc)
sp.setDTR(False)
