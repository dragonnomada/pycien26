# Introducción a la programación en Python

> Alan Badillo Salas
>
> Sábado 26, septiembre 2026

## Contenido

1. Variables y tipos de datos
2. Funciones
3. Listas e índices 
4. Iteradores y condicionales
5. Tuplas
6. Diccionarios 
7. Listas generadas
8. Manejo de archivos 
9. Objetos
10. Importación y uso de librerías

## Introducción

Python es un lenguaje de programación de propósito general en el que podemos escribir programas para resolver diferentes tipos de tareas, algunas de ellas están especialmente dirigidas al manejo de datos y la exposición de datos a través de servicios API y otros medios.

Una forma de entender Python es a través de algoritmos que resuelvan tareas tales como:

* Realizar cálculos y transformaciones, por ejemplo, resolver ecuaciones de modelos relacionados a diversas áreas científicas y sociales
* Automatizar tareas, como generar reportes y gráficos automatizados semanales, mensuales, trimestrales, etc.
* Generar modelos de predicción, hacer estadística descriptiva, inferencial y modelos de Machine Learning y Redes Neuronales
* Consumir IA Generativa, como la integración de modelos LLM de grandes empresas como OpenAI, para que agentes inteligentes resuelvan partes de las tareas empresariales, como la atención a clientes

Para comenzar a usar Python, podemos descargarlo directamente de https://python.org

Una de las versiones más estables es *Python 3.12.4* con soporte a muchas librerías, también se recomienda el uso de un entorno de desarrollo y editor de códigos como *Visual Code* para poder trabajar cómodamente en libretas mientras se aprende.

## Variables y tipos de datos

Las variables permiten retener valores nombrados, así cuando se guarda un valor en un cálculo u operación intermedia o resultante se pueda usar nuevamente en nuevas expresiones.

> **SINTAXIS:** `nombre = valor`

Nombre | Válido
--- | ---
temperatura | SI
_temperatura | SI
temperatura_ | SI
__temperatura | SI
temperatura__ | SI
precio_actual | SI
precioActual | SI
LIMITE | SI
MAXIMO | SI
VALOR_MAXIMO | SI
EDAD_MAXIMA | SI
persona1 | SI
1persona | NO
persona? | NO
persona-1 | NO
persona#1 | NO

El uso de nombre no válidos para variables puede provocar errores como `ERROR: Invalid syntax` o `ERROR: Name not found`

Las variables almacenan valores referentes o literales, por ejemplo, referentes al valor accedido de otra variable o valores literales como números y textos o combinaciones en expresiones más complicadas con el uso de operadores.

Tipo | Clase | Ejemplo de valor | Descripción
--- | --- | --- | ---
Número Entero | `int` | `123` o `1284` | Representa un número sin decimales
Número decimal | `float` | `1.234` o `8967.4563` | Representa un número con decimales
Texto simple | `str` | `"Hola mundo"` o `'Juan Escutia'` | Representa una cadena de caracteres o texto entrecomillado que se mantiene junto
Valor lógico | `bool` | `True` o `False` | Representa si algo es verdadero o falso
No definido o nulo | `NoneType` | `None` | Representa un valor sin significado actual

> Ejemplo del uso de variables, literales y tipos de datos

```py
precio_anterior = 23.5
precio_actual = 42.5

diferencia = precio_actual - precio_anterior

inflacion = diferencia / precio_anterior

print(inflacion)
```

Alternativamente

```py
precio_anterior = 23.5
precio_actual = 42.5

inflacion = (precio_actual - precio_anterior) / precio_anterior

print(f"Precio anterior: {precio_anterior}")
print(f"Precio actual: {precio_actual}")
print(f"Inflación: {inflacion}")
```

Observa que una cadena de texto que comienza con f (sufijo f) se considera un texto con formato (`f-string`), este explica que el texto puede incrustar valores provenientes de las variables o expresiones, y luego establecer un formato, para finalmente intentar incrustar el resultado dentro del texto sobre su plantilla, entonces, si tenemos un texto `"hola mundo"` no se considera con formato, solo es un texto simple, pero si tenemos `f"hola {nombre}"`, entonces, la plantilla de reemplazo ubicada, intentará recuperar el valor de la variable `nombre` y luego lo incrustará sobre el texto, por ejemplo, si `nombre = "Juan Escutia"`, entonces, se generará el texto `"Hola Juan Escutia"` (donde se inscrustó el valor recuperado).

Algunas conversiones importantes:

- `int(•)` - Intenta convertir lo que esté dentro de los paréntesis en un número entero, si falla marcará error, puede intentar convertir texto, enteros, decimales, valores lógicos, etc.
- `float(•)` - Intenta convertir lo que esté dentro de los paréntesis en un número decimal, si falla marcará error, puede intentar convertir texto, enteros, decimales, valores lógicos, etc.
- `str(•)` - Intenta convertir lo que esté dentro de los paréntesis en texto, si falla marcará error, puede intentar convertir texto, enteros, decimales, valores lógicos, etc. Aunque se recomienda hacerlo mejor con formatos.

Algunos adaptadores de formato importantes son:

- `{decimal:n.mf}` - Reserva exactamente `n` caracteres para inscrustación, y limita a `m` caracteres los decimales, por ejemplo, `8.2f` tendríamos un número máximo de `5` caracteres antes del punto, más el caracter punto, más `2` caracteres después del punto, en total `5 + 1 + 2 = 8` caracteres.
- `{texto:ns}` - Reserva aproximadamente `n` caracteres para inscrustación, de textos, por ejemplo, `20s` entonces textos con más de 20 caracteres solo muestran los primeros `20`.
- `{texto:>ns}` - Hace lo mismo pero carga el texto a la derecha.
- `{texto:^ns}` - Hace lo mismo pero centra el texto.

