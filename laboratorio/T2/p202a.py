import pandas

edades = pandas.Series([23, 25, 29, 28, 27, 34, 19, 32, 22])

print(f"""
EDADES:      {edades}
------------------------------------------------
TOTAL:       {edades.count():34d}
------------------------------------------------
SUMA:        {edades.sum():34.3f}
PROMEDIO:    {edades.mean():34.3f}
------------------------------------------------
VARIANZA:    {edades.var():34.3f}
DESV. EST.:  {edades.std():34.3f}
------------------------------------------------
MÍNIMO:      {edades.min():34d}
MÁXIMO:      {edades.max():34d}
------------------------------------------------
Q1 (25%):      {edades.quantile(0.25):34.3f}
Q2 (50%):      {edades.quantile(0.50):34.3f}
Q3 (75%):      {edades.quantile(0.75):34.3f}
------------------------------------------------
2.5%:          {edades.quantile(0.025):34.3f}
5%:            {edades.quantile(0.05):34.3f}
95%:           {edades.quantile(0.95):34.3f}
97.5%:         {edades.quantile(0.975):34.3f}
""")