
from kit import Kit
from sysConfig import SystemConfig
from effects import RingMod
from tbb2019 import setList
import os

class Tbb():
    def applySysConfigTo(self, c):
        c.footTriggerTypes = [29, 0] #29: RT-30K, 30: RT-30HR
        c.inAssign = 0 #master
        c.fxModOn = 1
        c.masterFx = RingMod()

    @staticmethod
    def addKit(cl, n, kn, loc, cpp):
        name = n[:8]
        Kit().build(cl, name, os.path.join(loc, "KIT"), kn)

        cpp.write("DefineTrack( %s ) {\n" % n)
        cpp.write("\ttbb_2019( tracks, %d, spdsx_fx::%s, %d );\n" % (kn + 1, "ringMod" if hasattr(cl, "applyMasterFx") else "none", cl.korg if hasattr(cl, "korg") else 13))
        cpp.write("}\n")

    def createIn(self, loc, idxStart):
        kn = idxStart

        with open("tbb_2019.h", "w") as cpp:
            for s in setList:
                Tbb.addKit(s, s.__name__, kn, loc, cpp)
                kn += 1

            oldSet = __import__("tbb2019")
            for n, cl in oldSet.__dict__.items():
                if isinstance(cl, type) and hasattr(cl, "level"):
                    Tbb.addKit(cl, n, kn, loc, cpp)

                    kn += 1
