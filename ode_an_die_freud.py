from py_beep_music import *

pt1=[(E3,VIERTEL),(E3,VIERTEL),(F3,VIERTEL),(G3,VIERTEL),(G3,VIERTEL),(F3,VIERTEL),(E3,VIERTEL),(D3,VIERTEL),(C3,VIERTEL),(C3,VIERTEL),(D3,VIERTEL),(E3,VIERTEL),(E3,PUNKTIERTE_VIERTEL),(D3,ACHTEL),(D3,HALBE)]
pt2=[(E3,VIERTEL),(E3,VIERTEL),(F3,VIERTEL),(G3,VIERTEL),(G3,VIERTEL),(F3,VIERTEL),(E3,VIERTEL),(D3,VIERTEL),(C3,VIERTEL),(C3,VIERTEL),(D3,VIERTEL),(E3,VIERTEL),(D3,PUNKTIERTE_VIERTEL),(C3,ACHTEL),(C3,HALBE)]
pt3=[(D3,VIERTEL),(D3,VIERTEL),(E3,VIERTEL),(C3,VIERTEL),(D3,VIERTEL),(E3,ACHTEL),(F3,ACHTEL),(E3,VIERTEL),(C3,VIERTEL),(D3,VIERTEL),(E3,ACHTEL),(F3,ACHTEL),(E3,VIERTEL),(D3,VIERTEL),(C3,VIERTEL),(D3,VIERTEL),(G2,VIERTEL)]
pt4=[(E3,HALBE),(E3,VIERTEL),(F3,VIERTEL),(G3,VIERTEL),(G3,VIERTEL),(F3,VIERTEL),(E3,VIERTEL),(D3,VIERTEL),(C3,VIERTEL),(C3,VIERTEL),(D3,VIERTEL),(E3,VIERTEL),(D3,PUNKTIERTE_VIERTEL),(C3,ACHTEL),(C3,HALBE)]

tune = pt1 + pt2 + pt3 + pt4

play(tune)
