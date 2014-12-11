import re
from collections import Counter

def makeWordList(textFile):
    '''
    Convert all the words to lower case and get rid of punctuations
    and special characters
    '''
    wordList=[]
    file = open(textFile, 'r')
    text = file.read().lower()
    file.close()
    text = re.sub('[^a-z\ \']+', " ", text)
    words = list(text.split())
    return words
print Counter(makeWordList('pg47498.txt'))
