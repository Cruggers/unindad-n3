# -*- coding: utf-8 -*-
"""
Created on Mon May  9 18:23:02 2022

@author: Emiliano
"""
import sys
class Carrera:
    __codigo:int 
    __nombre=""
    __fecha_inicio=""
    __duracion=""
    __titulo=""
    def __init__(self,codigo,nombre,fecha,duracion,titulo):
        self.__codigo=int(codigo)
        self.__nombre=nombre
        self.__fecha_inicio=fecha
        self.__duracion=duracion
        self.__titulo=titulo
    def __str__(self):
        return "nombre de carrera:%s duracion %s" % (self.__nombre,self.__duracion)
    def getNombre(self):
        return self.__nombre
    def getCodigo(self):
        return self.__codigo
    
