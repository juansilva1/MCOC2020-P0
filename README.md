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
  * L1d: 32 KB
  * L1i: 32 KB
  * L2: 256 KB
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

![mimatmul](https://user-images.githubusercontent.com/69159364/89746444-a44a6300-da87-11ea-8f6c-a9774ccedda5.png)

==> Si se desea graficar un número distinto de corridas, se deben cambiar las lineas 40 y 64, el i < (número de corridas que desees + 1)

1) Los gráficos difieren en que: 
-	Mi gráfico de "Tiempo trascurrido" presenta una menor dispercion inicial en cuanto al tiempo. 
-	Con respecto al grafico de “uso de memoria”, lo único en que difieren ambos gráficos en la línea punteada negra, en la que mi computador posee menor memoria RAM, siendo esta de 12 GB.
2) Estas diferencias se pueden deber a los procesadores de mi computador comienzan a trabajar al mismo tiempo para esta operacion, o sea que la recta formada para cada corrida siempre va a tener pendiente positiva. En el caso del grafico de Felipe al parecer en una de las corridas parten trabajando menos procesadores y luego comienza a funcionar el resto. También se debe a la cantidad de memoria RAM que posea cada computador.
3) El grafico de uso de memoria es lineal pues se obtiene de un cálculo matemático: (número N al cuadrado) * (3 matrices) * (8 bytes). Es por esto que el uso de memoria solo dependerá del tamaño de N, siendo N la cantidad de columnas o de filas (matriz cuadrada). 
Por otro lado el tiempo presenta leves cambios en la pendiente entre matrices de tamaño 2 al 20, a diferencia del codigo anterior ("timing_matmul"), todos los procesadores parten a trabajar desde el comienzo, por lo que la curva obtenida se asemeja mucho más a una recta (lineal).
4) Estoy utilizando la versión 3.7 de python.
5) Estoy utilizando la versión 1.18.1 de numpy.
6) Si, se llegan a utilizar los 8 procesadores pero estos trabajan considerablemente "más relajados" que para el codigo anterior ("matmul"), esto se puede deber a que la operacion empleada para la multiplicacion de matrices no es complicada, pero se tiene que repetir muchas veces (son 3 for anidados, por lo que es realmente ineficiente). adjunto la imagen a continuación.

![Número de procesadores funcionando2(N500)](https://user-images.githubusercontent.com/69159364/89744050-0058bb80-da77-11ea-88dc-10102ab8360f.JPG)
