import lcshift
import comply
import add1
import char2bin

def crypt(a,b,ky1,ro):
    ky = [0]*len(ky1)
    for x in range(len(ky)):
         ky[x]=comply.comp(ky1[x])
    #print('ky',ky1[x],'x',x)
    for i in range(ro):
        #h = comply.comp(b)
        b = add1.add(b,ky[(2*ro)+1-2*i])                                           #bin(int(b,2) + int(ky1[2*(ro+1)-1],2))[2:].zfill(32)
        tempp = int(a,2) % 32
        tempp = int(tempp)
        b = lcshift.rshift(b,tempp)
        b = bin(int(b,2) ^ int(a,2))[2:].zfill(32)
        #l = comply.comp(a)
        a = add1.add(a,ky[2*(ro)-2*i])
        tempp1 = int(b,2) % 32
        tempp1 = int(tempp1)
        a = lcshift.rshift(a,tempp1)
        a = bin(int(a,2) ^ int(b,2))[2:].zfill(32)
    a = add1.add(a,ky[0])
    b= add1.add(b,ky[1])
    plain = char2bin.ascistr(a,b)
    return plain