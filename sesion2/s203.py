import pandas

edades = pandas.Series([
    21, 25, 19,
    27, 31, 20,
    31, 34, 24,
    22, 17, 50, 45,
])

print(
    edades.describe()
)