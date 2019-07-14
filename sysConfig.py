#!/usr/bin/env python

import xml.dom.minidom
from effects import *


class MasterFilter():
	def asSpec(self):
		self.slope = 2 #= -36dB
		self.rateSyncOn = 0
		self.modRate = 11
		self.modDepth = 87
		self.lfoWave = 1 #= sine
		return [self.slope, self.rateSyncOn, self.modRate, 8, self.lfoWave, self.modDepth]

class MasterSyncDelay():
	type = 1
	
	def __init__(self):
		self.dt = 0
		self.leftTap = 100
		
	def delayTime(self, t):
		self.dt = t
		return self
		
	def leftTapTime(self, v):
		self.leftTap = v
		return self

	def asSpec(self):
		directLevel = 100
		minim = 10
		self.panOn = 2
		self.syncOn = 1 if self.dt == 0 else 0
		return [self.syncOn, self.dt, minim, self.leftTap, 0, 4, directLevel]
		
class MasterShortLooper():
	type = 1
	def asSpec(self):
		self.autoOn = 2
		self.rateSyncOn = 1
		self.interval = 4
		self.timingHalf = 0
		return [self.rateSyncOn, self.autoOn, self.interval, self.timingHalf]
		

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
	
def createSetup(fxModOn):
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
	param(doc, setup, "MIDICCCtrl", 1 if fxModOn else 0)
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
		
	#kd7s : need to reset this for TBB gig to 
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
	
def createSys(inAssign, fx2Assign):
	doc = xml.dom.minidom.parseString("<SysPrm/>")
	sys = doc.documentElement
	
	param(doc, sys, "ClickSndGrp", 0)
	param(doc, sys, "ClickSnd", 4)
	param(doc, sys, "ClickWv", 0)
	param(doc, sys, "ClickInterval", 0)
	param(doc, sys, "ClickPan", 15)
	param(doc, sys, "ClickAsgn", 2)
	param(doc, sys, "ClickLevel", 100)
	param(doc, sys, "AudInLevel", 75)
	param(doc, sys, "AudInAsgn", inAssign)
	param(doc, sys, "Fx2Asgn", fx2Assign)
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
	
def setUpFx(doc, onto, prefix, fx):
	param(doc, onto, "%sType" % prefix, fx.type if hasattr(fx, "type") else 0)
	for i in range(20):
		param(doc, onto, "%sPrm%d" % (prefix, i), fx.asSpec()[i] if i < len(fx.asSpec()) else 0)


class SystemConfig():
	def __init__(self, delay = None):
		self.fxModOn = 1
		self.inAssign = 0 #0: master, 1; sub
		
		self.masterFilter = MasterFilter()
		self.masterDelay = MasterSyncDelay() if (delay is None) else MasterSyncDelay().delayTime(delay.time).leftTapTime(delay.leftTap)
		self.masterShortLoop = MasterShortLooper()
		self.masterFx = RingMod().freq(9).sens(9).polarity(1).balance(0.5)

	def fx1On(self):
		return 1 if self.inAssign == 1 else 0
		
	def fx2Assign(self):
		return 0 if self.inAssign == 1 else 1
		
	def kitAssign(self): # for use in separate kit builder
		return 0 if self.inAssign == 1 else 1
	
	def createMasterEffects(self):
		doc = xml.dom.minidom.parseString("<MEfctPrm/>")
		eff = doc.documentElement
		
		param(doc, eff, "MEQLoGain", 0)
		param(doc, eff, "MEQMidFreq", 17)
		param(doc, eff, "MEQMidGain", 0)
		param(doc, eff, "MEQHiGain", 0)
		param(doc, eff, "FltrPreset", 0)
		param(doc, eff, "DlyPreset", 1)
		param(doc, eff, "SLoopPreset", 0)
		
		setUpFx(doc, eff, "Fltr", self.masterFilter)
		setUpFx(doc, eff, "Dr", self.masterDelay)
		setUpFx(doc, eff, "Sp", self.masterShortLoop)
		setUpFx(doc, eff, "Fx", self.masterFx)
		
		return eff
		
	def createIn(self, fqfn):
		file = open(fqfn, "w")
		createSetup(self.fxModOn).writexml(file, addindent="\t", newl="\n")
		createSys(self.inAssign, self.fx2Assign()).writexml(file, addindent="\t", newl="\n")
		createKitChain().writexml(file, addindent="\t", newl="\n")
		self.createMasterEffects().writexml(file, addindent="\t", newl="\n")
		file.close()
		
	def createTest(self):
		self.createIn("D:\\gear\\spd-sx\\sysparam_gen.spd")
		
		
		
