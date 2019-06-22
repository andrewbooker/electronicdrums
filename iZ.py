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
	allowedFx: [] # allow TapeEcho, Slicer, Wah, nothing that's already available in the Korg
		  
class FxKit():
	korgAssign = sub
	allowedFx = [Phaser] #etc... allow Filter+Dist, Phaser, Wah, Vibrato, Slicer, PitchShift, RingMod if BD is assigned to 

mode = FxKit()
fx = mode.allowedFx[randint(0, len(mode.allowedFx) - 1)]


print("writing files for %s %s bpm using %s%s" % (key, tempo, fx.__name__, " allowing FX mod" if allowFxMod == 1 else ""))

c = SystemConfig()

c.inAssign = mode.korgAssign
c.fxModOn = allowFxMod
c.masterFx = fx.createRandom()

c.createIn("E:\\Roland\\SPD-SX\\SYSTEM\\sysparam.spd")

kitDef = generate(key, "aeolian", tempo)
kitDef.pan = 0
Kit().buildNamed(kitDef, "E:\\Roland\\SPD-SX\\KIT", 70)

