import json

def decode(codes, bit_stream):
    
    reverse_codes = {code: char for char, code in codes.items()}
    
    decoded_string = []
    current_code = ""

    for bit in bit_stream:
        current_code += bit
        if current_code in reverse_codes:
            decoded_string.append(reverse_codes[current_code])
            current_code = ""

    return ''.join(decoded_string)

def read_binary_strings_from_file(filename):
    with open(filename, 'rb') as f:
        
        codes_str = f.readline().decode('utf-8').strip()
        
        codes = json.loads(codes_str)

        
        bit_stream = []
        while True:
            byte = f.read(1)
            if not byte:
                break
            
            bits = bin(int.from_bytes(byte, 'big'))[2:].zfill(8)  
            bit_stream.extend(bits)  
            
    
    return codes, ''.join(bit_stream)


    
codes, bit_stream = read_binary_strings_from_file(input("Podaj nazwę pliku, z jego rozszerzeniem: "))
decoded_data = decode(codes, bit_stream)


with open("odszyfrowane.txt", "w", encoding="utf-8") as f:
    f.write(decoded_data)

    

