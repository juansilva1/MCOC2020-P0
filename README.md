# MCOC2020-P0

* Marca/modelo: Aspire A515-52

* Tipo: Notebook

* Año adquisición: 2020

* Procesador:
  * Marca/Modelo: Intel(R) Core(TM) i7-8565U
  * Velocidad Base: 1,8 GHz
  * Velocidad Máxima:1,99 GHz
  * Número de núcleos: 4
  * Número de hilos: 8
  * Arquitectura: x64-based PC
  * Set de instrucciones:MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, EM64T, VT-x, AES, AVX, AVX2, FMA3
* Tamaño de las caches del procesador
  * L1: 256 KB
  * L2: 1,0 MB (lo modifiqué el día 12-08-2020)
  * L3: 8,0 MB
* Memoria
  * Total:12 GB (RAM)
  * Tipo memoria: DDR4
  * Velocidad: 2400 MHz
  * Número de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: Intel(R) UDH Graphics 620
  * Memoria total aprox: 6197 MB
  * Memoria pantalla (VRAM): 128 MB
  * Memoria Compartida: 6069 MB
  * Resolución: 1366 x 768
* Disco 1:
  * Marca/Modelo:WDC PC SN520 SDAPNUW-512G-1014
  * Tipo: SSD
  * Tamaño: 512 GB
  * Particiones: 4
  * Sistema de archivos: NTFS
* Dirección MAC de la targeta wifi: 3C-91-80-93-F3-E5
* Dirección IP (Interna, del router): 192.168.0.7
* Dirección IP (Externa, del ISP):190.161.70.243
* Proveedor interner: VTR Doble Pack
# Desempeño MATMUL

![Gráfico](https://user-images.githubusercontent.com/69159364/89664038-883a9c00-d8a4-11ea-9ddd-a736d8162ebf.JPG)

==> Si se desea graficar un número distinto de corridas, se deben cambiar las lineas 37 y 61, el i < (número de corridas que desees + 1)

1) Los gráficos difieren en que: 
-	El del profesor presenta una “cresta” en el intervalo N perteneciente [50,100], mientras que en mi gráfico esa cresta se forma en el intervalo N perteneciente [20,50]. 
-	En el grafico del profesor, con matrices mayores a N = 50 se demora mas de 0.1 ms, mientras que eso a mi me ocurre con matrices mayores a N = 100.
-	Con matrices de N = 10000 el grafico del profesor se completa antes que mi gráfico.
-	Con respecto al grafico de “uso de memoria”, lo único en que difieren ambos gráficos en la línea punteada negra, en la que mi computador posee menor memoria RAM, siendo esta de 12 GB.
2) Estas diferencias se pueden deber a los procesadores de cada computador, cuanto se demoran en funcionar en conjunto (por eso existen “crestas”, pues pasada esta cresta otros procesadores comienzan a trabajar, para agilizar el proceso y/o los cálculos). También se debe a la cantidad de memoria RAM que posea cada computador.
3) El grafico de uso de memoria es lineal pues se obtiene de un cálculo matemático: (número N al cuadrado) * (3 matrices) * (8 bytes). Es por esto que el uso de memoria solo dependerá del tamaño de N, siendo N la cantidad de columnas o de filas (matriz cuadrada). 
Por otro lado el tiempo no es lineal, esto ocurre por que al principio de la ejecución el computador comienza a utilizar un numero de procesadores (generalmente menor a N), por lo que realiza los cálculos que puede hasta que empieza a ponerse más “lento”, luego de esto se comienzan a utilizar más procesadores, con lo cual el tiempo vuelve a disminuir, finalmente cuando están trabajando todos los procesadores, la grafica se comienza a comportar de una forma más lineal.
4) Estoy utilizando la versión 3.7 de python.
5) Estoy utilizando la versión 1.18.1 de numpy.
6) Si, se llegan a utilizar los 8 procesadores, adjunto la imagen a continuación.

