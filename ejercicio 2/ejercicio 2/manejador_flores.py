# -*- coding: utf-8 -*-
"""
Created on Sun May 22 17:24:59 2022

@author: Emiliano
"""
import numpy as np
import sys
import csv
from classes.flores import Flores
class ManejadorF:
    __Cantidad=0
    __dimension=0
    __incremento=5
    
    def __init__(self,dimencion,incremento=5):
        self.__flores=np.empty(dimencion,dtype=Flores)
        self.__Cantidad=0
        self.__dimension=dimencion
    
    def setFlores(self,flores):
        if self.__Cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__persona.resize(self.__dimension)
        self.__flores[self.__Cantidad]=flores
        self.__Cantidad+=1
    
    def test(self):
        archivo = open('flores.csv',encoding = 'utf-8')
        reader = csv.reader(archivo,delimiter=';')
        for fila in reader:
            nuevo=Flores(fila[0], fila[1], fila[2], fila[3])
            self.setFlores(nuevo)
        archivo.close()
        
    def getFlores(self,i):
        return self.__flores[i]
    def getNombre(self,i):
        return self.__flores[i].getNombre()

    def BuscaFlores(self,busca):
        i=0
        while i < self.__dimension and busca != self.getNombre(i):
            i+=1
        if i != self.__dimension:
            return i
        else: return None
    def mostrar(self):
        for i in range(self.__Cantidad):
            print(self.getNombre(i))

    