w = '10110111111000010101000101100011'
q = '10011110001101110111100110111001'
a = bin(int(w,2))[2:].zfill(32)
b = bin(int(q,2))[2:].zfill(32)
print a,b
l = bin(int(w,2) + int(q,2))[2:].zfill(32)
print l