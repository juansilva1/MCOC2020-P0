# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:32:01 2020

@author: jpsil
"""
# Creador de archivos

from numpy import *
from math import *
import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from time import perf_counter
from scipy import sparse
from numpy import float16
from scipy import linalg
#generador de matriz laplaciana
def M_laplaz(Nf,Nc):# No se si son estrictamente cuadradas
    
    numero_elementos=Nf*Nc
    matriz=np.eye(Nf,Nc,dtype=np.half)*2
    matriz_up=np.eye(Nf,Nc,k=1,dtype=np.dtype(np.half))*-1
    matriz_down=np.eye(Nf,Nc,k=-1)*-1
    
    return matriz+matriz_up+matriz_down
# print(M_laplaz(3, 3))


def datos(numero):
    
    lista_N=[2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,2000]
    lista_final_tiempo=[]
    archivo_str='datos_'+str(numero)+'.txt'
    archivo=open(archivo_str,'w')
        
    lista_tiempo=[]
    for N in lista_N:
        A = M_laplaz(N,N)
        # B = np.random.rand(N,N)
        
        t1 = perf_counter()
        C=np.linalg.inv(A)
        t2 = perf_counter()
    
        dt = t2 - t1
        palabra=str(str(dt)+','+str(N)+'\n')
        archivo.write(palabra)
        lista_tiempo.append(dt)
    archivo.close()
    
i=1
while i<11:#funciona para 10 archivos
    datos(i)
    i+=1

# GRAFICADOR

def lectura_de_archivos(numero):
    palabra='datos_'+str(numero)+'.txt'
    infile = open(palabra)
    lista_x=[]
    lista_y=[]
    for line in infile.readlines():
        datos_xy=line.split(',')
        lista_x.append(float(datos_xy[0]))
        lista_y.append(float(datos_xy[1]))
    lista_final=[lista_x,lista_y]
    return lista_final

fig,ax =  plt.subplots(2,1)

i=1
while i<11:#funciona para 10 archivos
    # print('\n',i,'\n')
    plt.grid()
    datos=lectura_de_archivos(i)
    ax[0].plot(datos[1],datos[0],'-o')
    # ax[1].plot(datos[1],datos[0])
    # plt.grid()
    i+=1

    
ax[0].set_ylabel('Tiempo transcurrido')
ax[0].set_title('Rendimiento inversa caso 1 half')
ax[0].set_xscale('log')
ax[0].set_yscale('log')

ax[0].set_xticks([10,20,50,100,200,500,1000,2000,5000,10000,20000])
ax[0].set_xticklabels(['','','','','','','','','',''],rotation=45)
ax[0].set_yticks([0.0001,0.001,0.01,0.1,1,10,60,600])
ax[0].set_yticklabels(['0.1 ms','1 ms','10 ms','0.1 s','1 s','10 s','1 min','10 min'])
ax[0].set_xlim(0,20000)
ax[0].grid(True)


lista_N=[2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,2000]
lista_B=[]
for i in lista_N: 
    lista_B.append(4*(i**2)*2)#1 half = 2 bytes
#se ocupan 4 matrices para invertir esto lo explico en el "README.md" del "github".
ax[1].plot([0,20000],[12000000000,12000000000],'--k')
ax[1].plot(lista_N,lista_B,'-o')    
ax[1].set_ylabel('Uso memoria')
ax[1].set_xlabel('Tamaño matriz N')
ax[1].set_xscale('log')
ax[1].set_yscale('log')

ax[1].set_xticks([10,20,50,100,200,500,1000,2000,5000,10000,20000])
ax[1].set_xticklabels([10,20,50,100,200,500,1000,2000,5000,10000,20000],rotation=45)
ax[1].set_yticks([1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000])
ax[1].set_yticklabels(['1 KB','10 KB','100 KB','1 MB','10 MB','100 MB','1 G','10 GB'])
ax[1].set_xlim(0,20000)
plt.grid(True)


plt.tight_layout()
plt.savefig("numpy_half.png")

# En la consola aparece que no son validos los limites, por lo que los ignora, este codigo crea archivos, los lee y grafica.
# Entrega4 de las 23:59
