from urllib2 import Request, urlopen, URLError
import string
from BeautifulSoup import *

# Opens url from WSJ, parses it, finds all 'p' tags

input = raw_input('Enter URL or press enter - ') 
if (len(input) < 1): input = 'http://blogs.wsj.com/washwire/2015/06/16/donald-trump-\
transcript-our-country-needs-a-truly-great-leader/'
url = Request(input)

try:
    url = urlopen(url).read()
except URLError, e:
    if hasattr(e, 'reason'):
        print 'We failed to reach a server.'
        print 'Reason: ', e.reason
    elif hasattr(e, 'code'):
        print 'The server couldn\'t fulfill the request.'
        print 'Error code: ', e.code
else:
    print 'URL is good!'
    print input

    soup = BeautifulSoup(url)
    tags = soup.findAll('p')

# Appends text content to list from p tags containing the speech

    lst = []
    for i in range(len(tags)):
        paragraph = tags[i]
        if i < 5 or i > (len(tags) - 18):
            continue
        lst.append(paragraph.text)
    
# Cleans speech (removes all audience comments, and replaces html entities)
# Makes speech a single string and writes it to text file

    slst = [str(i) for i in lst]
    slst = [i for i in slst if not "AUDIENCE" in i]

    mapping = { '&#8217;': "'", '&#8212;': '', '&#8220;': '', '&#8221;': '', \
    '&#8230;': '', 'TRUMP:': '', '(LAUGHTER)': '', '(APPLAUSE)': '', '(ph)': '', }
    for k, v in mapping.iteritems():
        slst = [string.replace(i, k, v) for i in slst]
        

    speech = ' '.join(slst)
    speech = speech.strip()
    #print speech
    

#  Currently unable to acces WSJ article as requires subscription,
#  Use .txt file of the speech for rest of program

    with open('Trump_speech.txt', 'r') as text_file:
       print text_file.read()  
