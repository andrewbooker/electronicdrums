#!/usr/bin/env python

from datetime import date
import xml.dom.minidom

def kitNode(doc, onto, name):
	return onto.appendChild(doc.createElement(name))

def kitParam(doc, onto, name, value):
	kitNode(doc, onto, name).appendChild(doc.createTextNode(str(value)))
	
def setName(doc, onto, name):
	for i in range(8):
		kitParam(doc, onto, "Nm%d" % i, ord(name[i]))


def specItemFrom(padSpecs, item, i):
	k = str(i + 1)
	if (k in padSpecs):
		spec = padSpecs[k]
		if (item in spec):
			return spec[item]
	return -1
		

def createKit(zIndex, name, tempo, padSpecs):
	doc = xml.dom.minidom.parseString("<KitPrm/>")
	kitPrm = doc.documentElement
	kitParam(doc, kitPrm, "Level", 100)
	kitParam(doc, kitPrm, "Tempo", tempo * 10)
	setName(doc, kitPrm, name)
	
	for i in range(16):
		kitParam(doc, kitPrm, "SubNm%d" % i, 0)
	
	for i in range(15):
		pad = kitNode(doc, kitPrm, "PadPrm")
		kitParam(doc, pad, "Wv", specItemFrom(padSpecs, "sound", i))
		kitParam(doc, pad, "WvLevel", 100)
		kitParam(doc, pad, "WvPan", 15)
		kitParam(doc, pad, "PlayMode", 0)
		kitParam(doc, pad, "OutAsgn", 0)
		kitParam(doc, pad, "MuteGrp", 0)
		kitParam(doc, pad, "TempoSync", 0)
		kitParam(doc, pad, "PadMidiCh", 15)
		kitParam(doc, pad, "NoteNum", specItemFrom(padSpecs, "note", i))
		kitParam(doc, pad, "MidiCtrl", 0)
		kitParam(doc, pad, "Loop", 0)
		kitParam(doc, pad, "TrigType", 0)
		kitParam(doc, pad, "GateTime", -1)
		kitParam(doc, pad, "Dynamics", 1)
		kitParam(doc, pad, "VoiceAsgn", 1)
		kitParam(doc, pad, "Reverse", 0)
		kitParam(doc, pad, "SubWv", -1)
		kitParam(doc, pad, "SubWvLevel", 100)
		kitParam(doc, pad, "SubWvPan", 15)

	kitFn = "kit%03d.spd" % zIndex
	kitPrm.writexml(open("D:\\gear\\spd-sx\\sandbox\\Roland\\SPD-SX\\KIT\\%s" % kitFn, "w"), addindent="\t", newl="\n")
	#kitPrm.writexml(open("E:\\Roland\\SPD-SX\\KIT\\%s" % kitFn, "w"), addindent="\t", newl="\n")
	print("kit %s created in %s" % (name, kitFn))

#createKit(98, date.today().strftime("%Y%m%d"), 83, {}) 

kn = 50
set = __import__("tbb2019")
for n, cl in set.__dict__.items():
	if isinstance(cl, type):
		createKit(kn, n[:8], cl.tempo, cl.pads)
		kn += 1




