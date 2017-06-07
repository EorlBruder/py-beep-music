import os

PAUSE = 1
C0 = 16.351598
Cs0 = 17.323914
D0 = 18.354048
Ds0 = 19.445436
E0 = 20.601722
F0 = 21.826764
Fs0 = 23.124651
G0 = 24.499715
Gs0 = 25.956544
A0 = 27.500000
As0 = 29.135235
B0 = 30.867706
C1 = 32.703196
Cs1 = 34.647829
D1 = 36.708096
Ds1 = 38.890873
E1 = 41.203445
F1 = 43.653529
Fs1 = 46.249303
G1 = 48.999429
Gs1 = 51.913087
A1 = 55.000000
As1 = 58.270470
B1 = 61.735413
C2 = 65.406391
Cs2 = 69.295658
D2 = 73.416192
Ds2 = 77.781746
E2 = 82.406889
F2 = 87.307058
Fs2 = 92.498606
G2 = 97.998859
Gs2 = 103.826174
A2 = 110.000000
As2 = 116.540940
B2 = 123.470825
C3 = 130.812783
Cs3 = 138.591315
D3 = 146.832384
Ds3 = 155.563492
E3 = 164.813778
F3 = 174.614116
Fs3 = 184.997211
G3 = 195.997718
Gs3 = 207.652349
A3 = 220.000000
As3 = 233.081881
B3 = 246.941651
C4 = 261.625565
Cs4 = 277.182631
D4 = 293.664768
Ds4 = 311.126984
E4 = 329.627557
F4 = 349.228231
Fs4 = 369.994423
G4 = 391.995436
Gs4 = 415.304698
A4 = 440.000000
As4 = 466.163762
B4 = 493.883301
C5 = 523.251131
Cs5 = 554.365262
D5 = 587.329536
Ds5 = 622.253967
E5 = 659.255114
F5 = 698.456463
Fs5 = 739.988845
G5 = 783.990872
Gs5 = 830.609395
A5 = 880.000000
As5 = 932.327523
B5 = 987.766603
C6 = 1046.502261
Cs6 = 1108.730524
D6 = 1174.659072
Ds6 = 1244.507935
E6 = 1318.510228
F6 = 1396.912926
Fs6 = 1479.977691
G6 = 1567.981744
Gs6 = 1661.218790
A6 = 1760.000000
As6 = 1864.655046
B6 = 1975.533205
C7 = 2093.004522
Cs7 = 2217.461048
D7 = 2349.318143
Ds7 = 2489.015870
E7 = 2637.020455
F7 = 2793.825851
Fs7 = 2959.955382
G7 = 3135.963488
Gs7 = 3322.437581
A7 = 3520.000000
As7 = 3729.310092
B7 = 3951.066410
C8 = 4186.009045
Cs8 = 4434.922096
D8 = 4698.636287
Ds8 = 4978.031740
E8 = 5274.040911
F8 = 5587.651703
Fs8 = 5919.910763
G8 = 6271.926976
Gs8 = 6644.875161
A8 = 7040.000000
As8 = 7458.620184
B8 = 7902.132820
C9 = 8372.018090
Cs9 = 8869.844191
D9 = 9397.272573
Ds9 = 9956.063479
E9 = 10548.081821
F9 = 11175.303406
Fs9 = 11839.821527
G9 = 12543.853951
Gs9 = 13289.750323
A9 = 14080.000000
As9 = 14917.240369
B9 = 15804.265640

VIERTEL = 60000

ACHTEL = VIERTEL / 2
SECHZEHNTEL = ACHTEL / 2
ZWEIUNDDREISSIGSTEL = SECHZEHNTEL / 2

HALBE = VIERTEL * 2
GANZE = HALBE * 2

PUNKTIERTE_VIERTEL = VIERTEL + ACHTEL

STACCATO = 1
LEGATO = 0

def play(tune, speed=150):
	cmd='beep -f 1 -l 10 '
	for i,j,k in tune:
		cmd=cmd + ' -n -f '+ str(i) + ' -l'+str(j/speed-k*(speed/2)) + ' -n -f 1 -l'+str(speed/2)
	os.system(cmd)
