#!/usr/bin/env python

import sys
from random import randint
from kit import Kit
from iZgenKits import generate, modeNames
from sysConfig import SystemConfig
from effects import *

master = 0
sub = 1

class FxKorg():
	korgAssign = master
	allowedFx = [Slicer, TapeEcho, TouchWah]
		  
class FxKit():
	korgAssign = sub
	allowedFx = [RingMod, Phaser, FilterPlusDrive, Distortion, TouchWah, PitchShift, Vibrato, Reverb, Slicer]
	
effModes = {"kit": FxKit, "korg": FxKorg}

key = sys.argv[1].upper()
tempo = int(sys.argv[2])
mode = FxKorg if len(sys.argv) < 4 else effModes[sys.argv[3]]
allowFxMod = 1 if len(sys.argv) < 5 else int(sys.argv[4])


masterFx = mode.allowedFx[randint(0, len(mode.allowedFx) - 1)] #prefer tape echo if allowFxMod off

print("tempo %d bpm" % tempo)
print("master %s %s%s" % (mode.__name__, masterFx.__name__, " allowing FX mod" if allowFxMod == 1 else ""))

c = SystemConfig()

c.inAssign = mode.korgAssign
c.fxModOn = allowFxMod
c.masterFx = masterFx.createRandom()

c.createIn("E:\\Roland\\SPD-SX\\SYSTEM\\sysparam.spd")

kitFx1 = Thru
kitFx2 = FxKit.allowedFx[randint(0, len(FxKit.allowedFx) - 1)] # should avoid using the one picked for the master, once more effects are added
if (c.fx1On() == 1):
	kitFx1 = FxKit.allowedFx[randint(0, len(FxKit.allowedFx) - 1)] # should avoid using the one picked for the master or fx2, once more effects are added
	print("FX1 %s" % kitFx1.__name__)

print("FX2 %s" % kitFx2.__name__)

idx = 70
for modeName in modeNames:

	kitDef = generate(key, modeName, tempo)
	kitDef.pan = 0

	kitDef.fx1 = kitFx1.createRandom() if c.fx1On() == 1 else kitFx1()
	kitDef.fx2 = kitFx2.createRandom()
		
	# assign all sounds using c.kitAssign() and c.fx1On()
	padOutMaster = 0
	padOutFx1 = 1
	padOutFx2 = 2
	padOutSub = 3

	korgPercOut = padOutMaster if (c.inAssign == sub) else padOutSub
	topKitOut = padOutFx1 if (c.fx1On() == 1) else padOutFx2
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
	kitDef.pads[9]["outAssign"] = bdOut
	kitDef.pads[10]["outAssign"] = midKitOut
	kitDef.pads[11]["outAssign"] = midKitOut
	kitDef.pads[12]["outAssign"] = topKitOut

	Kit().buildNamed(kitDef, "E:\\Roland\\SPD-SX\\KIT", idx)
	idx += 1

