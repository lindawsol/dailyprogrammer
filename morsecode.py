import wave
MorseDict = {'a' : '.-',
             'b' : '-...',
             'c' : '-.-.',
             'd' : '-..',
             'e' : '.',
             'f' : '..-.',
             'g' : '--.',
             'h' : '....',
             'i' : '..',
             'j' : '.---',
             'k' : '-.-',
             'l' : '.-..',
             'm' : '--',
             'n' : '-.',
             'o' : '---',
             'p' : '.--.',
             'q' : '--.-',
             'r' : '.-.',
             's' : '...',
             't' : '-',
             'u' : '..-',
             'v' : '...-',
             'w' : '.--',
             'x' : '-..-',
             'y' : '-.--',
             'z' : '--..',
             '1' : '.----',
             '2' : '..---',
             '3' : '...---',
             '4' : '....-',
             '5' : '.....',
             '6' : '-....',
             '7' : '--...',
             '8' : '---..',
             '9' : '----.',
             '0' : '-----',
             ' ' : '/'}

def morse_code (input):
    output = ''
    input = input.lower()
    for i in input:
        try:
            output += MorseDict[i]
        except:
            return 'Invalid input: '+ i + ' is neither a letter or a number.'

    return output



print morse_code('cat mouse')
print morse_code('at@mouse')
