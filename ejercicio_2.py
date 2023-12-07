# Ingreso de datos
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

# Operaciones
variable_1 = nombre != "****"
variable_2 = edad > 5 and edad < 20

variable_3 = len(nombre) >= 4 and len(nombre) < 8
multi = edad * 3 >= 35

# Salidas
print(variable_1, variable_2, variable_3, multi)
