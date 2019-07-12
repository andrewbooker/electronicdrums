#!/usr/bin/env python

from random import randint

def any(a, ommitting = []):
	f = a[randint(0, len(a) - 1)]
	if f in ommitting:
		return any(a, ommitting)
	return f