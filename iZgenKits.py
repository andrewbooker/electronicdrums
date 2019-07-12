#!/usr/bin/env python

from sounds import sounds as wav
from utils import any

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
		 "eastern": [1, 3, 1, 2, 1, 2]}
		 
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


class NativeKitSounds():
		
	def rightFoot(self):
		return any(["Kick_110",
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
					"Kick_Proc5"]) #58 #00/Kick__19.wav
	
	def leftFoot(self):
		return any(["Tom_808_H",  #:128 #01/Tom_8.wav
					"Tom_808_L",  #:129 #01/Tom_8_01.wav
					"Tom_808_M",  #:130 #01/Tom_8_02.wav
					"Tom_Acou_H", #:131 #01/Tom_A.wav
					"Tom_Acou_L", #:132 #01/Tom_A_01.wav
					"Tom_Acou_M", #:133 #01/Tom_A_02.wav
					"Tom_Roto_H", #:137 #01/Tom_R.wav
					"Tom_Roto_L", #:138 #01/Tom_R_01.wav
					"Tom_Roto_M"]) #:139 #01/Tom_R_02.wav
	
	def padTop(self):
		return any(["Snare_110", #103 #01/Snare.wav
					"Snare_808", #104 #01/Snare_01.wav
					"Snare_909", #105 #01/Snare_02.wav
					"Snare_Acou1", #106 #01/Snare_03.wav
					"Snare_Acou2", #107 #01/Snare_04.wav
					"Snare_DbS", #108 #01/Snare_05.wav
					"Snare_DnB1", #109 #01/Snare_06.wav
					"Snare_DnB2", #110 #01/Snare_07.wav
					"Snare_Edrs", #111 #01/Snare_08.wav
					"Snare_Hph", #112 #01/Snare_09.wav
					"Snare_Hse1", #113 #01/Snare_10.wav
					"Snare_Hse2", #114 #01/Snare_11.wav
					"Snare_Proc1", #115 #01/Snare_12.wav
					"Snare_Proc2", #116 #01/Snare_13.wav
					"Snare_Proc3", #117 #01/Snare_14.wav
					"Snare_Proc4", #118 #01/Snare_15.wav
					"Snare_Proc5", #119 #01/Snare_16.wav
					"Snare_Proc6", #120 #01/Snare_17.wav
					"SnareXs_1", #121 #01/Snare_18.wav
					"SnareXs_2", #122 #01/Snare_19.wav
					"SnareXs_3", #123 #01/Snare_20.wav
					"SnareXs_4", #124 #01/Snare_21.wav
					"SnareXs_5", #125 #01/Snare_22.wav
					"SnareXs_6", #126 #01/Snare_23.wav
					"SnareXs_7"]) #:127 #01/Snare_24.wav]
					
	def padRim(self):
		return self.leftFoot()
		
	def cym(self):
		return any(["Cym_808",
				    "Ride_Acou",  #:82 #00/Ride_.wav
				    "Ride_DnB",   #:83 #00/Ride__01.wav
				    "Ride_Proc1", #:84 #00/Ride__02.wav
				    "Ride_Proc1Bl"])#:85 #00/Ride__03.wav
	
	def perc(self):
		return any(["Clap_Hse2", #:4 #00/Clap__04.wav
					"Clap_Min",  #:5 #00/Clap__05.wav
					"Clap_Verb1", #:6 #00/Clap__06.wav
					"P_GanzaTap",
					"SE_VerbPf"])
					
					

ks = NativeKitSounds()

def generate(r, m, t):
	notes = Notes(7, roots[r], modes[m])
	
	k = type("%s_%s" % (r, m), (), {})
	k.level = 100
	k.tempo = t
	k.pads = []
	notePerc = wav["P_GanzaTap"]
	
	k.pads.append({"sound": notePerc, "channel": 0, "note": notes.note(4)})
	k.pads.append({"sound": notePerc, "channel": 0, "note": notes.note(5)})
	k.pads.append({"sound": notePerc, "channel": 0, "note": notes.note(6)})
	k.pads.append({"sound": wav[ks.cym()]})
	k.pads.append({"sound": notePerc, "channel": 0, "note": notes.note(2)})
	k.pads.append({"sound": notePerc, "channel": 0, "note": notes.note(3)})
	k.pads.append({"sound": wav[ks.perc()]})
	k.pads.append({"sound": notePerc, "channel": 0, "note": notes.note(0)})
	k.pads.append({"sound": notePerc, "channel": 0, "note": notes.note(1)})
	k.pads.append({"sound": 9901})
	k.pads.append({"sound": wav[ks.leftFoot()]})
	k.pads.append({"sound": wav[ks.padTop()]})
	k.pads.append({"sound": wav[ks.padRim()]})

	return k
