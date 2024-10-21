firstString = 'Yunus'
secondString = 'Emre'
concatenatedString = firstString + secondString
print('The result of concatenation is:',concatenatedString)   # The result of concatenation is: YunusEmre (there is no whitespace)



firstName = 'Joe'
lastName = 'Schmoe'
fullName = (firstName + ' ' + lastName)
print('Hello', fullName, 'I hope you are doing well.')

def calculateAverage(p1, p2, p3, p4):
    total = p1 + p2 + p3 + p4
    average = total / 4

    return average

print('Average value is =', calculateAverage(1, 2, 3, 4))

def createHeader(fullName, gender):
    if gender == 'm':
        title = 'Mr.'
    else:
        title = 'Ms.'
    header = 'Dear ' + title + ' ' + fullName + ','
    return header
#A few test calls to the function
print(createHeader('Joe Smith', 'm'))
print(createHeader('Susan Jones', 'f'))
print(createHeader('Henry Jones', 'm'))