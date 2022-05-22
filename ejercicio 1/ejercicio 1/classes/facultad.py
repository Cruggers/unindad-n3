# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:22:56 2022

@author: Emiliano
"""
import sys
class Facultad:
    __codigo:int 
    __nombre=""
    __direccion=""
    __localidad=""
    __telefono=""
    __Carera=[]
    def __init__(self,codigo,nombre,direccion,localida,telefono):
        self.__codigo=int(codigo)
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localida
        self.__telefono=telefono
        self.__Carera=[]
    def __str__(self):
        return "%s, localidad:%s" % (self.__nombre,self.__localidad)
    def setCarrera(self,carrera):
        self.__Carera.append(carrera)
    def getNombre(self):
        return self.__nombre
    def getCodigo(self):
        return self.__codigo
    def getCarrera(self,i):
        return self.__Carera[i]
    def getTamañoCarrera(self):
        return len(self.__Carera)