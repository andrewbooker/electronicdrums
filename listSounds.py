#!/usr/bin/env python

import os
import xml.dom.minidom

loc = "D:\\gear\\spd-sx\\sandbox\\Roland\\SPD-SX\\WAVE\\PRM"
batches = ["00", "01", "02", "03"]

sounds = []

for batch in batches:
	for f in os.listdir("%s\\%s" % (loc, batch)):
		doc = xml.dom.minidom.parse("%s\\%s\\%s" % (loc, batch, f))
		
		kn = int("0%s%s" % (batch, f[:2]))
		n = []
		for i in range(12):
			c = int(doc.getElementsByTagName("Nm%d" % i)[0].childNodes[0].data)
			if c:
				n.append(c)
		
		name = "".join(chr(c) for c in n)
		sounds.append((name, kn))
	
print("sounds = {")
print(", \n".join("\"%s\":%d" % (s[0], s[1]) for s in sounds))
print("}")
	
