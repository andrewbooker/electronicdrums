#!/usr/bin/env python3

import soundfile as sf
import math
from random import uniform, randint
import xml.dom.minidom
from utils import MovingAvg, AbsMovingAvg
from utils import any as anyOf
from wave import Wave
import os
from datetime import datetime
import sys
import json


class Resize():
    def __init__(self, length):
        self.buffer = []
        self.length = length

    def add(self, d):
        self.buffer.append(d)

    def read(self, f):
        inSize = len(self.buffer)
        out = []
        i = 0
        done = False
        while not done:
            vol = 1 - (i / (1.0 * self.length))
            p = i / f(i)
            l = math.floor(p)
            u = math.ceil(p)
            if (u < inSize and l < inSize and i < self.length):
                dp = p - l
                out.append(vol * (((1 - dp) * self.buffer[l]) + (dp * self.buffer[u])))
            else:
                done = True
            i += 1
        return out

class Operation:
    def on(self, d1, d2, i, size):
        pass

    def reset(self):
        pass

    def isDone(self, hasF1, hasF2):
        return not hasF1 and not hasF2


class Avg(Operation):
    def __init__(self):
        self.reset()

    def reset(self):
        self.coeff = uniform(0.2, 0.8)

    def on(self, d1, d2, i, size):
        return (d1 * self.coeff) + (d2 * (1.0 - self.coeff))


class LinearXFade(Operation):
    def on(self, d1, d2, i, size):
        f = 1.0 * i / size
        return (d1 * (1 - f)) + (d2 * f)


class XChop(Operation):
    def __init__(self):
        self.reset()

    def reset(self):
        self.freq = uniform(400.0, 4000.0)

    def on(self, d1, d2, i, size):
        f = 1.0 + (0.5 * math.cos(i / self.freq))
        return (d1 * (1 - f)) + (d2 * f)


class ShortXFade(Operation):
    def on(self, d1, d2, i, size):
        f = 1.0 / ((20.0 * i / size) + 1.0)
        return (d1 * (1 - f)) + (d2 * f)


class EnvelopeFollow(Operation):
    def __init__(self):
        self.reset()

    def reset(self):
        self.movingAvg = AbsMovingAvg(randint(4, 10))

    def on(self, d1, d2, i, size):
        self.movingAvg.add(d1)
        return self.movingAvg.value() * d2


class Multiply(Operation):
    def __init__(self):
        self.movingAvg = MovingAvg(randint(4, 10))

    def on(self, d1, d2, i, size):
        self.movingAvg.add(d1 * d2)
        return self.movingAvg.value()
    

class Gradient():
    @staticmethod
    def anyWithin(lower, upper, length):
        return Gradient(uniform(lower, upper), uniform(lower, upper), length)

    @staticmethod
    def any(length):
        return Gradient.anyWithin(0.3, 2.7, length)

    def __init__(self, y1, y2, length):
        self.y1 = y1
        self.y2 = y2
        self.length = length

    def at(self, i):
        return self.y1 + (i * (self.y2 - self.y1) / self.length)


class Combiner:
    def __init__(self, baseDir, iterations):
        self.iterations = iterations
        self.sourceLoc = os.path.join(baseDir, "backup/Roland/SPD-SX/WAVE/DATA")
        self.baseOutLoc = os.path.join(baseDir, datetime.now().strftime("%Y%m%d"))
        self.audit = []


    def _combine(self, fnOnto, subDir, idx, s1, s2, grad1, grad2, op, newLength):
        f1 = sf.SoundFile(os.path.join(self.sourceLoc, s1), "r")
        f2 = sf.SoundFile(os.path.join(self.sourceLoc, s2), "r")

        print(type(op).__name__, "with", s1, "and", s2, f"lasting {(newLength / 44100.0):.02f}s")

        size = max(f1.frames, f2.frames)
        resize1 = Resize(newLength)
        resize2 = Resize(newLength)
        resize1.buffer = f1.read()
        resize2.buffer = f2.read()

        f1.close()
        f2.close()

        r1 = resize1.read(grad1.at)
        r2 = resize2.read(grad2.at)
        lr1 = len(r1)
        lr2 = len(r2)

        wave = Wave(self.baseOutLoc, idx, fnOnto)

        i = 0
        done = False
        op.reset()
        while (not done):
            hasF1 = i < lr1
            hasF2 = i < lr2
            data = [r1[i] if hasF1 else 0, r2[i] if hasF2 else 0]    
            wave.write(op.on(data[0], data[1], i, size))
            done = op.isDone(hasF1, hasF2)
            i += 1

        wave.close()


    def generateSoundRange(self, subDir, instr, setA, setB, combiners):
        print("generating", instr, "sounds")
        group = {"group": subDir, "instr": instr, "files": []}
        for i in range(self.iterations):
            newLength = randint(22050, 66150) # 0.5 to 1.5 seconds
            fn = f"{instr}{i:06d}.wav"
            group["files"].append(fn)
            waveFn = f"{subDir}/{fn}"
            s1 = anyOf(setA)
            cmb = anyOf(combiners)
            g1 = Gradient.anyWithin(0.9, 1.4, newLength) if instr == "bd" else Gradient.any(newLength)
            g2 = Gradient.any(newLength)
            self._combine(waveFn, subDir, i, s1, anyOf(setB, [s1]), g1, g2, cmb(), newLength)
        self.audit.append(group)

    def dumpAudit(self):
        with open("../html/files.js", "w") as f:
            f.write("const files = ")
            json.dump(self.audit, f, indent=4)
            f.write(";")


most = [EnvelopeFollow, XChop, Avg, ShortXFade]
every = [EnvelopeFollow, XChop, Avg, ShortXFade, Multiply]


