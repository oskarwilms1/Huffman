with open("wzór.txt","r") as wzor:
    Wzór = eval(wzor.read())

binary_strings = []
with open('zaszyfrowane.txt', 'rb') as f:
    while True:
        # Odczytujemy bajt długości
        length_byte = f.read(1)
        if not length_byte:
            break  # Koniec pliku

        length = int.from_bytes(length_byte, byteorder='big')
        value_bytes = f.read((length + 7) // 8)  # Odczytujemy odpowiednią ilość bajtów

        # Konwertujemy bajty z powrotem na wartość całkowitą
        integer_value = int.from_bytes(value_bytes, byteorder='big')
        # Przechodzimy na ciąg binarny
        binary_string = bin(integer_value)[2:]  # Konwertujemy na binarny, pomijając '0b'
        binary_string = binary_string.zfill(length)  # Dodajemy zera wiodące

        binary_strings.append(binary_string)

OdszyfrowanyTekst = ""
for string in binary_strings:
   OdszyfrowanyTekst = OdszyfrowanyTekst + Wzór[string]
with open("odszyfrowane.txt","w",encoding="utf-8") as odszyfrowane:
    odszyfrowane.write(OdszyfrowanyTekst)


    
