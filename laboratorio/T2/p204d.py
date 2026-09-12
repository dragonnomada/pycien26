import pandas
from matplotlib import pyplot
import seaborn

precios = pandas.Series([
    22.5, 22.9, 26.5, 21.45,
    21.5, 25.9, 27.5, 24.45,
    23.5, 26.9, 25.5, 26.45,
    24.5, 24.9, 24.5, 24.45,
    27.5, 27.9, 28.5, 21.45,
])

seaborn.kdeplot(x=precios, fill=True)
pyplot.show()