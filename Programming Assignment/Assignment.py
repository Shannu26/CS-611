def mapCharacters(pattern, text):
	charToIntMap = {}
	numberOfUniqueCharacters = 0

	for char in pattern:
		if char not in charToIntMap:
			charToIntMap[char] = numberOfUniqueCharacters
			numberOfUniqueCharacters += 1

	for char in text:
		if char not in charToIntMap:
			charToIntMap[char] = numberOfUniqueCharacters
			numberOfUniqueCharacters += 1

	return charToIntMap

def buildDFA(pattern, charToIntMap):
	rows = len(charToIntMap)
	columns = len(pattern)
	dfa = [[0] * columns for _ in range(rows)]
	dfa[0][0] = 1
	X = 0

	for j in range(1, columns):
		for c in range(rows):
			dfa[c][j] = dfa[c][X]
		dfa[charToIntMap[pattern[j]]][j] = j + 1
		X = dfa[charToIntMap[pattern[j]]][X]

	return dfa

def search(text, dfa, charToIntMap):
	j = 0
	N = len(text)
	M = len(dfa[0])

	for i in range(N):
		if text[i] not in charToIntMap: return -1
		j = dfa[charToIntMap[text[i]]][j]
		if j == M: return i - M + 1
	return -1


if __name__ == '__main__':
	testcases = [
				{ "pattern": "abcaby", "text": "abxabcabcaby"},
				{ "pattern": "ABABCABAB", "text": "ABABDABACDABABCABAB"},
				{ "pattern": "i am sas", "text": "Hello i am sasank"},
				{ "pattern": "i am sas", "text": "Hello i am bhavana"},
				{ "pattern": "rry pott", "text": "I am harry potter"},
				{ "pattern": "zyx", "text": "z"},
				{ "pattern": "zyx", "text": "xyz"},
				{ "pattern": "abbbbccccAA", "text": "AAnndjasbfjbasdbhabbbbccccAA"},
				{ "pattern": "of the rin", "text": "Lord of the rings"},
				{ "pattern": "game of", "text": "Game of Thrones"}
				]

	print("-----------------------------------------------------------------------------------------")

	for index, testcase in enumerate(testcases):
		pattern = testcase["pattern"]
		text = testcase["text"]
		charToIntMap = mapCharacters(pattern, text)
		dfa = buildDFA(pattern, charToIntMap)

		patternIndex = search(text, dfa, charToIntMap)
		resultText = ""
		if patternIndex == -1: resultText = "The given pattern is not found in the given text."
		else: resultText = "The given pattern is found in the given text at index " + str(patternIndex)

		print("Test Case - " + str(index + 1))
		print("\t\tPattern: " + pattern)
		print("\t\tText: " + text)
		print("\t\tResult: " + resultText)
		print("-----------------------------------------------------------------------------------------")

