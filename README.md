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

