import urllib
import string
import re
from BeautifulSoup import *

# Opens url from WSJ, parses it, finds all 'p' tags
url = raw_input('Enter - ')
if (len(url) < 1): url = 'http://blogs.wsj.com/washwire/2015/06/16/donald-trump-transcript-our-country-needs-a-truly-great-leader/'
print url
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = soup.findAll('p')

# Appends text content to list from p tags containing the speech
lst = []
for i in range(len(tags)):
    paragraph = tags[i]
    if i < 5 or i > (len(tags) - 18):
        continue
    lst.append(paragraph.text)
    

# Cleans the speech (removes all audience comments, and replaces bad html characters)
# Makes speech as single string from list items
# Writes the speech to a plain text file

slst = [str(i) for i in lst]
slst = [i for i in slst if not "AUDIENCE" in i]

mapping = { '&#8217;': "'", '&#8212;': '', '&#8220;': '', '&#8221;': '', '&#8230;': '', \
'TRUMP:': '', '(LAUGHTER)': '', '(APPLAUSE)': '', '(ph)': '', }
for k, v in mapping.iteritems():
    slst = [string.replace(i, k, v) for i in slst]
        

speech = ' '.join(slst)
speech = speech.strip()
print speech

with open('Trump_speech.txt', 'w') as text_file:
    text_file.write(speech)

    
    
# Opens the .txt file, reads it and removes punctuation
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
    
    print 'How many times says great!...', sdict['great']
    print 'How many times says his own name...', sdict['trump']
    print 'How many times says china...', sdict['china']
    print 'How many times says mexico...', sdict['mexico']
    print 'How many times says america...', sdict['america']
