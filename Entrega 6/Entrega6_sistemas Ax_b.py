# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:27:00 2020

@author: jpsil
"""

from numpy import *
from math import *
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from time import perf_counter
from numpy import float32
import scipy as sp
import scipy.linalg as spLinalg

archivo_str=['A_invB_inv.txt','A_invB_npSolve.txt','A_invB_spSolve.txt','A_invB_spSolve_gen.txt','A_invB_spSolve_gen_overwrite.txt','A_invB_spSolve_symmetric.txt','A_invB_spSolve_symmetric_overwrite.txt','A_invB_spSolve_pos.txt','A_invB_spSolve_pos_overwrite.txt']
lista_N=[2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,2000,5000,10000]

# Generador de matriz laplaciana
def M_laplaz(Nf,Nc):# No se si son estrictamente cuadradas
    
    numero_elementos=Nf*Nc
    matriz=np.eye(Nf,Nc,dtype=np.float32)*2
    matriz_up=np.eye(Nf,Nc,k=1,dtype=np.float32)*-1
    matriz_down=np.eye(Nf,Nc,k=-1,dtype=np.float32)*-1

    return matriz+matriz_up+matriz_down

# Esta funcion me creara 2 archivos cada uno con los tiempos promedios de 10 corridas y los N asociados (tamaño de la matriz)
def datos():

    archivo=[open(archi,'w') for archi in archivo_str]
    
    for N in lista_N:
        
        
        # A_invB_inv
        lista_promedios=[]
        for i in range (5):
            # print(i)
            A = M_laplaz(N,N)
            B = np.ones(N)

            t1 = perf_counter()
            A_invertida=np.linalg.inv(A)
            x=A_invertida@B
            t2 = perf_counter()
            dt = t2 - t1
            lista_promedios.append(dt)
        promedio_N=np.mean(lista_promedios)
        palabra=str(str(promedio_N)+','+str(N)+'\n')
        archivo[0].write(palabra)


        # A_invB_npSolve
        lista_promedios_1=[]
        for r in range (5):
            
            A = M_laplaz(N,N)
            B = np.ones(N)

            t1 = perf_counter()
            x=np.linalg.solve(A,B)
            t2 = perf_counter()
            dt = t2 - t1
            lista_promedios_1.append(dt)
        promedio_N_1=np.mean(lista_promedios_1)
        palabra=str(str(promedio_N_1)+','+str(N)+'\n')
        archivo[1].write(palabra)
        
        
        # A_invB_spSolve
        lista_promedios_2=[]
        for r in range (5):
            
            A = M_laplaz(N,N)
            B = np.ones(N)

            t1 = perf_counter()
            x=spLinalg.solve(A,B)
            t2 = perf_counter()
            dt = t2 - t1
            lista_promedios_2.append(dt)
        promedio_N_2=np.mean(lista_promedios_2)
        palabra=str(str(promedio_N_2)+','+str(N)+'\n')
        archivo[2].write(palabra)
        
        
        # A_invB_spSolve_gen
        lista_promedios_3=[]
        for r in range (5):
            
            A = M_laplaz(N,N)
            B = np.ones(N)

            t1 = perf_counter()
            x=spLinalg.solve(A,B,assume_a='gen')
            t2 = perf_counter()
            dt = t2 - t1
            lista_promedios_3.append(dt)
        promedio_N_3=np.mean(lista_promedios_3)
        palabra=str(str(promedio_N_3)+','+str(N)+'\n')
        archivo[3].write(palabra)
        
        
        # A_invB_spSolve_gen_overwrite
        lista_promedios_4=[]
        for r in range (5):
            
            A = M_laplaz(N,N)
            B = np.ones(N)

            t1 = perf_counter()
            x=spLinalg.solve(A,B,assume_a='gen',overwrite_a=True)
            t2 = perf_counter()
            dt = t2 - t1
            lista_promedios_4.append(dt)
        promedio_N_4=np.mean(lista_promedios_4)
        palabra=str(str(promedio_N_4)+','+str(N)+'\n')
        archivo[4].write(palabra)
        
        
        # A_invB_spSolve_symmetric
        lista_promedios_5=[]
        for r in range (5):
            
            A = M_laplaz(N,N)
            B = np.ones(N)

            t1 = perf_counter()
            x=spLinalg.solve(A,B,assume_a='sym')
            t2 = perf_counter()
            dt = t2 - t1
            lista_promedios_5.append(dt)
        promedio_N_5=np.mean(lista_promedios_5)
        palabra=str(str(promedio_N_5)+','+str(N)+'\n')
        archivo[5].write(palabra)
        

        # A_invB_spSolve_symmetric_overwrite
        lista_promedios_6=[]
        for r in range (5):
            
            A = M_laplaz(N,N)
            B = np.ones(N)

            t1 = perf_counter()
            x=spLinalg.solve(A,B,assume_a='sym',overwrite_a=True)
            t2 = perf_counter()
            dt = t2 - t1
            lista_promedios_6.append(dt)
        promedio_N_6=np.mean(lista_promedios_6)
        palabra=str(str(promedio_N_6)+','+str(N)+'\n')
        archivo[6].write(palabra)
        
        
        # A_invB_spSolve_pos
        lista_promedios_7=[]
        for r in range (5):
            
            A = M_laplaz(N,N)
            B = np.ones(N)

            t1 = perf_counter()
            x=spLinalg.solve(A,B,assume_a='pos')
            t2 = perf_counter()
            dt = t2 - t1
            lista_promedios_7.append(dt)
        promedio_N_7=np.mean(lista_promedios_7)
        palabra=str(str(promedio_N_7)+','+str(N)+'\n')
        archivo[7].write(palabra)
        
        
        # A_invB_spSolve_pos_overwrite
        lista_promedios_8=[]
        for r in range (5):
            
            A = M_laplaz(N,N)
            B = np.ones(N)

            t1 = perf_counter()
            x=spLinalg.solve(A,B,assume_a='pos',overwrite_a=True)
            t2 = perf_counter()
            dt = t2 - t1
            lista_promedios_8.append(dt)
        promedio_N_8=np.mean(lista_promedios_8)
        palabra=str(str(promedio_N_8)+','+str(N)+'\n')
        archivo[8].write(palabra)
        
        
    for t in range(len(archivo_str)):
        archivo[t].flush()
        archivo[t].close()


datos()

# Lector de Archivos
def lectura_de_archivos():

    infile=[open(infi) for infi in archivo_str]
    
    lista_archivos=[]
    for i in range(len(archivo_str)):
        lista_x=[]
        lista_y=[]
        
        for line in infile[i].readlines():
            datos_xy=line.split(',')
            lista_x.append(float(datos_xy[0]))
            lista_y.append(float(datos_xy[1]))
        lista_final=[lista_x,lista_y]
        lista_archivos.append(lista_final)
        
    return lista_archivos#[[[],[]],[[],[]]] de esta forma se entrega la lista
lista_con_archivos=lectura_de_archivos()

# Funcion para Graficar
def graficador(archivo_str):
    
    xtks=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    
    ytks=[0.1e-3,0.1e-2,0.1e-1,0.1,1,10,60,600]
    ytks_labels=['0.1 ms','1 ms','10 ms','0.1 s','1 s','10 s','1 min','10 min']
    
    plt.figure()
    contador=0
    for i in lista_con_archivos:

        tiempo=i[0]
        numero_N=i[1]
        
        plt.loglog(numero_N,tiempo,'-o',label=archivo_str[contador])
        plt.ylabel('Tiempo transcurrido (s)')
        plt.xlabel('Tamaño matriz $N$')
        plt.grid(True)
        plt.xticks(xtks,xtks,rotation=45)
        plt.yticks(ytks,ytks_labels)
        contador+=1
    plt.tight_layout()
    plt.legend()
    plt.savefig("Grafico Ax_b  performance.png")

graficador(archivo_str)