#Tenemos 3 AND OR NOT
#AND
resultado = True & True #Devuelve verdadero
resultado2 = False & True #Devuelve falso
resultado3 = True & False #Devuelve falso
resultado4 = False & False #Devuelve falso

#OR
resultado5 = True | True #Devuelve verdadero
resultado6 = False | True #Devuelve verdadero
resultado7 = True | False #Devuelve verdadero
resultado8 = False | False #Devuelve falso

#NOT
resultado9 = not True #Devuelve falso
"""
resultado9 not 2>23 #esto debería dar falso, pero como tiene un not detrás, lo cambia a verdadero
"""
resultado10 = not False #Devuelve verdadero

print(resultado10)