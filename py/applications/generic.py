
from utils import any
from effects import *
from kit import Kit
import sys
from random import randint
import os
from datetime import datetime


master = 0
sub = 1

class FxIn:
    inputAssign = master
    allowedFx = [Slicer, TapeEcho, TouchWah]


class FxKit:
    inputAssign = sub
    allowedFx = [RingMod, Phaser, FilterPlusDrive, Distortion, TouchWah, PitchShift, Vibrato, Reverb, Slicer]


class Generated:
    @staticmethod
    def _findIn(n):
        return (n * 100) + randint(0, 99)

    @staticmethod
    def rightFoot():
        return Generated._findIn(99)

    @staticmethod
    def leftFoot():
        return Generated._findIn(98)

    @staticmethod
    def padTop():
        return Generated._findIn(97)

    @staticmethod
    def padRim():
        return Generated._findIn(96)

    @staticmethod
    def perc():
        return Generated._findIn(95)

    @staticmethod
    def cym():
        return Generated._findIn(94)

    @staticmethod
    def note():
        return Generated._findIn(93)


padOutMaster = 0
padOutFx1Master = 1
padOutFx2Sub = 2
padOutSub = 3


class Generic:
    @staticmethod
    def _note(i):
        return i + 1

    def __init__(self, tempo):
        self.tempo = tempo
        self.sysConfig = None

    def applySysConfigTo(self, c):
        self.sysConfig = c
        effModes = { "kit": FxKit, "in": FxIn }
        fxMode = FxIn if len(sys.argv) < 4 else effModes[sys.argv[3]]
        allowFxMod = 1 if len(sys.argv) < 6 else int(sys.argv[5])
    

        masterFx = any(fxMode.allowedFx)

        c.inAssign = fxMode.inputAssign
        c.fxModOn = allowFxMod
        c.masterFx = masterFx.createRandom()
        self.kitFx1 = Thru
        self.kitFx2 = any(FxKit.allowedFx, [masterFx])
        if (c.fx1On() == 1):
            self.kitFx1 = any(FxKit.allowedFx, [masterFx, self.kitFx2])

        print("master %s %s%s" % (fxMode.__name__, masterFx.__name__, " allowing FX mod" if allowFxMod == 1 else ""))
        print("FX1 %s" % self.kitFx1.__name__)
        print("FX2 %s" % self.kitFx2.__name__)

    @staticmethod
    def _generate(name, t, notes):
        k = type(name, (), {})
        k.level = 100
        k.tempo = t
        noteVol = 50

        k.pads = [
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": notes.note(4)},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": notes.note(5)},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": notes.note(6)},
            {"sound": Generated.cym(), "soundb": Generated.cym()},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": notes.note(2)},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": notes.note(3)},
            {"sound": Generated.perc(), "soundb": Generated.perc()},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": notes.note(0)},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": notes.note(1)},
            {"sound": Generated.rightFoot(), "soundb": Generated.rightFoot()},
            {"sound": Generated.leftFoot(), "soundb": Generated.leftFoot()},
            {"sound": Generated.padTop(), "soundb": Generated.padTop()},
            {"sound": Generated.padRim(), "soundb": Generated.padRim()}
        ]

        return k

    def createKit(self, name, notes):
        kitDef = Generic._generate(name, self.tempo, notes)
        kitDef.pan = 0

        kitDef.fx1 = self.kitFx1.createRandom() if self.sysConfig.fx1On() == 1 else self.kitFx1()
        kitDef.fx2 = self.kitFx2.createRandom()

        # assign all sounds using c.kitAssign() and c.fx1On()

        topKitOut = padOutFx1Master if (self.sysConfig.fx1On() == 1) else padOutFx2Sub
        tunedMidiPercOut = padOutMaster if (self.sysConfig.inAssign == sub) else topKitOut
        midKitOut = padOutFx2Sub
        bdOut = padOutSub # allow padOutFx2 if not RingMod

        kitDef.pads[0]["outAssign"] = tunedMidiPercOut
        kitDef.pads[1]["outAssign"] = tunedMidiPercOut
        kitDef.pads[2]["outAssign"] = tunedMidiPercOut
        kitDef.pads[3]["outAssign"] = topKitOut
        kitDef.pads[4]["outAssign"] = tunedMidiPercOut
        kitDef.pads[5]["outAssign"] = tunedMidiPercOut
        kitDef.pads[6]["outAssign"] = midKitOut
        kitDef.pads[7]["outAssign"] = tunedMidiPercOut
        kitDef.pads[8]["outAssign"] = tunedMidiPercOut
        kitDef.pads[9]["outAssign"] = midKitOut
        kitDef.pads[10]["outAssign"] = midKitOut
        kitDef.pads[11]["outAssign"] = midKitOut
        kitDef.pads[12]["outAssign"] = topKitOut
        return kitDef


