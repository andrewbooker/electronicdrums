#!/usr/bin/env python

from xml.dom import minidom
import sys
import json
import math
from effects import *
from sounds import sounds

padOrder = [
    "topLeft",
    "topCentre",
    "topRight",
    "midLeft",
    "midCentre",
    "midRight",
    "bottomLeft",
    "bottomCentre",
    "bottomRight",
    "footRight",
    "footLeft",
    "padTop",
    "padRim"
]

genSounds = {
    93: "no",
    94: "cy",
    95: "pe",
    96: "pr",
    97: "pt",
    98: "lf",
    99: "bd"
}


doc = minidom.parse(sys.argv[1])


def kitNameFrom(node):
    n = []
    for i in range(8):
        c = int(node.getElementsByTagName("Nm%d" % i)[0].childNodes[0].data)
        if c > 31:
            n.append(chr(c))
    return "".join(n)

def effectFrom(node, n):
    a = []
    t = int(node.getElementsByTagName("Fx%dType" % n)[0].childNodes[0].data)
    for i in range(20):
        v = int(node.getElementsByTagName("Fx%dPrm%d" % (n, i))[0].childNodes[0].data)
        if v != 0:
            a.append(v)
    if t == 19:
        return Reverb.fromSpec(a)
    return {}

def soundFrom(i):
    if i > 9299:
        pref = genSounds[math.floor(i / 100)]
        idx = i % 100
        return "%s_%09d" % (pref, idx)

    for s in sounds:
        if sounds[s] == i:
            return s
    return ""

kit = {}

kit["name"] = kitNameFrom(doc)

root = doc.getElementsByTagName("KitPrm")[0]
for p in root.childNodes:
    if p.nodeType != p.TEXT_NODE:
        if p.tagName == "Level":
            kit["level"] = int(p.childNodes[0].data)
        if p.tagName == "Tempo":
            kit["tempo"] = int(0.1 * int(p.childNodes[0].data))


pads = doc.getElementsByTagName("PadPrm")

kit["pads"] = {}

for p in range(len(pads[:13])):
    pad = {}
    for c in pads[p].childNodes:
        if c.nodeType != c.TEXT_NODE:
            if c.tagName == "Wv":
                pad["wav"] = soundFrom(int(c.childNodes[0].data))
    kit["pads"][padOrder[p]] = pad

kit["fx1"] = effectFrom(doc, 1)
print(json.dumps(kit, indent="    "))
