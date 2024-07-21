#!/usr/bin/env python

from datetime import date
import xml.dom.minidom
from effects import Thru
import os

def kitNode(doc, onto, name):
    return onto.appendChild(doc.createElement(name))

def kitParam(doc, onto, name, value):
    kitNode(doc, onto, name).appendChild(doc.createTextNode(str(value)))
    
def setName(doc, onto, name):
    l = len(name)
    for i in range(8):
        kitParam(doc, onto, "Nm%d" % i, ord(name[i]) if i < l else 0x20)

def valueFrom(padSpecs, item, i, alternative = -1):
    if (i < len(padSpecs)):
    	spec = padSpecs[i]
    	if (item in spec):
    		return spec[item]
    return alternative
    
def setUpFx(doc, onto, fx, n):
    kitParam(doc, onto, "Fx%dSw" % n, 1 if fx.type > 0 else 0)
    kitParam(doc, onto, "Fx%dType" % n, fx.type)
    for i in range(20):
    	kitParam(doc, onto, "Fx%dPrm%d" % (n, i), fx.asSpec()[i] if i < len(fx.asSpec()) else 0)

    	
class Kit():
    def buildFrom(self, kitDef, name):
    	doc = xml.dom.minidom.parseString("<KitPrm/>")
    	kitPrm = doc.documentElement

    	kitParam(doc, kitPrm, "Level", kitDef.level)
    	kitParam(doc, kitPrm, "Tempo", kitDef.tempo * 10)
    	setName(doc, kitPrm, name)
    	
    	for i in range(16):
    		kitParam(doc, kitPrm, "SubNm%d" % i, 0)

    	kitParam(doc, kitPrm, "Fx2Asgn", 1 if hasattr(kitDef, "fx2") else 0) # does what?
    	kitParam(doc, kitPrm, "LinkPad0", -1)
    	kitParam(doc, kitPrm, "LinkPad1", -1)
    	setUpFx(doc, kitPrm, kitDef.fx1 if hasattr(kitDef, "fx1") else Thru(), 1)
    	setUpFx(doc, kitPrm, kitDef.fx2 if hasattr(kitDef, "fx2") else Thru(), 2)
    	
    	pan = kitDef.pan if hasattr(kitDef, "pan") else 15
    	
    	for i in range(15):
    		isPad = i < 13
    		
    		outAssign = 1 if (isPad and hasattr(kitDef, "fx1")) else 0
    		outAssign = valueFrom(kitDef.pads, "outAssign", i, outAssign) 

    		pad = kitNode(doc, kitPrm, "PadPrm")
    		kitParam(doc, pad, "Wv", valueFrom(kitDef.pads, "sound", i))
    		kitParam(doc, pad, "WvLevel", valueFrom(kitDef.pads, "vol", i, 100))
    		kitParam(doc, pad, "WvPan", pan)
    		kitParam(doc, pad, "PlayMode", 0)
    		kitParam(doc, pad, "OutAsgn", outAssign) 
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
    		kitParam(doc, pad, "SubWv", valueFrom(kitDef.pads, "soundb", i))
    		kitParam(doc, pad, "SubWvLevel", valueFrom(kitDef.pads, "vol", i, 100))
    		kitParam(doc, pad, "SubWvPan", 30)
    		
    	return kitPrm
    	
    def build(self, kitDef, name, kitDir, zIndex):
    	kitFn = "kit%03d.spd" % zIndex
    	file = open(os.path.join(kitDir, kitFn), "w")
    	self.buildFrom(kitDef, name).writexml(file, addindent="\t", newl="\n")
    	file.close()
    	print("kit %.3d %s created in %s" % (zIndex + 1, name, kitFn))
    
    def buildNamed(self, kitDef, dir, zIndex):
    	self.build(kitDef, kitDef.__name__, dir, zIndex)

