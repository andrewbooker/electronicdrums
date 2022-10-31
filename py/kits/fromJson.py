
from sounds import sounds as wav
import effects

import os
import json

inAssign = {
    "master": 0,
    "sub": 1
}

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


class FromJson():
    @staticmethod
    def readSet(fn):
        with open(os.path.join("kits", fn)) as js:
            return json.load(js)

    def __init__(self, fn):
        self.bandSet = FromJson.readSet(fn)

    def kits(self):
        kits = []

        for kit in self.bandSet["kits"]:
            k = type(kit["name"], (), {})
            k.level = kit["level"] if "level" in kit else 100
            k.tempo = kit["tempo"]
            k.pads = []
            if "korg" in kit:
                k.korg = kit["korg"]

            for i in range(13):
                pad = {}
                if padNames[i] in kit["pads"]:
                    padSpec = kit["pads"][padNames[i]]
                    if "wav" in padSpec:
                        pad["sound"] = wav[padSpec["wav"]]
                    if "outAssign" in padSpec:
                        pad["outAssign"] = padOutAssign[padSpec["outAssign"]]
                    if "vol" in padSpec:
                        pad["vol"] = padSpec["vol"]
                    if "note" in padSpec:
                        pad["note"] = padSpec["note"]
                    if "channel" in padSpec:
                        pad["channel"] = padSpec["channel"]
                k.pads.append(pad)

            if "fx1" in kit:
                eff = kit["fx1"]
                k.fx1 = getattr(effects, eff["type"])()
                for p in eff["params"]:
                    getattr(k.fx1, p)(int(eff["params"][p]))
            kits.append(k)
        return kits
