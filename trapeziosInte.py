# trabalho por Arthur Angelo Cenci Silva

import numpy as np

a = 1 # limite inferior de integração
b = 4 # limite superior de integração
m = 8 # número de subintervalos

def f(x):
    return 2*x

def integra (a, b, m):

    h = (b-a)/m # tamanho do subintervalo

    somatorio = 0 # inicializa o somatório
    for j in range(1,m):
        somatorio = somatorio + f(a + j * (b-a)/m)    

    I = (h/2)*(f(a) + f(b) + 2*somatorio)

    return I
    
def Simpsons(a, b, m):
    h = (b-a)/m # tamanho do subintervalo

    somatorio = 0 # inicializa o somatório
    
    for i in range(1,m):
        x = a + i * h
        if i%2 == 0:
            somatorio = somatorio + 2*f(x)
        else:
            somatorio = somatorio + 4*f(x)
    
    

    Integral = (h/3)*(f(a) + f(b) + somatorio)
    return Integral

resultado = integra(a, b, m)
resultado2 = Simpsons(a, b, m)
print("O resultado do integração é: ", resultado)
print("O resultado do integração por simpson é: ", resultado2)