#!/usr/bin/env python

from xml.dom import minidom
import sys
import json

doc = minidom.parse(sys.argv[1])


kit = {}

root = doc.getElementsByTagName("KitPrm")[0]
for p in root.childNodes:
    if p.nodeType != p.TEXT_NODE:
        if p.tagName == "Level":
            kit["level"] = int(p.childNodes[0].data)
        if p.tagName == "Tempo":
            kit["tempo"] = int(0.1 * int(p.childNodes[0].data))

print(kit)
