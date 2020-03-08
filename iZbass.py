#!/usr/bin/env python

import sys
from utils import any, DelayTimes
from kit import Kit
from iZgenKits import Notes, modes, modeNames
from sysConfig import SystemConfig
from effects import *
#from random import randint


master = 0
sub = 1

if (len(sys.argv) < 2):
	print("iZbass.py <key> <tempo>")
	print("eg iZbass.py F#")
	exit()

key = sys.argv[1].upper()
tempo = 120 if (len(sys.argv) < 3) else int(sys.argv[2])

roots = {"E": 40, 
		 "F": 41,
		 "F#": 42,
		 "Gb": 42,
		 "G": 43,
		 "G#": 44,
		 "Ab": 44,
		 "A": 33,
		 "A#": 34,
		 "Bb": 34,
		 "B": 35,
		 "C": 36,
		 "C#": 37,
		 "Db": 37,
		 "D": 38,
		 "D#": 39,
		 "Eb": 39}


idx = 85
loc = 90 # from iZgenBass
allowedFx = [Chorus, Phaser, FilterPlusDrive, Distortion, TouchWah, Vibrato, Slicer]
noteSeq = [5, 6, 0, 1, 2, 3, 4, 5, 6]
padOutMaster = 0
padOutFx1 = 1
padOutFx2 = 2
padOutSub = 3

for modeName in modeNames:
	notes = Notes(7, roots[key], modes[modeName])
	
	kitDef = type("%s_%s" % (key, modeName), (), {})
	kitDef.level = 100
	kitDef.pan = 0
	kitDef.tempo = tempo
	kitDef.fx1 = any(allowedFx, []).createRandom()
	kitDef.fx2 = Thru()
	kitDef.pads = []
	
	#assume one bass wav available per note, in sequence.
	for n in noteSeq:
		kitDef.pads.append({"sound": str((loc * 100) + notes.note(n)), "channel": 0, "vol": 100, "note": notes.note(n), "outAssign": padOutFx1})

	Kit().buildNamed(kitDef, "E:\\Roland\\SPD-SX\\KIT", idx)
	idx += 1