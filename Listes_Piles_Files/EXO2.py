class Cellule:

    def __init__(self, contenu, suivante):
        self.contenu = contenu
        self.suivante = suivante

class Pile:
    def __init__(self):
        self.data = None

    def est_vide(self):
        return self.data==None

    def empile(self, x):
        self.data=Cellule(x,self.data)

    def depile(self):
        v=self.data.contenu
        self.data=self.data.suivante
        return v

    def __str__(self):
        return str(self.data.contenu)

a=Pile()
a.empile(10)
print(a)
a.empile(54)
a.empile(98)
print(a)