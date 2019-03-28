#!/usr/bin/env python

class Thru():
	type = 0
	def asSpec(self):
		return []

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
		return [self.freq, self.sens, 0, 15, 15, int(100 * self.balance), 100]
		
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