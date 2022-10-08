x = int(input("Birinci sayıyı girin :") )
y = int(input("İkinci sayıyı girin :") )
z = input("işlem seçeneğini seçin :")
u = "*"
t = "+"
q = "-"

if z == u:
    print(x*y)

elif z == t:
    print(x+y)
    
elif z == q:
    print(x-y)
print( "kullandığınız için teşekkürler")