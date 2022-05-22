# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:22:39 2022

@author: Emiliano
"""
import sys
from manejadorFacultad import manejador_facultad
if __name__ == "__main__":
    nuevo=manejador_facultad()
    nuevo.test()
    ban=True
    while ban:
        print("menu")
        print("1- busqueda de facultad:")
        print("2- busquea de carrera")
        print("0- para terminar: ")
        op=int(input("ingrese su opcion:"))
        if op==1:
            nuevo.mostrar()
            input("precione una tecla para continuar")
        elif op==2:
            nuevo.buscaCarrera()
            input("precione una tecla para continuar")
        elif op==0:
            ban=False
            print("saliendo....")
        else: 
            print("la opcion ingresada no es valida")
            input("precione una tecla para continuar")


