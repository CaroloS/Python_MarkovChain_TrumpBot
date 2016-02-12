# Opens text file, reads it and removes punctuation
# Makes a word count dictionary
# Sorts by count in reverse, prints top 50 words over 4 letters long

import re

with open('Trump_speech.txt', 'r') as fh:
    speech = fh.read()

    speech_count = speech.lower()
    speech_count = re.sub(r'[?|,|.|\'|!]',r'', speech_count)
    speech_count = speech_count.split()
    print 'Speech total word count:  ', len(speech_count)
    
    sdict = dict()
    
    for word in speech_count:
        sdict[word] = sdict.get(word, 0) + 1
    
    most_common = sorted([(value,key) for (key,value) in sdict.items() if len(key)>4], reverse=True)
    print 'Trump_speech most frequent words dictionary:', '\n', most_common[0:50]
    
    print 'How many times says great...', sdict['great']
    print 'How many times says his own name...', sdict['trump']
    print 'How many times says china...', sdict['china']
    print 'How many times says mexico...', sdict['mexico']
    print 'How many times says america...', sdict['america']
