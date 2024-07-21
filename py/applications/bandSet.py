
from kit import Kit
from applications.fromJson import FromJson
import os

class BandSet():
    def __init__(self, fn, actName):
        self.spec = FromJson(fn, actName)

    def applySysConfigTo(self, c):
        self.spec.applyTo(c)

    def addKit(self, cl, kn, loc):
        name = cl.__name__[:8]
        Kit().build(cl, name, os.path.join(loc, "KIT"), kn)

    def createIn(self, loc, idxStart):
        kn = idxStart
        for s in self.spec.kits():
            self.addKit(s, kn, loc)
            kn += 1


class Tbb(BandSet):
    def __init__(self):
        BandSet.__init__(self, "tbb_2019.json", "tbb")
        self.cpp = open("tbb_2019.h", "w")

    def __del__(self):
        print("closing .h file")

    def addKit(self, cl, kn, loc):
        n = cl.__name__

        self.cpp.write("DefineTrack( %s ) {\n" % n)
        self.cpp.write("\ttbb_2019( tracks, %d, spdsx_fx::%s, %d );\n" % (kn + 1, "ringMod" if hasattr(cl, "applyMasterFx") else "none", cl.korg if hasattr(cl, "korg") else 13))
        self.cpp.write("}\n")
        BandSet.addKit(self, cl, kn, loc)
