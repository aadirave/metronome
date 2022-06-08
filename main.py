from cProfile import run
from pydub import AudioSegment
from pydub.playback import play
import time
from tkinter import *

root = Tk()
root.title('Metronome')

duration = 150 # time taken for the beat files to play (in ms)

strong_beat = AudioSegment.from_wav('strong_beat.wav')
weak_beat = AudioSegment.from_wav('weak_beat.wav')
sub_strong_beat = AudioSegment.from_wav('sub_strong_beat.wav')

class Beat:
    run  = True

    def __init__(self, bpm, beats_per_bar=4, accents=[1]):
        self.bpm = bpm
        self.beats_per_bar = beats_per_bar
        self.accents = [accent - 1 for accent in accents] # adjusting for zero index
    
    def play(self):
        delay = ((60000 / self.bpm) - duration) / 1000 # delay in ms

        count = 0

        while run:
            if count % self.beats_per_bar in self.accents and count % self.beats_per_bar == 0:
                play(strong_beat)
            elif count % self.beats_per_bar in self.accents and count  % self.beats_per_bar != 0:
                play(sub_strong_beat)
            else:
                play(weak_beat)

            print(count % self.beats_per_bar + 1)

            count += 1

            time.sleep(delay)

def get_bpm():
    bpm = float(e1.get())
    accents = e2.get().split(',')
    accents = [float(accent) for accent in accents]
    beats_per_bar = int(e3.get())

    global bt
    bt = Beat(bpm=bpm, accents=accents, beats_per_bar=beats_per_bar)

    bt.play()

e1 = Entry(root, width=40)
e1.grid(row=0, column=0, columnspan=5)
e1.insert(0, 'Enter BPM here')
e2 = Entry(root, width=20)
e2.grid(row=1, column=1)
e2.insert(0, 'Enter accents here')
e3 = Entry(root, width=20)
e3.insert(0, 'Enter beats per bar')
e3.grid(row=1, column=0)
button = Button(root, text='Play', width=40, command=get_bpm)
button.grid(row=2, column=0, columnspan=2)

root.mainloop()

