import numpy
from matplotlib import pyplot

x = numpy.array([1, 3, 6, 7, 9])
y = numpy.array([4, 5, 20, 16, 11])

pyplot.plot(x, y, 
            marker="s", linestyle="--", 
            color="red", markerfacecolor="blue")
pyplot.savefig("g2.png", dpi=300)
pyplot.show()