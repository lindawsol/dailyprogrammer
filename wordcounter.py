import re
from collections import Counter

def makeWordList(textFile):
    '''
    Convert all the words to lower case and get rid of punctuations
    and special characters and put them all in a list.
    '''
    wordList=[]
    file = open(textFile, 'r')
    text = file.read().lower()
    file.close()
    # replaces anything that is not a lowercase letter, a space, or an
    # apostrophe with a space.
    text = re.sub('[^a-z\ \']+', " ", text)
    words = list(text.split())
    return words

#count the list.
print Counter(makeWordList('pg47498.txt'))
