import unittest
from tasks import agregar_tarea, completar_tarea, pendientes


class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", "  Estudio  ")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertEqual(tarea["categoria"], "Estudio")
        self.assertFalse(tarea["completada"])

    def test_categoria_vacia(self):
        for vacia in ("", "   "):
            with self.assertRaises(ValueError):
                agregar_tarea([], "Tarea", vacia)

    def test_filtrar_por_categoria(self):
        tareas = []
        agregar_tarea(tareas, "A", "Estudio")
        agregar_tarea(tareas, "B", "Casa")
        agregar_tarea(tareas, "C", "estudio")
        completar_tarea(tareas, 3)
        self.assertEqual(len(pendientes(tareas)), 2)
        self.assertEqual([t["id"] for t in pendientes(tareas, "ESTUDIO")], [1])
        self.assertEqual(pendientes(tareas, "Inexistente"), [])

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Estudio")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])


if __name__ == "__main__":
    unittest.main()
