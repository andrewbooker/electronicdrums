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
    {"song": "The Warm-Up Man Forever", "tempo": 122, "korg": 19, "spd-sx": 26},
    {"song": "Sing To Me", "tempo": 63},
    {"song": "Watching Over Me", "tempo": 102},
    {"song": "Sorry Looking Soldier", "tempo": 42},
    {"song": "Brightest Blue", "tempo": 84},
    {"song": "A Stand-Up For The Dying", "tempo": 60},
    {"song": "Wherever There Is Light", "tempo": 60},
    {"song": "Rainmark", "tempo": 126},
    {"song": "Days Turn Into Years", "tempo": 84, "korg": 4, "spd-sx": 19},
    {"song": "Pretty Genius", "tempo": 69},
    {"song": "Time Travel In Texas", "tempo": 78, "spd-sx": 25},
    {"song": "Mixtaped", "tempo": 47, "korg": 21, "spd-sx": 24}
]


class ControlChangeSender:
    def __init__(self, channel, number, midiOut, freq):
        self.channel = channel
        self.number = number
        self.midiOut = midiOut
        self.freq = freq

    def start(self, shouldStop):
        start_time = time.monotonic()
        interval = 0.2
        while not shouldStop.is_set():
            elapsed = time.monotonic() - start_time
            v = math.sin(2 * math.pi * self.freq * elapsed)
            outport.send(mido.Message("control_change", channel=self.channel, control=self.number, value=math.floor(56 * (1.0 + v))))

            next_time = start_time + (int(elapsed / interval) + 1) * interval
            time.sleep(max(0, next_time - time.monotonic()))


def sendProgramChange(song, instr):
    p = song[instr] if instr in song else devices[instr]["defaultProg"]
    c = devices[instr]["channel"]
    outport.send(mido.Message("program_change", channel=c, program=p))

def selectSong(idx):
    song = setList[idx]
    sendProgramChange(song, "korg")
    sendProgramChange(song, "spd-sx")


for i in range(len(setList)):
    s = setList[i]
    print(f"{(1 + i):2d}", s["song"])


songIdx = 0
selectSong(songIdx)


controlSignals = [
    ControlChangeSender(devices["korg"]["channel"], 12, outport, 0.2),
    ControlChangeSender(devices["korg"]["channel"], 13, outport, 1.8),
    ControlChangeSender(devices["spd-sx"]["channel"], 12, outport, 0.5),
    ControlChangeSender(devices["spd-sx"]["channel"], 13, outport, 2.7)
]

shouldStop = threading.Event()
threads = [threading.Thread(target=c.start, args=(shouldStop,), daemon=True) for c in controlSignals]
[t.start() for t in threads]
done = False

print("Started. Press 'q' to exit")
while not done:
    c = readchar.readchar()
    if c == "q":
        done = True
        shouldStop.set()
        [t.join() for t in threads]
    if c == "n":
        outport.send(mido.Message("note_on", channel=0, note=60, velocity=64, time=0))
        time.sleep(1)
        outport.send(mido.Message("note_off", channel=0, note=60, velocity=0, time=0))

