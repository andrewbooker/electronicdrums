#!/usr/bin/env python

import os
import xml.dom.minidom

loc = "D:\\gear\\spd-sx\\sandbox\\Roland\\SPD-SX\\WAVE\\PRM"
batch = "01"

for f in os.listdir("%s\\%s" % (loc, batch)):
	doc = xml.dom.minidom.parse("%s\\%s\\%s" % (loc, batch, f))
	
	n = []
	for i in range(12):
		n.append(int(doc.getElementsByTagName("Nm%d" % i)[0].childNodes[0].data))
		
	print("0%s%s: %s" % (batch, f[:2], "".join(chr(c) for c in n)))
	
	
