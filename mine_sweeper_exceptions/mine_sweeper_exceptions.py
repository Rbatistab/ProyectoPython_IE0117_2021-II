class TerminateMineSweeper(Exception):
    pass

# Necesitamos un exception para el reset:
# El manejo del programa se hace desde el controlador, este consume el UI,
# pero cuando un usuario toca un boton de reset
# el boton lo toca en el UI y este no tiene acceso al controlador. Para hacer
# un reset (full o soft) necesitamos una
# exception que ordene el reset
