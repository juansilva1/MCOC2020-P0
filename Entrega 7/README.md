# Matrices dispersas y complejidad computacional
*A tener en cuenta, las matrices de tamaño 2 no se consideran en este análisis, pues por lo general sus tiempos de ensamble y solución son extremadamente mayores en comparación a matrices de tamaños superiores, por lo que afectarían en gran medida el análisis realizado en cuanto a complejidad algorítmica.*
## Complejidad algorítmica de Matmul

### Análisis por cada gráfico

#### Matriz llena

![Grafico Matmul_AB_llena](https://user-images.githubusercontent.com/69159364/90836993-c01ef600-e31e-11ea-84dd-b7d907bc3c74.png)
 

**Análisis**

*Ensamblado*
- Para Tamaños de matrices superiores a N = 100 se estabiliza la curva, por lo que esta adopta una complejidad de O(N^2).
- Al menos para matrices pequeñas, no se parecen todas.

*Solución*

- Para Tamaños de matrices superiores a N = 100 se estabiliza la curva, por lo que esta adopta una complejidad de O(N^3).
- Al menos para matrices pequeñas, no se parecen todas.

#### Matriz dispersa

![Grafico Matmul_AB_dispersa](https://user-images.githubusercontent.com/69159364/90837063-e8a6f000-e31e-11ea-9b5a-d4a7e8a07bbb.png)

**Análisis**

*Ensamblado*

- Para cualquier tamaño de matrices, se adopta una complejidad “Constante”.
- Al menos para matrices pequeñas, no se parecen todas.

*Solución*

- Para cualquier tamaño de matrices, se adopta una complejidad casi constante, que para tamaños mayores a 4000 tiende una complejidad de O(N).
- Al menos para matrices pequeñas, no se parecen todas.

### Preguntas generales
1)	Para Matrices de tamaño N < 500, el ensamblado de las matrices llenas resulta más eficiente que el de las matrices dispersas. Pasado este punto, el ensamblaje de las matrices dispersas se vuelve el más eficiente.
    
    Para Matrices de tamaño N < 250, la solución se obtiene de forma más eficiente en las matrices llenas. Pasado este punto, mediante la utilización de matrices dispersas, la solución se obtiene significativamente antes que en las matrices llenas (matrices dispersas mucho más eficientes que matrices llenas).

2)	Ensamblado matrices llenas (N -- > oo): O(N^2).

    Solución matrices llenas (N -- > oo): O(N^3).

    Ensamblado matrices dispersas (N -- > oo): “Constante”.

    Solución matrices dispersas (N -- > oo): O(N). 

3)	Ensamblado matrices llenas: parte comportándose como una función constante hasta las matrices de tamaño 32 aproximadamente, después de este punto pasa a tener una complejidad de O(N^2). 

    Solución matrices llenas: parte comportándose como una función constante hasta las matrices de tamaño 16 aproximadamente, después de este punto pasa a tener una complejidad de O(N) hasta llegar al tamaño de matrices superiores a N = 125. Pasado este tamaño se adopta una complejidad de O(N^3).

    Ensamblado matrices dispersas: prácticamente toda la función es Constante, sin embargo, en las matrices con un N = 4000 en adelante se aprecia una leve pendiente, por lo que asumo que para matrices de mayor tamaño tendrá una complejidad de O(N).

    Solución matrices dispersas: prácticamente toda la función es Constante, sin embargo en las matrices con un N = 2000 en adelante se aprecia una leve pendiente, por lo que asumo que para matrices de mayor tamaño tendrá una complejidad de O(N).

4)  Las corridas por lo general son estables, solo al comienzo, con matrices muy pequeñas, tienden a diferir del resto de corridas.


## Complejidad algorítmica de Solve

### Análisis por cada gráfico

#### Matriz llena

