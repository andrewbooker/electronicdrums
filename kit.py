#!/usr/bin/env python

from datetime import date
import xml.dom.minidom

doc = xml.dom.minidom.parseString("<KitPrm/>")

def kitNode(onto, name):
	return onto.appendChild(doc.createElement(name))

def kitParam(onto, name, value):
	kitNode(onto, name).appendChild(doc.createTextNode(str(value)))
	
def setName(onto, name):
	for i in range(8):
		kitParam(onto, "Nm%d" % i, ord(name[i]))
	
	
kitPrm = doc.documentElement
kitParam(kitPrm, "Level", 100)
kitParam(kitPrm, "Tempo", 790)

setName(kitPrm, date.today().strftime("%Y%m%d"))
for i in range(16):
	kitParam(kitPrm, "SubNm%d" % i, 0)
	

for i in range(15):
	pad = kitNode(kitPrm, "PadPrm")
	kitParam(pad, "Wv", -1)
	#kitParam(pad, "WvLevel", 100)
	#kitParam(pad, "WvPan", 15)
	#kitParam(pad, "PlayMode", 0)
	#kitParam(pad, "OutAsgn", 0)
	#kitParam(pad, "MuteGrp", 0)
	#kitParam(pad, "TempoSync", 0)
	kitParam(pad, "PadMidiCh", 15)
	kitParam(pad, "NoteNum", i + 1)
	#kitParam(pad, "MidiCtrl", 0)
	#kitParam(pad, "Loop", 0)
	#kitParam(pad, "TrigType", 0)
	#kitParam(pad, "GateTime", -1)
	#kitParam(pad, "Dynamics", 1)
	#kitParam(pad, "VoiceAsgn", 1)
	#kitParam(pad, "Reverse", 0)
	kitParam(pad, "SubWv", -1)
	#kitParam(pad, "SubWvLevel", 100)
	#kitParam(pad, "SubWvPan", 15)

kitPrm.writexml(open("D:\\gear\\spd-sx\\sandbox\\Roland\\SPD-SX\\KIT\\kit099.spd", "w"), addindent="\t", newl="\n")
kitPrm.writexml(open("E:\\Roland\\SPD-SX\\KIT\\kit099.spd", "w"), addindent="\t", newl="\n")
