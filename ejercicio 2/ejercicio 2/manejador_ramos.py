# -*- coding: utf-8 -*-
"""
Created on Sun May 22 17:52:07 2022

@author: Emiliano
"""
from classes.ramos import Ramos

import sys
class manejadorR:
    __ramos=[]
    
    def __init__(self):
        
        self.__ramos=[]
        
    def setRamos(self,flores):
        tamaño=int(input("tamaño de ramo:\n 1:pequeño\n 2: mediano\n 3:grande\n ingrese su opcion:"))
        if tamaño == 1:
            self.__ramos.append(Ramos("pequeño"))        
        elif tamaño == 2:
            self.__ramos.append(Ramos("mediano"))    
        elif tamaño == 3:
            self.__ramos.append(Ramos("grande"))
        ban=True
        while ban:
            i=flores.BuscaFlores(input("ingrese tipo de flor:"))
            if i != None:
                j=len(self.__ramos)-1
                self.setFlores((j),flores.getFlores(i))
            op=input("precione n para terminar:")
            if op=="n":
                ban=False
            
    def getTamaño(self,i):
        return self.__ramos[i].getTamaño()
    def getFlores(self,i):
        return self.__ramos[i].getFlores().getNombre()
    def getTamañoFlor(self,i):
        self.__ramos[i].getTamañoFlores()
    def setFlores(self,i,flor):
        self.__ramos[i].setFlores(flor)
    def mostrar1(self,flores):
        pass
    
    def mostrar2(self):
        tamaño=input("ingrese tamaño del ramo:")
        for i in range(len(self.__ramos)):
            lis=self.getFlores(i)
            if tamaño==self.getTamaño(i):
                for flor in lis:
                    print(flor)
                    
            
            
        
    
    