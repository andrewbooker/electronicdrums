#!/usr/bin/env python

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
	
class RingMod():
	type = 16

	def freq(self, v):
		self.freq = v
		return self
		
	def sens(self, v):
		self.sens = v
		return self
		
	def balance(self, v):
		self.balance = v
		return self
		
	def asSpec(self):
		polarity = 0
		return [self.freq, self.sens, polarity, 15, 15, int(100 * self.balance), 100]
		
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