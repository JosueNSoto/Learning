"""
if condicion is TRUE:
    accion
if conticion is FALSE:
    accion
"""
##Ejemplo 1
edad = 19
#Las identaciones son OBLIGATORIAS para que funcione else and if
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Eres menor de edad")


##Ejemplo 2  
contraseña_bs = "josveS"
contraseña_escrita = "Josve"

if contraseña_bs == contraseña_escrita:
    print("Bievenido")
else:
    print("Acceso denegado :)")
    

##Ejemplo 3
##Es posible meter un if dentro de otro if, if anidados
ingreso_mensual = 70000
gasto_mensual = 69000
if ingreso_mensual >= 30000:
    if ingreso_mensual - gasto_mensual < 0:
        print("gastas más de lo que ganas")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estás bien")
    else:
        print("Estás gastando mucho HDTPM")
elif ingreso_mensual >= 20000:
    print("Estás bien en latam")
else:
    print("No hay ni para el pan bro")