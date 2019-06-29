#!/usr/bin/env python

import soundfile as sf
import os


def generateRightFoot(fnOnto):
	loc = "D:\\gear\\spd-sx\\sandbox\\Roland\\SPD-SX\\WAVE\\DATA"
	f1 = sf.SoundFile("%s\\%s" % (loc, "00\\Kick__17.wav"), "r")
	f2 = sf.SoundFile("%s\\%s" % (loc, "01\\Tom_A_01.wav"), "r")
	
	locOut = "E:\\Roland\\SPD-SX\\WAVE\\DATA"
	fqfnOut = "%s\\%s" % (locOut, fnOnto)
	
	if os.path.exists(fqfnOut):
		os.remove(fqfnOut)
	
	out = sf.SoundFile(fqfnOut, mode="x", samplerate=44100, channels=1, subtype="PCM_16")
	
	i = 0
	done = False
	while (not done):
		hasF1 = f1.tell() < f1.frames
		hasF2 = f2.tell() < f2.frames
		
		data = [0, 0]
		if hasF1:
			data[0] = f1.read(1)[0]
		if hasF2:
			data[1] = f2.read(1)[0]
			
		out.write(data[0] * data[1])
		done = not hasF1 and not hasF2
	
	f1.close()
	f2.close()
	out.close()
	
	