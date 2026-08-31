#!/usr/bin/env python3

import sys
import os
import json


inDir = sys.argv[1]
d = os.path.join(inDir, "WAVE")
js = []
for f in os.listdir(d):
    g = {"group": f}
    files = os.listdir(os.path.join(d, f))
    if files:
        g["instr"] = files[0][:2]
        g["files"] = files
    js.append(g)

with open("files.js", "w") as f:
    f.write("const files = ")
    json.dump(js, f, indent=4)
    f.write(";")

