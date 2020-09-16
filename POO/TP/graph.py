import matplotlib.pyplot as plt

def graphique(t, nb):
    fig, ax = plt.subplots()
    ax.plot(nb, t)
    ax.set(xlabel='NB Balle', ylabel='Temps (s)',
           title='')
    ax.grid()
    plt.show()
