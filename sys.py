#!/usr/bin/env python

import xml.dom.minidom
from effects import *


def node(doc, onto, name):
	return onto.appendChild(doc.createElement(name))

def param(doc, onto, name, value):
	node(doc, onto, name).appendChild(doc.createTextNode(str(value)))
	
def addEmptyKitChain(doc, onto):
	base = node(doc, onto, "KitChain")
	
	for i in range(10):
		param(doc, base, "Nm%d" % i, "")
		
	for i in range(20):
		param(doc, base, "Stp%d" % i, -1)
	
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
		
	#kd7s
	for i in range(2):
		pad = node(doc, setup, "ExtPad")
		param(doc, pad, "InputMode", 1)
		param(doc, pad, "PadType", 0)
		param(doc, pad, "Sens", 7)
		param(doc, pad, "Threshold", 8)
		param(doc, pad, "Curve", 0)
		param(doc, pad, "ScanTime", 16)
		param(doc, pad, "RetrigCxl", 6)
		param(doc, pad, "MaskTime", 10)
		param(doc, pad, "XtalkCxl", 56)
		param(doc, pad, "RimAdjust", 0)
		param(doc, pad, "RimGain", 0)
		param(doc, pad, "NoiseCxl", 0)
		
	#single PD-8, but could adjust to dual head with a bit of initiative (eg make two, InputMode = 1, no rim settings etc)
	pad = node(doc, setup, "ExtPad")
	param(doc, pad, "InputMode", 0)
	param(doc, pad, "PadType", 6)
	param(doc, pad, "Sens", 8)
	param(doc, pad, "Threshold", 5)
	param(doc, pad, "Curve", 0)
	param(doc, pad, "ScanTime", 12)
	param(doc, pad, "RetrigCxl", 4)
	param(doc, pad, "MaskTime", 8)
	param(doc, pad, "XtalkCxl", 56)
	param(doc, pad, "RimAdjust", 0)
	param(doc, pad, "RimGain", 15)
	param(doc, pad, "NoiseCxl", 0)

	return setup
	
def createSys():
	doc = xml.dom.minidom.parseString("<SysPrm/>")
	sys = doc.documentElement
	
	param(doc, sys, "ClickSndGrp", 0)
	param(doc, sys, "ClickSnd", 4)
	param(doc, sys, "ClickWv", 0)
	param(doc, sys, "ClickInterval", 0)
	param(doc, sys, "ClickPan", 15)
	param(doc, sys, "ClickAsgn", 2)
	param(doc, sys, "ClickLevel", 100)
	param(doc, sys, "AudInLevel", 60)
	param(doc, sys, "AudInAsgn", 0)
	param(doc, sys, "Fx2Asgn", 1)
	param(doc, sys, "SystemGain", 0)
	param(doc, sys, "SubOutLevel", 100)
	param(doc, sys, "USBDAudInLevel", 80)
	
	param(doc, sys, "KitChainSw", 0)
	param(doc, sys, "KitChainBank", 0)
	param(doc, sys, "PadCtrlPad1", 0)
	param(doc, sys, "PadCtrlPad2", 0)
	param(doc, sys, "PadCtrlPad3", 0)
	param(doc, sys, "PadCtrlPad4", 0)
	param(doc, sys, "PadCtrlPad5", 0)
	param(doc, sys, "PadCtrlPad6", 0)
	param(doc, sys, "PadCtrlPad7", 0)
	param(doc, sys, "PadCtrlPad8", 0)
	param(doc, sys, "PadCtrlPad9", 0)
	param(doc, sys, "PadCtrlExt1", 0)
	param(doc, sys, "PadCtrlExt2", 0)
	param(doc, sys, "PadCtrlExt3", 0)
	param(doc, sys, "PadCtrlExt4", 0)
	param(doc, sys, "PadCtrlFS1", 0)
	param(doc, sys, "PadCtrlFS2", 0)
	param(doc, sys, "VLinkMode", 0)
	param(doc, sys, "VLinkBank", -1)
	param(doc, sys, "VLinkCh", 0)
	param(doc, sys, "VLinkKnob1CC", 0)
	param(doc, sys, "VLinkKnob2CC", 0)
	param(doc, sys, "VLinkCtrlOnly", 0)
	
	return sys
	
def createKitChain():
	doc = xml.dom.minidom.parseString("<KitChainPrm/>")
	chain = doc.documentElement
	
	for i in range(8):
		addEmptyKitChain(doc, chain)
		
	return chain
	
class MasterFilter():
	def asSpec(self):
		self.slope = 2 #= -36dB
		self.rateSyncOn = 0
		self.modRate = 47
		self.modDepth = 54
		self.lfoWave = 1 #= sine
		return [self.slope, self.rateSyncOn, self.modRate, 8, self.lfoWave, self.modDepth]

class MasterSyncDelay():	
	def leftTapTime(self, v):
		self.leftTapTime = v
		return self
		
	def effLevel(self, v):
		self.effLevel = v
		return self
		
	def asSpec(self):
		self.panOn = 1
		self.syncOn = 1
		self.directLevel = 100
		return [self.panOn, self.syncOn, 6, self.leftTapTime, 0, 9, self.directLevel]
		
class MasterShortLooper():
	type = 1
	def asSpec(self):
		self.autoOn = 2
		self.rateSyncOn = 1
		self.interval = 4
		self.timingHalf = 0
		return [self.rateSyncOn, self.autoOn, self.interval, self.timingHalf]
	
def setUpFx(doc, onto, prefix, fx):
	param(doc, onto, "%sType" % prefix, fx.type if hasattr(fx, "type") else 0)
	for i in range(20):
		param(doc, onto, "%sPrm%d" % (prefix, i), fx.asSpec()[i] if i < len(fx.asSpec()) else 0)
	
def createMasterEffects():
	doc = xml.dom.minidom.parseString("<MEfctPrm/>")
	eff = doc.documentElement
	
	param(doc, eff, "MEQLoGain", 0)
	param(doc, eff, "MEQMidFreq", 17)
	param(doc, eff, "MEQMidGain", 0)
	param(doc, eff, "MEQHiGain", 0)
	param(doc, eff, "FltrPreset", 0)
	param(doc, eff, "DlyPreset", 1)
	param(doc, eff, "SLoopPreset", 0)
	
	setUpFx(doc, eff, "Fltr", MasterFilter())
	setUpFx(doc, eff, "Dr", MasterSyncDelay().leftTapTime(50).effLevel(60))
	setUpFx(doc, eff, "Sp", MasterShortLooper())
	#setUpFx(doc, eff, "Fx", Phaser().rate(47).depth(60).manual(50).resonance(73).separation(88))
	setUpFx(doc, eff, "Fx", RingMod().freq(9).sens(9).polarity(1).balance(0.5))
	
	return eff
	
#file = open("D:\\gear\\spd-sx\\sysparam_gen.spd", "w"); #E:\\Roland\\SPD-SX\\SYSTEM
file = open("E:\\Roland\\SPD-SX\\SYSTEM\\sysparam.spd", "w");
createSetup().writexml(file, addindent="\t", newl="\n")
createSys().writexml(file, addindent="\t", newl="\n")
createKitChain().writexml(file, addindent="\t", newl="\n")
createMasterEffects().writexml(file, addindent="\t", newl="\n")
file.close()