![Número de procesadores funcionando](https://user-images.githubusercontent.com/69159364/89663772-0ea2ae00-d8a4-11ea-8499-d0a960805093.JPG)

# Desempeño MIMATMUL

![mimatmul](https://user-images.githubusercontent.com/69159364/89794586-40f71a00-daf5-11ea-9f06-434e3c237762.png)

==> Si se desea graficar un número distinto de corridas, se deben cambiar las lineas 40 y 64, el i < (número de corridas que desees + 1).

==> Para este gráfico posee un N = 1000 pues se demora demasido (entre 20-40 para N = 1000).

1) Los gráficos (de esta ves) difieren en que: 
-	Mi gráfico de "Tiempo trascurrido" presenta una menor dispercion inicial en cuanto al tiempo. 
-	Con respecto al grafico de “uso de memoria”, lo único en que difieren ambos gráficos en la línea punteada negra, en la que mi computador posee menor memoria RAM, siendo esta de 12 GB.
2) Estas diferencias se pueden deber a los procesadores de mi computador comienzan a trabajar al mismo tiempo para esta operacion, o sea que la recta formada para cada corrida siempre va a tener pendiente positiva. En el caso del grafico de Felipe al parecer en una de las corridas parten trabajando menos procesadores y luego comienza a funcionar el resto. También se debe a la cantidad de memoria RAM que posea cada computador.
3) El grafico de uso de memoria es lineal pues se obtiene de un cálculo matemático: (número N al cuadrado) * (3 matrices) * (8 bytes). Es por esto que el uso de memoria solo dependerá del tamaño de N, siendo N la cantidad de columnas o de filas (matriz cuadrada). 
Por otro lado el tiempo presenta leves cambios en la pendiente entre matrices de tamaño 2 al 20, a diferencia del codigo anterior ("timing_matmul"), todos los procesadores parten a trabajar desde el comienzo, por lo que la curva obtenida se asemeja mucho más a una recta (lineal).
4) Estoy utilizando la versión 3.7 de python.
5) Estoy utilizando la versión 1.18.1 de numpy.
6) Si, se llegan a utilizar los 8 procesadores pero estos trabajan considerablemente "más relajados" que para el codigo anterior ("matmul"), esto se puede deber a que la operacion empleada para la multiplicacion de matrices no es complicada, pero se tiene que repetir muchas veces (son 3 for anidados, por lo que es realmente ineficiente). adjunto la imagen a continuación.

