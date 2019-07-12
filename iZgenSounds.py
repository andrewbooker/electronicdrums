#!/usr/bin/env python

import soundfile as sf
import os
import math
from random import uniform, randint
import xml.dom.minidom


def any(a, exceptions = []):
	f = a[randint(0, len(a) - 1)]
	if f in exceptions:
		return any(a, exceptions)
	return f


class Resize():
	maxLength = 66150 #1.5 seconds
	
	def __init__(self):
		self.buffer = []
		
	def add(self, d):
		self.buffer.append(d)
		
	def read(self, f):
		inSize = len(self.buffer)
		out = []
		i = 0
		done = False
		while not done:
			vol = 1 - (i / (1.0 * Resize.maxLength))
			p = i / f(i)
			u = math.floor(p)
			l = math.ceil(p)
			if (u < inSize and l < inSize and i < Resize.maxLength):
				dp = p - l
				out.append(vol * (((1 - dp) * self.buffer[l]) + (dp * self.buffer[u])))
			else:
				done = True
			i += 1

		return out
		
class Avg():
	def on(self, d1, d2, i, size):
		return (d1 * 0.5) + (d2 * 0.5)
	
	def isDone(self, hasF1, hasF2):
		return not hasF1 and not hasF2
		
class LinearXFade():
	def on(self, d1, d2, i, size):
		f = 1.0 * i / size
		return (d1 * (1 - f)) + (d2 * f)
	
	def isDone(self, hasF1, hasF2):
		return not hasF1 and not hasF2
		
class XChop():
	def __init__(self):
		self.freq = uniform(400.0, 4000.0)
		
	def on(self, d1, d2, i, size):
		f = 1.0 + (0.5 * math.cos(i / self.freq))
		return (d1 * (1 - f)) + (d2 * f)
	
	def isDone(self, hasF1, hasF2):
		return not hasF1 and not hasF2
		
class ShortXFade():
	def on(self, d1, d2, i, size):
		f = 1.0 / ((20.0 * i / size) + 1.0)
		return (d1 * (1 - f)) + (d2 * f)
	
	def isDone(self, hasF1, hasF2):
		return not hasF1 and not hasF2

class EnvelopeFollow():
	def on(self, d1, d2, i, size):
		return abs(d1) * d2
	
	def isDone(self, hasF1, hasF2):
		return not hasF1 or not hasF2
		
class Multiply():
	def on(self, d1, d2, i, size):
		return d1 * d2
	
	def isDone(self, hasF1, hasF2):
		return not hasF1 or not hasF2
		

class Gradient():
	@staticmethod
	def any():
		return Gradient(uniform(0.3, 2.7), uniform(0.3, 2.7))

	def __init__(self, y1, y2):
		self.y1 = y1
		self.y2 = y2
		
	def at(self, i):
		return self.y1 + (i * (self.y2 - self.y1) / Resize.maxLength)
		


def prepFqFnOut(fnOnto, type):
	subDir, fnOut = fnOnto.split("/")
	locOut = "E:\\Roland\\SPD-SX\\WAVE"
	dir = "%s\\%s\\%s" % (locOut, type, subDir)
	if not os.path.exists(dir):
		os.makedirs(dir)
	return "%s\\%s" % (dir, fnOut)

def combine(fnOnto, s1, s2, op):
	loc = "D:\\gear\\spd-sx\\sandbox\\Roland\\SPD-SX\\WAVE\\DATA"
	f1 = sf.SoundFile("%s\\%s" % (loc, s1), "r")
	f2 = sf.SoundFile("%s\\%s" % (loc, s2), "r")
	
	print("combining %s with %s using %s" % (s1, s2, type(op).__name__))
	fqfnOut = prepFqFnOut(fnOnto, "DATA")
	
	size = max(f1.frames, f2.frames)
	resize1 = Resize()
	resize2 = Resize()
	
	resize1.buffer = f1.read()
	resize2.buffer = f2.read()
	
	f1.close()
	f2.close()
	
	g1 = Gradient.any()
	g2 = Gradient.any()
	r1 = resize1.read(g1.at)
	r2 = resize2.read(g2.at)
	lr1 = len(r1)
	lr2 = len(r2)
	
	if os.path.exists(fqfnOut):
		os.remove(fqfnOut)
	out = sf.SoundFile(fqfnOut, mode="x", samplerate=44100, channels=1, subtype="PCM_16")
	
	i = 0
	done = False
	while (not done):
		hasF1 = i < lr1
		hasF2 = i < lr2
		data = [r1[i] if hasF1 else 0, r2[i] if hasF2 else 0]	
		out.write(op.on(data[0], data[1], i, size))
		done = op.isDone(hasF1, hasF2)
		i += 1
	
	out.close()
	
	


def param(doc, onto, name, value):
	onto.appendChild(doc.createElement(name)).appendChild(doc.createTextNode(str(value)))
	

def prm(fnOnto, name, wavPath):
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
	
	fqfnOut = prepFqFnOut(fnOnto, "PRM")
	file = open(fqfnOut, "w")
	wvPrm.writexml(file, addindent="\t", newl="\n")
	file.close()
	
	

