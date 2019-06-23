#!/usr/bin/env python

from sounds import sounds as wav

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
	k.pads.append({"sound": wav["Kick_Acou1"]})
	k.pads.append({"sound": wav["SnareXs_4"]})
	k.pads.append({"sound": wav["SnareXs_7"]})
	k.pads.append({"sound": wav["SE_VerbPf"]})	

	return k
