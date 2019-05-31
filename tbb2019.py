#!/usr/bin/env python

from sounds import sounds as wav
from effects import *
from standardPatch import StandardPatch

note = "note"
channel = "channel"
sound = "sound"
bypassFx = "bypassFx"




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
            {sound: wav["Clap_909"]}, # bottom left
			{sound: wav["P_GanzaTap"]},
			{sound: wav["P_Triangl_cl"]},
			{sound: wav["Kick_Acou2"]}, # foot R
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
			{sound: wav["SnareXs_6"]}, # pad top
			{sound: wav["Snare_Proc4"]}] # pad rim

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

class Borderline():
	level = 100
	tempo = 87 # check
	pads = [{sound: wav["Cym_Splash1"]}, #top left
			{sound: wav["Cym_Splash2"]},
			{sound: wav["Cym_Crotale"]},
			{sound: wav["Clap_Hse2"]}, # mid left
			{sound: wav["P_GanzaTap"], note: 62, channel: 0},
			{sound: wav["P_Tamb_DnB"], note: 64, channel: 0},
            {sound: wav["Clap_Min"]}, # bottom left
			{sound: wav["P_GanzaTap"]},
			{sound: wav["P_Tamb_DnB"]},
			{sound: wav["Kick_Acou1"], note: 57, channel: 0}, # foot R
			{sound: wav["Clap_808"]}, # foot L
			{sound: wav["P_Tambourine"]}, # pad top
			{sound: wav["Snare_Proc4"]}] # pad rim

class ThingsChange():
	level = 100
	tempo = 60
	pads = [{sound: wav["Cym_Splash1"]}, #top left
			{sound: wav["P_Triangl_op"]},
			{sound: wav["Cym_Crotale"]},
			{sound: wav["Ride_DnB"], note: 66, channel: 0}, # mid left
			{sound: wav["Ride_DnB"], note: 68, channel: 0},
			{sound: wav["Ride_DnB"], note: 71, channel: 0},
			{sound: wav["Ride_DnB"], note: 59, channel: 0}, # bottom left
			{sound: wav["Ride_DnB"], note: 63, channel: 0},
			{sound: wav["Ride_DnB"], note: 64, channel: 0},
			{sound: wav["Kick_Acou1"]}, # foot R
			{sound: wav["timbaleQ"]}, # foot L
			{sound: wav["Clap_Min"]}, # pad top
			{sound: wav["Snare_Proc4"]}] # pad rim
			
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
			{sound: wav["SnareXs_4"]}, # foot L
			{sound: wav["Snare_Proc4"]}, # pad top
			{sound: wav["SE_Noise1"]}] # pad rim
			
class WhereverThereIsLight():
	level = 100
	tempo = 63
	pads = [{note: 61, channel: 0, sound: wav["Cym_Splash1"]},
			{note: 63, channel: 0, sound: wav["P_Triangl_op"]},
			{note: 64, channel: 0, sound: wav["Cym_Crotale"]},
			{note: 66, channel: 0},
			{note: 68, channel: 0},
			{note: 69, channel: 0},
			{note: 52, channel: 0},
			{note: 56, channel: 0},
			{note: 59, channel: 0},
			{sound: wav["Kick_808_L"]}, # foot R
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
			{sound: wav["Ride_DnB"]}, # foot L
			{sound: wav["Clap_909"]}, # pad top
			{sound: wav["Clap_110"]}] # pad rim
	
class AllTheBlueChanges(): #58
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
			
class Mixtaped():
	level = 100
	tempo = 47
	pads = [{note: 71, channel: 0, sound: wav["HH_909_op"]}, #top left
			{note: 74, channel: 0, sound: wav["Cym_Fx2"]},
			{note: 76, channel: 0, sound: wav["Cym_Crotale"]},
			{note: 60, channel: 0, sound: wav["P_Tabla_Te"]}, # mid left
			{note: 62, channel: 0, sound: wav["Snare_Proc4"]},
			{note: 64, channel: 0, sound: wav["Ride_Acou"]},
            {note: 40, channel: 0, sound: wav["Kick_808_L"]}, # bottom left
			{note: 45, channel: 0, sound: wav["Snare_Hph"]},
			{note: 59, channel: 0, sound: wav["HH_Proc2_cl"]},
			{sound: wav["Kick_Acou1"]}, # foot R
			{sound: wav["SE_Noise4"]}, # foot L
			{note: 66, channel: 0, sound: wav["SE_Crasher"]}, # pad top
			{note: 88, channel: 0, sound: wav["SE_VerbPf"]}] # pad rim
	fx = Reverb().time(30).preDelay(5).density(10).effLevel(100)
	
