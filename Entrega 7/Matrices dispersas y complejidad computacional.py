# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:28:48 2020

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
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.sparse import csc_matrix

# metodo para crear matrices laplacianas de tamaño N que estan llenas
def M_laplaz_llena(N):
    
    matriz=np.eye(N,N,dtype=np.double)*2
    matriz_up=np.eye(N,N,k=1,dtype=np.double)*-1
    matriz_down=np.eye(N,N,k=-1,dtype=np.double)*-1

    return matriz+matriz_up+matriz_down



# metodo para crear matrices laplacianas de tamaño N que solo tienen valores utiles (matrices dispersas)
def M_laplaz_dispersas(N):# No se si son estrictamente cuadradas
    
    matriz=sparse.eye(N,N,dtype=np.double)*2
    matriz_up=sparse.eye(N,N,k=1,dtype=np.double)*-1
    matriz_down=sparse.eye(N,N,k=-1,dtype=np.double)*-1
    
    return matriz+matriz_up+matriz_down

# metodo para crear los archivos
def creador_de_archivos(n,nombre_de_la_funcion):
    
    lista_archivos=[]
    for i in range(n):
        archivo_str = f'{nombre_de_la_funcion}_datos_{i}.txt'
        # archivo = open(archivo_str,'w')
        lista_archivos.append(archivo_str)
    
    
    # archivos_finales=[open(archi,'w') for archi in lista_archivos]
    return lista_archivos

#metodo para leer los archivos y recolectar sus datos
def lectura_de_archivos(X):

    infile=[open(infi) for infi in X]
    
    lista_archi=[]
    for i in range(len(X)):
        lista_tamano_N=[]
        lista_tiempo_ensamblaje=[]
        lista_tiempo_solucion=[]
        
        for line in infile[i].readlines():
            datos_xy=line.split(',')
            lista_tamano_N.append(np.double(datos_xy[0]))
            lista_tiempo_ensamblaje.append(np.double(datos_xy[1]))
            lista_tiempo_solucion.append(np.double(datos_xy[2]))
        lista_final=[lista_tamano_N,lista_tiempo_ensamblaje,lista_tiempo_solucion]
        lista_archi.append(lista_final)
        
    return lista_archi#[[[N],[Te],[Ts]],[[],[],[]]] de esta forma se entrega la lista


#ahora procedere a obtener los valores maximos de ensamblaje y de solucion
def valores_max(lista_datos_archivos):
    lista_ensamble=[]
    lista_solucion=[]
    for i in range(len(lista_datos_archivos)):
        lista_ensamble.append(max(lista_datos_archivos[i][1]))
        lista_solucion.append(max(lista_datos_archivos[i][2]))
    lista_max=[max(lista_ensamble),max(lista_solucion)]
    return lista_max

#ahora procedere a obtener los valores maximos finales de ensamblaje y solucion
def valores_finales_max(lista_datos_archivos):
    lista_ensamble=[]
    lista_solucion=[]
    for i in range(len(lista_datos_archivos)):
        lista_ensamble.append(lista_datos_archivos[i][1][-1])
        lista_solucion.append(lista_datos_archivos[i][2][-1])
    lista_max=[max(lista_ensamble),max(lista_solucion)]
    return lista_max

#poner una potencia
def unicode_exp(exp):
    if exp == 1:
       return chr(0xB9)
    if exp == 2 or exp == 3:
       return chr(0xB0 + exp)
    else:
       return chr(0x2070 + exp)

def graficador_complejidad(posicion,lista_datos_archivos):
    # graficar las lineas de complejidad en colores
    lista_max=valores_finales_max(lista_datos_archivos)
    
    lista_N_reves=lista_datos_archivos[0][0]
    lista_N_reves=lista_N_reves[::-1]
    lista_comple_2=[lista_max[posicion]/(1**(i)) for i in range(len(lista_N_reves))]
    
    plt.loglog(lista_N_reves,lista_comple_2,'--',color='steelblue',label='Constante')
    
    # plt.ylim(0.1e-5,600)
    
    #complejidad 1
    lista_N_reves=lista_datos_archivos[0][0]
    lista_N_reves=lista_N_reves[::-1]
    lista_comple_2=[lista_max[posicion]/(2**(i)) for i in range(len(lista_N_reves))]
    
    plt.loglog(lista_N_reves,lista_comple_2,'--',color='darkorange',label='O($N$)')
    
    #complejidad 2
    lista_N_reves=lista_datos_archivos[0][0]
    lista_N_reves=lista_N_reves[::-1]
    lista_comple_2=[lista_max[posicion]/(4**(i)) for i in range(len(lista_N_reves))]
    
    plt.loglog(lista_N_reves,lista_comple_2,'--',color='forestgreen',label='O({}{})'.format('$N$',unicode_exp(2)))
    
    # plt.ylim(0.1e-5,600)
    
    #complejidad 3
    lista_N_reves=lista_datos_archivos[0][0]
    lista_N_reves=lista_N_reves[::-1]
    lista_comple_2=[lista_max[posicion]/(8**(i)) for i in range(len(lista_N_reves))]
    a=0.5
    plt.loglog(lista_N_reves,lista_comple_2,'--',color='firebrick',label='O({}{})'.format('$N$',unicode_exp(3)))
    
    
    #complejidad 4
    lista_N_reves=lista_datos_archivos[0][0]
    lista_N_reves=lista_N_reves[::-1]
    lista_comple_2=[lista_max[posicion]/(16**(i)) for i in range(len(lista_N_reves))]
    
    plt.loglog(lista_N_reves,lista_comple_2,'--',color='mediumpurple',label='O({}{})'.format('$N$',unicode_exp(4)))
    
    plt.ylim(0.1e-4,600)

