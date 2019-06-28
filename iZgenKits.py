#!/usr/bin/env python

from sounds import sounds as wav
from random import randint

roots = {"E": 64, 
		 "F": 65,
		 "F#": 66,
		 "Gb": 66,
		 "G": 67,
		 "G#": 68,
		 "Ab": 68,
		 "A": 69,
		 "A#": 70,
		 "Bb": 70,
		 "B": 71,
		 "C": 72,
		 "C#": 73,
		 "Db": 73,
		 "D": 74,
		 "D#": 75,
		 "Eb": 75}

modes = {"aeolian": [2, 1, 2, 2, 1, 2],
		 "dorian": [2, 1, 2, 2, 2, 1],
		 "ionian": [2, 2, 1, 2, 2, 2],
		 "mixolydian": [2, 2, 1, 2, 2, 1],
		 "lydian": [2, 2, 2, 1, 2, 2],
		 "eastern": [1, 3, 1, 2, 1, 3]}
		 
modeNames = modes.keys()


class Notes():
	def __init__(self, padCount, root, mode):
		octaves = -1
		base = root
		self.root = root
		self.notes = []
		for n in range(padCount):
			if ((n % (len(mode) + 1)) == 0):
				octaves += 1
				base = root + (octaves * 12)
			else:
				base += mode[(n - 1) % len(mode)]
			
			self.notes.append(base)

	def note(self, i):
		return self.notes[i]

class KitSounds():
	@staticmethod
	def any(a):
		return a[randint(0, len(a) - 1)]
		
	rightFoot = ["Kick_110",
				 "Kick_808_L", #:40 #00/Kick__01.wav
				 "Kick_808_S", #41 #00/Kick__02.wav
				 "Kick_909", #42 #00/Kick__03.wav
				 "Kick_909_Atk", #43 #00/Kick__04.wav
				 "Kick_Acou1", #44 #00/Kick__05.wav
				 "Kick_Acou2", #45 #00/Kick__06.wav
				 "Kick_DbS", #46 #00/Kick__07.wav
				 "Kick_DnB1", #47 #00/Kick__08.wav
				 "Kick_DnB2", #48 #00/Kick__09.wav
				 "Kick_Edrs1", #49 #00/Kick__10.wav
				 "Kick_Edrs2", #50 #00/Kick__11.wav
				 "Kick_Hph", #51 #00/Kick__12.wav
				 "Kick_Hse1", #52 #00/Kick__13.wav
				 "Kick_Hse2", #53 #00/Kick__14.wav
				 "Kick_Proc1", #54 #00/Kick__15.wav
				 "Kick_Proc2", #55 #00/Kick__16.wav
				 "Kick_Proc3", #56 #00/Kick__17.wav
				 "Kick_Proc4", #57 #00/Kick__18.wav
				 "Kick_Proc5"] #58 #00/Kick__19.wav
				 
	perc = [] #left foot, bottom left SPD-SX, pad rim
	backbeat = [] #pad head
	cym = [] #top left SPD-SX

def generate(r, m, t):
	notes = Notes(7, roots[r], modes[m])
	
	k = type("%s_%s" % (r, m), (), {})
	k.level = 100
	k.tempo = t
	k.pads = []
	
	k.pads.append({"sound": wav["P_Triangl_op"], "channel": 0, "note": notes.note(4)})
	k.pads.append({"sound": wav["P_Triangl_op"], "channel": 0, "note": notes.note(5)})
	k.pads.append({"sound": wav["P_Triangl_op"], "channel": 0, "note": notes.note(6)})
	k.pads.append({"sound": wav["Cym_808"]})
	k.pads.append({"sound": wav["P_Triangl_op"], "channel": 0, "note": notes.note(2)})
	k.pads.append({"sound": wav["P_Triangl_op"], "channel": 0, "note": notes.note(3)})
	k.pads.append({"sound": wav["P_GanzaTap"]})
	k.pads.append({"sound": wav["P_Triangl_op"], "channel": 0, "note": notes.note(0)})
	k.pads.append({"sound": wav["P_Triangl_op"], "channel": 0, "note": notes.note(1)})
	k.pads.append({"sound": wav[KitSounds.any(KitSounds.rightFoot)]})
	k.pads.append({"sound": wav["SnareXs_4"]})
	k.pads.append({"sound": wav["SnareXs_7"]})
	k.pads.append({"sound": wav["SE_VerbPf"]})	

	return k
