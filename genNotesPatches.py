#!/usr/bin/env python


roots = {"E": 64, "G": 67, "A": 69, "C": 72, "D": 74}
modes = {"aeolian": [2, 1, 2, 2, 1, 2],
		 "dorian": [2, 1, 2, 2, 2, 1],
		 "ionian": [2, 2, 1, 2, 2, 2],
		 "lydian": [2, 2, 2, 1, 2, 2]}


class Notes():
	def __init__(self, padCount, root, mode):
		octaves = -1
		base = root
		self.root = root
		self.notes = []
		for n in range(padCount):
			if ((n % len(mode)) == 0):
				octaves += 1
				base = root + (octaves * 12)
			else:
				base += mode[(n - 1) % len(mode)]
			
			self.notes.append(base)
		
		
	def note(self, i):
		return self.notes[i]
		

	
def pad(n):
	return "P_GanzaTap"

def generate(r, m):
	notes = Notes(11, roots[r], modes[m])
	
	print("class %s_%s():" % (r, m))
	print("\tlevel = 100")
	print("\ttempo = 86")
	print("\tpads = [{note: %d, channel: 0, sound: wav[\"%s\"]}," % (notes.note(8), pad(8)))
	print("\t\t\t{note: %d, channel: 0, sound: wav[\"%s\"]}," % (notes.note(7), pad(7)))
	print("\t\t\t{note: %d, channel: 0, sound: wav[\"%s\"]}," % (notes.note(6), pad(6)))
	print("\t\t\t{note: %d, channel: 0, sound: wav[\"%s\"]}," % (notes.note(5), pad(5)))
	print("\t\t\t{note: %d, channel: 0, sound: wav[\"%s\"]}," % (notes.note(4), pad(4)))
	print("\t\t\t{note: %d, channel: 0, sound: wav[\"%s\"]}," % (notes.note(3), pad(3)))
	print("\t\t\t{note: %d, channel: 0, sound: wav[\"%s\"]}," % (notes.note(2), pad(2)))
	print("\t\t\t{note: %d, channel: 0, sound: wav[\"%s\"]}," % (notes.note(1), pad(1)))
	print("\t\t\t{note: %d, channel: 0, sound: wav[\"%s\"]}," % (notes.note(0), pad(0)))
	print("\t\t\t{sound: wav[\"%s\"]}," % "Kick_Acou1")
	print("\t\t\t{note: %d, channel: 0, sound: wav[\"%s\"]}," % (notes.root + 24, "SnareXs_4"))
	print("\t\t\t{note: %d, channel: 0, sound: wav[\"%s\"]}," % (notes.note(9), "SE_Crasher")) # pad top
	print("\t\t\t{note: %d, channel: 0, sound: wav[\"%s\"]}]" % (notes.note(10), "SE_VerbPf"))  #pad rim
	print("")


for root in roots:
	for mode in modes:
		generate(root, mode)