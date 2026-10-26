from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes

tareas = []
agregar_tarea(tareas, "Estudiar agentes cloud", "Estudio")
agregar_tarea(tareas, "Preparar laboratorio", "Laboratorio")
completar_tarea(tareas, 1)
agregar_tarea(tareas, "Tarea de ejemplo", "Ejemplo")
eliminada = eliminar_tarea(tareas, 3)
print(f'Eliminada: {eliminada["id"]}: {eliminada["titulo"]}')

for tarea in pendientes(tareas):
    print(f'- {tarea["id"]}: {tarea["titulo"]} [{tarea["categoria"]}]')
