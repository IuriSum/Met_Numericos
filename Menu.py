# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:57:18 2020

@author: iuri_
"""

def Caso_1():
    print("Selecione o método:")
    print("1 – Bissecção:")
    print("2 - Newton")
    print("3 – Secantes")
    x = int(input("Método: "))
    if 0<x<4:
        if x == 1:
            print("Bissecção Selecionada")
        elif x == 2:
            print("Newton Selecionado")
        else:
            print("Secantes")
    else:
        return
    

def Caso_2():
    print("Selecione o método:")
    print("1 – Eliminação de Gauss:")
    print("2 - Decomposição LU")
    print("3 – Jacobi-Richardson")
    print("4 - Gauss-Seidel")
    x = int(input("Método: "))
    if 0<x<5:
        if x ==1:
            print("Eliminação de Gauss")
        elif x ==2:
            print("Decomposição LU")
        elif x == 3:
            print("Jacobi-Richardson")
        else:
            print("Gauss-Seidel")
    else:
        return
    
    
def Caso_3():
    print("Selecione o método:")
    print("1 – Lagrange:")
    print("2 - Newton")
    x = int(input("Método: "))
    
    if 0<x<3:
        if x ==1:
            print("Lagrange")
        else:
            print("Newton")
    else:
        return
    
    
def Caso_4():
    print("Selecione o método:")
    print("1 – Trapézio:")
    print("2 - 1/3 de Simpson")
    print("3 – 3/8 de Simpson")
    x = int(input("Método: "))
    
    if 0<x<4:
        if x ==1:
            print("Trapézio")
        elif x ==2:
            print("1/3 de Simpson")
        else:
            print("3/8 de Simpson")
    else:
        return
    
    
def Caso_5():
    print("Runge-Kutta 4ª Ordem:")
    
def Tema():
    print("Selecione o tema de estudo:\n 1 - raizes\n 2 - Sistemas de equaçoes lineares\n 3 - Interpolaçao Polinomial\n 4 - Integraçao Numerica\n 5 - Equaçoes diferenciais oridnarias")
    x = int(input("Tema:"))
    if 0<x<6:
        if x == 1:
            Caso_1()
        elif x == 2:
            Caso_2()
        elif x == 3:
            Caso_3()
        elif x == 4:
            Caso_4()
        else:
            Caso_5()
    else:
        return
    
    
    
    
    
print("Metodos Numericos Computacionais\n")         
Tema()
