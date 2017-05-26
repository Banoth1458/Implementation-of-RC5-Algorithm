#a = (['b','a','n','o','t','h'])
#b = (['h','t','o','n','a','b'])
a=raw_input("enter plaintext:")
b=raw_input("enter 2:")
c = [None]*len(a)
d = [None]*len(a)
e = [None]*len(a)
for i in range(len(a)):
   c[i]=bin(ord(a[i]))[2:].zfill(8)
   d[i]=bin(ord(b[i]))[2:].zfill(8)
print c,d
for j in range(len(a)):
    c[j]=int(c[j],2)
    d[j]=int(d[j],2)
    e[j]=c[j]^d[j]
print e
for k in range(len(a)):
    e[k]=bin(e[k])[2:].zfill(8)
print e
q=int(e[1],2) << 2
w=bin(q)[2:].zfill(8)
print w
