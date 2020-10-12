class Pile:
    def __init__(self):
        self.list=[]

    def est_vide(self):
        return self.list==[]

    def empile(self,nb):
        self.list.append(nb)
        return self.list

    def depile(self):
        print(self.list[-1])
        self.list.pop(-1)
p=Pile()
print(p.est_vide())
print(p.empile(10))
print(p.empile(15))
print(p.est_vide())
print(p.depile())
print(p.est_vide())