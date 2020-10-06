#Exo Tours de Hanoï auto récursif
no=0
def hanoi(n, A, B, C):
    global no
    if n == 1:
        no+=1
        print("No{0} {1} vers {2}".format(no,A,C))
    else:
        hanoi(n - 1,A,C,B)
        no+=1
        print("No{0} {1} vers {2}".format(no,A,C))
        hanoi(n-1,B,A,C)



hanoi(6, "A", "B", "C")
