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
		return [0, 7, 100, self.feedback, 1, 9, self.effLevel, 100] #note the delay will max out at 1300ms
	
class TapeEcho():
	type = 3
	
	@staticmethod
	def createRandom():
		e = TapeEcho()
		e.mode = 5 #med+long
		e.repeatRate = 30 #0-127, modulated
		e.intensity = 50 #0-127, modulated
		e.distortion = randint(1, 5)
		e.wowFlutterRate = randint(10, 110)
		e.wowFlutterDepth = randint(50, 127)
		return e
	
	def asSpec(self):
		return [self.mode, self.repeatRate, self.intensity, 12, 10, 64, 1, 127, self.distortion, self.wowFlutterRate, self.wowFlutterDepth, 65, 100, 100]
		
	
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
		
	@staticmethod
	def createRandom():
		e = Chorus()
		e.rate(randint(10, 100))
		e.depth(randint(40, 100))
		e.preDelayMs(randint(1, 100))
		return e
	
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
		e.cutoff = randint(20, 127) # modulated
		e.resonance = randint(40, 127)
		e.drive = randint(10, 120) # modulated
		return e
		
	def asSpec(self):
		return [self.cutoff, self.resonance, self.drive, 80]

class TouchWah():
	type = 14
	
	@staticmethod
	def createRandom():
		e = TouchWah()
		e.polarity = randint(0, 1)
		e.sensitivity = randint(20, 100) # modulated
		e.cutoff = randint(10, 100) # modulated
		e.q = randint(50, 100)
		return e
	
	def asSpec(self):
		return [0, self.polarity, self.sensitivity, self.cutoff, self.q, 100, 100]
	
class Distortion():
	type = 15
	
	@staticmethod
	def createRandom():
		e = Distortion()
		e.distType = randint(0, 24)
		e.drive = randint(10, 120)
		e.bottom = 50 #0-100
		e.tone = 40 #0-100
		e.level = 30 # 0-100 keep low, maybe fn of disttype and drive
		return e
	
	def asSpec(self):
		return [self.distType, self.drive, self.bottom, self.tone, self.level, 50]
	
class RingMod():
	type = 16
	
	def __init__(self):
		self.balance = 0.5
		self.polarity(0)
		self.freq(64)
		self.sens(10)

	def freq(self, v):
		self.frequ = v
		return self
		
	def sens(self, v):
		self.sensi = v
		return self
		
	def polarity(self, v):
		self.pol = v
		return self
	
	def asSpec(self):
		return [self.frequ, self.sensi, self.pol, 15, 15, int(100 * self.balance), 100]
		
	@staticmethod
	def createRandom():
		e = RingMod()
		e.freq(randint(1, 127))
		e.sens(randint(30, 127))
		e.polarity(randint(0, 1))
		return e
		
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
		
	@staticmethod
	def createRandom():
		e = PitchShift()
		e.pitch(randint(-24, 24))
		e.feedback(randint(1, 99))
		return e
		
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
		
	@staticmethod
	def createRandom():
		e = Vibrato()
		e.rate(randint(5, 100))
		e.depth(randint(20, 100))
		return e
		
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
		
	@staticmethod
	def createRandom():
		e = Reverb()
		e.time(randint(10, 90))
		e.preDelay(randint(10, 99))
		e.density(randint(1, 10))
		e.effLevel(50)
		return e
		
class Slicer():
	type = 20
	
	@staticmethod
	def createRandom():
		e = Slicer()
		e.pattern = randint(0, 15)
		e.attack = randint(1, 127)
		return e
		
	def asSpec(self):
		return [self.pattern, 1, 8, self.attack]