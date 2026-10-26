import unittest
from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes


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

    def test_filtrar_categoria_inexistente_devuelve_lista_vacia(self):
        tareas = []
        agregar_tarea(tareas, "A", "Estudio")
        self.assertEqual(pendientes(tareas, "Trabajo"), [])

    def test_filtrar_ignora_espacios_alrededor_de_la_categoria(self):
        tareas = []
        agregar_tarea(tareas, "A", "Estudio")
        self.assertEqual(len(pendientes(tareas, "  estudio  ")), 1)

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Estudio")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_eliminar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Uno", "Estudio")
        agregar_tarea(tareas, "Dos", "Estudio")
        eliminada = eliminar_tarea(tareas, 2)
        self.assertEqual(eliminada["titulo"], "Dos")
        self.assertEqual([t["id"] for t in tareas], [1])

    def test_eliminar_tarea_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Uno", "Estudio")
        with self.assertRaises(ValueError) as ctx:
            eliminar_tarea(tareas, 99)
        self.assertEqual(str(ctx.exception), "Tarea no encontrada")
        self.assertEqual(len(tareas), 1)

    def test_eliminar_conserva_otras_tareas(self):
        tareas = []
        for titulo in ("Uno", "Dos", "Tres"):
            agregar_tarea(tareas, titulo, "Estudio")
        completar_tarea(tareas, 3)
        eliminar_tarea(tareas, 2)
        self.assertEqual(
            tareas,
            [
                {"id": 1, "titulo": "Uno", "categoria": "Estudio", "completada": False},
                {"id": 3, "titulo": "Tres", "categoria": "Estudio", "completada": True},
            ],
        )


if __name__ == "__main__":
    unittest.main()
