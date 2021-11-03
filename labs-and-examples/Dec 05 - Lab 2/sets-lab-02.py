firstSentence = input("Enter your first sentence")
secondSentence = input("Enter your second sentence")

firstSet = set(firstSentence)
secondSet = set(secondSentence)

bothLetters = firstSet.intersection(secondSet)
print("There are letters used in both sentences: ", bothLetters)

oneOrMoreSentences = firstSet.union(secondSet)
print("These are letters used in one sentence or both sentences:", oneOrMoreSentences)

notInSentence2 = firstSet.difference(secondSet)
print("These are letters in sentence1 not in sentence2", notInSentence2)

notInSentence1 = secondSet.difference(firstSet)
print("These are letters in sentence2 not in sentence1", notInSentence1)

existsInOneSentenceNotBoth = firstSet.symmetric_difference(secondSet)
print("These are letters in only one sentence not both", existsInOneSentenceNotBoth)
