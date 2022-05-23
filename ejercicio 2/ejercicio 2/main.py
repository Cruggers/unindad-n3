# -*- coding: utf-8 -*-
"""
Created on Sun May 22 17:15:57 2022

@author: Emiliano
"""
from manejador_flores import ManejadorF
from manejador_ramos import manejadorR

if __name__  == "__main__":
    flores=ManejadorF(5)
    flores.test()
    ramos=manejadorR()
    ramos.setRamos(flores)