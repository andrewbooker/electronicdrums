#!/usr/bin/env python

import os
import glob

locDump = "D:\\gear\\spd-sx\\kit dumps\\2019-05-27"
locGen = "D:\\gear\\spd-sx\\sandbox\\Roland\\SPD-SX\\KIT"

#actuals = glob.glob("%s\\*" % locDump)
actuals = os.listdir(locDump)
ignore = ["kit057.spd", "kit068.spd"]
f = 0
for a in actuals:
	actual = open("%s\\%s" % (locDump, a), "r")
	gfn = "%s\\%s" % (locGen, a)
	if (os.path.isfile(gfn) and int(a[3:6]) > 49 and a not in ignore):
		anything = False
		generated = open("%s\\%s" % (locGen, a), "r")
		
		
		
		als = actual.readlines()
		gls = generated.readlines()
		i = 0
		
		for al in als:
			if ((len(gls) > i) and (al != gls[i])):
				if (not anything):
					print(a)
					anything = True
				print("%d: actual %s != generated %s" % (i, al, gls[i]))
				f += 1
			i += 1
		
		generated.close()
	actual.close()
	
print("%d diff%s found" % (f, "s" if (f != 1) else ""))
		
	

