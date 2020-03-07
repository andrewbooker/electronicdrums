#!/usr/bin/env python

import soundfile as sf
import os
import xml.dom.minidom
from wave import Wave

sampledir = "D:\\Samples\\bass\\synth"
samples = [34, 36, 38, 39, 41, 43]

fn = "%s\\%s\\%s" % (sampledir, samples[0], "02_Bb.wav")
sampleFile = sf.SoundFile(fn, "r")
size = sampleFile.frames
print("found %d frames in %s" % (size, fn))


idx = 0
waveFn = "%s/%s%.4d.wav" % (90, "bass", idx)
wave = Wave(idx, "90", waveFn)
for i in range(size):
	wave.write(sampleFile.read())
wave.close()

print("done")
