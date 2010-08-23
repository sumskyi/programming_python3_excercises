#!/usr/bin/env python3

# generates awful poems

import random


articles    = ("the", "a", "another", "her", "his")
subjects    = ("cat", "dog", "horse", "man", "woman", "boy", "girl")
verbs       = ("sang", "ran", "jumped", "said", "fought", "swam",
                "saw", "heard", "felt", "slept", "hopped", "hoped", "cried", "laughed", "walked")
adverbs     = ("loudly", "quietly", "quickly", "slowly", "well",
                "badly", "rudely", "politely")

def random_word(seq):
    return random.choice(seq)

for _ in [1, 2, 3, 4, 5]:
    sentence = [random_word(articles), random_word(subjects), random_word(verbs)]
    if random.randint(0, 1):
        pass
    else:
        sentence.append(random_word(adverbs))
    print(*sentence)
