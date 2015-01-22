
def validate_isbn(input):
    # get the dashes out and turn the x into a 10.
    input = input.lower()
    formatted_isbn=[]
    for char in input:
        if char.isdigit():
            formatted_isbn.append(int(char))
        elif char == 'x':
            formatted_isbn.append(10)

    # make sure we only have 10 digits.
    if len(formatted_isbn) != 10:
        return False

    calculated_isbn =[]
    multiplier = 10
    for i in formatted_isbn:
        calculated_isbn.append(i*multiplier)
        multiplier -= 1

    if (sum(calculated_isbn)) %11 == 0:
        return True
    else:
        return False



print validate_isbn('0-7475-3269-X'), ', 0-7475-3269-X should be False'
print validate_isbn('0-7475-3269-9'), ', 0-7475-3269-9 should be True'
print validate_isbn('X'), 'X shoudl be False'
