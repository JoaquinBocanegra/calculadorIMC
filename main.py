"""
Funciones para calcular el IMC de una persona.
Siguiendo los pasos del curso de python hecho por el canal de youtube: Lucas Moy.
https://www.youtube.com/watch?v=swdcD6OPMlk

Adaptado por : Joaquin bocanegra
https://github.com/JoaquinBocanegra

"""

def calcularIMC(peso,altura):
    """
    Calcula el indice de masa corporal.
    Primer parametro de tipo int
    Segundo parametro de tipo float
    """
    imc = peso/(altura * altura)
    return imc

def pedirAlturaPeso():
    """Pide al usuario los valores del peso en kg y la altura en metros."""
    peso = int(input("Ingrese su peso en kg:"))
    altura = float(input("Ingrese su altura en metros:"))
    imc = calcularIMC(peso, altura)
    if imc < 20:
        print("Su estado actual de IMC es delgadez")
    if imc >= 20 and imc < 26:
        print("Su estado actual de IMC es normal")
    if imc >= 26 and imc < 30:
        print("Su estado actual de IMC es sobrepeso")
    if imc >= 30:
        print("Su estado actual de IMC es obesidad")

    print("Su IMC es de : " + str(imc))

print("Bienvenido a el calculador de IMC")
pedirAlturaPeso()