kick = [
    "00/Kick_.wav",
    "00/Kick__01.wav",
    "00/Kick__02.wav",
    "00/Kick__03.wav",
    "00/Kick__04.wav",
    "00/Kick__05.wav",
    "00/Kick__06.wav",
    "00/Kick__07.wav",
    "00/Kick__08.wav",
    "00/Kick__09.wav",
    "00/Kick__10.wav",
    "00/Kick__11.wav",
    "00/Kick__12.wav",
    "00/Kick__13.wav",
    "00/Kick__14.wav",
    "00/Kick__15.wav",
    "00/Kick__16.wav",
    "00/Kick__17.wav",
    "00/Kick__18.wav",
    "00/Kick__19.wav"
]

snare = [
    "01/Snare.wav",
    "01/Snare_01.wav",
    "01/Snare_02.wav",
    "01/Snare_03.wav",
    "01/Snare_04.wav",
    "01/Snare_05.wav",
    "01/Snare_06.wav",
    "01/Snare_07.wav",
    "01/Snare_08.wav",
    "01/Snare_09.wav",
    "01/Snare_10.wav",
    "01/Snare_11.wav",
    "01/Snare_12.wav",
    "01/Snare_13.wav",
    "01/Snare_14.wav",
    "01/Snare_15.wav",
    "01/Snare_16.wav",
    "01/Snare_17.wav",
    "01/Snare_18.wav",
    "01/Snare_19.wav",
    "01/Snare_20.wav",
    "01/Snare_21.wav",
    "01/Snare_22.wav",
    "01/Snare_23.wav",
    "01/Snare_24.wav"
]

cym = [
    "00/Ride_.wav",
    "00/Ride__01.wav",
    "00/Ride__02.wav",
    "00/Ride__03.wav",
    "00/Ride__04.wav",
    "00/Cym_8.wav",
    "00/Cym_C_03.wav",
    "00/Cym_F_01.wav",
    "00/Cym_S_01.wav",
    "00/P_Gon.wav",
    "00/P_Tri_01.wav",
    "00/HH_01.wav",
    "00/HH_03.wav",
    "00/HH_Ac_01.wav",
    "00/HH_Db_01.wav",
    "00/HH_Dn_01.wav",
    "00/HH_Hs_01.wav",
    "00/HH_Hs_03.wav",
    "00/HH_Pr_01.wav",
    "00/HH_Pr_03.wav",
    "00/HH_Hp_01.wav",
    "01/SE_Ve.wav"
]

tom = [
    "01/Tom_8.wav",
    "01/Tom_8_01.wav",
    "01/Tom_8_02.wav",
    "01/Tom_A.wav",
    "01/Tom_A_01.wav",
    "01/Tom_A_02.wav",
    "01/Tom_E.wav",
    "01/Tom_E_01.wav",
    "01/Tom_E_02.wav",
    "01/Tom_R.wav",
    "01/Tom_R_01.wav",
    "01/Tom_R_02.wav",
    "00/P_Tim.wav",
    "00/P_Tim_01.wav"
]

perc = [
    "00/Clap_.wav",
    "00/Clap__01.wav",
    "00/Clap__02.wav",
    "00/Clap__03.wav",
    "00/Clap__04.wav",
    "00/Clap__05.wav",
    "00/Clap__06.wav",
    "00/Clap__07.wav",
    "00/HH.wav",
    "00/HH_02.wav",
    "00/HH_Ac.wav",
    "00/HH_Db.wav",
    "00/HH_Dn.wav",
    "00/HH_Hp.wav",
    "00/HH_Hs.wav",
    "00/HH_Hs_02.wav",
    "00/HH_Pr.wav",
    "00/HH_Pr_02.wav",
    "00/HH_Pr_04.wav",
    "00/P_Gan.wav",
    "00/P_Cla.wav",
    "00/P_Con.wav",
    "00/P_Con_01.wav",
    "00/P_Con_02.wav",
    "00/P_Tab.wav",
    "00/P_Tab_01.wav",
    "00/P_Tab_02.wav",
    "00/P_Tab_03.wav",
    "00/P_Tam.wav",
    "00/P_Tam_01.wav",
    "00/P_Tam_02.wav",
    "00/P_Tri.wav",
    "00/SE_Cr.wav",
    "01/SE_Sw.wav"
]

note = [
    "00/Ride_.wav",
    "00/Ride__01.wav",
    "00/Ride__02.wav",
    "00/Ride__03.wav",
    "00/Ride__04.wav",
    "00/P_Tri_01.wav",
    "00/HH.wav",
    "00/HH_02.wav",
    "00/HH_Ac.wav",
    "00/HH_Db.wav",
    "00/HH_Dn.wav",
    "00/HH_Hp.wav",
    "00/HH_Hs.wav",
    "00/HH_Hs_02.wav",
    "00/HH_Pr.wav",
    "00/HH_Pr_02.wav",
    "00/HH_Pr_04.wav",
    "00/P_Gan.wav",
    "00/P_Cla.wav",
    "00/P_Tri.wav",
    "00/SE_Cr.wav",
    "01/SE_Sw.wav"
]

baseDir = sys.argv[1]

combiner = Combiner(baseDir, 2)

strategies = {
    "bd": (kick, kick + tom, most),
    "lf": (tom + perc, snare + perc, every),
    "pt": (snare, snare, most),
    "pr": (tom, tom, every),
    "pe": (perc, perc, every),
    "cy": (cym, cym, [XChop, Avg, ShortXFade]),
    "no": (note, note, every)
}

group = sys.argv[2] if len(sys.argv) > 2 else None
startAt = 99
for s, p in strategies.items():
    if group is None or group == s:
        combiner.generateSoundRange(str(startAt), s, *p)
    startAt -= 1
combiner.dumpAudit()


