import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
def suma(numero1, numero2):
    return numero1 + numero2


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros pares del 1 al 1000
"""


# start-->
def sumaPares(num1, num2):
    result = sum([iter for iter in range(num1, num2 + 1) if iter % 2 == 0])
    return result


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area total de superficie de un cilindro
radio = 5 m
altura = 7 m
area lateral: 2*pi*r*a
area circulo: 2*pi*r^2
area total: area lateral + area circulo
"""


# start-->
a = 7
r = 5


def areaTotalCilindro(arealateral, areaCirculo):
    result = arealateral + areaCirculo
    return result


def areaLateral(r, a):
    result = 2 * math.pi * r * a
    return result


def areaCirculo(r, a):
    result = 2 * math.pi * (r * r)
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cilindro:
    def __init__(self, areaCirculo, areaLateral):
        self.areaCirculo = areaCirculo
        self.areaLateral = areaLateral

    def areaTotalCilindro(self):
        result = self.areaLateral + self.areaCirculo


"""
***************************************************************
@@ ejercicio 5 @@
restaurante de pizzas
pizza
    nombre
    lugar
    costo
    conDescuento
    descuento
"""


class Restaurante:
    def ordenar(self, nombre, lugar, costo, conDescuento, descuento):
        pass

    def costoTotal(self):
        return 0

    def costoTotalConDescuento(self):
        return 0


class Pizza:
    pass


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
