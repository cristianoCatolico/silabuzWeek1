name = input(f"Ingrese su nombre: ")
last_name = input(f"Ingrese su apellido: ")
age = input(f"Ingrese su edad: ")

person = { "name": name.capitalize(), "last_name": last_name.capitalize(), "age": age}
print(f"Hola, mi nombre es {person['name']} {person['last_name']} y tengo {person['age']} años.")
