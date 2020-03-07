#!/usr/bin/env python

import os
import soundfile as sf
import xml.dom.minidom


def param(doc, onto, name, value):
	onto.appendChild(doc.createElement(name)).appendChild(doc.createTextNode(str(value)))
	

def prm(fqfnOut, name, wavPath):
	doc = xml.dom.minidom.parseString("<WvPrm/>")
	wvPrm = doc.documentElement
	
	for i in range(12):
		param(doc, wvPrm, "Nm%d" % i, ord(name[i]))

	param(doc, wvPrm, "Tag", 0)
	param(doc, wvPrm, "Tempo", 1200)
	param(doc, wvPrm, "Beat", 0)
	param(doc, wvPrm, "Measure", 0)
	param(doc, wvPrm, "Start", 0)
	param(doc, wvPrm, "End", 0)
	param(doc, wvPrm, "Path", wavPath)
	
	file = open(fqfnOut, "w")
	wvPrm.writexml(file, addindent="\t", newl="\n")
	file.close()
	


class Wave():
	@staticmethod
	def prepFqFnOut(fnOnto, type):
		subDir, fnOut = fnOnto.split("/")
		locOut = "E:\\Roland\\SPD-SX\\WAVE"
		dir = "%s\\%s\\%s" % (locOut, type, subDir)
		if not os.path.exists(dir):
			os.makedirs(dir)
		return "%s\\%s" % (dir, fnOut)
		
	def __init__(self, idx, subDir, fn):
		self.fn = fn
		self.idx = idx
		self.subDir = subDir
		fqn = Wave.prepFqFnOut(fn, "DATA")
		
		if os.path.exists(fqn):
			os.remove(fqn)
			
		print("creating %s" % fqn)
		self.file = sf.SoundFile(fqn, mode="x", samplerate=44100, channels=1, subtype="PCM_16")
	
	def write(self, d):
		self.file.write(d)
		
	def close(self):
		self.file.close()
		fqn = Wave.prepFqFnOut("%s/%.2d.spd" % (self.subDir, self.idx), "PRM")
		print("creating %s" % fqn)
		prm(fqn, "bd_%.10d" % self.idx, self.fn) 