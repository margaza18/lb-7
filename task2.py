from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import pylab



def count_letters(sentence: str):
    counts = Counter(sentence.replace(" ", ""))

sentence = ['P', 'y', 't', 'h', 'o', 'n',\
                'i', 's',\
                'a',\
                'p', 'r', 'o', 'g','r', 'a', 'm', 'm', 'n', 'g',\
                'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e',\
                'w', 'i', 't', 'h',\
                'd', 'y', 'n', 'a', 'm', 'i', 'c',\
                's', 'e', 'm', 'a', 'n', 't', 'i', 'c', 's',\
                ]


for a in range(0, len(sentence)):
    plt.bar(a, sentence[a])
plt.show()