class Generic2024(Generic):
    def _createKit(self, name):
        kitDef = type(name, (), {})
        kitDef.level = 100
        kitDef.tempo = self.tempo
        kitDef.pan = 0
        kitDef.fx1 = self.kitFx1.createRandom() if self.sysConfig.fx1On() == 1 else self.kitFx1()
        kitDef.fx2 = self.kitFx2.createRandom()

        kitDef.pads = [
            # top left to right
            {"outAssign": padOutFx2Sub, "sound": Generated.cym(), "soundb": Generated.cym()},
            {"outAssign": padOutFx2Sub, "sound": Generated.cym(), "soundb": Generated.cym()},
            {"outAssign": padOutFx2Sub, "sound": Generated.cym(), "soundb": Generated.cym()},
            # upper three
            {"outAssign": padOutFx2Sub, "sound": Generated.cym(), "soundb": Generated.cym()},
            {"outAssign": padOutFx2Sub, "sound": Generated.padRim(), "soundb": Generated.padRim()},
            {"outAssign": padOutFx2Sub, "sound": Generated.perc(), "soundb": Generated.perc()},
            # lower three
            {"outAssign": padOutFx2Sub, "sound": Generated.cym(), "soundb": Generated.cym(), "vol": 50, "channel": 0, "note": 1},
            {"outAssign": padOutSub, "sound": Generated.padTop(), "soundb": Generated.padTop()},
            {"outAssign": padOutSub, "sound": Generated.perc(), "soundb": Generated.perc()},
            # externals
            {"outAssign": padOutSub, "sound": Generated.rightFoot(), "soundb": Generated.rightFoot()},
            {"outAssign": padOutFx2Sub, "sound": Generated.leftFoot(), "soundb": Generated.leftFoot()},
            {"outAssign": padOutSub, "sound": Generated.padTop(), "soundb": Generated.padTop()},
            {"outAssign": padOutSub, "sound": Generated.padRim(), "soundb": Generated.padRim()}
        ]

        return kitDef

    def createIn(self, loc, idxStart):
        for i in range(10):
            kitDef = self._createKit("gen_%02d" % i)
            Kit().buildNamed(kitDef, os.path.join(loc, "KIT"), idxStart + i)


class Generic2026(Generic):
    def _createKit(self, name):
        kitDef = type(name, (), {})
        kitDef.level = 100
        kitDef.tempo = self.tempo
        kitDef.pan = 0
        kitDef.fx1 = self.kitFx1.createRandom() if self.sysConfig.fx1On() == 1 else self.kitFx1()
        kitDef.fx2 = self.kitFx2.createRandom()

        kitDef.pads = [
            # top left to right
            {"outAssign": padOutFx2Sub, "sound": 4050, "soundb": 4051, "vol": 50, "channel": 0, "note": 101},  # cym
            {"outAssign": padOutFx2Sub, "sound": 4052, "soundb": 4053, "vol": 50, "channel": 0, "note": 102},  # cym
            {"outAssign": padOutFx2Sub, "sound": 4054, "soundb": 4055, "vol": 50, "channel": 0, "note": 103},  # cym
            # upper three
            {"outAssign": padOutFx2Sub, "sound": 4056, "soundb": 4057},  # cym
            {"outAssign": padOutFx2Sub, "sound": 4030, "soundb": 4031},  # pad rim
            {"outAssign": padOutFx2Sub, "sound": 4060, "soundb": 4061, "vol": 70, "channel": 0, "note": 1}, # note
            # lower three
            {"outAssign": padOutSub, "sound": 4020, "soundb": 4021},  # pad top
            {"outAssign": padOutSub, "sound": 4040, "soundb": 4041},  # perc
            {"outAssign": padOutFx2Sub, "sound": 4058, "soundb": 4059, "vol": 80},  # cym
            # externals
            {"outAssign": padOutSub, "sound": 4000, "soundb": 4001},
            {"outAssign": padOutFx2Sub, "sound": 4010, "soundb": 4011},
            {"outAssign": padOutSub, "sound": 4022, "soundb": 4023}, # pad top
            {"outAssign": padOutSub, "sound": 4032, "soundb": 4033, "vol": 90, "channel": 0, "note": 100}  # pad rim
        ]

        return kitDef

    def createIn(self, loc, idxStart):
        kn = datetime.now().strftime("%Y%m%d")
        kitDef = self._createKit(kn)
        Kit().buildNamed(kitDef, os.path.join(loc, "KIT"), idxStart)