## Funciones

Las funciones simplifican la forma en la que hace un cálculo y permiten abstraer lógica y operaciones de forma simple en un modelo que consiste en recibir parámetros y devolver opcionalmente un resultado.

Las funciones permiten evaluar código en el cuerpo de la función y con la palabra `return` devolver el resultado final.

Cuando se llama o una función (se le conoce como invocación de la función), entonces, los parámetros asumen valores en ese momento y permiten realizar las operaciones internas de la función para generar el resultado.

> **SINTAXIS:** `def nombre(parametros):`

```py
def suma(a, b):
    return a + b

resultado = suma(100, 89)

print(resultado)
```

La definición de función se hace una única vez y queda como un prototipo o modelo para que en el evaluaciones se sepa exactamente que hacer con los valores parametrizados, por ejemplo, `100` envía el valor al parámetros `a` y `89` a `b`, luego ya se puede determinar `a + b` y el resultado es devuelto inmediatamente por la función, entonces, cuando se invoca a la función `suma(100, 89)`, el resultado es almacenado como valor de la variable `resultado`.

Entonces, es como si en lugar de hacer `resultado = 100 + 89`, crearamos un molde que lo opere internamente como `resultado = suma(100, 89)`.

## Listas e índices 

Las listas retienen valores acumulados e indexados sobre un mismo objeto llamado la **lista** del tipo `list`, entonces, una lista, se puede entender como un espacio de memoria que acumula valores y los recupera mediante un índice que comienza en `0`.

Las listas tienen el objetivo de almacenar grandes cantidades de valores y poder accederlos mediante un índice o un iterador secuencial.

Por ejemplo, si quisiéramos retener los valores de las edades de 100 personas tendríamos:

> **SINTAXIS:** `nombre = [elemento0, elemento1, elemento2, ..., elementoN-1]`
> 
> para una lista con `N` elementos

```py
edades = [
    23, 35, 43, 25, 27, 21, 58, 87, 56, 10,
    45, 31, 41, 25, 24, 21, 58, 87, 56, 10,
    32, 30, 48, 25, 27, 20, 58, 87, 56, 15,
    33, 32, 49, 23, 24, 21, 58, 87, 56, 10,
    28, 33, 47, 25, 23, 21, 58, 89, 56, 10,
    21, 38, 43, 25, 27, 21, 58, 87, 56, 19,
    59, 37, 43, 21, 26, 21, 58, 87, 56, 10,
    32, 39, 44, 25, 25, 21, 59, 87, 56, 19,
    67, 36, 43, 22, 26, 21, 58, 87, 56, 18,
    61, 64, 42, 20, 27, 21, 58, 87, 56, 10,
]

print(type(edades)) # <list>
```

Métodos de alteración:

- `.append(•)` - Agregar un elemento nuevo al final
- `.remove(•)` - Quitar un elemento si existe, o marca error
- `.count(•)` - Devuelve las veces que se repite un elemento o 0
- `.pop()` - Quita el último elemento de la lista y lo devuelve
- `.pop(index)` - Quita el elemento de la lista en el índice `index` y lo devuelve
- `.insert(index, •)` - Inserta un elemento en la lista en el índice `index` y desplaza los demás

Acceso por índices:

- `[index]` - Recupera el elemento en índice `index`
- `[i:j]` - Recupera la lista de todos los elementos desde el índice `i` hasta el índice `j - 1`, es decir, nunca se llega al último índice, por ejemplo, `[4:8]`, devulve los elementos `[4]`, `[5]`, `[6]`, `[7]`, es decir, `[elemento4, element5, elemento6, elemento7]`
- `[:j]` - Recupera la lista de todos elementos hasta `j-1` (sin tocarlo)
- `[i:]` - Recupera la lista de todos los elementos desde `i` y hasta el último alcanzable
- `[i:j:k]` - Recupera la lista de los elementos desde `i` hasta `j - 1`, de `k` en `k` posisiciones, por ejemplo, `2:10:3`, entonces los índices serían `2, 5, 8`, pero si fuera por ejemplo, `3:10:2`, entonces serían `3, 5, 7, 9`, pero para `3:9:2`, solo serían `3, 5, 7`

## Iteradores y condicionales

Una secuencia de elementos puede ser una lista, un rango o alguna colección o función generadora más avanzada, pero por lo general son objetos que se pueden recorrer de manera secuencial tomando el siguiente elemento, y luego el siguiente y así sucesivamente, cuando la secuencia ya no tiene elementos, se dice que ya se recorrió.

Un iterador, es una estructura de control llamada `for-in` que toma cada elemento de una secuencia como podría ser cada elemento de una lista o cada elemento de un rango y luego para ese elemento retenido (el valor se vuelve el iterando), entonces, podemos ejecutar un bloque de instrucciones, por ejemplo, recorrer las calificaciones y obtener la suma de ellas o recorrer los primeros 100 números naturales y sumarlos, o recorrer una lista de precios y calcular el precio total.

> **SINTAXIS:** `for elemento in secuencia:`

```py
suma = 0

for numero in range(1, 101): # Los rangos no llegan al último
    suma = suma + numero

print(suma)
```

Esto obtendría la suma de $0 + 1 + 2 + ... + 99 + 100$, entonces la suma es lo sumado hasta que se tiene el siguiente número.

## Tuplas

## Diccionarios 

## Listas generadas

## Manejo de archivos 

## Objetos

## Importación y uso de librerías
