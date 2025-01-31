"""A program designed to update the lore tidbit in chatlog.txt, to be used
in tandem with OBS to generate loading screen fun facts.

@author: Judah Munoz"""
import csv
import random
import time
from io import TextIOWrapper


delay = 20
"""Delay between text changing in seconds."""

def load_text(f: TextIOWrapper, textdump: str, index: int):
    """Writes a lore tidbit into a file.

    @param f: the file to write to
    @param textdump: a list of lore tidbit strings

    """
    f.write("\n" + textdump[index])
    f.flush()
    

if __name__ == "__main__":
    textdump = []

    with open('load_text.csv', newline='\n') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            textdump += row

    file = open('chatlog.txt', 'w')
    count = len(textdump) - 1

    while (True):
        load_text(file, textdump, random.randint(0, count))
        time.sleep(delay)


    load_text(file, textdump, 9)
    