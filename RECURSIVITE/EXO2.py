#Exercice 2
#Écrire une fonction récursive boucle(i,k) qui affiche les entiers entre i et k. Par exemple, boucle(2,5) doit afficher 2 3 4 5

def boucle(i,k):
    return k if i==k else str(i)+' '+str(boucle(i+1,k))
print(boucle(2,5))