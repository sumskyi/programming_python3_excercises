#!/usr/bin/env python3

# generates awful poems

import random
import sys

articles    = ("the", "a", "another", "her", "his")
subjects    = ("cat", "dog", "horse", "man", "woman", "boy", "girl")
verbs       = ("sang", "ran", "jumped", "said", "fought", "swam",
                "saw", "heard", "felt", "slept", "hopped", "hoped", "cried", "laughed", "walked")
adverbs     = ("loudly", "quietly", "quickly", "slowly", "well",
                "badly", "rudely", "politely")

lines = 5
if(len(sys.argv) > 0):
    try:
        tmp = int(sys.argv[1])
        if(1 <= tmp <= 10):
            lines = tmp
        else:
            print('lines must be 1-10')
    except ValueError:
        print("usage: {} [lines]".format(__file__))

def random_word(seq):
    return random.choice(seq)

#while lines:
for i in range(1, lines + 1):
    sentence = [random_word(articles), random_word(subjects), random_word(verbs)]
    if random.randint(0, 1):
        pass
    else:
        sentence.append(random_word(adverbs))
    print(*sentence)
    #lines -= 1
