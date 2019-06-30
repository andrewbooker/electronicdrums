#!/usr/bin/env python

import soundfile as sf
import os
import math


class Stretch():
	def __init__(self):
		self.buffer = []
		
	def on(self, d, i, f):
		self.buffer.append(d)
		if (len(self.buffer) == 1):
			return d
		
		p = i / f
		u = math.floor(p)
		l = math.ceil(p)
		dp = p - l
		return ((1 - dp) * self.buffer[l]) + (dp * self.buffer[u])
		
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
	
	if os.path.exists(fqfnOut):
		os.remove(fqfnOut)
	
	out = sf.SoundFile(fqfnOut, mode="x", samplerate=44100, channels=1, subtype="PCM_16")
	
	i = 0
	done = False

	size = max(f1.frames, f2.frames)
	stretch = Stretch()
	while (not done):
		hasF1 = f1.tell() < f1.frames
		hasF2 = f2.tell() < f2.frames
		
		data = [0, 0]
		if hasF1:
			data[0] = stretch.on(f1.read(1)[0], i, 1.6)
		if hasF2:
			data[1] = f2.read(1)[0]
			
		out.write(op.on(data[0], data[1], i, size))
		done = op.isDone(hasF1, hasF2)
		i += 1
	
	f1.close()
	f2.close()
	out.close()


def generateRightFoot(fnOnto):
	print("generating right foot sound")
	combine(fnOnto, "00\\Kick__17.wav", "01\\Tom_A_01.wav", EnvelopeFollow())
	
def generateCym(fnOnto):
	print("generating cymbal sound")
	combine(fnOnto, "00\\Cym_8.wav", "00\\Ride__02.wav", ShortXFade())
	
	
	