liczba_bitowa = 0b11101 #29
print("Przesunięcie bitowe w lewo ", liczba_bitowa<<1) # => 0b111010
print("Przesunięcie bitowe w prawo ", liczba_bitowa>>1) # => 0b1110
print("XOR: ", liczba_bitowa ^ 0b1) # => 11101 xor 00001 => 11100

print("AND: ", 0b1 & 0b1) # 1&1 => 1; 
print("AND: ", 0b0 & 0b1) # 0&1 => 0; 
print("AND: ", 0b1 & 0b0) # 1&0 => 0; 
print("AND: ", 0b0 & 0b0) # 0&1 => 0; 