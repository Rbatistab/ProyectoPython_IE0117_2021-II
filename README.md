# ProyectoPython_IE0117_2021-II
Proyecto # 1(Python) IE-0117 Buscaminas

### Integrantes:

* Russell Batista B. 	B00857
* Luis Diego Araya C. B60478

Instrucciones de uso:

Para jugar buscaminas se debe entar al directorio principal, ` ProyectoPython_IE0117_2021-II` y correr:

```
$ python minesweeper_controller.py 
```



Con esto se levanta una ventana que solicita la cantidad de filas y columnas de la matriz del juego, luego otra ventana para elegir la cantidad de minas.

Un vez elegidas estas se muestra el juego, consistente de `n` filas y `m` columnas en las que todos los elementos son casillas ocultas, para hacer visible una casilla debe darle un click izquierdo a la casilla deseada:

* Si es una mina, explotan y pierde el juego
* Si no es una mina se muestra un bloque (de una casilla o mas), en las que cada casilla visible tiene un numero con la cantidad de minas que tiene las casillas inmediatamnte adjacentes (arriba, abajo, izquierda, derecha y diagonales).
* Si una casilla no tiene numero, quiere decir que no tiene minas en las casillas contiguas

Cabe la opcion de poner una marca:

* Una **bandera** para indicar una mina sobre una casilla (no es obligatorio para ganar el juego)
* Un **signo de pregunta** para poner un signo de pregunta (esta es para ayudarse en caso de duda, pero no tiene efecto en el juego)

Para poner una marca se debe marca el ***"check"*** que dice Etiquetar casilla ocula, al darle un click derecho se muestra una **bandera**, con otro click derecho adicional se coloca un **signo de pregunta**, y con uno mas regresa a su estado original sin marca. Esto sucede ciclicamente cada 3 clicks izquierdos.

### ¿Cómo se gana el juego?

Para ganar el usuario debe hacer visibles todas las casillas que no tengan minas y dejar ocultas todas las casillas con minas.

### Características del juego

* Reinicio: hay 2 tipos de reincio, uno suave que genera un nuevo juego con la misma cantidad de filas, columnas y minas que el juego actual, y un reinicio fuerte que consulta nuevamente por dimensiones y minas del juego. El reinicio se puede hacer durante el juego, al haber perdido o al haber ganado.
* Puntajes: Al comenzar el juego con el primer click inicia un contador. Al ganar cabe la posibilidad de guardar una marca personal y un puntaje, y siempre es posible ver los puntajes.
