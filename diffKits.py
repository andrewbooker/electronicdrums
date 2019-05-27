#!/usr/bin/env python

import os
import glob

locDump = "D:\\gear\\spd-sx\\kit dumps\\2019-05-27"
locGen = "D:\\gear\\spd-sx\\sandbox\\Roland\\SPD-SX\\KIT"

#actuals = glob.glob("%s\\*" % locDump)
actuals = os.listdir(locDump)
for a in actuals:
	actual = open("%s\\%s" % (locDump, a), "r")
	gfn = "%s\\%s" % (locGen, a)
	if (os.path.isfile(gfn)):
		generated = open("%s\\%s" % (locGen, a), "r")
		
		print(a)
		
		als = actual.readlines()
		gls = generated.readlines()
		i = 0
		
		for al in als:
			if ((len(gls) > i) and (al != gls[i])):
				print("%d: actual %s != generated %s" % (i, al, gls[i]))
			i += 1
		
		generated.close()
	actual.close()
		
	

