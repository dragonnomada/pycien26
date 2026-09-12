import numpy
from matplotlib import pyplot

x = numpy.linspace(-numpy.pi, numpy.pi, 20)

y1 = numpy.sin(x)
y2 = numpy.cos(x)

pyplot.plot(x, y1, 
            marker=".", linestyle="--", 
            color="pink", markerfacecolor="red")
pyplot.plot(x, y2, 
            marker=".", linestyle="--", 
            color="skyblue", markerfacecolor="blue")
pyplot.savefig("g3.png", dpi=300)
pyplot.show()