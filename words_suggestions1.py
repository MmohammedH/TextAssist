import numpy as np
import pandas as pd
import textdistance 
from collections import Counter
import re

words = []
with open('autocorrect book1.txt','r',encoding='utf-8') as f:
    data = f.read()
    data = data.lower()
    word = re.findall('\w+', data)
    words +=word

print(words[0:10])

len(words)
V = set(words)
word_freq_dict = Counter(words)
word_freq_dict.most_common(10)
Total_words_freq = sum(word_freq_dict.values())


probs = {}
for k in word_freq_dict.keys():
    probs[k] = word_freq_dict[k] / Total_words_freq
probs

def autocorrect(word):
    word = word.lower()
    if word in V:
        return('Your word seems to be correct', word)
    else:
        similarities = [1-(textdistance.Jaccard(qval=2).distance(v,word))  for v in word_freq_dict.keys()]
        df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
        df = df.rename(columns={'index':'Word',0:'Prob'})
        df['Similarity'] = similarities
        output = df.sort_values(['Similarity','Prob'],ascending=False).head(3)
        return(output)
autocorrect("helo")