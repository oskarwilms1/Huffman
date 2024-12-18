#Podstawowa definicja węzła, dziele go na dwa typy (umownie):
#Typ 1: Węzęł nieprawidłowy (nie posiada prawego i lewego)
#Typ 2: Węzęł prawidłowy (posiada prawy i lewy)

class Węzęł:
    def __init__(self,labelka,czestotliwosc,lewy=None,prawy=None):
        self.labelka = labelka
        self.czestotliwosc = czestotliwosc
        self.prawy = prawy
        self.lewy = lewy
        self.code = ''
    def __lt__(self,other):
        return self.czestotliwosc < other.czestotliwosc
    def zwiększCzestotliwosc(self):
        self.czestotliwosc += 1
#Definiuje potrzebne funkcje

def min_heapify(lista,dlugosc,index):
    najmniejszy_index = index
    lewy = 2 * index + 1
    prawy = 2 * index + 2

    if lewy < dlugosc and lista[lewy] < lista[najmniejszy_index]:
        najmniejszy_index = lewy

    if prawy < dlugosc and lista[prawy] < lista[najmniejszy_index]:
        najmniejszy_index = prawy
    
    if najmniejszy_index != index:
        lista[index],lista[najmniejszy_index] = lista[najmniejszy_index],lista[index]
        min_heapify(lista,dlugosc,najmniejszy_index)
def build_heap(lista):
    dlugosc = len(lista)
    for index in range(dlugosc // 2 - 1, -1, -1):
        min_heapify(lista,dlugosc,index)
def Huffman(lista):
    Kolejka = lista
    dlugosc = len(lista)
    for i in range(1,dlugosc):
        Kolejka[0],Kolejka[-1] = Kolejka[-1],Kolejka[0]
        lewy = Kolejka.pop()
        min_heapify(Kolejka,dlugosc-i,0)
        prawy = Kolejka[0]
        czestotliwosc = lewy.czestotliwosc + prawy.czestotliwosc
        Kolejka[0] = Węzęł(lewy.labelka+prawy.labelka,czestotliwosc,lewy,prawy)
        min_heapify(Kolejka,dlugosc-i,0)
        #ListaWszystkich.append(Węzęł(lewy.labelka+prawy.labelka,czestotliwosc))
    return Kolejka[0]
def encode(wezel,WszystkieKody):
    
    if wezel.lewy != None:
        wezel.lewy.code = wezel.code + '0'
        encode(wezel.lewy,WszystkieKody)
    if wezel.prawy != None:
        wezel.prawy.code = wezel.code +'1'
        encode(wezel.prawy,WszystkieKody)
    if wezel.lewy == None and wezel.prawy == None:
        WszystkieKody.update({wezel.code:wezel.labelka})
    return WszystkieKody
def write_binary_strings_to_file(strings, filename):
    with open(filename, 'wb') as f:
        for binary_string in strings:
            # Konwertujemy łańcuch binarny na wartość całkowitą
            integer_value = int(binary_string, 2)
            # Otrzymujemy długość łańcucha binarnego
            length = len(binary_string)
            
            # Pakujemy długość oraz wartość całkowitą do bajtów
            length_byte = length.to_bytes(1, byteorder='big')
            value_bytes = integer_value.to_bytes((length + 7) // 8, byteorder='big')

            # Zapisujemy bajty długości oraz wartości do pliku
            f.write(length_byte)
            f.write(value_bytes)
#Definiuje zmienne

ListaWezlow = []
SłownikLiter = {} # Słownik zawiera informacje o częstotliwości
ListaLiter = []

#Odczytuje plik podany przez użytkownika i zapisuje go w liście

try:
    plik = open(input("Podaj nazwe pliku z jego rozszerzeniem: "),"r",encoding="utf-8")
    Zawartosc = plik.read()
except:
    print("Błędna nazwa pliku")

#Tworze węzły "nieprawidłowe" i dodaje je do listy wszyskich węzłów

for litera in Zawartosc:
    if litera not in ListaLiter:
        ListaLiter.append(litera)
        SłownikLiter.update({litera : 1})     
    else:
       SłownikLiter[litera] += 1
for litera in ListaLiter:
    ListaWezlow.append(Węzęł(litera,SłownikLiter[litera]))

#Buduję kopiec
build_heap(ListaWezlow)

ZłączenieWęzłów = Huffman(ListaWezlow)
Kody = {}
encode(ZłączenieWęzłów,Kody)
Kodyv2 = {y: x for x, y in Kody.items()}
#print(Kody)
#print(Kodyv2)

ZakodowanyTekst= []
for litera in Zawartosc:
    ZakodowanyTekst.append(Kodyv2[litera])

Wzór = str(Kody)
write_binary_strings_to_file(ZakodowanyTekst, "zaszyfrowane.txt")
f = open('Wzór.txt','w')
f.write(Wzór+"\n") # write new content at the beginning
f.close()