![Número de procesadores funcionando2(N500)](https://user-images.githubusercontent.com/69159364/89744050-0058bb80-da77-11ea-88dc-10102ab8360f.JPG)

Diferencia con respecto a los graficos de la entrega 2 y la 3:
- los graficos de la entrega 2 ocupan programacion de bajo nivel (numpy), por lo que se obtienen varias veces más rapidas que los graficos de la entrega 3, los cuales se hacen en python, por lo que se ocupa programacion de alto nivel siendo así un proceso mucho más lento.

# Entrega4

En mi Sistema no se alcanza a notar un cambio significativo al momento de utilizar “overwrite_a=True” de “scipy.linalg.inv”. (al menos hasta el N =2000)
Los tamaños en memoria para cada uno de estos tipos de datos en Python para mi sistema son de:
-	np.half = 2 bytes.
-	np.single = 4 bytes.
-	np.double = 8 bytes.
-	np.longdouble = 8 bytes.
==> Se puede apreciar que np.double es de un tipo muy similar a np.longdouble, por lo que se mostraran solo 9 programas (se considerara el caso de double=longdouble esta decisión la tome por que el profesor me dijo que graficara 9 gráficos en vez de 12).
## Comparación en cuanto tipo de datos:
Al ver los gráficos y teniendo en cuenta lo anterior el uso de memoria sigue siendo lineal para los distintos tipos de datos.

En cuanto al uso de memoria, los programas que utilizan datos del tipo “np.half” emplean menos memoria, seguidos de los que tienen datos del tipo “np.single” por ultimo los que más utilizan memoria son los programas que utilizan datos de tipo “np.double” y “np.longdouble”.

En cuanto al tiempo transcurrido los datos de tipo “np.double” son en algunos casos (caso 1, “numpy.linalg.inv”) levemente mayores que los datos de tipo “np.single” y “np.half” y en los casos 2 y 3 ya se puede apreciar una diferencia más significativa (“np.double”>” np.single” y “np.single”).

## Comparación en cuanto tipo de función empleada:
Para mi sistema y la versión de Python que estoy utilizando, la función que se desempeña de mejor forma para matrices de “grandes dimensiones” es la función “scipy.linalg.inv”.

Nota: para los cálculos del uso de memoria se consideran 2 matrices. Este número se obtuvo a través de la división de la cantidad de memoria empleada para invertir una matriz de N = 10000 y la memoria teórica.

La cantidad de memoria se puede ver en “administrador de tareas” > “procesos” > se busca la ventana de Python que más utilice memoria mientras se ejecuta el programa (sin considerar la creación de gráficos, pues estos añaden mucho uso de memoria).

El resultado de esta división es muy probable que sea con decimales, ósea es muy difícil obtener un numero entero, por lo que se aproxima para abajo. A continuación menciono el número de matrices necesarias para invertir una matriz con funciones distintas:

- numpy.linalg.inv => 4 matrices
- scipy.linalg.inv con overwrite=False => 2 matrices
- scipy.linalg.inv con overwrite=True => 2 matrices

1)	Con lo anterior asumo que “scipy.linalg.inv” calcula la inversa mediante la adjunción (método de Cholesky)
Mientras que “numpy.linalg.inv” utiliza descomposición de valores singulares (A = UΣVT)

2)	Consideraciones: tengo 

-	Caché L1: 256 kB
-	Caché L2: 1,0 MB
-	Caché L3: 8,0 MB
-	 RAM: 12 GB
-	Disco SSD: 512 GB

Mientras más arriba se encuentre en la lista, mayor será su capacidad de procesamiento de datos (aproximadamente cada vez que uno baja un nivel, se vuelve 10 veces más lento).

Esto me dice que los primeros cálculos de las matrices se hacen de forma casi inmediata para memorias menores a los 9.256 MB pues estas son las memorias más rápidas, mientras que, si la matriz presenta un N tan grande que es capaz de superar los 12 GB de RAM, esto hará que todos los cálculos sean extremadamente lentos, pues estamos hablando de que los cálculos se ralentizaron por 10^-4.

Tomando en cuanta lo anterior. Los datos que “pesen” más serán los que correrán el riesgo de pasar sobre los 12 GB de RAM, por esto mismo y para acelerar los cálculos emplee un N_max = 2000. Con esto los cálculos se llevan a cabo de forma rápida y sin ocupar un exceso de memoria.

EL paralelismo funciona en llenar los almacenadores de memoria, primero se van llenando los más rapidos (caché) y luego los más lentos, es por esto que si se entrega un tipo de dato mas "pesado" como lo es el np.double, este sera más lento que otros datos, pues ocupa más memoria, el cual si se pasa de la memoria RAM, se vuelve lentisimo.

## 9 Gráficos (en canvas no queda claro si es necesario subirlos)

### numpy.linalg.inv

