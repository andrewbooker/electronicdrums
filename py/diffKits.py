#!/usr/bin/env python

import os
import sys

if len(sys.argv) < 3:
    print("usage:")
    print("./diffKits.py <original-location> <test-location>")
    exit()

kitLoc = os.path.join("Roland", "SPD-SX", "KIT")
locLive = os.path.join(sys.argv[1], kitLoc)
locGen = os.path.join(sys.argv[2], kitLoc)

actuals = os.listdir(locLive)
generated = os.listdir(locGen)
ignore = []#["kit057.spd", "kit061.spd", "kit062.spd", "kit068.spd"]
f = 0
for g in generated:
    gfn = os.path.join(locGen, g)

    if (os.path.isfile(gfn) and g not in ignore):
        generated = open(gfn, "r")
        actual = open(os.path.join(locLive, g), "r")
        anything = False

        als = actual.readlines()
        gls = generated.readlines()
        i = 0

        for al in als:
            if ((len(gls) > i) and (al != gls[i])):
                if (not anything):
                    print(g)
                    anything = True
                print("%d: actual %s != generated %s" % (i, al, gls[i]))
                f += 1
            i += 1

        generated.close()
    actual.close()

print("%d diff%s found" % (f, "s" if (f != 1) else ""))
