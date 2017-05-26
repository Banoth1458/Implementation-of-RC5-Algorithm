def strASCII(s):
    c = []
    for x in s:
        c.append(format(ord(x), 'b').zfill(8))
    c = "".join(c)
    return c
def ascistr(l,r):
    joi = [l,r]
    joi = ''.join(joi)
    joi = list(map("".join, zip(*[iter(joi)] * 8)))
    #print joi
    for x in range(len(joi)):
        joi[x] = chr(int(joi[x],2))
    joi = ''.join(joi)
    return joi


