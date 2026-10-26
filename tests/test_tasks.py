import unittest
from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes


class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertFalse(tarea["completada"])

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_eliminar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Uno")
        agregar_tarea(tareas, "Dos")
        eliminada = eliminar_tarea(tareas, 2)
        self.assertEqual(eliminada["titulo"], "Dos")
        self.assertEqual([t["id"] for t in tareas], [1])

    def test_eliminar_tarea_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Uno")
        with self.assertRaises(ValueError) as ctx:
            eliminar_tarea(tareas, 99)
        self.assertEqual(str(ctx.exception), "Tarea no encontrada")
        self.assertEqual(len(tareas), 1)

    def test_eliminar_conserva_otras_tareas(self):
        tareas = []
        for titulo in ("Uno", "Dos", "Tres"):
            agregar_tarea(tareas, titulo)
        completar_tarea(tareas, 3)
        eliminar_tarea(tareas, 2)
        self.assertEqual(
            tareas,
            [
                {"id": 1, "titulo": "Uno", "completada": False},
                {"id": 3, "titulo": "Tres", "completada": True},
            ],
        )


if __name__ == "__main__":
    unittest.main()
