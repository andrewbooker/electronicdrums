#!/usr/bin/env python

from sounds import sounds as wav
from effects import *
from standardPatch import StandardPatch

note = "note"
channel = "channel"
sound = "sound"
outAssign = "outAssign"
vol = "vol"
padOutMaster = 0
padOutFx1 = 1
padOutFx2 = 2
padOutSub = 3
padOutPhones = 4



# 1st is 51
class Ghostlike(StandardPatch):
    level = 100
    tempo = 120

class WhereverThereIsLight():
    level = 100
    tempo = 63
    korg = 15
    pads = [{note: 61, channel: 0, sound: wav["Cym_Splash1"]},
            {note: 63, channel: 0, sound: wav["P_Triangl_op"]},
            {note: 64, channel: 0, sound: wav["Cym_Crotale"]},
            {note: 66, channel: 0, sound: wav["Ride_DnB"], vol: 70},
            {note: 68, channel: 0, sound: wav["Ride_DnB"], vol: 70},
            {note: 69, channel: 0, sound: wav["Ride_DnB"], vol: 70},
            {note: 52, channel: 0, sound: wav["Ride_DnB"], vol: 70},
            {note: 56, channel: 0, sound: wav["Ride_DnB"], vol: 70},
            {note: 59, channel: 0, sound: wav["Ride_DnB"], vol: 70},
            {sound: wav["Kick_808_L"]}, # foot R
            {sound: wav["SE_Crasher"]}, # foot L
            {sound: wav["Snare_Proc4"]}, # pad top
            {sound: wav["SE_Noise1"]}] # pad rim

class AllTheBlueChanges():
    level = 90
    tempo = 122
    korg = 24
    pads = [{note: 60, channel: 0}, #top left
            {note: 62, channel: 0},
            {note: 64, channel: 0},
            {note: 52, channel: 0, vol: 60, sound: wav["HH_DbS_cl"]}, # mid left
            {note: 57, channel: 0, vol: 60, sound: wav["Cym_Fx2"]},
            {note: 59, channel: 0, vol: 60, sound: wav["SE_SweepSlap"]},
            {sound: wav["P_Tamb_Proc"]}, # bottom left
            {sound: wav["P_Tambourine"]},
            {sound: wav["P_Tambourine"]},
            {sound: wav["Kick_Proc3"]}, # foot R
            {sound: wav["SnareXs_2"]}, # foot L
            {sound: wav["Clap_Min"]}, # pad top
            {sound: wav["Clap_110"]}] # pad rim

class WarmupMan():
    level = 100
    tempo = 122
    korg = 19
    pads = [{note: 65, channel: 0, sound: wav["Tom_808_L"]},
            {note: 70, channel: 0, sound: wav["Tom_808_M"]},
            {note: 72, channel: 0, sound: wav["Tom_808_H"]},
            {note: 53, channel: 0, sound: wav["Tom_Roto_L"]},
            {note: 55, channel: 0, sound: wav["Tom_Roto_M"]},
            {note: 62, channel: 0, sound: wav["Tom_Roto_H"]},
            {note: 24, channel: 0, sound: wav["Tom_Acou_L"]},
            {note: 46, channel: 0, sound: wav["Tom_Acou_M"]},
            {note: 51, channel: 0, sound: wav["Tom_Acou_H"]},
            {note: 36, channel: 0, sound: wav["Kick_Acou1"], outAssign: padOutMaster},
            {note: 48, channel: 0, sound: wav["SnareXs_4"]},
            {note: 60, channel: 0, sound: wav["Ride_Acou"]},
            {note: 70, channel: 0, sound: wav["Ride_Proc1Bl"]}]
    fx1 = Vibrato().rate(77).depth(69)

class ItsTheWorld(StandardPatch):
    level = 100
    tempo = 73
    applyMasterFx = True
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

