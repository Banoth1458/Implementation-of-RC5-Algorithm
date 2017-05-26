import add1
import char2bin
import lcshift
import comply


def keyexpansion(key, ksize, round):
    A = '00000000000000000000000000000000'  # 32-bit string A{0's}
    B = '00000000000000000000000000000000'  # 32-bit string A{0's}
    tor = ((ksize - 1) / 4) + 1  # key size in bytes divided by 4 gives size of temp array L[]
    L = [0] * (tor)  # temp array L initialising with 0's =L[]=5 if key equal to 16 byte(128bits)
    for i in range(len(L)):  # copying input key to temp array in 4 bytes each index remaining padding
        #if i == len(L) - 1:
         #   L[i] = str(A)
          #  break
        L[i] = key[4 * i:4 * i + 4]
    #print L
    for x in range(len(L)):
        L[x] = char2bin.strASCII(L[x])  # converting bytes to bits
    #print L
    t = 2 * (round + 1)  # key expansion array size with 32-bit each
    gt = 3 * max(tor, t)  # times to mix secret key s[]
    s = [0] * t
    k = [0] * t
    P = '10110111111000010101000101100011'  # magic constant
    q = '10011110001101110111100110111001'  # magic constant
    # o = bin(int(q,2))[2:].zfill(32)
    # x = '01100001110010001000011001000111'
    # l=[0]*t
    s[0] = P  # initial 1-index of s[] with P(magic constant(32-bit)
    # print s[0],q
    # print A,B
    #q = comply.comp(q)
    for i in range(t - 1):
        # a = bin(int(s[i+1], 2))[2:].zfill(32)
        #s[i] = comply.comp(s[i]) #bin(int(s[i], 2) + int(q, 2))[2:].zfill(32)
        s[i+1] = add1.add(s[i],q)
        # s[i+1]=add1.add(s[i], q)               #initializing s[]
    # print('key expand', s)
    # print len(s)
    d = 0
    e = 0
    shiftbit = 3
    while gt != 0:  # generating key expansion of size 2*(r+1) with index of 32-bit
        #A = comply.comp(A)      #bin(int(A, 2) + int(B, 2))[2:].zfill(32)  # add1.add(A,B)
        #B = comply.comp(B)
        #s[d] = comply.comp(s[d])
        # print('var', var)
        temp1 = add1.add(A,B)
        temp2 = add1.add(s[d],temp1)
        #temp1 = bin(int(s[d], 2) + int(var, 2))[2:].zfill(32)  # add1.add(s[d], var)
        # print('temp1', temp1)
        A = s[d] = lcshift.shift(temp2, shiftbit)
        # print('A', A)
        #go = comply.comp(A)
        #L[e] = comply.comp(L[e])

        var1 = add1.add(A,B) #bin(int(A, 2) + int(B, 2))[2:].zfill(32)  # add1.add(A,B)
        var2 = add1.add(L[e],var1)
        var3 = add1.add(A,B)
        # print var1
        mod = int(var3, 2) % 32
        mod1 = int(mod)
        #temp4 = bin(int(L[e], 2) + int(var1, 2))[2:].zfill(32)  # add1.add(L[e],var1)
        B = L[e] = lcshift.shift(var2, mod1)
        d = (d + 1) % t
        e = (e + 1) % (tor)
        gt -= 1
    return s
