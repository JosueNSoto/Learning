cadena1 = "Este Es Un Test"
cadena2 = "Bienvenido a este codigo"

#Como está declarado acá, es una función
#resultado = Upper(cadena1)

#Como está declarado acá, es el método de esta cadena1
#NO OLVIDES LOS PARÉNTERIS
resultado = cadena1.startswith("E")
print(resultado)

"""
Acá vamos a enlistar todos los métodos vistos

dir - Esta función devolverá todas las propiedades y métodos

upper - convierte en mayus
lower - convierte en minus
capitalize - primera en mayus

find - se utiliza para buscar la primera ocurrencia de una subcadena en una cadena dada y devuelve la posición de inicio de la subcadena si la encuentra, podemos buscar palabras o letras. Si no encuentra un valor, devuelve -1
index - se utiliza para encontrar la primera aparición de un valor especificado en una lista. Si no encuentra nada, manda excepción

isnumeric - si es numérico, devuelve true
isalpha - si es alfa numérico devuelve true, sólo LETRAS y sin espacios

count - devuelve el número de ocurrencias de una subcadena en la cadena dada, es un parámetro que busca en una cadena
len - cuenta los caracteres de una cadena. ES UNA FUNCIÓN -> len(cadena1)

startswith - verifica si una cadena comienza con
endswith - verifica si una cadena termina con 
**Ambos son case sensitive

replace - reemplaza un valor por otro
cadena_nueva = cadena1.replace("Este","Esta maquina")
split - separa por el parámetro dado por un parámetro que le demos. Nos devuelve una lista con los elementos separados en una cadena
"""