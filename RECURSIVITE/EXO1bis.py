#Exercice 1
#Écrire une fonction récursive puissance(x,n) qui calcule le nombre  x**n .

def puissance(x,n):
    return 1 if n==0 else x*puissance(x,n-1)

print(puissance(3,3))