![Grafico Solve_Axb_llena](https://user-images.githubusercontent.com/69159364/90837126-155b0780-e31f-11ea-805c-61b1e63bedee.png)

**Análisis**

*Ensamblado*
- Para Tamaños de matrices superiores a N = 100 se estabiliza la curva, por lo que esta adopta una complejidad de O(N^2) hasta las matrices de tamaño N = 4000, pasado este punto presenta una complejidad de O(N^3) (muy cerca del O(N^4), para N mayores puede darse el caso de que se adopte esta complejidad). 
- Al menos para matrices de tamaño N menores a 500 son bastante diferentes entre sí, pasado este punto, las corridas se comportan de forma muy similar.

*Solución*

- Para Tamaños de matrices superiores a N = 250 se estabiliza la curva, por lo que esta adopta una complejidad de O(N^3).
- Al menos para matrices de tamaño N menores a 250 son bastante diferentes entre sí, pasado este punto, las corridas se comportan prácticamente de la misma forma.

#### Matriz dispersa

![Grafico Solve_Axb_dispersa](https://user-images.githubusercontent.com/69159364/90837178-3ae81100-e31f-11ea-8bd7-725d3c2fb0f6.png)

**Análisis**

*Ensamblado*

- Por lo general para cualquier tamaño de matrices, se adopta una complejidad “Constante”.
- Al menos para matrices pequeñas, no se parecen todas.

*Solución*

- Hasta las matrices de tamaño N = 125 se adopta una complejidad casi constante, que para tamaños mayores tiende a una complejidad de O(N).
- No se parecen todas, hay una que por así decirlo “se desordena” y a pesar de tener pendientes similares tiende a distanciarse de las otras corridas. 

### Preguntas generales
1)	Para Matrices de tamaño N < 250, el ensamblado de las matrices llenas resulta más eficiente que el de las matrices dispersas. Pasado este punto, el ensamblaje de las matrices dispersas se vuelve el más eficiente.

    Para Matrices de tamaño N < 16, la solución se obtiene de forma más eficiente en las matrices llenas. Pasado este punto, mediante la utilización de matrices dispersas, la solución se obtiene significativamente antes que en las matrices llenas (matrices dispersas mucho más eficientes que matrices llenas).

2)	Ensamblado matrices llenas (N -- > oo): O(N^4).

    Solución matrices llenas (N -- > oo): O(N^3).

    Ensamblado matrices dispersas (N -- > oo): O(N).

    Solución matrices dispersas (N -- > oo): O(N). 

3)	Ensamblado matrices llenas: parte comportándose como una función constante hasta las matrices de tamaño 32 aproximadamente (las corridas no son parecidas en este punto, pero las pendientes individuales tienden a “constante”), después de este punto pasa a tener una complejidad de O(N^2) hasta N = 8000, pasado este punto la complejidad tiende a O(N^4). 

    Solución matrices llenas: parte comportándose como un función lineal (O(N)) hasta las matrices de tamaño 125. Pasado este tamaño se adopta una complejidad de O(N^3).

    Ensamblado matrices dispersas: prácticamente toda la función es Constante, sin embargo, en las matrices con un N = 8000 en adelante se aprecia una leve pendiente, por lo que asumo que para matrices de mayor tamaño tendrá una complejidad de O(N).

    Solución matrices dispersas: prácticamente toda la función es Constante, sin embargo en las matrices con un N = 250 en adelante se aprecia una complejidad de O(N).

4)	Las corridas por lo general no son estables, hay casos en que para que todas se comporten de la misma forma el N tiene que pasar de 8000.


## Complejidad algorítmica de INV

### Análisis por cada gráfico

#### Matriz llena

![Grafico inv_A_llena](https://user-images.githubusercontent.com/69159364/90837218-68cd5580-e31f-11ea-924d-cd79af1dc414.png)

**Análisis**

*Ensamblado*
- Para Tamaños de matrices superiores a N = 500 se estabiliza la curva, por lo que esta adopta una complejidad de O(N^2) hasta las matrices de tamaño N = 8000, pasado este punto presenta una complejidad de O(N^3). 
- Al menos para matrices de tamaño N menores a 500 son bastante diferentes entre sí, pasado este punto, las corridas se comportan prácticamente de la misma forma.

*Solución*

- Para Tamaños de matrices superiores a N = 1000 se estabiliza la curva, por lo que esta adopta una complejidad de O(N^3).
- Al menos para matrices de tamaño N menores a 1000 son bastante diferentes entre sí, pasado este punto, las corridas se comportan de forma muy similar.

#### Matriz dispersa

![Grafico inv_A_dispersa](https://user-images.githubusercontent.com/69159364/90837257-8a2e4180-e31f-11ea-83c1-e50b472572b8.png)

**Análisis**

*Ensamblado*

- Por lo general para cualquier tamaño de matrices, se adopta una complejidad “Constante”.
- Al menos para matrices pequeñas, no se parecen todas.

*Solución*

- Hasta las matrices de tamaño N = 4000 se adopta una complejidad O(N), que para tamaños mayores tiende a una complejidad de O(N^3).
- Todas las corridas se parecen. 

### Preguntas generales
1)	Para Matrices de tamaño N < 125, el ensamblado de las matrices llenas resulta más eficiente que el de las matrices dispersas. Pasado este punto, el ensamblaje de las matrices dispersas se vuelve el más eficiente.

    Para Matrices de tamaño N < 4000, la solución se obtiene de forma más eficiente en las matrices llenas. Pasado este punto, mediante la utilización de matrices dispersas, la solución se obtiene ligeramente antes que en las matrices llenas (matrices dispersas levemente más eficientes para estos números, probablemente para matrices mucho más grandes si se puede apreciar de mejor esta eficiencia).

2)	Ensamblado matrices llenas (N -- > oo): O(N^3).

    Solución matrices llenas (N -- > oo): O(N^3).

    Ensamblado matrices dispersas (N -- > oo): O(N).

    Solución matrices dispersas (N -- > oo): O(N^3). 

