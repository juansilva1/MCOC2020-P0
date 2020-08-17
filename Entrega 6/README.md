# Entrega 6

## Comparación de los distintos métodos para resolver A*x = b

Tras comparar 9 funciones, se obtiene el siguiente gráfico:



Procederé a ser una comparación más en detalle, primero comparando por grupos de 2-3 funciones. Para este análisis se toman en cuenta 10 corridas por función (se utilizan en el promedio), para obtener datos más exactos.

### Grupo inv, npSolve, spSolve;



Para matrices de tamaño N < 100:
-	La función que resuelve el problema de forma más eficiente es “A_invB_npSolve”, mientras que la más ineficiente es “A_invB_spSolve”.

Esto es distinto a lo esperado, pues en entregas anteriores, las funciones que usaban la librería scipy eran las que resultaban ser más eficientes. Lo anterior se puede deber a que para matrices “Pequeñas”, scipy hace más operaciones para resolver este tipo de problemas.
Para matrices de tamaño 100 <= N <= 10000:
-	Pasado este punto, la función “A_invB_spSolve” se comporta de forma similar a la “A_invB_npSolve”, siendo estas 2 las funciones más eficientes para matrices de este tamaño.
-	Pasado este punto la función “A_invB_inv” pasa a ser la más ineficiente. Esto se puede deber a que para esta función se realiza la operación de invertir y multiplicar, por lo que al tener 2 matrices “muy grandes”, estos cálculos se vuelven más lentos.

### Grupo gen:



-	Por lo general las funciones “A_invB_spSolve_gen” y “A_invB_spSolve_gen_overwrite” son muy similares, siendo la que utiliza “overwrite=True” levemente más eficiente.

### Grupo sym:



-	Por lo general las funciones “A_invB_spSolve_sym” y “A_invB_spSolve_sym_overwrite” son muy similares, siendo la que utiliza “overwrite=True” levemente más eficiente.

### Grupo pos:



-	Por lo general las funciones “A_invB_spSolve_pos” y “A_invB_spSolve_pos_overwrite” son muy similares, siendo la que utiliza “overwrite=True” en un principio (N < 10) bastante más eficiente que la otra función, pero para matrices de mayor tamaño se comportan prácticamente iguales.

	Algo que se puede notar de los últimos 3 gráficos es que por lo general utilizar “overwrite=True”, vuelve la función más eficiente pues esto te permite sobrescribir datos.

## Comparación del gráfico final obtenido (9 funciones)
Para este análisis se toman en cuenta 5 corridas por función (se utilizan en el promedio).
-	Para matrices con N < 50 la función “A_invB_npSolve” es la más eficiente. Pasado este punto otras funciones pasan a ser más eficientes.
-	Para matrices con N > 1000 la función más eficiente es “A_invB_spSolve_pos_overwrite”.
