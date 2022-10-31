
from kit import Kit
from sysConfig import SystemConfig
from effects import RingMod
from kits.fromJson import FromJson
import os


class Tbb():
    def __init__(self):
        self.spec = FromJson("tbb_2019.json")

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
            for s in self.spec.kits():
                Tbb.addKit(s, s.__name__, kn, loc, cpp)
                kn += 1
