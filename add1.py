def add(w,y):
    w=list(w)
    y=list(y)
    k=[0]*32
    c=[0]*32
    #print w[31]
    if w[31]=='1' and y[31]=='1':
        c[31]='0'
        k[30]='1'
    elif w[31]=='0'and y[31]=='0':
        c[31]='0'
        k[30]='0'
    else:
        c[31]='1'
        k[30]='0'
    for i in range(31):
        if w[30-i]=='1' and y[30-i]=='1' and k[30-i]=='1':
            c[30-i]='1'
            k[29-i]='1'
        elif w[30-i]=='0' and y[30-i]=='0' and k[30-i]=='1':
            c[30-i]='1'
            k[29-i]='0'
        elif w[30 - i] == '0' and y[30 - i] == '0' and k[30 - i] == '0':
            c[30 - i] = '0'
            k[29 - i] = '0'
        elif w[30-i]=='1' and y[30-i]=='1' and k[30-i]=='0':
            c[30-i]='0'
            k[29-i]='1'
        elif w[30-i]=='1' and y[30-i]=='0' and k[30-i]=='0' or w[30-i]=='0' and y[30-i]=='1' and k[30-i]=='0':
            c[30-i]='1'
            k[29-i]='0'
        elif w[30-i]=='1' and y[30-i]=='0' and k[30-i]=='1' or w[30-i]=='0' and y[30-i]=='1' and k[30-i]=='1':
            c[30-i]='0'
            k[29-i]='1'
    c=''.join(c)
    return c
