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

seaborn.boxplot(y=edades, hue=fitness, showfliers=False)
pyplot.show()