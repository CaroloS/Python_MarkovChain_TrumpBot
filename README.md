# Donald Trump Markov Chain Sonnet Generator and TwitterBot
A Program in Python, consisting of 3 files. This program takes the transcript from a Donald Trump speech, makes a word count dictionary to analyse word frequency, and inputs the speech into a Markov-Chain generator. This produces pseudo-random text from the speech, which is made into sonnets and tweeted line by line.

# get_speech.py
Requests the Wall Street Journal URL containing the speech, parses the HTML and writes the speech to a text file, Trump_speech.txt. (NB - the speech is no longer available from the website - due to a paywall. trump_dict and markov_gen work using the Trump_speech.txt file saved in this project. Code for this file left, as an example of using python to parse a website.)


# trump_dict.py
Reads the text file, Trump_speech.txt, makes a word count dictionary and prints out the top 50 most common words over 4 letters long, and looks up specific word counts.

# markov_gen.py
Uses MarkovChain class from cc_markov file (cloned from https://github.com/Codecademy/markov_python ) - generates pseudo-random text from Trump Speech. Converts the output into sonnet form. Tweets a Trump sonnet line by line using twitter API.  
