class Carro:
    marca = ""
    color = ""

    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        self.__encendido = False

    def encender(self):
        self.__encendido = True

    def get_encendido(self):
        return self.__encendido

# Crear una instancia de la clase y llamar al método
carro1 = Carro("Toyota", "Blanco")

print(f'Marca: {carro1.marca}, Color: {carro1.color}')

# Obtener el estado actual del atributo __encendido utilizando el método get_encendido()
if carro1.get_encendido():
    print("El carro está encendido")
else:
    print("El carro está apagado")



# Herencia:permite que una clase adquiera las propiedades y comportamientos de otra clase, conocida 
# como clase padre o superclase. La clase que hereda se denomina clase hija o subclase. La herencia permite reutilizar 
# código y establecer una jerarquía de clases, donde las clases hijas pueden agregar o modificar atributos y métodos 
# adicionales, además de heredar los que provienen de la clase padre. Esto promueve la reutilización de código y facilita
# la organización y estructura de las clases en un programa.

# para el siguiente ejemplo se creará una clase donde se heredará la clase "Carro", luego se pasará otra clase llamada
# "Carro_4x4" para hacer herencia múltiple.

class Carro_4x4:
    rueda_size: 0


class Carro_deportivo(Carro, Carro_4x4):
  cv = 0

  def __init__ (self, marca, color, cv, rueda_size):
    self.marca = marca
    self.color = color
    self.cv = cv
    self.rueda_size = rueda_size

sport = Carro_deportivo("BMW","Rojo", 288, 20)
print(f'Marca: {sport.marca}, Color: {sport.color}, Velocidad: {sport.cv}, Tamaño de la rueda: {sport.rueda_size}')

