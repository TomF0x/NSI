class TriangleRect:
    def __init__(self, cote1, cote2):
        self.cote1 = cote1
        self.cote2 = cote2
        self.hypothenuse = (cote1 ** 2 + cote2 ** 2) ** 0.5


triangleabc = TriangleRect(17, 5)

print(triangleabc.hypothenuse)
