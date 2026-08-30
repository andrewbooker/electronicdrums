#!/usr/bin/env python

import os
import soundfile as sf
import xml.dom.minidom


def param(doc, onto, name, value):
    onto.appendChild(doc.createElement(name)).appendChild(doc.createTextNode(str(value)))


def prm(fqfnOut, name, wavPath):
    doc = xml.dom.minidom.parseString("<WvPrm/>")
    wvPrm = doc.documentElement

    for i in range(12):
        param(doc, wvPrm, "Nm%d" % i, ord(name[i]))

    param(doc, wvPrm, "Tag", 0)
    param(doc, wvPrm, "Tempo", 1200)
    param(doc, wvPrm, "Beat", 0)
    param(doc, wvPrm, "Measure", 0)
    param(doc, wvPrm, "Start", 0)
    param(doc, wvPrm, "End", 0)
    param(doc, wvPrm, "Path", wavPath)

    file = open(fqfnOut, "w")
    wvPrm.writexml(file, addindent="\t", newl="\n")
    file.close()


class Wave():
    def __init__(self, baseDir, idx, fn):
        print("creating wave file", fn, "in", baseDir)
        self.idx = idx
        self.fn = fn
        self.subDir = os.path.dirname(fn)
        self.waveDir = os.path.join(baseDir, "WAVE")
        self.prmDir = os.path.join(baseDir, "PRM")
        for d in [self.waveDir, self.prmDir]:
            fd = os.path.join(d, self.subDir)
            if not os.path.exists(fd):
               os.makedirs(fd) 

        fqfn = os.path.join(self.waveDir, fn)
        print("creating", fqfn)
        if os.path.exists(fqfn):
            os.remove(fqfn)
        self.file = sf.SoundFile(fqfn, mode="x", samplerate=44100, channels=1, subtype="PCM_16")

    def write(self, d):
        self.file.write(d)

    def close(self):
        self.file.close()
        fqn = os.path.join(self.prmDir, self.subDir, f"{self.idx:02d}.spd")
        print("creating", fqn)
        prm(fqn, "iz_%.10d" % self.idx, self.fn)

