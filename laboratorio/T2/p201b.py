import numpy

edades = numpy.array([23, 25, 29, 28, 27, 34, 45, 19, 32, 22])

print(f"""
EDADES:      {edades}
------------------------------------------------
TOTAL:       {edades.size:34d}
------------------------------------------------
SUMA:        {edades.sum():34.3f}
PROMEDIO:    {edades.mean():34.3f}
------------------------------------------------
VARIANZA:    {edades.var():34.3f}
DESV. EST.:  {edades.std():34.3f}
------------------------------------------------
MÍNIMO:      {edades.min():34d}
MÁXIMO:      {edades.max():34d}
""")