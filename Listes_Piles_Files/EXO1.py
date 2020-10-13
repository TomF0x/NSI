class Pile:
    def __init__(self):
        self.list = []

    def est_vide(self):
        return self.list == []

    def empile(self, nb):
        self.list.append(nb)
        return self.list

    def depile(self):
        if self.est_vide() == True:
            raise IndexError("Vous avez essayé de dépiler une pile vide")
        self.list.pop()

    def __str__(self):
        return "".join(["|" + str(a) for a in self.list])


p = Pile()
print(p.est_vide())
print(p.empile(10))
print(p.empile(15))
print(p.empile(5))
print(p)
print(p.est_vide())
print(p.depile())
