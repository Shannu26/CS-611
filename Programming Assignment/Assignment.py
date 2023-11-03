def mapCharacters(pattern):
	charToIntMap = {}
	numberOfUniqueCharacters = 0

	for char in pattern:
		if char not in charToIntMap:
			charToIntMap[char] = numberOfUniqueCharacters
			numberOfUniqueCharacters += 1

	print(charToIntMap)
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

	print(dfa)
	return dfa

def search(text, dfa, charToIntMap):
	j = 0
	N = len(text)
	M = len(dfa[0])

	for i in range(N):
		j = dfa[charToIntMap[text[i]]][j]
		if j == M: return i - M
	return -1


if __name__ == '__main__':
	pattern = input("Enter the pattern: ")
	text = input("Enter the text: ")

	charToIntMap = mapCharacters(pattern)
	dfa = buildDFA(pattern, charToIntMap)

	patternIndex = search(text, dfa, charToIntMap)
	print(patternIndex)
