import key_expand
import math
import RC5
def clas(Plain_text,Key,rounds):
    #Key = raw_input("enter secretkey:")
    size = len(Key)
    #rounds = raw_input("enter rounds:")
    rounds = int(rounds)
    Key = key_expand.keyexpansion(Key, size, rounds)
    #Plain_text = raw_input("enter text:")
    plength = len(Plain_text)
    if plength % 8 != 0:
        val = plength % 8
        pad = 8 - val
        pad1 = ''.ljust(pad, '0')
        Plain_text = Plain_text + pad1
    alength = int(math.ceil((len(Plain_text)) / float(8)))
    #print alength
    if plength % 8 == 0:
        arr = list(map("".join, zip(*[iter(Plain_text)] * 8)))
    else:
        arr = [0] * alength
        arr = list(map("".join, zip(*[iter(Plain_text)] * 8)))
    te = [0]*len(arr)
    l = [0]*len(arr)
    ri = [0]*len(arr)
    for x in range(len(arr)):
        [te[x],l[x],ri[x]] = RC5.ENC(arr[x], Key, rounds)
    te = ''.join(te)
    return te,l,ri
    #text = [0]*len(arr)
    #for y in range(len(arr)):
    #    text[y] = RC5.DEC(l[y], ri[y], Key, rounds)
    #tex = ''.join(text)
    #tex = tex[:plength]
    #print te
    #print tex