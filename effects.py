#!/usr/bin/env python

from random import randint

class Thru():
	type = 0
	def asSpec(self):
		return []

class SyncDelay():
	type = 2
	
	def feedback(self, v):
		self.feedback = v
		return self
		
	def effLevel(self, v):
		self.effLevel = v
		return self
		
	def asSpec(self):
		return [0, 7, 100, self.feedback, 1, 9, self.effLevel, 100]
	
class TapeEcho():
	type = 3
	
	@staticmethod
	def createRandom():
		e = TapeEcho()
		e.mode = 2 #long
		e.repeatRate = 30 #0-127, modulated
		e.intensity = 50 #0-127, modulated
		e.distortion = 4 #0-5
		e.wowFlutterRate = 47 #0-127
		e.wowFlutterDepth = 81 #0-127
		return e
	
	def asSpec(self):
		return [self.mode, self.repeatRate, self.intensity, 12, 10, 64, 64, 64, self.distortion, self.wowFlutterRate, self.wowFlutterDepth, 65, 100, 100]
		
	
class Chorus():
	type = 4
	
	def rate(self, v):
		self.rate = v
		return self
		
	def depth(self, v):
		self.depth = v
		return self
		
	def preDelayMs(self, v):
		self.preDelayMs = v
		return self
		
	def asSpec(self):
		return [1, self.rate, self.depth, self.preDelayMs * 2, 4, 9, 50, 100]
	
class Phaser():
	type = 7
	def rate(self, v):
		self.rate = v
		return self
		
	def depth(self, v):
		self.depth = v
		return self
		
	def manual(self, v):
		self.manual = v
		return self
		
	def resonance(self, v):
		self.resonance = v
		return self
		
	def separation(self, v):
		self.separation = v
		return self
		
	def asSpec(self):
		stageType = 1
		rateSync = 0
		return [stageType, rateSync, self.rate, 0, self.depth, self.manual, self.resonance, self.separation, 100, 100]
		
	@staticmethod
	def createRandom():
		e = Phaser()
		e.rate(randint(10, 100))
		e.depth(randint(40, 100))
		e.manual(randint(40, 100))
		e.resonance(randint(40, 100))
		e.separation(randint(10, 100))
		return e
	
class FilterPlusDrive():
	type = 12
	
	@staticmethod
	def createRandom():
		e = FilterPlusDrive()
		e.cutoff = 64 #0-127 modulated
		e.resonance = 21 #0-127
		e.drive = 39 #0-127 modulated
		return e
		
	def asSpec(self):
		return [self.cutoff, self.resonance, self.drive, 80]

class RingMod():
	type = 16

	def freq(self, v):
		self.freq = v
		return self
		
	def sens(self, v):
		self.sens = v
		return self
		
	def polarity(self, v):
		self.polarity = v
		return self
		
	def balance(self, v):
		self.balance = v
		return self
		
	def asSpec(self):
		return [self.freq, self.sens, self.polarity, 15, 15, int(100 * self.balance), 100]
		
class PitchShift():
	type = 17
	
	def pitch(self, v):
		self.pitch = v
		return self
		
	def feedback(self, v):
		self.feedback = v
		return self
		
	def asSpec(self):
		fine = 50
		return [24 + self.pitch, fine, self.feedback, 100, 100]
		
class Vibrato():
	type = 18
	
	def rate(self, v):
		self.rate = v
		return self
		
	def depth(self, v):
		self.depth = v
		return self
		
	def asSpec(self):
		return [self.rate, self.depth]
		
		
class Reverb():
	type = 19
	
	def time(self, v):
		self.time = v
		return self
		
	def preDelay(self, v):
		self.preDelay = v
		return self
		
	def density(self, v):
		self.density = v
		return self
	
	def effLevel(self, v):
		self.effLevel = v
		return self
	
	def asSpec(self):
		directLevel = 100
		globalReverbLevel = 50
		return [2, self.time, self.preDelay, 1, 2, self.density, self.effLevel, directLevel, globalReverbLevel]
		
		
