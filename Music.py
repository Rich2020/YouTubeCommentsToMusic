import os
from playsound import playsound
from os import listdir
import time


class Notes:

    available_names = ['A0','ASharp0','B0','C1','CSharp1','D1','DSharp1','E1','F1','FSharp1','G1','GSharp1','A1','ASharp1','B1','C2','CSharp2','D2','DSharp2','E2','F2','FSharp2','G2','GSharp2','A2','ASharp2','B2','C3','CSharp3','D3','DSharp3','E3','F3','FSharp3','G3','GSharp3','A3','ASharp3','B3','C4','CSharp4','D4','DSharp4','E4','F4','FSharp4','G4','GSharp4','A4','ASharp4','B4','C5','CSharp5','D5','DSharp5','E5','F5','FSharp5','G5','GSharp5','A5','ASharp5','B5','C6','CSharp6','D6','DSharp6','E6','F6','FSharp6','G6','GSharp6','A6','ASharp6','B6','C7','CSharp7','D7','DSharp7','E7','F7','FSharp7','G7','GSharp7','A7','ASharp7','B7','C8']
    mp3_folder = 'piano_notes_mp3'

    class A0:
        Name = 'A0'
        Frequency = 27.5
        MIDI = 21

    class ASharp0:
        Name = 'ASharp0'
        Frequency = 29.1352
        MIDI = 22

    class B0:
        Name = 'B0'
        Frequency = 30.8677
        MIDI = 23

    class C1:
        Name = 'C1'
        Frequency = 32.7032
        MIDI = 24

    class CSharp1:
        Name = 'CSharp1'
        Frequency = 34.6478
        MIDI = 25

    class D1:
        Name = 'D1'
        Frequency = 36.7081
        MIDI = 26

    class DSharp1:
        Name = 'DSharp1'
        Frequency = 38.8909
        MIDI = 27

    class E1:
        Name = 'E1'
        Frequency = 41.2034
        MIDI = 28

    class F1:
        Name = 'F1'
        Frequency = 43.6535
        MIDI = 29

    class FSharp1:
        Name = 'FSharp1'
        Frequency = 46.2493
        MIDI = 30

    class G1:
        Name = 'G1'
        Frequency = 48.9994
        MIDI = 31

    class GSharp1:
        Name = 'GSharp1'
        Frequency = 51.9131
        MIDI = 32

    class A1:
        Name = 'A1'
        Frequency = 55.0
        MIDI = 33

    class ASharp1:
        Name = 'ASharp1'
        Frequency = 58.2705
        MIDI = 34

    class B1:
        Name = 'B1'
        Frequency = 61.7354
        MIDI = 35

    class C2:
        Name = 'C2'
        Frequency = 65.4064
        MIDI = 36

    class CSharp2:
        Name = 'CSharp2'
        Frequency = 69.2957
        MIDI = 37

    class D2:
        Name = 'D2'
        Frequency = 73.4162
        MIDI = 38

    class DSharp2:
        Name = 'DSharp2'
        Frequency = 77.7817
        MIDI = 39

    class E2:
        Name = 'E2'
        Frequency = 82.4069
        MIDI = 40

    class F2:
        Name = 'F2'
        Frequency = 87.3071
        MIDI = 41

    class FSharp2:
        Name = 'FSharp2'
        Frequency = 92.4986
        MIDI = 42

    class G2:
        Name = 'G2'
        Frequency = 97.9989
        MIDI = 43

    class GSharp2:
        Name = 'GSharp2'
        Frequency = 103.8262
        MIDI = 44

    class A2:
        Name = 'A2'
        Frequency = 110.0
        MIDI = 45

    class ASharp2:
        Name = 'ASharp2'
        Frequency = 116.5409
        MIDI = 46

    class B2:
        Name = 'B2'
        Frequency = 123.4708
        MIDI = 47

    class C3:
        Name = 'C3'
        Frequency = 130.8128
        MIDI = 48

    class CSharp3:
        Name = 'CSharp3'
        Frequency = 138.5913
        MIDI = 49

    class D3:
        Name = 'D3'
        Frequency = 146.8324
        MIDI = 50

    class DSharp3:
        Name = 'DSharp3'
        Frequency = 155.5635
        MIDI = 51

    class E3:
        Name = 'E3'
        Frequency = 164.8138
        MIDI = 52

    class F3:
        Name = 'F3'
        Frequency = 174.6141
        MIDI = 53

    class FSharp3:
        Name = 'FSharp3'
        Frequency = 184.9972
        MIDI = 54

    class G3:
        Name = 'G3'
        Frequency = 195.9977
        MIDI = 55

    class GSharp3:
        Name = 'GSharp3'
        Frequency = 207.6523
        MIDI = 56

    class A3:
        Name = 'A3'
        Frequency = 220.0
        MIDI = 57

    class ASharp3:
        Name = 'ASharp3'
        Frequency = 233.0819
        MIDI = 58

    class B3:
        Name = 'B3'
        Frequency = 246.9417
        MIDI = 59

    class C4:
        Name = 'C4'
        Frequency = 261.6256
        MIDI = 60

    class CSharp4:
        Name = 'CSharp4'
        Frequency = 277.1826
        MIDI = 61

    class D4:
        Name = 'D4'
        Frequency = 293.6648
        MIDI = 62

    class DSharp4:
        Name = 'DSharp4'
        Frequency = 311.127
        MIDI = 63

    class E4:
        Name = 'E4'
        Frequency = 329.6276
        MIDI = 64

    class F4:
        Name = 'F4'
        Frequency = 349.2282
        MIDI = 65

    class FSharp4:
        Name = 'FSharp4'
        Frequency = 369.9944
        MIDI = 66

    class G4:
        Name = 'G4'
        Frequency = 391.9954
        MIDI = 67

    class GSharp4:
        Name = 'GSharp4'
        Frequency = 415.3047
        MIDI = 68

    class A4:
        Name = 'A4'
        Frequency = 440.0
        MIDI = 69

    class ASharp4:
        Name = 'ASharp4'
        Frequency = 466.1638
        MIDI = 70

    class B4:
        Name = 'B4'
        Frequency = 493.8833
        MIDI = 71

    class C5:
        Name = 'C5'
        Frequency = 523.2511
        MIDI = 72

    class CSharp5:
        Name = 'CSharp5'
        Frequency = 554.3653
        MIDI = 73

    class D5:
        Name = 'D5'
        Frequency = 587.3295
        MIDI = 74

    class DSharp5:
        Name = 'DSharp5'
        Frequency = 622.254
        MIDI = 75

    class E5:
        Name = 'E5'
        Frequency = 659.2551
        MIDI = 76

    class F5:
        Name = 'F5'
        Frequency = 698.4565
        MIDI = 77

    class FSharp5:
        Name = 'FSharp5'
        Frequency = 739.9888
        MIDI = 78

    class G5:
        Name = 'G5'
        Frequency = 783.9909
        MIDI = 79

    class GSharp5:
        Name = 'GSharp5'
        Frequency = 830.6094
        MIDI = 80

    class A5:
        Name = 'A5'
        Frequency = 880.0
        MIDI = 81

    class ASharp5:
        Name = 'ASharp5'
        Frequency = 932.3275
        MIDI = 82

    class B5:
        Name = 'B5'
        Frequency = 987.7666
        MIDI = 83

    class C6:
        Name = 'C6'
        Frequency = 1046.5023
        MIDI = 84

    class CSharp6:
        Name = 'CSharp6'
        Frequency = 1108.7305
        MIDI = 85

    class D6:
        Name = 'D6'
        Frequency = 1174.6591
        MIDI = 86

    class DSharp6:
        Name = 'DSharp6'
        Frequency = 1244.5079
        MIDI = 87

    class E6:
        Name = 'E6'
        Frequency = 1318.5102
        MIDI = 88

    class F6:
        Name = 'F6'
        Frequency = 1396.9129
        MIDI = 89

    class FSharp6:
        Name = 'FSharp6'
        Frequency = 1479.9777
        MIDI = 90

    class G6:
        Name = 'G6'
        Frequency = 1567.9817
        MIDI = 91

    class GSharp6:
        Name = 'GSharp6'
        Frequency = 1661.2188
        MIDI = 92

    class A6:
        Name = 'A6'
        Frequency = 1760.0
        MIDI = 93

    class ASharp6:
        Name = 'ASharp6'
        Frequency = 1864.655
        MIDI = 94

    class B6:
        Name = 'B6'
        Frequency = 1975.5332
        MIDI = 95

    class C7:
        Name = 'C7'
        Frequency = 2093.0045
        MIDI = 96

    class CSharp7:
        Name = 'CSharp7'
        Frequency = 2217.461
        MIDI = 97

    class D7:
        Name = 'D7'
        Frequency = 2349.3181
        MIDI = 98

    class DSharp7:
        Name = 'DSharp7'
        Frequency = 2489.0159
        MIDI = 99

    class E7:
        Name = 'E7'
        Frequency = 2637.0205
        MIDI = 100

    class F7:
        Name = 'F7'
        Frequency = 2793.8259
        MIDI = 101

    class FSharp7:
        Name = 'FSharp7'
        Frequency = 2959.9554
        MIDI = 102

    class G7:
        Name = 'G7'
        Frequency = 3135.9635
        MIDI = 103

    class GSharp7:
        Name = 'GSharp7'
        Frequency = 3322.4376
        MIDI = 104

    class A7:
        Name = 'A7'
        Frequency = 3520.0
        MIDI = 105

    class ASharp7:
        Name = 'ASharp7'
        Frequency = 3729.3101
        MIDI = 106

    class B7:
        Name = 'B7'
        Frequency = 3951.0664
        MIDI = 107

    class C8:
        Name = 'C8'
        Frequency = 4186.009
        MIDI = 108


