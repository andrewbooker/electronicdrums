#!/usr/bin/env python

from kit import Kit
from sysConfig import SystemConfig
from effects import RingMod

loc = "E:\\Roland\\SPD-SX"
#loc = "D:\\gear\\spd-sx\\sandbox\\Roland\\SPD-SX"


def buildKits():
	cpp = open("tbb_2019.h", "w")
	kn = 50
	set = __import__("tbb2019")
	for n, cl in set.__dict__.items():
		if isinstance(cl, type) and hasattr(cl, "level"):
			name = n[:8]
			Kit().build(cl, name, "%s\\KIT" % loc, kn)

			cpp.write("DefineTrack( %s ) {\n" % n) 
			cpp.write("\ttbb_2019( tracks, %d, spdsx_fx::%s, %d );\n" % (kn + 1, "ringMod" if hasattr(cl, "applyMasterFx") else "none", cl.korg if hasattr(cl, "korg") else 13))
			cpp.write("}\n")
			
			kn += 1
	cpp.close()
			
buildKits()
		
c = SystemConfig()
c.footTriggerTypes = [29, 0] #29: RT-30K, 30: RT-30HR
c.inAssign = 0 #master
c.fxModOn = 1
c.masterFx = RingMod()

c.createIn("%s\\SYSTEM\\sysparam.spd" % loc)