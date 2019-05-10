#!/usr/bin/env python

from sounds import sounds as wav
from effects import *
from standardPatch import StandardPatch

note = "note"
channel = "channel"
sound = "sound"




#Ghostlike -- acoustic only
#Forest Almost Burning -- acoustic
#--Not Married Any More -- claps for brush/stick
#Strange Gods --  all the claps, cabasa
#I Go Deeper  -- acoustic
#--The War On Me (might be dropped) - electronic
#Killing To Survive  -- acoustic
#Never Needing -- electronic 808 plus shakers, reverb snare 2nd half
#It’s The World -- acoustic
#Borderline -- tuned figure electronics (3 notes), shakers, dampened drums

#Things Change - electronic: piano
#Housewives - electronics - bongo shit
#Wherever There Is Light - electronic
#Time Travel In Texas
#All The Blue Changes
#Mixtaped
#The Warm-Up Man Forever
#Only Rain - electronic
#Days Turn Into Years - electronic
#WatchingOverMe - electronic


# eventually, put these in set order
# 1st is 51
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

class StrangeGods():
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

class TheWarOnMe():
	level = 100
	tempo = 120
	pads = [{sound: wav["Cym_Splash1"]}, #top left
			{sound: wav["Cym_Splash2"]},
			{sound: wav["Cym_Crotale"]},
			{sound: wav["Tom_808_L"]}, # mid left
			{sound: wav["P_Tabla_Te"]},
			{sound: wav["Snare_808"]},
            {sound: wav["Kick_808_L"]}, # bottom left
			{sound: wav["Clap_909"]},
			{sound: wav["P_GanzaTap"]},
			{sound: wav["Kick_Acou1"]}, # foot R
			{sound: wav["Tom_808_H"]}, # foot L
			{sound: wav["Snare_Proc4"]}, # pad top
			{sound: wav["Tom_808_M"]}] # pad rim
	fx = Phaser().rate(47).depth(60).manual(50).resonance(73).separation(88)

#never needing

class Borderline():
	level = 100
	tempo = 87 # check
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

class ThingsChange():
	level = 100
	tempo = 60
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
			
class WhereverThereIsLight():
	level = 100
	tempo = 60
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
			{sound: wav["SE_Noise1"]}, # foot L
			{sound: wav["Clap_909"]}, # pad top
			{sound: wav["Clap_110"]}] # pad rim
	fx = PitchShift().pitch(4).feedback(50)
	
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
			
class Mixtaped():
	level = 100
	tempo = 60
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
	
			
class DaysTurnIntoYears():
	level = 100
	tempo = 60
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
	

class WatchingOverMe(StandardPatch):
	level = 100
	tempo = 120
	