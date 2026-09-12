import pandas

from matplotlib import pyplot
import seaborn

edades = pandas.Series([
    21, 25, 19,
    27, 31, 20,
    31, 34, 24,
    22, 17, 50, 45,
])

fitness = pandas.Series([
    1, 0, 1,
    1, 1, 0,
    1, 0, 1,
    0, 0, 0, 1,
])

# Kernel Density Estimation
# La estimación de la densidad de las edades
# se aproxima a qué tan importante es
# cada valor dentro del eje, de forma continua
# La densidad de probabilidad 
# de que se presente un dato
seaborn.kdeplot(x=edades, fill=True, color="gray")
seaborn.kdeplot(x=edades, hue=fitness, fill=True)
pyplot.show()

