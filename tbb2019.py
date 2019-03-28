#!/usr/bin/env python

from sounds import sounds as wav
from effects import *

sound = "sound"
note = "note"
channel = "channel"

# eventually, put these in set order
class ItCouldBeHome():
	level = 100
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
			{sound: wav["Kick_Acou1"]}, # foot R
			{sound: wav["SE_Crasher"]}, # foot L
			{sound: wav["Snare_Proc4"]}, # pad top
			{sound: wav["SE_Noise1"]}] # pad rim


class BraveDreams():
	level = 100
	tempo = 93
	pads = [{sound: wav["Cym_Splash1"]}, #top left
			{sound: wav["Cym_Splash2"]},
			{sound: wav["Cym_Crotale"]},
			{sound: wav["Clap_Hse1"]}, # mid left
			{sound: wav["HH_Proc2_op"]},
			{sound: wav["Cym_Fx2"]},
            {sound: wav["Kick_808_L"]}, # bottom left
			{sound: wav["P_Tambourine"]},
			{sound: wav["P_GanzaTap"]},
			{sound: wav["Kick_Acou1"]}, # foot R
			{sound: wav["SE_Crasher"]}, # foot L
			{sound: wav["Snare_Proc4"]}, # pad top
			{sound: wav["SE_Noise1"]}] # pad rim


class TheWarOnMe():
	level = 100
	tempo = 120
	pads = [{sound: wav["Cym_Splash1"]}, #top left
			{sound: wav["Cym_Splash2"]},
			{sound: wav["Cym_Crotale"]},
			{sound: wav["Clap_Hse1"]}, # mid left
			{sound: wav["HH_Proc2_op"]},
			{sound: wav["Cym_Fx2"]},
            {sound: wav["Kick_808_L"]}, # bottom left
			{sound: wav["P_Tambourine"]},
			{sound: wav["P_GanzaTap"]},
			{sound: wav["Kick_Acou1"]}, # foot R
			{sound: wav["SE_Crasher"]}, # foot L
			{sound: wav["Snare_Proc4"]}, # pad top
			{sound: wav["SE_Noise1"]}] # pad rim
	

class NotMarriedAnyMore():
	level = 100
	tempo = 89
	pads = [{sound: wav["Cym_Splash1"]}, #top left
			{sound: wav["Cym_Splash2"]},
			{sound: wav["Cym_Crotale"]},
			{sound: wav["Clap_Hse1"]}, # mid left
			{sound: wav["HH_Proc2_op"]},
			{sound: wav["Cym_Fx2"]},
            {sound: wav["Kick_808_L"]}, # bottom left
			{sound: wav["P_Tambourine"]},
			{sound: wav["P_GanzaTap"]},
			{sound: wav["Kick_Acou1"]}, # foot R
			{sound: wav["SE_Crasher"]}, # foot L
			{sound: wav["Snare_Proc4"]}, # pad top
			{sound: wav["SE_Noise1"]}] # pad rim


class Housewives():
	level = 100
	tempo = 100
	pads = [{sound: wav["Cym_Splash1"]}, #top left
			{sound: wav["Cym_Splash2"]},
			{sound: wav["Cym_Crotale"]},
			{sound: wav["Clap_Hse1"]}, # mid left
			{sound: wav["HH_Proc2_op"]},
			{sound: wav["Cym_Fx2"]},
            {sound: wav["Kick_808_L"]}, # bottom left
			{sound: wav["P_Tambourine"]},
			{sound: wav["P_GanzaTap"]},
			{sound: wav["Kick_Acou1"]}, # foot R
			{sound: wav["SE_Crasher"]}, # foot L
			{sound: wav["Snare_Proc4"]}, # pad top
			{sound: wav["SE_Noise1"]}] # pad rim
			
class AllTheBlueChanges():
	level = 90
	tempo = 122
	pads = [{note: 60, channel: 0}, #top left
			{note: 62, channel: 0},
			{note: 64, channel: 0},
			{note: 52, channel: 0, sound: wav["HH_DbS_cl"]}, # mid left
			{note: 57, channel: 0, sound: wav["Cym_Fx2"]},
			{note: 59, channel: 0, sound: wav["SE_SweepSlap"]},
            {note: 45, channel: 0}, # bottom left
			{note: 47, channel: 0},
			{note: 50, channel: 0, sound: wav["P_Tambourine"]},
			{sound: wav["Kick_Proc3"]}, # foot R
			{sound: wav["SnareXs_2"]}, # foot L
			{sound: wav["Clap_Min"]}, # pad top
			{sound: wav["Clap_110"]}] # pad rim
	fx = Chorus().rate(28).depth(70).preDelayMs(5) #not sure - this was for when notes were wavs
			
class TimeTravel():
	level = 100
	tempo = 78
	pads = [{sound: wav["S00236"]}, #top left
			{sound: wav["S00237"]},
			{sound: wav["S00238"]},
			{sound: wav["Cym_Fx2"]}, # mid left
			{sound: wav["SE_SweepSlap"]},
			{sound: wav["SnareXs_7"]},
            {sound: wav["Kick_909_Atk"]}, # bottom left
			{sound: wav["Snare_Proc4"]},
			{sound: wav["HH_808_cl"]},
			{sound: wav["Kick_Proc3"]}, # foot R
			{sound: wav["P_Tamb_DnB"]}, # foot L
			{sound: wav["Clap_909"]}, # pad top
			{sound: wav["Clap_110"]}] # pad rim
	fx = RingMod().freq(97).sens(10).balance(0.5)
	
class WarmupMan():
	level = 100
	tempo = 122
	pads = [{note: 65, channel: 0},
			{note: 70, channel: 0},
			{note: 72, channel: 0},
			{note: 53, channel: 0},
			{note: 55, channel: 0},
			{note: 62, channel: 0},
			{note: 24, channel: 0},
			{note: 46, channel: 0},
			{note: 51, channel: 0},
			{note: 36, channel: 0},
			{note: 48, channel: 0},
			{note: 60, channel: 0},
			{note: 70, channel: 0}]
	fx = Vibrato().rate(77).depth(69)
	