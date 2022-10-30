
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

def readKits(fn):
    with open(os.path.join("kits", fn)) as js:
        return json.load(js)

def readFromJson(fn):
    into = []
    kits = readKits(fn)
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
                if "outAssign" in padSpec:
                    pad["outAssign"] = padOutAssign[padSpec["outAssign"]]
                if "vol" in padSpec:
                    pad["vol"] = padSpec["vol"]
                if "note" in padSpec:
                    pad["note"] = padSpec["note"]
                if "channel" in padSpec:
                    pad["channel"] = padSpec["channel"]
            k.pads.append(pad)
        into.append(k)
    return into