# Metodo para graficar
def graficador(lista_datos_archivos,nombre):
    
    xtks=[10,20,50,100,200,500,1000,2000,5000,10000,20000]
    
    ytks=[0.1e-3,0.1e-2,0.1e-1,0.1,1,10,60,600]
    ytks_labels=['0.1 ms','1 ms','10 ms','0.1 s','1 s','10 s','1 min','10 min']
    
    plt.subplot(211)
    graficador_complejidad(0,lista_datos_archivos)
    contador=0
    transparencia=0.5
    for i in lista_datos_archivos:

        numero_N=i[0]
        tiempo_ensamble=i[1]
        
        plt.loglog(numero_N,tiempo_ensamble,'-ok',alpha=transparencia)
        plt.ylabel('Tiempo de ensamblado')
        # plt.xlabel('Tamaño matriz $N$')
        # plt.grid(True)
        plt.xticks(xtks,xtks,rotation=45)
        plt.xticks([])
        plt.yticks(ytks,ytks_labels)
        contador+=1
    
    plt.subplot(212)
    graficador_complejidad(1,lista_datos_archivos)
    
    contador=0
    for i in lista_datos_archivos:

        numero_N=i[0]
        tiempo_ensamble=i[2]
        
        plt.loglog(numero_N,tiempo_ensamble,'-ok',alpha=transparencia)
        plt.ylabel('Tiempo de solucion')
        plt.xlabel('Tamaño matriz $N$')
        # plt.grid(True)
        plt.xticks(xtks,xtks,rotation=45)
        plt.yticks(ytks,ytks_labels)
        contador+=1
    
    plt.tight_layout()
    plt.legend()
    plt.savefig(f"Grafico {nombre}.png")
    plt.close()
    
    
    

############################

# funciones Matmul

# Datos a utilizar:

# Tamaño de la matriz
lista_N=[2,4,8,17,34,68,125,250,500,1000,2000,4000,8000]#,600,800,1000,2000,5000,10000]

corridas=5
lista_archivos_1=creador_de_archivos(corridas,'Matmul_AB_llena') # se crea una lista con el nombre de los archivos
archivo=[open(archi,'w') for archi in lista_archivos_1] # se abren los archivos de la lista anterior
contador=0

while contador<corridas:
    for N in lista_N:
        t1 = perf_counter()
        
        A = M_laplaz_llena(N)
        B = M_laplaz_llena(N)
        
        t2 = perf_counter()
        
        x = A@B
        
        t3 = perf_counter()
        
        palabra = f'{N},{t2-t1},{t3-t2}\n'
        archivo[contador].write(palabra)
    
    archivo[contador].flush()
    archivo[contador].close()

    contador+=1

#hasta aca tengo todos los archivos creados con sus respectivos datos
#ahora procedere a guardar los datos en una lista

lista_datos_archivos = lectura_de_archivos(lista_archivos_1)


#Me entrega los 2 graficos loglog 
graficador(lista_datos_archivos,'Matmul_AB_llena')





############################

# Datos a utilizar:

# Tamaño de la matriz
lista_N=[2,4,8,17,34,68,125,250,500,1000,2000,4000,8000]#,600,800,1000,2000,5000,10000]

corridas=5
lista_archivos_2=creador_de_archivos(corridas,'Matmul_AB_dispersa') # se crea una lista con el nombre de los archivos
archivo=[open(archi,'w') for archi in lista_archivos_2] # se abren los archivos de la lista anterior
contador=0

while contador<corridas:
    for N in lista_N:
        t1 = perf_counter()
        
        A = csc_matrix(M_laplaz_dispersas(N))
        B = csc_matrix(M_laplaz_dispersas(N))
        
        t2 = perf_counter()
        
        x = A@B
        
        t3 = perf_counter()
        
        palabra = f'{N},{t2-t1},{t3-t2}\n'
        archivo[contador].write(palabra)
    
    archivo[contador].flush()
    archivo[contador].close()

    contador+=1

#hasta aca tengo todos los archivos creados con sus respectivos datos
#ahora procedere a guardar los datos en una lista

lista_datos_archivos = lectura_de_archivos(lista_archivos_2)



