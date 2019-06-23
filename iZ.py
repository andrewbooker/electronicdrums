#!/usr/bin/env python

import sys
from random import randint
from kit import Kit
from genNotesPatches import generate
from sysConfig import SystemConfig
from effects import *

key = sys.argv[1].upper()
tempo = int(sys.argv[2])
allowFxMod = 1 if len(sys.argv) < 4 else int(sys.argv[3])

master = 0
sub = 1

class FxKorg():
	korgAssign = master
	allowedFx = [FilterPlusDrive] # allow TapeEcho, Slicer, Wah, nothing that's already available in the Korg
		  
class FxKit():
	korgAssign = sub
	allowedFx = [Phaser] #etc... allow Filter+Dist, Phaser, Wah, Vibrato, Slicer, PitchShift, RingMod if BD is assigned to 

mode = FxKorg()
#mode = FxKit()
masterFx = mode.allowedFx[randint(0, len(mode.allowedFx) - 1)]
 


print("writing files for %s %s bpm using %s%s" % (key, tempo, masterFx.__name__, " allowing FX mod" if allowFxMod == 1 else ""))

c = SystemConfig()

c.inAssign = mode.korgAssign
c.fxModOn = allowFxMod
c.masterFx = masterFx.createRandom()

c.createIn("E:\\Roland\\SPD-SX\\SYSTEM\\sysparam.spd")

kitDef = generate(key, "aeolian", tempo)
kitDef.pan = 0



kitDef.fx2 = FxKit.allowedFx[randint(0, len(FxKit.allowedFx) - 1)].createRandom() # should avoid using the one picked for the master, once more effects are added
if (c.fx1On() == 1):
	kitDef.fx1 = FxKit.allowedFx[randint(0, len(FxKit.allowedFx) - 1)].createRandom() # should avoid using the one picked for the master or fx2, once more effects are added

	
# assign all sounds using c.kitAssign() and c.fx1On()
padOutMaster = 0
padOutFx1 = 1
padOutFx2 = 2
padOutSub = 3

korgPercOut = padOutMaster if (c.inAssign == sub) else padOutSub
topKitOut = padOutFx1 if (c.fx1On() == 1) else padOutFx2
midKitOut = padOutFx2
bdOut = padOutSub

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

Kit().buildNamed(kitDef, "E:\\Roland\\SPD-SX\\KIT", 70)

