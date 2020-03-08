#!/usr/bin/env python

import soundfile as sf
import os
import xml.dom.minidom
from wave import Wave

sampledir = "D:\\Samples\\bass\\synth"
samples = {34: ["02_Bb.wav"]}

num = 0 #goes with 90 as the location
for sampleNote, wavs in samples.items():
	for idx in range(len(wavs)):
		fn = "%s\\%s\\%s" % (sampledir, sampleNote, wavs[idx])
		data, sampleRate = sf.read(fn)
		size = len(data)
		print("found %d frames in %s" % (size, fn))

		loc = 90
		waveFn = "%s/%s%d%.2d.wav" % (loc, "bass", sampleNote, idx)
		wave = Wave(num, str(90), waveFn)
		for i in range(size):
			c = 1.0 if i < (size / 2) else (2.0 - (2.0 * i / size)) 
			wave.write(c * data[i])
		wave.close()
		num += 1

print("done")
