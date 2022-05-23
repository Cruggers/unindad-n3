# -*- coding: utf-8 -*-
"""
Created on Sun May 22 17:16:20 2022

@author: Emiliano
"""

class Flores:
    __Numero:int
    __Nombre=""
    __Color=""
    __Descripcion=""
    def __init__(self,numero,nombre,color,descripcion):
        self.__Numero=int(numero)
        self.__Nombre=nombre
        self.__Color=color
        self.__Descripcion=descripcion
    def getNombre(self):
        return self.__Nombre
    def __str__(self):
        return "tipo de flor:%s"%(self.__Nombre)
    
    