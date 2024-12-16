from collections import deque
# Definicja węzła, który będzie głównym obiektem na którym będę wykonywał wszyskie operacje.
# Postanowiłem, że węzły będą występować w dwóch typach:
# Typ 1:
# Węzeł nieprawidłowy, czyli taki "udawany" węzeł, który nie posiada jeszcze left i right.
# Typ 2:
# Węzeł prawidłowy, czyli taki który posiada left i right.

class Węzęł:
    def __init__(self,label,frequency):
        self.label = label
        self.left = None
        self.right = None
        self.frequency = frequency
        self.parent = None
    def setParent(node):
        parent = node
    def setLeft(node):
        left = node
    def setRight(node):
        right = node
    def increaseFrequency():
        frequency += 1
    def __lt__():
        pass
def getNameFromUser():
# Pytam o nazwę pliku użytkownika ??? muszę zapytać się o to
    fileName=input("Wpisz nazwę pliku wraz z jego rozszerzeniem.\n")
    try:
        file = open(fileName, "r") 
    except Exception as e:
        print(e)
    return file
def convertFiletoString(file):
    FileContent = file.read()
    return FileContent
def calculateFrequencies(file_content,DictOfLetters : dict):
    for letter in file_content:
        if letter not in DictOfLetters:
            DictOfLetters.update({letter:1})
        else:
            DictOfLetters[letter] += 1
def convertDictToList(DictOfLetters):
    ListOfLetters = []
    for letter in list(DictOfLetters.keys()):
        ListOfLetters.append(letter+str(DictOfLetters[letter]))
    return ListOfLetters

def heapify(ListOfLetters,length,index):
    smallest = index
    left = 2 * index + 1  
    right = 2 * index + 2  

    
    if left < length and int(ListOfLetters[left][1]) < int(ListOfLetters[smallest][1]):
        smallest = left

    
    if right < length and int(ListOfLetters[right][1]) < int(ListOfLetters[smallest][1]):
        smallest = right

    
    if smallest != index:
        ListOfLetters[index], ListOfLetters[smallest] = ListOfLetters[smallest], ListOfLetters[index]  

        heapify(ListOfLetters, length, smallest)

def build_min_heap(ListOfLetters):
    length = len(ListOfLetters)
    
    for i in range(length-1,-1,-1):
        heapify(ListOfLetters,length,i)
def Huffman(ListOfLetters):
    Q = deque(ListOfLetters)
    pass


def main():

    DictOfLetters = {}
    content = convertFiletoString(getNameFromUser())
    calculateFrequencies(content,DictOfLetters)
    ListOfLetters = convertDictToList(DictOfLetters)
    build_min_heap(ListOfLetters)
    print(DictOfLetters)
    print(ListOfLetters)
    


if __name__ == "__main__":
    main()
