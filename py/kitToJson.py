#!/usr/bin/env python3

from xml.dom import minidom
import sys
import os
import json
import math
import time
import serial  # sudo pip install pyserial
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


class KitLocation:
    @staticmethod
    def config():
        with open("py/config.json") as conf:
            return json.load(conf)

    def __init__(self):
        self.mediaLoc = KitLocation.config()["mediaLoc"]
        self.isSpdSx = "/media" in self.mediaLoc
        self.sp = None
        if os.path.exists("/dev/ttyUSB0"):
            self.sp = serial.Serial("/dev/ttyUSB0")

    def __del__(self):
        if self.isSpdSx and self.sp is not None:
            print("Disconnecting from SPD-SX")
            os.system("umount %s" % self.mediaLoc)
            self.sp.setDTR(False)

    def get(self):
        if self.isSpdSx and self.sp is not None:
            print("Connecting to SPD-SX")
            self.sp.setDTR(True)
            while not os.path.exists(self.mediaLoc):
                time.sleep(0.1)
        return os.path.join(self.mediaLoc, "Roland", "SPD-SX")


kitLoc = KitLocation()
doc = minidom.parse(os.path.join(kitLoc.get(), "KIT", sys.argv[1]))


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


kit = dict()
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
with open(sys.argv[2], "w") as outfile:
    print(json.dump(kit, outfile, indent=4))
