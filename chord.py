import pandas as pd
from plotapi import Chord
import numpy as np
import json

Chord.user = "annylin@gmail.com"
Chord.key = "PLOTAPI-P-aaa63a3a-f584-4ad3-b148-f9aa97bf2752"

names = ["RPG","Action","Racing","Adventure","Strategy","Indie","Free to Play",'Simulation',"Casual","Sports","Massively Multiplayer","Early Access"]

matrix = [
[100,91,76,90,92,89,38,81,83,74,31,34],
[91,100,85,94,90,91,38,83,88,83,28,35],
[76,85,100,86,84,81,33,88,89,92,31,45],
[90,94,86,100,89,94,32,84,93,85,23,36],
[92,90,84,89,100,90,35,92,88,81,27,37],
[89,91,81,94,90,100,36,79,92,81,19,32],
[38,38,33,32,35,36,100,30,31,35,57,17],
[81,83,88,84,92,79,30,100,86,83,33,46],
[83,88,89,93,88,92,31,86,100,89,24,39],
[74,83,92,85,81,81,35,83,89,100,26,41],
[31,28,31,23,27,19,57,33,24,26,100,16],
[34,35,45,36,37,32,17,46,39,41,16,100],
]

Chord(matrix, names).to_html("out.html")
