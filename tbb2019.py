#!/usr/bin/env python

from sounds import sounds as wav

sound = "sound"
note = "note"

class ItCouldBeHome():
	tempo = 90
	pads = [{sound: wav["Cym_Splash1"]}, #top left
			{sound: wav["Cym_Splash2"]},
			{sound: wav["Cym_Crotale"]},
			{sound: wav["Clap_Hse1"]}, # mid left
			{sound: wav["HH_Proc2_op"]},
			{sound: wav["Cym_Fx2"]},
            {sound: wav["Kick_808_L"]}, # bottom left
			{sound: wav["P_Tambourine"]},
			{sound: wav["P_GanzaTap"]},
			{sound: wav["SE_Crasher"]}, # foot L
			{sound: wav["Kick_Acou1"]}, # foot R
			{sound: wav["Snare_Proc4"]}, # pad top
			{sound: wav["SE_Noise1"]}] # pad rim


class BraveDreams():
	tempo = 93
	pads = []


class TheWarOnMe():
	tempo = 120
	pads = []
	

class NotMarriedAnyMore():
	tempo = 89
	pads = {}
	