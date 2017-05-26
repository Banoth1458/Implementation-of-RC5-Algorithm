import lcshift
import add1
import char2bin
import comply

def crypt(left, right, ky, rou):
    #left =comply.comp(left) #bin(int(left, 2) + int(ky[0], 2))[2:].zfill(32)
    #ky[0] = comply.comp(ky[0])
    left = add1.add(left,ky[0])
    #ky[1] = comply.comp(ky[1])
    #right =comply.comp(right) #bin(int(right, 2) + int(ky[1], 2))[2:].zfill(32)
    right = add1.add(right,ky[1])
    for i in range(rou):
        left = bin(int(left, 2) ^ int(right, 2))[2:].zfill(32)
        tem = int(right, 2) % 32
        tem = int(tem)
        # print('tem',tem)
        left = lcshift.shift(left, tem)
        # print('left',left)
        #left = comply.comp(left)
        #ky[2 * (i + 1)] = comply.comp(ky[2 * (i + 1)])
        left = add1.add(left, ky[2 * (i + 1)])  # bin(int(left, 2) + int(ky[2*(i+1)], 2))[2:].zfill(32)
        # print left
        right = bin(int(right, 2) ^ int(left, 2))[2:].zfill(32)
        tem1 = int(left, 2) % 32
        tem1 = int(tem1)
        # print('temp1',tem1)
        right = lcshift.shift(right, tem1)
        # print('right',right)
        #right = comply.comp(right)
        #ky[2 * (i + 1) + 1] = comply.comp(ky[2 * (i + 1) + 1])
        right = add1.add(right, ky[2 * (i + 1) + 1])  # bin(int(right, 2) + int(ky[2*(i+1)+1], 2))[2:].zfill(32)
        # print('err',right)
    # print len(left), len(right)
    cipher = char2bin.ascistr(left, right)
    #print('cii',cipher)
    return left, right, cipher
