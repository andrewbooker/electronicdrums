#!/usr/bin/env python

class Thru():
	type = 0
	def asSpec(self):
		return []

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