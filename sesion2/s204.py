import pandas

from matplotlib import pyplot
import seaborn

edades = pandas.Series([
    21, 25, 19,
    27, 31, 20,
    31, 34, 24,
    22, 17, 50, 45,
])

# El histograma parte el espacio
# en intervalos iguales
# para explicar la frecuencia
# de las observaciones que hay
# en cada intervalo, aproximando
# la masa o distribución de los datos
# A mayor frecuencia, mayor acumulación
# de observaciones en ese intervalo
seaborn.histplot(x=edades, bins=6)
pyplot.show()

