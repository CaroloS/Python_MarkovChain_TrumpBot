# Imports markov_python module and makes an instance of the MarkovChain class
# Adds speech text file

from markov_python.cc_markov import MarkovChain    
    
mc = MarkovChain()
MarkovChain.add_file(mc, 'Trump_speech.txt')
 
# Generates text and alters output into 'sonnet' form
# Uses a while loop to generate 12 words for 14 lines
# Capitalises first letters. Indents last 2 lines, to make a 'couplet'
   
print 'A little Trump sonnet...  ', '\n'
     
count = 0
sonnet = []
while count <15:
    x = MarkovChain.generate_text(mc, max_length=12)
    s = ''.join([i[0].upper() + i[1:] for i in (x[0].split())])
    y = s + ' ' + ' '.join(x[1:])
    if count == 13: 
        y = '   ' + y
        sonnet.append(y)
    elif count == 14:
        y = '   ' + y + '...'
        sonnet.append(y)
    else:
        sonnet.append(y)
    count +=1
    
sonnet = '\n'.join(sonnet)
print sonnet

# Imports tweepy, assigns the specific authorisation keys to access the API
# Iterates through one 'sonnet' and tweets each line every 15 minutes

import tweepy, time
 
enter the corresponding information from your Twitter application:
CONSUMER_KEY = '*************************'
CONSUMER_SECRET = '**************************' 
ACCESS_KEY = '**********************************'
ACCESS_SECRET = '*********************************'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
tweet = sonnet.splitlines()
print tweet[0]
    
for line in tweet:    
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
    
    
    

    
