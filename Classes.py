class User:
  def __init__(self, nombre, apellidos):
    self.nombre = nombre
    self.apellidos = apellidos
  
  def postear(self, mensaje):
      print(mensaje)

usuario1 = User( "juanito", "perez")
usuario1.postear("Hola Mundo")
usuario2= User("pepito", "perez")

print(usuario1.nombre, usuario1.apellidos)
print(usuario2.nombre, usuario2.apellidos)

        