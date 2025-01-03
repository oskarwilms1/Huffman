#Podstawowa definicja węzła, dziele go na dwa typy (umownie):
#Typ 1: Węzęł nieprawidłowy (nie posiada prawego i lewego)
#Typ 2: Węzęł prawidłowy (posiada prawy i lewy)
import json

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
def write_binary_strings_to_file(strings, codes, filename):
    
    codes_str = json.dumps(codes)
    
    with open(filename, 'wb') as f:
       
        f.write(codes_str.encode('utf-8')+b'\n')
        
        bit_buffer = 0
        bits_in_buffer = 0
        
        for binary_string in strings:
            for bit in binary_string:
                bit_buffer = (bit_buffer << 1) | int(bit)  # Przesuń w lewo i dodaj bit
                bits_in_buffer += 1
                
                if bits_in_buffer == 8:  # jeżeli buffor jest pełny
                    f.write(bytes([bit_buffer]))
                    bit_buffer = 0
                    bits_in_buffer = 0
            
        # Jeżeli pozostały jakieś bity w buforze to je wpisz do pliku
        if bits_in_buffer > 0:
            bit_buffer <<= (8 - bits_in_buffer)  # Przesuń w lewo pozostałe bity
            f.write(bytes([bit_buffer]))
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

ZakodowanyTekst = []
for litera in Zawartosc:
    ZakodowanyTekst.append(Kodyv2[litera])


write_binary_strings_to_file(ZakodowanyTekst, Kodyv2, "zaszyfrowane.txt")
