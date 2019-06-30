#!/usr/bin/env python

import soundfile as sf
import os
import math


class Resize():
	def __init__(self):
		self.buffer = []
		
	def add(self, d):
		self.buffer.append(d)
		
	def read(self, f):
		out = []
		for i in range(len(self.buffer)):
			p = i / f(i)
			u = math.floor(p)
			l = math.ceil(p)
			dp = p - l
			out.append(((1 - dp) * self.buffer[l]) + (dp * self.buffer[u]))
		
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
		

def combine(fnOnto, s1, s2, op):
	loc = "D:\\gear\\spd-sx\\sandbox\\Roland\\SPD-SX\\WAVE\\DATA"
	f1 = sf.SoundFile("%s\\%s" % (loc, s1), "r")
	f2 = sf.SoundFile("%s\\%s" % (loc, s2), "r")
	
	locOut = "E:\\Roland\\SPD-SX\\WAVE\\DATA"
	fqfnOut = "%s\\%s" % (locOut, fnOnto)
	
	size = max(f1.frames, f2.frames)
	resize1 = Resize()
	resize2 = Resize()
	
	resize1.buffer = f1.read()
	resize2.buffer = f2.read()
	
	f1.close()
	f2.close()
		
	print("%d in %s" % (len(resize1.buffer), s1))
	print("%d in %s" % (len(resize2.buffer), s2))
	r1 = resize1.read(lambda i: 1.7)
	r2 = resize2.read(lambda i: 1.2)
	lr1 = len(r1)
	lr2 = len(r2)
	print("now %d in %s" % (lr1, s1))
	print("now %d in %s" % (lr2, s2))
	
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


def generateRightFoot(fnOnto):
	print("generating right foot sound")
	combine(fnOnto, "00\\Kick__17.wav", "01\\Tom_A_01.wav", EnvelopeFollow())
	
def generateCym(fnOnto):
	print("generating cymbal sound")
	combine(fnOnto, "00\\Cym_8.wav", "00\\Ride__02.wav", ShortXFade())
	
	
	