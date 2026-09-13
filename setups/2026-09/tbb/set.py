#!/usr/bin/env python3

# sudo pip install mido
# sudo pip install python-rtmidi
import mido
import time
import math
import threading
import readchar


portNames = mido.get_output_names()
portName = portNames[1]
outport = mido.open_output(portName)

devices = {
    "korg": {"channel": 0, "defaultProg": 35},
    "spd-sx": {"channel": 13, "defaultProg": 81}
}


setList = [
    {"name": "Warm-Up Man Forever", "tempo": 122, "korg": 19, "spd-sx": 26},
    {"name": "Sing To Me", "tempo": 63},
    {"name": "Watching Over Me", "tempo": 102},
    {"name": "Sorry Looking Soldier", "tempo": 42},
    {"name": "Brightest Blue", "tempo": 84},
    {"name": "Stand-Up For The Dying", "tempo": 60},
    {"name": "Wherever There Is Light", "tempo": 60},
    {"name": "Rainmark", "tempo": 126},
    {"name": "Days Turn Into Years", "tempo": 84, "korg": 4, "spd-sx": 19},
    {"name": "Pretty Genius", "tempo": 69},
    {"name": "Time Travel In Texas", "tempo": 78, "spd-sx": 25},
    {"name": "Mixtaped", "tempo": 47, "korg": 21, "spd-sx": 24}
]


def sendProgramChange(song, instr):
    p = song[instr] if instr in song else devices[instr]["defaultProg"]
    c = devices[instr]["channel"]
    outport.send(mido.Message("program_change", channel=c, program=p))


def selectSong(idx):
    song = setList[idx]
    print("Setting to", song["name"])
    sendProgramChange(song, "korg")
    sendProgramChange(song, "spd-sx")


for i in range(len(setList)):
    song = setList[i]
    print(f"{(1 + i):2d}", song["name"])


songIdx = 0
selectSong(songIdx)

