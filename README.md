# ProyectoPython_IE0117_2021-II
Proyecto # 1(Python) IE-0117 Buscaminas

## Planes iniciales de alto y bajo nivel:
Ver tambien, [lluvia de ideas](https://docs.google.com/spreadsheets/d/1ExaA3SSjnD2yHSH6oEkQ7PLAEW0kYarp5tVv0T_rSxA/edit#gid=0)

### mine_sweeper_controller.py -> Controlador consume al UI, logica de mas alto nivel
* Solicitar informacion para el juego
* Iniciar el juego con informacion del paso anterior
* Jugar
* cerrar

### mine_swepper_UI (DIR) -> consume al mine_swepper_backend, logica UI (segundo alto nivel):
* Menu: preguntar dimensiones
* Menu: preguntar minas
* Pintar matriz
* Permitir jugar
* Mostrar iconitos
* permitir reiniciar
* Permitir salir

### mine_swepper_backend, logica de juego
* Crear Matriz
* Distribuir minas


### Ultimo avance funcional del proyecto final:
Correr:
```
$ python3 minesweeper_controller.py 
```


Se puede ver el menu que solicita las dimensiones del buscaminas y luego se imprimen en la consola