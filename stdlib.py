import os
print(os.getcwd())     # current working dir
os.chdir("Tutorial.py")
dir(os)

import glob
print(glob.glob("*.py"))    # suche nach Dateien/Verzeichnissen

import math
ergebnis = math.sqrt(144)*2
print(ergebnis) # 24

# Internet
from urllib.request import urlopen
for line in urlopen("https://andre-nas.servebeer.com/"):
    line = line.decode('utf-8') # binär nach text decodieren
    #if 'EST' in line or 'EDT' in line:
    print(line)
