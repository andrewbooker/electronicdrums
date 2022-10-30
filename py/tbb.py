
from kit import Kit
from sysConfig import SystemConfig
from effects import RingMod
from sounds import sounds as wav
import os
import json

padOutAssign = {
    "padOutMaster": 0,
    "padOutFx1": 1,
    "padOutFx2": 2,
    "padOutSub": 3,
    "padOutPhones": 4
}

padNames = [
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

def readKits():
    with open(os.path.join("kits", "tbb_2019.json")) as js:
        return json.load(js)

def readFromJson():
    into = []
    kits = readKits()
    for kit in kits:
        k = type(kit["name"], (), {})
        k.level = kit["level"] if "level" in kit else 100
        k.tempo = kit["tempo"]
        k.pads = []

        for i in range(13):
            pad = {}
            if padNames[i] in kit["pads"]:
                padSpec = kit["pads"][padNames[i]]
                if "wav" in padSpec:
                    pad["sound"] = wav[padSpec["wav"]]
                if "vol" in padSpec:
                    pad["vol"] = wav[padSpec["vol"]]
                if "outAssign" in padSpec:
                    pad["outAssign"] = padOutAssign[padSpec["outAssign"]]
            k.pads.append(pad)
        into.append(k)
    return into


class Tbb():
    def applySysConfigTo(self, c):
        c.footTriggerTypes = [29, 0] #29: RT-30K, 30: RT-30HR
        c.inAssign = 0 #master
        c.fxModOn = 1
        c.masterFx = RingMod()

    @staticmethod
    def addKit(cl, n, kn, loc, cpp):
        name = n[:8]
        Kit().build(cl, name, os.path.join(loc, "KIT"), kn)

        cpp.write("DefineTrack( %s ) {\n" % n)
        cpp.write("\ttbb_2019( tracks, %d, spdsx_fx::%s, %d );\n" % (kn + 1, "ringMod" if hasattr(cl, "applyMasterFx") else "none", cl.korg if hasattr(cl, "korg") else 13))
        cpp.write("}\n")

    def createIn(self, loc, idxStart):
        kn = idxStart

        with open("tbb_2019.h", "w") as cpp:
            for s in readFromJson():
                Tbb.addKit(s, s.__name__, kn, loc, cpp)
                kn += 1

            oldSet = __import__("tbb2019")
            for n, cl in oldSet.__dict__.items():
                if isinstance(cl, type) and hasattr(cl, "level"):
                    Tbb.addKit(cl, n, kn, loc, cpp)

                    kn += 1
