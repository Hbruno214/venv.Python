#a = 'Aaaaaaa'
#b = 'bbbbbb'
#c = 1.1
#string = 'a ={}b={}c={:.2f}'
#formato = string.format(a, b, c,)
#print(formato)

a  =  'AAAA'
b  =  'BBBBBB'
c  =  1,1
string = 'b={nome2} a={nome1} a={0} c={nome3:.2f}'
formato = string.formato(
    nome1=a,nome2=b,nome3=c
)

print(formato)