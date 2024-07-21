
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


class GeneratedSounds:
    @staticmethod
    def _findIn(n):
        return (n * 100) + randint(0, 99)

    @staticmethod
    def rightFoot():
        return GeneratedSounds._findIn(99)

    @staticmethod
    def leftFoot():
        return GeneratedSounds._findIn(98)

    @staticmethod
    def padTop():
        return GeneratedSounds._findIn(97)

    @staticmethod
    def padRim():
        return GeneratedSounds._findIn(96)

    @staticmethod
    def perc():
        return GeneratedSounds._findIn(95)

    @staticmethod
    def cym():
        return GeneratedSounds._findIn(94)

    @staticmethod
    def note():
        return GeneratedSounds._findIn(93)


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
        ks = GeneratedSounds
        k = type(name, (), {})
        k.level = 100
        k.tempo = t
        k.pads = []
        noteVol = 50

        k.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(4)})
        k.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(5)})
        k.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(6)})
        k.pads.append({"sound": ks.cym(), "soundb": ks.cym()})
        k.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(2)})
        k.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(3)})
        k.pads.append({"sound": ks.perc(), "soundb": ks.perc()})
        k.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(0)})
        k.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(1)})
        k.pads.append({"sound": ks.rightFoot(), "soundb": ks.rightFoot()})
        k.pads.append({"sound": ks.leftFoot(), "soundb": ks.leftFoot()})
        k.pads.append({"sound": ks.padTop(), "soundb": ks.padTop()})
        k.pads.append({"sound": ks.padRim(), "soundb": ks.padRim()})

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
        ks = GeneratedSounds
        kitDef = type(name, (), {})
        kitDef.level = 100
        kitDef.tempo = self.tempo
        kitDef.pads = []
        noteVol = 50

        kitDef.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(4)})
        kitDef.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(5)})
        kitDef.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(6)})
        kitDef.pads.append({"sound": ks.cym(), "soundb": ks.cym()})
        kitDef.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(2)})
        kitDef.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(3)})
        kitDef.pads.append({"sound": ks.perc(), "soundb": ks.perc()})
        kitDef.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(0)})
        kitDef.pads.append({"sound": ks.note(), "soundb": ks.note(), "channel": 0, "vol": noteVol, "note": Generic2024._note(1)})
        kitDef.pads.append({"sound": ks.rightFoot(), "soundb": ks.rightFoot()})
        kitDef.pads.append({"sound": ks.leftFoot(), "soundb": ks.leftFoot()})
        kitDef.pads.append({"sound": ks.padTop(), "soundb": ks.padTop()})
        kitDef.pads.append({"sound": ks.padRim(), "soundb": ks.padRim()})

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
