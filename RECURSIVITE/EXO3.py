def pgcd(a,b):
    return a if b==0 else pgcd(b,a%b)

print(pgcd(18,12))