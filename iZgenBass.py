#!/usr/bin/env python

import soundfile as sf
import os
import xml.dom.minidom
from wave import Wave

sampledir = "D:\\Samples\\bass\\synth"

baseNote = 33
samples = {}
for n in range(12):
	note = baseNote + n
	notePath = os.path.join(sampledir, str(note))
	if os.path.isdir(notePath):
		samples[baseNote + n] = [f for f in os.listdir(notePath) if os.path.isfile(os.path.join(notePath, f))]

num = 0
loc = 90

for sampleNote, wavs in samples.items():
	for idx in range(len(wavs)):
		fn = "%s\\%s\\%s" % (sampledir, sampleNote, wavs[idx])
		data, sampleRate = sf.read(fn)
		size = len(data)
		print("found %d frames in %s" % (size, fn))
		
		waveFn = "%s/%s%d%.2d.wav" % (loc, "bass", sampleNote, idx)
		wave = Wave(num, str(loc), waveFn)
		for i in range(size):
			c = 1.0 if i < (size / 2) else (2.0 - (2.0 * i / size)) 
			wave.write(c * data[i])
		wave.close()
		num += 1

print("done")
