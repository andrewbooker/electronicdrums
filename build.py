#!/usr/bin/env python

from kit import createKit

#createKit(98, date.today().strftime("%Y%m%d"), 83, {}) 

kn = 50
set = __import__("tbb2019")
for n, cl in set.__dict__.items():
	if isinstance(cl, type) and hasattr(cl, "pads"):
		createKit(kn, n[:8], cl)
		kn += 1
