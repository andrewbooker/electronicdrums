
from utils import any
from effects import *
from kit import Kit
import sys
from random import randint
import os

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


class Generic:
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
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(4)},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(5)},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(6)},
            {"sound": Generated.cym(), "soundb": Generated.cym()},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(2)},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(3)},
            {"sound": Generated.perc(), "soundb": Generated.perc()},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(0)},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(1)},
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
        padOutMaster = 0
        padOutFx1 = 1
        padOutFx2 = 2
        padOutSub = 3

        topKitOut = padOutFx1 if (self.sysConfig.fx1On() == 1) else padOutFx2
        tunedMidiPercOut = padOutMaster if (self.sysConfig.inAssign == sub) else topKitOut
        midKitOut = padOutFx2
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
    @staticmethod
    def _note(i):
        return i + 1
    
    def _createKit(self, name):
        kitDef = type(name, (), {})
        kitDef.level = 100
        kitDef.tempo = self.tempo
        kitDef.pads = []
        noteVol = 50

        kitDef.pads = [
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(4)},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(5)},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(6)},
            {"sound": Generated.cym(), "soundb": Generated.cym()},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(2)},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(3)},
            {"sound": Generated.perc(), "soundb": Generated.perc()},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(0)},
            {"sound": Generated.note(), "soundb": Generated.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(1)},
            {"sound": Generated.rightFoot(), "soundb": Generated.rightFoot()},
            {"sound": Generated.leftFoot(), "soundb": Generated.leftFoot()},
            {"sound": Generated.padTop(), "soundb": Generated.padTop()},
            {"sound": Generated.padRim(), "soundb": Generated.padRim()}
        ]
        kitDef.pan = 0
        kitDef.fx1 = self.kitFx1.createRandom() if self.sysConfig.fx1On() == 1 else self.kitFx1()
        kitDef.fx2 = self.kitFx2.createRandom()

        # assign all sounds using c.kitAssign() and c.fx1On()
        padOutMaster = 0
        padOutFx1 = 1
        padOutFx2 = 2
        padOutSub = 3

        topKitOut = padOutFx1 if (self.sysConfig.fx1On() == 1) else padOutFx2
        tunedMidiPercOut = padOutMaster if (self.sysConfig.inAssign == sub) else topKitOut
        midKitOut = padOutFx2
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

    def createIn(self, loc, idxStart):
        for i in range(10):
            kitDef = self._createKit("gen_%02d" % i)
            Kit().buildNamed(kitDef, os.path.join(loc, "KIT"), idxStart + i)