class Player:

    def __init__(self):

        self.notes = {}

        for f in listdir(Notes.mp3_folder):
            if not f.startswith('.'):

                file_name_no_extension = int(f.split('.')[0])
                note_name = Notes.available_names[file_name_no_extension-1]

                path_to_file = os.path.join(Notes.mp3_folder, f)
                self.notes[note_name] = path_to_file

    def play_notes(self, the_notes, interval_between_notes = 1):
        for note in the_notes:
            self.play(note)
            time.sleep(interval_between_notes)

    def play(self, the_note):
        playsound(self.notes[the_note],block=False)


class GenerateSelf:

    @staticmethod
    def generate():

        import pandas as pd
        from io import StringIO

        music_notes_table = StringIO("""
        Frequency,Note,MIDI
        27.5000,A0,21
        29.1352,A#0,22
        30.8677,B0,23
        32.7032,C1,24
        34.6478,C#1,25
        36.7081,D1,26
        38.8909,D#1,27
        41.2034,E1,28
        43.6535,F1,29
        46.2493,F#1,30
        48.9994,G1,31
        51.9131,G#1,32
        55.0000,A1,33
        58.2705,A#1,34
        61.7354,B1,35
        65.4064,C2,36
        69.2957,C#2,37
        73.4162,D2,38
        77.7817,D#2,39
        82.4069,E2,40
        87.3071,F2,41
        92.4986,F#2,42
        97.9989,G2,43
        103.8262,G#2,44
        110.0000,A2,45
        116.5409,A#2,46
        123.4708,B2,47
        130.8128,C3,48
        138.5913,C#3,49
        146.8324,D3,50
        155.5635,D#3,51
        164.8138,E3,52
        174.6141,F3,53
        184.9972,F#3,54
        195.9977,G3,55
        207.6523,G#3,56
        220.0000,A3,57
        233.0819,A#3,58
        246.9417,B3,59
        261.6256,C4,60
        277.1826,C#4,61
        293.6648,D4,62
        311.1270,D#4,63
        329.6276,E4,64
        349.2282,F4,65
        369.9944,F#4,66
        391.9954,G4,67
        415.3047,G#4,68
        440.0000,A4,69
        466.1638,A#4,70
        493.8833,B4,71
        523.2511,C5,72
        554.3653,C#5,73
        587.3295,D5,74
        622.2540,D#5,75
        659.2551,E5,76
        698.4565,F5,77
        739.9888,F#5,78
        783.9909,G5,79
        830.6094,G#5,80
        880.0000,A5,81
        932.3275,A#5,82
        987.7666,B5,83
        1046.5023,C6,84
        1108.7305,C#6,85
        1174.6591,D6,86
        1244.5079,D#6,87
        1318.5102,E6,88
        1396.9129,F6,89
        1479.9777,F#6,90
        1567.9817,G6,91
        1661.2188,G#6,92
        1760.0000,A6,93
        1864.6550,A#6,94
        1975.5332,B6,95
        2093.0045,C7,96
        2217.4610,C#7,97
        2349.3181,D7,98
        2489.0159,D#7,99
        2637.0205,E7,100
        2793.8259,F7,101
        2959.9554,F#7,102
        3135.9635,G7,103
        3322.4376,G#7,104
        3520.0000,A7,105
        3729.3101,A#7,106
        3951.0664,B7,107
        4186.0090,C8,108
        """)

        df = pd.read_csv(music_notes_table, sep=",")

        for index, row in df.iterrows():
            name = row['Note'].replace('#', 'Sharp')
            freq = row['Frequency']
            midi = row['MIDI']
            line = "class {NAME}:\n\tName = '{NAME}'\n\tFrequency = {FREQ}\n\tMIDI = {MIDI}".\
                format(NAME=name, FREQ=freq, MIDI=midi)
            print()
            print()
            print(line)
