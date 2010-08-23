#!/usr/bin/env python3

# print digit banner
#  000     1    222   55555     4
# 0   0   11   2   2  5        44
#0     0   1   2  2   5       4 4
#0     0   1     2     555   4  4
#0     0   1    2         5  444444
# 0   0    1   2      5   5     4
#  000    111  22222   555      4

import sys


Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]

One = [" * ",
       "** ",
       " * ",
       " * ",
       " * ",
       " * ",
       "***"]

Two = [" *** ",
       "*   *",
       "*  * ",
       "  *  ",
       " *   ",
       "*    ",
       "*****"]

Three = [" *** ",
         "*   *",
         "    *",
         "  ** ",
         "    *",
         "*   *",
         " *** "]

Four = ["   *  ",
        "  **  ",
        " * *  ",
        "*  *  ",
        "******",
        "   *  ",
        "   *  "]

Five = ["*****",
        "*    ",
        "*    ",
        " *** ",
        "    *",
        "*   *",
        " *** "]

Six = [" *** ",
       "*    ",
       "*    ",
       "**** ",
       "*   *",
       "*   *",
       " *** "]

Seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         "*    ",
         "*    "]

Eight = [" *** ",
         "*   *",
         "*   *",
         " *** ",
         "*   *",
         "*   *",
         " *** "]

Nine = [" ****",
        "*   *",
        "*   *",
        " ****",
        "    *",
        "    *",
        "    *"]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    heigth = len(Zero)
    row = 0
    while row < heigth:
        line = ''
        for digit in digits:
            line += Digits[int(digit)][row].replace('*', digit)
            line += '  '
        print(line)
        row += 1
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