class WarmupMan():
	level = 100
	tempo = 122
	pads = [{note: 65, channel: 0, sound: wav["Tom_808_L"]},
			{note: 70, channel: 0, sound: wav["Tom_808_M"]},
			{note: 72, channel: 0, sound: wav["Tom_808_H"]},
			{note: 53, channel: 0, sound: wav["Tom_Roto_L"]},
			{note: 55, channel: 0, sound: wav["Tom_Roto_M"]},
			{note: 62, channel: 0, sound: wav["Tom_Roto_H"]},
			{note: 24, channel: 0, sound: wav["Tom_Acou_L"]},
			{note: 46, channel: 0, sound: wav["Tom_Acou_M"]},
			{note: 51, channel: 0, sound: wav["Tom_Acou_H"]},
			{note: 36, channel: 0, sound: wav["Kick_Acou1"]},
			{note: 48, channel: 0, sound: wav["SnareXs_4"]},
			{note: 60, channel: 0, sound: wav["Ride_Acou"]},
			{note: 70, channel: 0, sound: wav["Ride_Proc1Bl"]}]
	fx = Vibrato().rate(77).depth(69)

class DaysTurnIntoYears():
	level = 100
	tempo = 84
	pads = [{note: 79, channel: 0, sound: wav["S00238"]}, #top left
			{note: 81, channel: 0, sound: wav["S00240"]},
			{note: 83, channel: 0, sound: wav["S00241"]},
			{note: 69, channel: 0, sound: wav["daysRad1"]}, # mid left
			{note: 71, channel: 0, sound: wav["daysRad2"]},
			{note: 74, channel: 0, sound: wav["daysRad3"]},
            {note: 52, channel: 0, sound: wav["Kick_DnB2"]}, # bottom left
			{note: 64, channel: 0, sound: wav["Clap_Min"]},
			{note: 76, channel: 0, sound: wav["P_Claves"]},
			{sound: wav["Kick_Acou1"]}, # foot R
			{sound: wav["SE_Crasher"]}, # foot L
			{note: 57, channel: 0, sound: wav["P_Claves"]}, # pad top
			{note: 59, channel: 0, sound: wav["P_Claves"]}] # pad rim
	fx = Reverb().time(60).preDelay(50).density(10).effLevel(100)

class WatchingOverMe(StandardPatch): #062
	level = 100
	tempo = 102
	pads = [{sound: wav["P_Triangl_cl"]}, #top left
			{sound: wav["P_Triangl_op"]},
			{sound: wav["Cym_Crotale"]},
			{sound: wav["roto8"]}, # mid left
			{sound: wav["timbale2"]},
			{sound: wav["P_Timbale_L"]},
            {sound: wav["Kick_808_L"]}, # bottom left
			{sound: wav["P_CongaProcH"]},
			{sound: wav["P_Tabla_Ge"]},
			{sound: wav["Kick_Acou1"], bypassFx: True}, # foot R
			{sound: wav["Clap_Hse2"]}, # foot L
			{sound: wav["Clap_Min"]}, # pad top
			{sound: wav["P_CongaProcS"]}] # pad rim
	fx = SyncDelay().feedback(31).effLevel(60)
			
class NeverNeeding():
	level = 100
	tempo = 120
	pads = [{sound: wav["Cym_Splash1"], bypassFx: True}, #top left
			{sound: wav["Cym_Splash2"], bypassFx: True},
			{sound: wav["Cym_Crotale"], bypassFx: True},
			{sound: wav["Clap_Hse1"]}, # mid left
			{sound: wav["HH_Proc2_op"], bypassFx: True},
			{sound: wav["Cym_Fx2"], bypassFx: True},
            {sound: wav["Kick_808_L"], bypassFx: True}, # bottom left
			{sound: wav["P_Tambourine"], bypassFx: True},
			{sound: wav["P_GanzaTap"], bypassFx: True},
			{sound: wav["Kick_Acou1"], bypassFx: True}, # foot R
			{sound: wav["SE_Crasher"], bypassFx: True}, # foot L
			{sound: wav["Snare_Proc4"]}, # pad top
			{sound: wav["SE_Noise1"]}] # pad rim
	fx = Reverb().time(73).preDelay(63).density(10).effLevel(80)
	
# acoustic songs
class Ghostlike(StandardPatch):
	level = 100
	tempo = 120
	
class ForestAlmostBurning(StandardPatch):
	level = 100
	tempo = 120

class IGoDeeper(StandardPatch):
	level = 100
	tempo = 120
	
class TheWarOnMe(StandardPatch):
	level = 100
	tempo = 120
	
class KillingToSurvive(StandardPatch):
	level = 100
	tempo = 120

class ItsTheWorld(StandardPatch):
	level = 100
	tempo = 73
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
			{sound: wav["Kick_DbS"]}, # foot L
			{sound: wav["Snare_Proc4"]}, # pad top
			{sound: wav["SE_Noise1"]}] # pad rim
	