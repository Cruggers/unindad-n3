# -*- coding: utf-8 -*-
"""
Created on Fri May 20 20:45:48 2022

@author: Emiliano
"""

from classes.facultad import Facultad
from classes.carrera import Carrera
import sys
import csv

class manejador_facultad:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def getFacultad(self,i):
        return self.__lista[i]
    def setFacultad(self,facultad):
        self.__lista.append(facultad)
    def getTamaño(self):
        return len(self.__lista)
    def setCarrera(self,i,carrera):
        self.__lista[i].setCarrera(carrera)
    def getCodigo(self,i):
        return self.__lista[i].getCodigo()
    def getCarrera(self,i,j):
        return self.__lista[i].getCarrera(j)
    def getNombreCarrera(self,i,j):
        return self.getCarrera(i, j).getNombre()
    def getTamañoCarrera(self,i):
        return self.__lista[i].getTamañoCarrera()
    def test(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            if len(fila) == 5:
                nuevo=Facultad(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.setFacultad(nuevo)
            elif len(fila) == 6:
                nuevo=Carrera(fila[1], fila[2], fila[3], fila[4], fila[5])
                i=int(fila[0])-1
                self.setCarrera(i, nuevo)
        archivo.close() 
    def buscaCodigo(self,busca):
        i=0
        while i<self.getTamaño() and busca != self.getCodigo(i):
            i+=1
        if i != self.getTamaño():
            return i
        else: return None
    def buscaCarrera(self):
        i=0
        j=0
        ban=True
        busca=input("ingrese nombre de carrera: ")
        while i < self.getTamaño() and  ban:
            while j < self.getTamañoCarrera(i) and ban:
                if busca != self.getNombreCarrera(i, j):
                    j+=1
                else:
                    ban=False
            if ban == False:
                print("codigo:",self.getCodigo(i),self.getCarrera(i, j).getCodigo())
                print(self.getFacultad(i))
            else: i+=1
            

    def mostrar(self):
        i=self.buscaCodigo(int(input("ingrese codigo de facultad:")))
        if i != None:
            print(self.getFacultad(i).getNombre())
            print("_______________________________________")
            for j in range(self.getTamañoCarrera(i)):
                print(self.getCarrera(i, j))
        else: print("el codigo ingresado no es valido")
                
        
        