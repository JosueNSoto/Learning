#Variable declaration with snake_case
#Recommended by the developer
full_name = "Josue Soto"
#Variable declaration with camelCase
#Not recommended
fullName = "Noe Millán"

#----------#

#Concatenate with +
bienvenida1 = "Hola " + " ¿Cómo estás?"
#Concatenate with f-strings
#Si la variable full_name es un número, automáticamente el f-strings lo transforma el a un string
bienvenida2 = f"Hola {full_name}, ¿Como estás?"

print(bienvenida2)

#----------#

#Membership operators / Operadores de pertenencia (in / not in)
print("Soto" in full_name)
print("Millán" not in fullName)