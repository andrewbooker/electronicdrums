#!/usr/bin/env python3

# sudo pip install mido
# sudo pip install python-rtmidi
import mido
import time


setList = [
    {"song": "The Warm-Up Man Forever", "tempo": 122, "korg": 19, "spd-sx": 27},
    {"song": "Sing To Me", "tempo": 63},
    {"song": "Watching Over Me", "tempo": 102},
    {"song": "Sorry Looking Soldier", "tempo": 42},
    {"song": "Brightest Blue", "tempo": 84},
    {"song": "A Stand-Up For The Dying", "tempo": 60},
    {"song": "Wherever There Is Light", "tempo": 60},
    {"song": "Rainmark", "tempo": 126},
    {"song": "Days Turn Into Years", "tempo": 84, "korg": 4, "spd-sx": 20},
    {"song": "Pretty Genius", "tempo": 69},
    {"song": "Time Travel In Texas", "tempo": 78, "spd-sx": 26},
    {"song": "Mixtaped", "tempo": 47, "korg": 21, "spd-sx": 25}
]



for i in range(len(setList)):
    s = setList[i]
    print(f"{(1 + i):2d}", s["song"])


print(mido.get_output_names())

korgChannel = 0
outport = mido.open_output("USB Midi:USB Midi MIDI 1 20:0")
outport.send(mido.Message("note_on", channel=korgChannel, note=60, velocity=64, time=0))
time.sleep(1)
outport.send(mido.Message("note_off", channel=korgChannel, note=60, velocity=0, time=0))
