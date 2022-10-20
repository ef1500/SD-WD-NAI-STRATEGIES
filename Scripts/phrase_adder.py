# Simple Script to append phrase at the end of each text file
import glob
textfiles = glob.glob('*.txt')

PHRASE_TO_ADD = "nanashi mumei"

for file in textfiles:
    fopen = open(file, 'a+')
    fopen.write(", " + PHRASE_TO_ADD)
    fopen.close()
    