DictOfLetters = {'A': 9, 'l': 1, 'm': 1, ' ': 5, 'K': 1, 'O': 1, 'T': 1, 'B': 3, 'R': 4, 'b': 1, 'a': 1, 'r': 1}
ListOfLetters = []
for letter in list(DictOfLetters.keys()):
    ListOfLetters.append(letter+str(DictOfLetters[letter]))