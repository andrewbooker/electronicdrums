
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

footTriggers = {
    "KD-7": 0,
    "RT-30K": 29,
    "RT-30HR": 30
}

genSounds = {
    "no": 93,
    "cy": 94,
    "pe": 95,
    "pr": 96,
    "pt": 97,
    "lf": 98,
    "bd": 99
}


def soundIdxFrom(name):
    if name in wav:
        return wav[name]
    pref = name[:2]
    if pref not in genSounds:
        return -1
    return int(genSounds[pref] * 100) + int(name[-2:])


class FromJson:
    @staticmethod
    def readSet(fn):
        with open(os.path.join("kits", fn)) as js:
            return json.load(js)

    def __init__(self, fn, actName):
        self.bandSet = FromJson.readSet(fn)
        self.actName = actName

    def applyTo(self, sysConf):
        if "system" in self.bandSet:
            sysSetup = self.bandSet["system"]
            sysConf.footTriggerTypes = [footTriggers[f] for f in sysSetup["footTriggerTypes"]]
            sysConf.inAssign = inAssign[sysSetup["inAssign"]]
            sysConf.fxModOn = int(sysSetup["fxModOn"])
            if "masterFx" in sysSetup:
                sysConf.masterFx = getattr(effects, sysSetup["masterFx"]["type"])()

    @staticmethod
    def asKit(kit):
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
                    pad["sound"] = soundIdxFrom(padSpec["wav"])
                if "outAssign" in padSpec:
                    pad["outAssign"] = padOutAssign[padSpec["outAssign"]]
                if "vol" in padSpec:
                    pad["vol"] = padSpec["vol"]
                if "note" in padSpec:
                    pad["note"] = padSpec["note"]
                if "channel" in padSpec:
                    pad["channel"] = padSpec["channel"]
            k.pads.append(pad)

        if "fx1" in kit and "type" in kit["fx1"]:
            eff = kit["fx1"]
            k.fx1 = getattr(effects, eff["type"])()
            for p in eff["params"]:
                getattr(k.fx1, p)(int(eff["params"][p]))

        return k

    def kits(self):
        kits = []
        parentDir = os.path.dirname(os.getcwd())
        p = os.path.join(parentDir, "json", self.actName)

        for t in self.bandSet["setList"]:
            fn = f"{t}.json"
            useGeneral = not os.path.exists(os.path.join(p, fn))
            if useGeneral:
                fn = "General.json"
            with open(os.path.join(p, fn)) as js:
                kit = json.load(js)
                if useGeneral:
                    kit["name"] = t[:8]
                kits.append(FromJson.asKit(kit))

        if "kits" in self.bandSet:
            for kit in self.bandSet["kits"]:
                kits.append(FromJson.asKit(kit))

        return kits
