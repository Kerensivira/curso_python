# COMENTARIOS EN PYTHON: Se realizan colocando un "#" al principio
# de la línea.

# DECLARACIÓN DE VARIABLES: igual a JS, la diferencia es que puedes 
#declarar una variable sin usar las palabras reservadas "let, var y const"
# y no se convertirá en una variable global. ejm:

name = "Alberto "
last_name = "Alcachofa"
age = 32

print(name)
print(last_name)
print(age)
print(f"Me llamo {name} {last_name} y tengo {age} años y ({5-5}) en el banco")
print(name*5)

# LISTAS: Las listas en Python son similares a los arreglos en JavaScript. Son uno de
# los tipos de datos integrados en Python que se utilizan para almacenar colecciones de datos.

list_snake = ["Anaconda", "Boa constrictor", "Cobra real", "Víbora de cascabel", "Serpiente de maíz", "Pitón reticulada", "Mamba negra"]
print(list_snake[0])
list_snake[0] = 'manzana'
list_snake.insert(4, "zanahoria")
list_snake.append("Serpiente coral")
print(list_snake)

# TUPLAS: Muy parecidas a las listas porque ambas son para agregar elementos indexables pero a su vez tienen 
# diferencias notables.

# 1. Las tuplas en Python son inmutables, lo que significa que una vez creada una tupla, sus elementos no pueden cambiar. 
# Las tuplas # no pueden ser alteradas (véase: añadir, reasignar o eliminar algún elemento). Si intentas cambiar el 
# valor de uno de sus elementos, obtendrás un error, lo que implica que su longitud tampoco variará en el ciclo de vida del 
# programa.

tuple_vegetables = ("zanahoria", "brócoli", "lechuga", "espinaca", "calabacín", "tomate", "cebolla", "pepino", "pimiento", "apio")
print(tuple_vegetables)
print(tuple_vegetables[3])
print(tuple_vegetables[-1])

# DICCIONARIOS: En resumen, es una estructura de datos que permite almacenar pares clave-valor. Es mutable, lo que
# significa que puedes modificar, agregar o eliminar elementos después de crearlo. Las claves deben ser únicas y se
# utilizan para acceder a sus valores correspondientes. Proporciona una forma eficiente de buscar y recuperar datos en
# función de una clave. Los diccionarios en Python son muy versátiles y se utilizan ampliamente para representar 
# información estructurada y relacionada.

persona = { "name": "Juan", "age": 30, "city": "Madrid"}  #datos originales
persona['last_name'] = 'Carrasco' #dato agregado
print(f'Mi nombre es {persona["name"]} {persona["last_name"]}')
# del persona['age'] #dato eliminado
print(len(persona)) # mostrar la longitud del objeto
print(persona["name"]) # mostrar sólo el nombre por medio de su clave que almacena ese valor
print(persona) # mostrar el diccionario completo


# SENTENCIA IF/ELSE: Decide si determinadas sentencias deben ejecutarse o no. La sentencia «If» permite ejecutar 
# el código Python si se cumple una condición.
#if my condition == true //// las condiciones siempre inician en true por defecto. 


my_condition = True

if my_condition: 
    print("se ejecutó la condición")

print("la condición continúa")

# CICLO WHILE: estructura de control que repite un bloque de código mientras se cumpla una condición específica.
# permite ejecutar repetidamente un conjunto de instrucciones siempre que la condición sea verdadera. Si en algún momento la
#  condición se vuelve falsa, el ciclo se detiene y el programa continúa con la ejecución normal.

my_condition_ = 0

while my_condition_ <= 10:
    print(my_condition_)
    my_condition_ += 2


#Bucle for: El bucle for se utiliza para iterar sobre una secuencia de elementos, como listas, tuplas, cadenas o rangos,
# en un orden definido. A diferencia del bucle while, el bucle for se ejecuta un número específico de veces, dependiendo 
# del número de elementos en la secuencia. Es útil cuando se conoce la cantidad de elementos que se deben recorrer y se 
# desea ejecutar un bloque de código para cada elemento de la secuencia.

names = ["Juan", "María", "Pedro"]
for name in names:
    print(name)


#tabla de multiplicar: 

table = int(input('¿Qué tabla deseas ver?'))
range_numbers = range(0, 11)
for num in range_numbers: 
    result = table * num
    print(f'{table} x {num} = {result}')