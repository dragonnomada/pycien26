# Numpy - Librería de arreglos n-dimensionales
# operaciones con matrices y vectores
import numpy
# Pandas - Librería de tablas y series
# operaciones estadísticas superiores a numpy
import pandas

# Matplotlib/Pyplot - Librería para graficar
# personaliza las gráficas y 
# las guarda en archivos o las muestra
from matplotlib import pyplot
# Seaborn - Librería más avanzada para graficar
# construye mapas de calor, regresiones, etc.
import seaborn

# numpy.linspace construye un arreglo/vector en un intervalo
# entre (a, b) y genera n puntos
# numpy.linspace(a, b, n)
# El primer valor siempre `a` y último `b`
# y quedan igualmente espaciados, por ejemplo,
# numpy.linspace(1, 5, 3) produce el arreglo [1, 3, 5]
x = numpy.linspace(-numpy.pi, numpy.pi, 20)
# numpy.sin(x) - Funciones aplicadas en arreglos/vectores
# aplica la función seno a cada elemento de x, por ejemplo,
# numpy.sin([0, PI/2, PI, 3PI/2]) -> [0, 1, 0, -1]
# a esto le conoce como aplicar la función elemento-elemento
y = numpy.sin(x)

# pandas.DataFrame(...) construye una tabla con
# las columnas descritas en un frame ({ "NOMBRE": VALORES, ... })
# Imprime la tabla de x, y
print(
    pandas.DataFrame({
        "x": x,
        "y": y,
    })
)

# Grafica los puntos de x, y unidos líneas
seaborn.lineplot(x=x, y=y)
# Muestra la gráfica
pyplot.show()