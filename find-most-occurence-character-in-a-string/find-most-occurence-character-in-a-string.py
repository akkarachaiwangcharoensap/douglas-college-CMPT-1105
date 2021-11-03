textInput = 'aaa bb acacacdefafsszokasfmasfaaaasfasfamasfmasfmalolwtfisthisshitbutitworkshopefully'

nextCharacterToCheck = ''
currentCharacterToCheck = ''

mostFrequentCharacter = ''

highestCount = 0
currentCount = 0

for index in range(len(textInput)):
        nextCharacterToCheck = textInput[index]

        if (nextCharacterToCheck == '' or nextCharacterToCheck == currentCharacterToCheck):
                continue

        currentCharacterToCheck = nextCharacterToCheck

        for innerIndex in range(len(textInput)):
                nextNextCharacter = textInput[innerIndex]
                
                if (currentCharacterToCheck == nextNextCharacter):
                        highestCount = highestCount + 1

        if (highestCount > currentCount):
                currentCount = highestCount
                mostFrequentCharacter = currentCharacterToCheck

        # reset
        highestCount = 0
        nextCharacterToCheck = ''
        currentCharacterToCheck = ''

print('The most frequent character is: ' + mostFrequentCharacter)
