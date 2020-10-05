#Exercice 40.0.

#La conjecture de Syracuse (ou de Collatz) postule ceci :
#Prenons un nombre  n  : si  n  est pair, on le divise par 2, sinon on le multiplie par 3 puis on ajoute 1. On recommence \n
#cette opération tant que possible. Au bout d'un certain temps, on finira toujours par tomber sur le nombre 1.
#Proposer un programme récursif syracuse(n) écrivant tous les termes de la suite de Syracuse, s'arrêtant (on l'espère) à la valeur 1.

def syracuse(n):
  print(n)
  if n==1:
    return n
  if n%2==0:
    return syracuse(n//2)
  else:
    return syracuse(n*3+1)

print(syracuse(14))