class Chrono:
    def __init__(self, heures, minutes, secondes):
        self.heures = heures
        self.minutes = minutes
        self.secondes = secondes

    def affiche(self):
        return print("Il est {0}h {1}min et {2}s".format(self.heures, self.minutes, self.secondes))

    def avance(self, s):
        self.secondes += s
        self.minutes += self.secondes // 60
        self.secondes = self.secondes % 60
        self.heures += self.minutes // 60
        self.minutes = self.minutes % 60

temps = Chrono(1, 34, 45)
temps.affiche()
temps.avance(10)
temps.affiche()
temps.avance(120)
temps.affiche()
temps.avance(1600)
temps.affiche()
