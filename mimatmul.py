# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 14:24:26 2020

@author: jpsil
"""

import numpy as np
from time import perf_counter

def mimatmul(X,Y):
    # Y=np.random.rand(N,N)
    # X=np.random.rand(N,N)
    
    #dimensiones de las matrices
    filas_Y=len(Y)
    columnas_Y=len(Y[0])
    
    filas_X=len(X)
    columnas_X=len(X[0])
    
    #comprobar si se pueden multiplicar
    if columnas_Y!=filas_X:
        return False
    matriz_final=np.zeros((filas_Y,columnas_X))
    
    #multiplicacion     
    for i in range(0,filas_Y):
        for j in range(0,columnas_X):
            for k in range(0,filas_X):
                matriz_final[i,j]+=Y[i,k]*X[k,j]
    return matriz_final
    