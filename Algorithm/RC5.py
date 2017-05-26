import key_expand
import char2bin
import Encrypt
import Decrypt


# Plain = raw_input("enter plaintext:")
# Key = raw_input("enter key:")
# size = len(Key)
# r = raw_input("enter no.of rounds:")
# r = int(r)
def ENC(Plain, Key, r):
    a = (Plain[:len(Plain) / 2])
    b = (Plain[len(Plain) / 2:])
    a = list(a)
    b = list(b)
    # Key = key_expand.keyexpansion(Key, size, r)
    for x in range(len(a)):
        a[x] = char2bin.strASCII(a[x])
    for x in range(len(b)):
        b[x] = char2bin.strASCII(b[x])
    a = ''.join(a)
    b = ''.join(b)
    #get = char2bin.ascistr(a, b)
    [enc, enc1, c] = Encrypt.crypt(a, b, Key, r)
    return c, enc, enc1


def DEC(enc, enc1, Key, r):
    dec = Decrypt.crypt(enc, enc1, Key, r)
    return dec
