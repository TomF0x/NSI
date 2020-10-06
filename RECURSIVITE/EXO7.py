#Exo 7 recherche dico

lst = [2, 5, 7, 8, 8, 12, 13]


def recherche(lst, m):
    mid = len(lst) // 2
    if lst[mid] == m:
        return True
    if len(lst) == 1:
        return False
    if lst[mid] > m:
        return recherche(lst[:mid], m)
    if lst[mid] < m:
        return recherche(lst[mid:], m)


print(recherche(lst, 5))
