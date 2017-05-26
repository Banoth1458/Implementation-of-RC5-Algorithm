import add1
def comp(ke):
    lit = '00000000000000000000000000000001'
    ke=list(ke)
    for x in range(len(ke)):
        if ke[x] == '0':
            ke[x]='1'
        elif ke[x] == '1':
            ke[x] = '0'
    ke = ''.join(ke)
    ke = add1.add(ke,lit)
    #ke = bin(int(ke,2) + int(lit,2))[2:].zfill(32)
    return ke