graficador(lista_datos_archivos,'Matmul_AB_dispersa')





############################

# funciones Solve

# Datos a utilizar:

# Tamaño de la matriz
lista_N=[2,4,8,17,34,68,125,250,500,1000,2000,4000,8000,16000]#,600,800,1000,2000,5000,10000]

corridas=5
lista_archivos_1=creador_de_archivos(corridas,'Solve_Axb_llena') # se crea una lista con el nombre de los archivos
archivo=[open(archi,'w') for archi in lista_archivos_1] # se abren los archivos de la lista anterior
contador=0

while contador<corridas:
    for N in lista_N:
        t1 = perf_counter()
        
        A = M_laplaz_llena(N)
        b = np.ones(N)
        
        t2 = perf_counter()
        
        x = spLinalg.solve(A,b)
        
        t3 = perf_counter()
        
        palabra = f'{N},{t2-t1},{t3-t2}\n'
        archivo[contador].write(palabra)
    
    archivo[contador].flush()
    archivo[contador].close()

    contador+=1

#hasta aca tengo todos los archivos creados con sus respectivos datos
#ahora procedere a guardar los datos en una lista

lista_datos_archivos = lectura_de_archivos(lista_archivos_1)


#Me entrega los 2 graficos loglog 
graficador(lista_datos_archivos,'Solve_Axb_llena')





############################

# Datos a utilizar:

# Tamaño de la matriz
lista_N=[2,4,8,17,34,68,125,250,500,1000,2000,4000,8000,16000]#,600,800,1000,2000,5000,10000]

corridas=5
lista_archivos_2=creador_de_archivos(corridas,'Solve_Axb_dispersa') # se crea una lista con el nombre de los archivos
archivo=[open(archi,'w') for archi in lista_archivos_2] # se abren los archivos de la lista anterior
contador=0

while contador<corridas:
    for N in lista_N:
        t1 = perf_counter()
        
        A = csc_matrix(M_laplaz_dispersas(N))
        b = np.ones(N)
        
        t2 = perf_counter()
        
        x = sparse.linalg.spsolve(A,b)
        
        t3 = perf_counter()
        
        palabra = f'{N},{t2-t1},{t3-t2}\n'
        archivo[contador].write(palabra)
    
    archivo[contador].flush()
    archivo[contador].close()

    contador+=1

#hasta aca tengo todos los archivos creados con sus respectivos datos
#ahora procedere a guardar los datos en una lista

lista_datos_archivos = lectura_de_archivos(lista_archivos_2)



graficador(lista_datos_archivos,'Solve_Axb_dispersa')





############################

# funciones INVERSA


# Datos a utilizar:

# Tamaño de la matriz
lista_N=[2,4,8,17,34,68,125,250,500,1000,2000,4000,8000,16000]#,600,800,1000,2000,5000,10000]

corridas=5
lista_archivos_1=creador_de_archivos(corridas,'inv_A_llena') # se crea una lista con el nombre de los archivos
archivo=[open(archi,'w') for archi in lista_archivos_1] # se abren los archivos de la lista anterior
contador=0

while contador<corridas:
    for N in lista_N:
        t1 = perf_counter()
        
        A = M_laplaz_llena(N)
        
        t2 = perf_counter()
        
        x = spLinalg.inv(A)
        
        t3 = perf_counter()
        
        palabra = f'{N},{t2-t1},{t3-t2}\n'
        archivo[contador].write(palabra)
    
    archivo[contador].flush()
    archivo[contador].close()

    contador+=1

#hasta aca tengo todos los archivos creados con sus respectivos datos
#ahora procedere a guardar los datos en una lista

lista_datos_archivos = lectura_de_archivos(lista_archivos_1)


#Me entrega los 2 graficos loglog 
graficador(lista_datos_archivos,'inv_A_llena')


############################

# Datos a utilizar:

# Tamaño de la matriz
lista_N=[2,4,8,17,34,68,125,250,500,1000,2000,4000,8000,16000]#,600,800,1000,2000,5000,10000]

corridas=5
lista_archivos_2=creador_de_archivos(corridas,'inv_A_dispersa') # se crea una lista con el nombre de los archivos
archivo=[open(archi,'w') for archi in lista_archivos_2] # se abren los archivos de la lista anterior
contador=0

while contador<corridas:
    for N in lista_N:
        t1 = perf_counter()
        
        A = csc_matrix(M_laplaz_dispersas(N))
        
        t2 = perf_counter()
       
        x = sparse.linalg.inv (A)
        
        t3 = perf_counter()
        
        palabra = f'{N},{t2-t1},{t3-t2}\n'
        archivo[contador].write(palabra)
    
    archivo[contador].flush()
    archivo[contador].close()

    contador+=1

#hasta aca tengo todos los archivos creados con sus respectivos datos
#ahora procedere a guardar los datos en una lista

lista_datos_archivos = lectura_de_archivos(lista_archivos_2)



graficador(lista_datos_archivos,'inv_A_dispersa')