3)	Ensamblado matrices llenas: parte comportándose como una función lineal (O(N)) hasta las matrices de tamaño N = 500, después de este punto pasa a tener una complejidad de O(N^2) hasta las matrices de tamaño N = 8000, pasado este punto presenta una complejidad de O(N^3).

    Solución matrices llenas: parte comportándose como un función lineal (O(N)) hasta las matrices de tamaño N = 250. Pasado este tamaño se adopta una complejidad de O(N^3).

    Ensamblado matrices dispersas: prácticamente toda la función es Constante, sin embargo, en las matrices con un N = 8000 en adelante se aprecia una leve pendiente, por lo que asumo que para matrices de mayor tamaño tendrá una complejidad de O(N).

    Solución matrices dispersas: Hasta las matrices de tamaño N = 4000 se adopta una complejidad O(N), que para tamaños mayores tiende a una complejidad de O(N^3).

4)	Las corridas de las matrices llenas no son estables, al menos para matrices de tamaños menores a N = 1000, posterior a esto, las corridas son prácticamente iguales.

    Por el contrario, las corridas de las matrices dispersas son muy similares de principio a fin.


## Códigos para la creación de matrices Laplacianas
```
# metodo para crear matrices laplacianas de tamaño N que estan llenas
def M_laplaz_llena(N):
    
    matriz=np.eye(N,N,dtype=np.double)*2
    matriz_up=np.eye(N,N,k=1,dtype=np.double)*-1
    matriz_down=np.eye(N,N,k=-1,dtype=np.double)*-1

    return matriz+matriz_up+matriz_down
```

```
# metodo para crear matrices laplacianas de tamaño N que solo tienen valores utiles (matrices dispersas)
def M_laplaz_dispersas(N):# No se si son estrictamente cuadradas
    
    matriz=sparse.eye(N,N,dtype=np.double)*2
    matriz_up=sparse.eye(N,N,k=1,dtype=np.double)*-1
    matriz_down=sparse.eye(N,N,k=-1,dtype=np.double)*-1
    
    return matriz+matriz_up+matriz_down
```
### Elección de código y su repercusión en el desempeño y complejidad algorítmica
El paso de la creación de matrices es el que define que tan eficiente va a ser tu código (para matrices relativamente grandes).

En el caso de la primera función creada, se rellenan todos los “espacios” por así decirlo, incluso los que tienen 0, que en matrices Laplacianas son la mayor parte de los elementos, posteriormente se muchas hacen operaciones que obviamente son 0. Por ejemplo, la multiplicación de matrices.

En el caso de la segunda función creada, **no** se rellenan los espacios con ceros, por lo que para matrices con muchos ceros como las Laplacianas, se ahorra tiempo en **no** rellenar estos espacios. Adicionalmente al no tener “ceros”, no se realizan operaciones innecesarias como multiplicaciones por 0, por lo que la complejidad del código se reduce significativamente.
### Resumen 
Para matrices con gran cantidad de “ceros” y que sean relativamente grandes (N > 8000), conviene utilizar matrices dispersas, pues se logra un mejor desempeño y la complejidad del algoritmo desciende significativamente.

Lo anterior se analizo para matrices Laplacianas, para matrices que no tengan una gran cantidad de “ceros”, el código tiene a ser un poco más ineficiente.

#### Extra
*Además de este README.md voy a subir imágenes del uso de memoria y los procesadores durante la ejecución del programa.*

*Por supuesto también va incluido el código empleado, el cual es solo 1 archivo, el cual te genera 5 archivos de texto por cada gráfico, les agrega datos, los lee y posteriormente grafica los resultados, así todo queda guardado en el mismo sitio.*
