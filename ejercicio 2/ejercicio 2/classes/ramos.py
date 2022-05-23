# -*- coding: utf-8 -*-
"""
Created on Sun May 22 17:16:25 2022

@author: Emiliano
"""

class Ramos:
    __Tamaño=""
    __Flores=[]
    def __init__(self,tamaño):
        self.__Tamaño=tamaño
        self.__Flores=[]
    def setFlores(self,flores):
        self.__Flores.append(flores)
    def getFlores(self):
        return self.__Flores
    def getTamañoFlores(self):
        return len(self.__Flores)
    def getTamaño(self):
        return self.__Tamaño
        
        