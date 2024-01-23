import turtle
import time
import random

def escribir_pizarra(frase, color="black"):
    turtle.pencolor(color)
    turtle.pendown()
    turtle.write(frase, align="center", font=("Arial", 24, "normal"))
    turtle.penup()

def fuegos_artificiales():
    for _ in range(100):
        color = random.choice(["red", "orange", "yellow", "green", "blue", "purple"])
        turtle.pencolor(color)
        turtle.dot(random.randint(1, 10))
        turtle.forward(random.randint(5, 20))
        turtle.right(random.randint(0, 360))
    turtle.penup()

def desvanecer_fuegos_artificiales():
    for _ in range(100):
        turtle.clear()
        time.sleep(0.05)

def main():
    while True:
        turtle.speed(1)
        turtle.bgcolor("white")
        turtle.penup()

        # Escribir la frase inicial
        escribir_pizarra("Feliz día del administrador, mi administradora favorita")
        time.sleep(5)

        # Transición a fuegos artificiales
        fuegos_artificiales()
        time.sleep(5)

        # Desvanecer los fuegos artificiales
        desvanecer_fuegos_artificiales()

        # Escribir "TKM"
        escribir_pizarra("TKM")
        time.sleep(7)

        # Limpiar pantalla y reiniciar animación
        turtle.clear()

if __name__ == "__main__":
    turtle.Screen().exitonclick()