kick = [
	"00/Kick_.wav",
	"00/Kick__01.wav",
	"00/Kick__02.wav",
	"00/Kick__03.wav",
	"00/Kick__04.wav",
	"00/Kick__05.wav",
	"00/Kick__06.wav",
	"00/Kick__07.wav",
	"00/Kick__08.wav",
	"00/Kick__09.wav",
	"00/Kick__10.wav",
	"00/Kick__11.wav",
	"00/Kick__12.wav",
	"00/Kick__13.wav",
	"00/Kick__14.wav",
	"00/Kick__15.wav",
	"00/Kick__16.wav",
	"00/Kick__17.wav",
	"00/Kick__18.wav",
	"00/Kick__19.wav"
]
		
snare = [
	"01/Snare.wav",
	"01/Snare_01.wav",
	"01/Snare_02.wav",
	"01/Snare_03.wav",
	"01/Snare_04.wav",
	"01/Snare_05.wav",
	"01/Snare_06.wav",
	"01/Snare_07.wav",
	"01/Snare_08.wav",
	"01/Snare_09.wav",
	"01/Snare_10.wav",
	"01/Snare_11.wav",
	"01/Snare_12.wav",
	"01/Snare_13.wav",
	"01/Snare_14.wav",
	"01/Snare_15.wav",
	"01/Snare_16.wav",
	"01/Snare_17.wav",
	"01/Snare_18.wav",
	"01/Snare_19.wav",
	"01/Snare_20.wav",
	"01/Snare_21.wav",
	"01/Snare_22.wav",
	"01/Snare_23.wav",
	"01/Snare_24.wav",
	"02/snare.wav",
	"02/snare_01.wav",
	"02/snare_02.wav"
]

cym = [
	"00/Ride_.wav",
	"00/Ride__01.wav",
	"00/Ride__02.wav",
	"00/Ride__03.wav",
	"00/Ride__04.wav",
	"00/Cym_8.wav",
	"00/Cym_C_03.wav",
	"00/Cym_F_01.wav",
	"00/Cym_S_01.wav",
	"00/P_Gon.wav",
	"00/P_Tri_01.wav",
	"00/HH_01.wav",
	"00/HH_03.wav",
	"00/HH_Ac_01.wav",
	"00/HH_Db_01.wav",
	"00/HH_Dn_01.wav",
	"00/HH_Hs_01.wav",
	"00/HH_Hs_03.wav",
	"00/HH_Pr_01.wav",
	"00/HH_Pr_03.wav",
	"00/HH_Hp_01.wav",
	"01/SE_Ve.wav"
]

tom = [
	"01/Tom_8.wav",
	"01/Tom_8_01.wav",
	"01/Tom_8_02.wav",
	"01/Tom_A.wav",
	"01/Tom_A_01.wav",
	"01/Tom_A_02.wav",
	"01/Tom_E.wav",
	"01/Tom_E_01.wav",
	"01/Tom_E_02.wav",
	"01/Tom_R.wav",
	"01/Tom_R_01.wav",
	"01/Tom_R_02.wav",
	"02/roto8.wav",
	"02/roto8_01.wav",
	"00/P_Tim.wav",
	"00/P_Tim_01.wav",
	"02/timba.wav",
	"02/timba_01.wav",
	"02/timba_02.wav",
	"02/tom13.wav",
	"02/tom13_01.wav",
	"02/tom13_02.wav",
	"02/tom16.wav",
	"02/tom16_01.wav"
]

perc = [
	"00/Clap_.wav",
	"00/Clap__01.wav",
	"00/Clap__02.wav",
	"00/Clap__03.wav",
	"00/Clap__04.wav",
	"00/Clap__05.wav",
	"00/Clap__06.wav",
	"00/Clap__07.wav",
	"00/HH.wav",
	"00/HH_02.wav",
	"00/HH_Ac.wav",
	"00/HH_Db.wav",
	"00/HH_Dn.wav",
	"00/HH_Hp.wav",
	"00/HH_Hs.wav",
	"00/HH_Hs_02.wav",
	"00/HH_Pr.wav",
	"00/HH_Pr_02.wav",
	"00/HH_Pr_04.wav",
	"00/P_Gan.wav",
	"00/P_Cla.wav",
	"00/P_Con.wav",
	"00/P_Con_01.wav",
	"00/P_Con_02.wav",
	"00/P_Tab.wav",
	"00/P_Tab_01.wav",
	"00/P_Tab_02.wav",
	"00/P_Tab_03.wav",
	"00/P_Tam.wav",
	"00/P_Tam_01.wav",
	"00/P_Tam_02.wav",
	"00/P_Tri.wav",
	"00/SE_Cr.wav",
	"01/SE_Sw.wav"
]
		 

def generateRightFoot(fnOnto):
	print("generating right foot sound")
	s1 = any(kick)
	combine(fnOnto, s1, any(kick, [s1]), XChop())
	
def generateLeftFoot(fnOnto):
	print("generating left foot sound")
	combine(fnOnto, any(tom),  any(perc), XChop())
	
def generatePadTop(fnOnto):
	print("generating pad top sound")
	s1 = any(snare)
	combine(fnOnto, s1, any(snare, [s1]), XChop())
	
def generatePadRim(fnOnto):
	print("generating pad rim sound")
	s1 = any(tom)
	combine(fnOnto, s1, any(tom, [s1]), XChop())
	
def generateCym(fnOnto):
	print("generating cymbal sound")
	s1 = any(cym)
	combine(fnOnto, s1, any(cym, [s1]), XChop())
	
def generatePerc(fnOnto):
	print("generating perc sound")
	s1 = any(perc)
	combine(fnOnto, s1, any(perc, [s1]), XChop())
	
	
	