#!/usr/bin/env python

import xml.dom.minidom


def node(doc, onto, name):
	return onto.appendChild(doc.createElement(name))

def param(doc, onto, name, value):
	node(doc, onto, name).appendChild(doc.createTextNode(str(value)))


def createSetup():
	doc = xml.dom.minidom.parseString("<SetupPrm/>")
	setup = doc.documentElement
	param(doc, setup, "LCDContrast", 4)
	param(doc, setup, "LCDBright", 7)
	param(doc, setup, "PadIllumi", 1)
	param(doc, setup, "TempoIndi", 1)
	param(doc, setup, "FS1Porality", 0)
	param(doc, setup, "FS2Porality", 0)
	param(doc, setup, "MIDICh", 13)
	param(doc, setup, "MIDISync", 0)
	param(doc, setup, "LocalCtrl", 1)
	param(doc, setup, "SoftThru", 1)
	param(doc, setup, "MIDIPCCtrl", 1)
	param(doc, setup, "MIDICCCtrl", 1)
	param(doc, setup, "MEfctCCSel", 64)
	param(doc, setup, "MEfctCCKnob1", 12)
	param(doc, setup, "MEfctCCKnob2", 13)
	param(doc, setup, "USBMIDIThru", 0)
	param(doc, setup, "PadLock", 0)
	param(doc, setup, "AutoPowerOff", 0)
	param(doc, setup, "DispMode", 1)
	param(doc, setup, "MultiView", 0)
	param(doc, setup, "USBDevMode", 0)
	param(doc, setup, "StartupKit", 70)
	
	for i in range(9):
		pad = node(doc, setup, "IntPad")
		param(doc, pad, "Sens", 8)
		param(doc, pad, "Threshold", 2)
		param(doc, pad, "Curve", 0)
	
	for i in range(4):
		pad = node(doc, setup, "ExtPad")
		param(doc, pad, "InputMode", 1)
		param(doc, pad, "PadType", 29)
		param(doc, pad, "Sens", 12)
		param(doc, pad, "Threshold", 17)
		param(doc, pad, "Curve", 1)
		param(doc, pad, "ScanTime", 38)
		param(doc, pad, "RetrigCxl", 14)
		param(doc, pad, "MaskTime", 42)
		param(doc, pad, "XtalkCxl", 56)
		param(doc, pad, "RimAdjust", 0)
		param(doc, pad, "RimGain", 0)
		param(doc, pad, "NoiseCxl", 1)

	return doc
	
def createSys():
	doc = xml.dom.minidom.parseString("<SysPrm/>")
	
	return doc
	
	
file = open("D:\\gear\\spd-sx\\test.xml", "w");
createSetup().writexml(file, addindent="\t", newl="\n")
file.close()