![numpy_half](https://user-images.githubusercontent.com/69159364/90074710-c59a9180-dcc9-11ea-8868-4a2d507c731c.png)

![numpy_single](https://user-images.githubusercontent.com/69159364/90074726-cdf2cc80-dcc9-11ea-93d4-00c427fd6459.png)

![numpy_double](https://user-images.githubusercontent.com/69159364/90074743-d814cb00-dcc9-11ea-81b8-c58937dc2610.png)

### scipy.linalg.inv con overwrite_a=False

![scipy_false_half](https://user-images.githubusercontent.com/69159364/90074765-e4008d00-dcc9-11ea-9c90-90acc577dd19.png)

![scipy_false_single](https://user-images.githubusercontent.com/69159364/90074784-ebc03180-dcc9-11ea-8704-abd6f3ab8ff6.png)

![scipy_false_double](https://user-images.githubusercontent.com/69159364/90074808-f7135d00-dcc9-11ea-98c2-5853452fac35.png)

### scipy.linalg.inv con overwrite_a=True

![scipy_true_half](https://user-images.githubusercontent.com/69159364/90074862-10b4a480-dcca-11ea-862b-c5c8c16145be.png)

![scipy_true_single](https://user-images.githubusercontent.com/69159364/90074881-1a3e0c80-dcca-11ea-80b6-34229ddafcef.png)

![scipy_true_double](https://user-images.githubusercontent.com/69159364/90074900-275afb80-dcca-11ea-9b52-ca3fb0063a92.png)

## 3 Gráficos de los Procesadores (en canvas no queda claro si es necesario subirlos)

### Procesadores datos tipo np.half (casos 1-2-3 ordenados de izquierda a derecha)

![Procesadores half casos 1-2-3](https://user-images.githubusercontent.com/69159364/90075633-e4018c80-dccb-11ea-8dd2-74f1cfaa4344.JPG)

### Procesadores datos tipo np.single (casos 1-2-3 ordenados de izquierda a derecha)

![Procesadores single casos 1-2-3](https://user-images.githubusercontent.com/69159364/90075704-085d6900-dccc-11ea-8a28-bcc7aec2ebb0.JPG)

### Procesadores datos tipo np.double (casos 1-2-3 ordenados de izquierda a derecha)

![Procesadores double casos 1-2-3](https://user-images.githubusercontent.com/69159364/90075714-0b585980-dccc-11ea-9a5e-25a4332ebf61.JPG)

Se puede apreciar en los gráficos anteriores:
- los casos 1 (utilizando numpy.linalg.inv) ocupan menos CPU que los otros 2 casos.
- el caso 2 (utilizando scipy.linalg.inv con overwrite_a=False) ocupa el mayor porcentaje de CPU.

# Entrega 5

![Grafico Ax_b 2 funciones](https://user-images.githubusercontent.com/69159364/90295969-48515700-de58-11ea-8c20-3527f447a637.png)

Por lo general la funcion A_invB_npSolve.txt es más eficiente que A_invB_inv.

# Entrega 7

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
### Elección del código y su repercusión en el desempeño y complejidad algorítmica
El paso de la creación de matrices es el que define que tan eficiente va a ser tu código (para matrices relativamente grandes).

En el caso de la primera función creada, se rellenan todos los “espacios” por así decirlo, incluso los que tienen 0, que en matrices Laplacianas son la mayor parte de los elementos, posteriormente se muchas hacen operaciones que obviamente son 0. Por ejemplo, la multiplicación de matrices.

En el caso de la segunda función creada, **no** se rellenan los espacios con ceros, por lo que para matrices con muchos ceros como las Laplacianas, se ahorra tiempo en **no** rellenar estos espacios. Adicionalmente al no tener “ceros”, no se realizan operaciones innecesarias como multiplicaciones por 0, por lo que la complejidad del código se reduce significativamente.
### Resumen 
Para matrices con gran cantidad de “ceros” y que sean relativamente grandes (N > 8000), conviene utilizar matrices dispersas, pues se logra un mejor desempeño y la complejidad del algoritmo desciende significativamente.

Lo anterior se analizo para matrices Laplacianas, para matrices que no tengan una gran cantidad de “ceros”, el código tiene a ser un poco más ineficiente.

#### Extra
*Además de este README.md voy a subir imágenes del uso de memoria y los procesadores durante la ejecución del programa.*

*Por supuesto también va incluido el código empleado, el cual es solo 1 archivo, el cual te genera 5 archivos de texto por cada gráfico, les agrega datos, los lee y posteriormente grafica los resultados, así todo queda guardado en el mismo sitio.*

