#!/usr/bin/env python

import soundfile as sf
import os
import xml.dom.minidom
from wave import Wave

sampledir = "D:\\Samples\\bass\\synth"
samples = {34: ["02_Bb.wav"]}

for sampleNote, wavs in samples.items():
	for idx in range(len(wavs)):
		fn = "%s\\%s\\%s" % (sampledir, sampleNote, wavs[idx])
		sampleFile = sf.SoundFile(fn, "r")
		size = sampleFile.frames
		print("found %d frames in %s" % (size, fn))

		waveFn = "%s/%s%d%.2d.wav" % (90, "bass", sampleNote, idx)
		wave = Wave(idx, "90", waveFn)
		for i in range(size):
			wave.write(sampleFile.read())
		wave.close()

print("done")
