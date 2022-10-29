
from utils import any
from effects import *
from iZgenKits import generate
import sys
from random import randint

master = 0
sub = 1

class FxIn():
    inputAssign = master
    allowedFx = [Slicer, TapeEcho, TouchWah]

class FxKit():
    inputAssign = sub
    allowedFx = [RingMod, Phaser, FilterPlusDrive, Distortion, TouchWah, PitchShift, Vibrato, Reverb, Slicer]

class Generic():
    def __init__(self, tempo):
        self.tempo = tempo

    def applySysConfigTo(self, c):
        effModes = { "kit": FxKit, "in": FxIn }
        fxMode = FxIn if len(sys.argv) < 4 else effModes[sys.argv[3]]
        allowFxMod = 1 if len(sys.argv) < 6 else int(sys.argv[5])
    
        self.c = c
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

    def _createKit(self, name, notes, kitFx1, kitFx2, sysConfig):
        kitDef = generate(name, self.tempo, notes)
        kitDef.pan = 0

        kitDef.fx1 = kitFx1.createRandom() if sysConfig.fx1On() == 1 else kitFx1()
        kitDef.fx2 = kitFx2.createRandom()

        # assign all sounds using c.kitAssign() and c.fx1On()
        padOutMaster = 0
        padOutFx1 = 1
        padOutFx2 = 2
        padOutSub = 3

        topKitOut = padOutFx1 if (sysConfig.fx1On() == 1) else padOutFx2
        tunedMidiPercOut = padOutMaster if (sysConfig.inAssign == sub) else topKitOut
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
        pass
