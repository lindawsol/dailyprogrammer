import re

def word_war (input):
    #make everything lowercase.
    input = input.lower()
    #parse input into 2 words.
    wordList = re.sub("[^\w]", " ",  input).split()

    #check to see if we only have 2 words.
    if len(wordList) != 2:
        return 'Only 2 word are allowed in this battle!'

    left = wordList[0]
    right = wordList[1]

    #turn it into a list bc list we we can actually change it.
    left_list = list(left)
    right_list = list(right)

    #go through every letter in the left word.
    #if the letter is in the right word, remove from both lists.
    for letter in left:
        if letter in right_list:
            left_list.remove(letter)
            right_list.remove(letter)

    #convert these lists into string.         
    left_list_string = ''.join(right_list)
    right_list_string = ''.join(left_list)

    valley = left_list_string + right_list_string

    if len(left_list) > len(right_list):
        return 'Between: ' + input+ '\n' + 'Winner: Left. \nLetters that fell in the valley: ' + valley + '\n'
    elif len(right_list) > len(left_list):
        return 'Between: ' + input+ '\n' + 'Winner: Right. \nLetters that fell in the valley: ' + valley + '\n'
    else:
        return 'Between: ' + input+ '\n' + 'Tie. \nLetters that fell in the valley: ' + valley + '\n'



print word_war('because cause')
print word_war('hit miss')
print word_war('hiss miss')
print word_war('combo jumbo')
print word_war('hELLO below')
print word_war('rekt pwn')
print word_war('critical optical')
print word_war('isoenzyme apoenzyme')
print word_war('tribesman brainstem')
print word_war('blames nimble')
print word_war('yakuza wizard')
print word_war('longbow blowup')
