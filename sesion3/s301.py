import numpy
import pandas

from matplotlib import pyplot
import seaborn

# Tabla -> pandas.DataFrame
# tabla <- pandas.read_csv(...) | pandas.read_excel(...)

habits = pandas.read_csv("conjuntos/student_habits_performance.csv")

print(habits)

print(habits.info())

# SINTAXIS: Recuperar la serie o columna de una tabla
# <tabla>[<columna>]
edades = habits["age"] # Series([23, 20, 21, ..., 20, 24, 19])

print(edades)

# kdeplot(x=edades, fill=True)
# histplot(x=edades, bins=5)
# boxplot(x=edades, fill=False)
# seaborn.kdeplot(x=edades, fill=True)
# seaborn.histplot(x=edades, bins=5)
seaborn.boxplot(x=edades, fill=False)
pyplot.show()