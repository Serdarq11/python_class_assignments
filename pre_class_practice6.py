def countCharInString(char, str):
    counter = 0
    for letter in str:
        if char == letter:
            counter+=1

    return counter

print(countCharInString('o', 'dormitory'))
print(countCharInString('a', 'middle east technical university'))
print(countCharInString('m', 'dilemma'))
print(countCharInString('u', 'congratulations!'))
print(countCharInString('i', 'individual'))