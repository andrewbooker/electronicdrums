#!/usr/bin/env python

from sounds import sounds as wav

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
	