class NotMarriedAnyMore():
    level = 100
    tempo = 89
    pads = [{sound: wav["Cym_Splash1"]}, #top left
            {sound: wav["Cym_Splash2"]},
            {sound: wav["Cym_Crotale"]},
            {sound: wav["Clap_Hse1"]}, # mid left
            {sound: wav["HH_Proc2_op"]},
            {sound: wav["Cym_Fx2"]},
            {sound: wav["Snare_Proc4"]}, # bottom left
            {sound: wav["P_GanzaTap"]},
            {sound: wav["P_Triangl_cl"]},
            {sound: wav["Kick_Acou2"]}, # foot R
            {sound: wav["SE_Crasher"]}, # foot L
            {sound: wav["Snare_Proc4"]}, # pad top
            {sound: wav["SE_Noise1"]}] # pad rim

class KillingToSurvive(StandardPatch):
    level = 100
    tempo = 120

class Mixtaped():
    level = 100
    tempo = 47
    korg = 21
    applyMasterFx = True
    pads = [{note: 71, channel: 0, sound: wav["HH_909_op"]}, #top left
            {note: 74, channel: 0, sound: wav["Cym_Fx2"]},
            {note: 76, channel: 0, sound: wav["Cym_Crotale"]},
            {note: 60, channel: 0, sound: wav["P_Tabla_Te"]}, # mid left
            {note: 62, channel: 0, sound: wav["Snare_Proc4"]},
            {note: 64, channel: 0, sound: wav["Ride_Acou"]},
            {note: 40, channel: 0, sound: wav["Kick_808_L"]}, # bottom left
            {note: 45, channel: 0, sound: wav["Snare_Hph"]},
            {note: 59, channel: 0, sound: wav["HH_Proc2_cl"]},
            {sound: wav["Kick_Acou1"], outAssign: padOutSub}, # foot R
            {sound: wav["SE_Noise4"]}, # foot L
            {note: 66, channel: 0, sound: wav["SE_Crasher"]}, # pad top
            {note: 88, channel: 0, sound: wav["SE_VerbPf"]}] # pad rim
    fx1 = Reverb().time(30).preDelay(5).density(10).effLevel(100)


class ThingsChange():
    level = 100
    tempo = 60
    korg = 15
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

## end of Lorelei ##
class ForestAlmostBurning(StandardPatch):
    level = 100
    tempo = 120


class NeverNeeding():
    level = 100
    tempo = 120
    pads = [{sound: wav["Cym_Splash1"], outAssign: padOutMaster}, #top left
            {sound: wav["Cym_Splash2"], outAssign: padOutMaster},
            {sound: wav["Cym_Crotale"], outAssign: padOutMaster},
            {sound: wav["Clap_Hse1"]}, # mid left
            {sound: wav["HH_Proc2_op"], outAssign: padOutMaster},
            {sound: wav["Cym_Fx2"], outAssign: padOutMaster},
            {sound: wav["Kick_808_L"], outAssign: padOutMaster}, # bottom left
            {sound: wav["P_Tambourine"], outAssign: padOutMaster},
            {sound: wav["P_GanzaTap"], outAssign: padOutMaster},
            {sound: wav["Kick_Acou1"], outAssign: padOutMaster}, # foot R
            {sound: wav["SE_Crasher"], outAssign: padOutMaster}, # foot L
            {sound: wav["Snare_Proc4"]}, # pad top
            {sound: wav["SE_Noise1"]}] # pad rim
    fx1 = Reverb().time(73).preDelay(63).density(10).effLevel(80)

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
    fx1 = Reverb().time(60).preDelay(50).density(10).effLevel(100)

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
            {sound: wav["Kick_Acou1"], outAssign: padOutMaster}, # foot R
            {sound: wav["Clap_Hse2"]}, # foot L
            {sound: wav["Clap_Min"]}, # pad top
            {sound: wav["P_CongaProcS"]}] # pad rim
    fx1 = SyncDelay().feedback(31).effLevel(60)

class Borderline():
    level = 100
    tempo = 87 # check
    korg = 21
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

