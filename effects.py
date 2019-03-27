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