#!/usr/bin/env python

import xml.dom.minidom
doc = xml.dom.minidom.parseString("<KitPrm/>")

kitPrm = doc.documentElement
level = kitPrm.appendChild(doc.createElement("Level"))
level.appendChild(doc.createTextNode("100"))


kitPrm.writexml(open("D:\\gear\\spd-sx\\sandbox\\Roland\\SPD-SX\\KIT\\kit099.spd", "w"), addindent="\t", newl="\n")

