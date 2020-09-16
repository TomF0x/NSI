class Eleve:
    def __init__(self, nom, classe, note):
        self.nom = nom
        self.classe = classe
        self.note = note
        self.test=0

def mnote(elevea, eleveb):
    return elevea.nom if elevea.note > eleveb.note else eleveb.nom


theo = Eleve("Théo", "TG9", 19)
esteban = Eleve("Esteban", "TG1", 15)
thomas = Eleve("Thomas", "TG9", 4)

print(mnote(esteban, theo))
