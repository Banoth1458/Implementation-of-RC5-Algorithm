def shift(var, k):
    var = list(var)
    for x in range(k):
        t = '00000000000000000000000000000000'
        t = list(t)
        temp = var[0]
        for y in range(len(var)):
            t[30 - y] = var[31 - y]
        t[31] = temp
        var = t
    var = ''.join(var)
    # print var
    return var
def rshift(var1, k1):
    var1 = list(var1)
    for x in range(k1):
        t1 = '00000000000000000000000000000000'
        t1 = list(t1)
        temp = var1[31]
        for y in range(len(var1)-1):
            t1[y+1] = var1[y]
        t1[0] = temp
        var1 = t1
    var1 = ''.join(var1)
    return var1
