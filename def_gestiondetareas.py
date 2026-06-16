# ============================================================
#   SISTEMA DE GESTIÓN DE TAREAS PENDIENTES
# ============================================================

tareas = []


# ── MENÚ ────────────────────────────────────────────────────

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar tarea")
    print("2. Buscar tarea")
    print("3. Eliminar tarea")
    print("4. Actualizar estado")
    print("5. Mostrar tareas")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    try:
        opcion = int(input("Elige una opción: "))
        return opcion
    except ValueError:
        return -1


# ── VALIDACIONES ─────────────────────────────────────────────

def validar_descripcion(descripcion):
    return len(descripcion.strip()) > 0


def validar_prioridad(prioridad_str):
    try:
        prioridad = int(prioridad_str)
        return 1 <= prioridad <= 10
    except ValueError:
        return False


def validar_tiempo(tiempo_str):
    try:
        tiempo = float(tiempo_str)
        return tiempo > 0
    except ValueError:
        return False


# ── OPCIÓN 1: AGREGAR ────────────────────────────────────────

def agregar_tarea(lista):
    print("\n--- Agregar tarea ---")

    descripcion = input("Descripción: ")
    if not validar_descripcion(descripcion):
        print("Error: la descripción no puede estar vacía.")
        return

    prioridad_str = input("Prioridad (1-10): ")
    if not validar_prioridad(prioridad_str):
        print("Error: la prioridad debe ser un número entero entre 1 y 10.")
        return

    tiempo_str = input("Tiempo estimado (horas): ")
    if not validar_tiempo(tiempo_str):
        print("Error: el tiempo estimado debe ser un número mayor que cero.")
        return

    tarea = {
        "descripcion": descripcion.strip(),
        "prioridad": int(prioridad_str),
        "tiempo_estimado": float(tiempo_str),
        "completada": False
    }
    lista.append(tarea)
    print(f"Tarea '{descripcion.strip()}' registrada correctamente.")


# ── OPCIÓN 2: BUSCAR ─────────────────────────────────────────

def buscar_tarea(lista, descripcion):
    for i in range(len(lista)):
        if lista[i]["descripcion"] == descripcion:
            return i
    return -1


# ── OPCIÓN 3: ELIMINAR ───────────────────────────────────────

def eliminar_tarea(lista):
    print("\n--- Eliminar tarea ---")
    descripcion = input("Descripción a eliminar: ")
    posicion = buscar_tarea(lista, descripcion)

    if posicion != -1:
        lista.pop(posicion)
        print(f"Tarea '{descripcion}' eliminada correctamente.")
    else:
        print(f"La tarea '{descripcion}' no se encuentra registrada.")


# ── OPCIÓN 4: ACTUALIZAR ESTADO ──────────────────────────────

def actualizar_estado(lista):
    for tarea in lista:
        if tarea["prioridad"] >= 5:
            tarea["completada"] = True
        else:
            tarea["completada"] = False


# ── OPCIÓN 5: MOSTRAR ────────────────────────────────────────

def mostrar_tareas(lista):
    actualizar_estado(lista)

    if len(lista) == 0:
        print("\nNo hay tareas registradas.")
        return

    print("\n=== LISTA DE TAREAS ===\n")
    for tarea in lista:
        estado = "COMPLETADA" if tarea["completada"] else "PENDIENTE"
        print(f"Descripción: {tarea['descripcion']}")
        print(f"Prioridad: {tarea['prioridad']}")
        print(f"Tiempo estimado: {tarea['tiempo_estimado']}")
        print(f"Estado: {estado}")
        print("*" * 45)


# ── PROGRAMA PRINCIPAL ───────────────────────────────────────

def main():
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_tarea(tareas)
        elif opcion == 2:
            print("\n--- Buscar tarea ---")
            descripcion = input("Descripción a buscar: ")
            posicion = buscar_tarea(tareas, descripcion)
            if posicion != -1:
                t = tareas[posicion]
                print(f"\nTarea encontrada en posición {posicion}:")
                print(f"  Descripción    : {t['descripcion']}")
                print(f"  Prioridad      : {t['prioridad']}")
                print(f"  Tiempo estimado: {t['tiempo_estimado']}")
                print(f"  Completada     : {t['completada']}")
            else:
                print(f"La tarea '{descripcion}' no se encuentra registrada.")
        elif opcion == 3:
            eliminar_tarea(tareas)
        elif opcion == 4:
            actualizar_estado(tareas)
            print("Estado de tareas actualizado correctamente.")
        elif opcion == 5:
            mostrar_tareas(tareas)
        elif opcion == 6:
            print("\nGracias por usar el sistema. Vuelva Pronto")
            break
        else:
            print("Opción no válida. Elige un número del 1 al 6.")


main()