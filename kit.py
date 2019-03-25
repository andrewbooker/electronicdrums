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

def valueFrom(padSpecs, item, i, alternative = -1):
	if (i < len(padSpecs)):
		spec = padSpecs[i]
		if (item in spec):
			return spec[item]
	return alternative
	
def setUpFx(doc, onto, n):
	kitParam(doc, onto, "Fx%dSw" % n, 1)
	kitParam(doc, onto, "Fx%dType" % n, 1)
	for i in range(20):
		kitParam(doc, onto, "Fx%dPrm%d" % (n, i), 0)

def createKit(zIndex, name, kitDef):
	doc = xml.dom.minidom.parseString("<KitPrm/>")
	kitPrm = doc.documentElement

	kitParam(doc, kitPrm, "Level", kitDef.level)
	kitParam(doc, kitPrm, "Tempo", kitDef.tempo * 10)
	setName(doc, kitPrm, name)
	
	for i in range(16):
		kitParam(doc, kitPrm, "SubNm%d" % i, 0)

	kitParam(doc, kitPrm, "Fx2Asgn", 0)
	kitParam(doc, kitPrm, "LinkPad0", -1)
	kitParam(doc, kitPrm, "LinkPad1", -1)
	setUpFx(doc, kitPrm, 1)
	setUpFx(doc, kitPrm, 2)
	
	for i in range(15):
		pad = kitNode(doc, kitPrm, "PadPrm")
		kitParam(doc, pad, "Wv", valueFrom(kitDef.pads, "sound", i))
		kitParam(doc, pad, "WvLevel", 100)
		kitParam(doc, pad, "WvPan", 15)
		kitParam(doc, pad, "PlayMode", 0)
		kitParam(doc, pad, "OutAsgn", 0)
		kitParam(doc, pad, "MuteGrp", 0)
		kitParam(doc, pad, "TempoSync", 0)
		kitParam(doc, pad, "PadMidiCh", valueFrom(kitDef.pads, "channel", i))
		kitParam(doc, pad, "NoteNum", valueFrom(kitDef.pads, "note", i))
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






