vehiculos = []

def validar_modelo(modelo):
    return len(modelo.strip()) > 0


def validar_año(año_str):
    try:
        año = int(año_str)
        return año > 1900
    except ValueError:
        return False


def validar_precio(precio_str):
    try:
        precio = float(precio_str)
        return precio > 0
    except ValueError:
        return False

def agregar_vehiculo(lista):
    print("\n--- Agregar vehículo ---")

    modelo = input("Modelo: ")
    if not validar_modelo(modelo):
        print("Error: el modelo no puede estar vacío.")
        return

    anio_str = input("Año: ")
    if not validar_año(anio_str):
        print("Error: el año debe ser un número entero mayor que 1900.")
        return

    precio_str = input("Precio: ")
    if not validar_precio(precio_str):
        print("Error: el precio debe ser un número mayor que cero.")
        return

    vehiculo = {
        "modelo": modelo.strip(),
        "anio": int(anio_str),
        "precio": float(precio_str),
        "disponible": False
    }
    lista.append(vehiculo)
    print(f"Vehículo '{modelo.strip()}' registrado correctamente.")

def buscar_vehiculo(lista, modelo):
    for i in range(len(lista)):
        if lista[i]["modelo"] == modelo:
            return i
    return -1

def eliminar_vehiculo(lista):
    print("\n--- Eliminar vehículo ---")
    modelo = input("Modelo a eliminar: ")
    posicion = buscar_vehiculo(lista, modelo)

    if posicion != -1:
        lista.pop(posicion)
        print(f"Vehículo '{modelo}' eliminado correctamente.")
    else:
        print(f"El vehículo '{modelo}' no se encuentra registrado.")

def actualizar_disponibilidad(lista):
    for vehiculo in lista:
        if vehiculo["anio"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False

def mostrar_vehiculos(lista):
    actualizar_disponibilidad(lista)

    if len(lista) == 0:
        print("\nNo hay vehículos registrados.")
        return

    print("\n=== LISTA DE VEHICULOS ===\n")
    for vehiculo in lista:
        estado = "DISPONIBLE" if vehiculo["disponible"] else "NO DISPONIBLE"
        print(f"Modelo: {vehiculo['modelo']}")
        print(f"Año: {vehiculo['anio']}")
        print(f"Precio: {vehiculo['precio']}")
        print(f"Estado: {estado}")
        print("*" * 45)

try:
    while True:
        print("\n===== M E N U  P R I N C I P A L ===== \n   1. Agregar vehiculo \n   2. Buscar vehiculo \n   3. Eliminar vehiculo \n   4. Actualizar disponibilidad \n   5. Mostrar vehiculos \n   6. Salir")
        opcion = int(input("\n   (1-6) : "))

        if opcion == 6:
            print("\nGracias por usar el sistema. \nVuelva pronto")

        elif opcion in [1, 2, 3, 4, 5]:
            if opcion == 1:
                agregar_vehiculo(vehiculos)

            elif opcion == 2:
                print("Buscar vehiculo")
                descripcion = input("Modelo a buscar: ")
                posicion = buscar_vehiculo(vehiculos, descripcion)
                if posicion != -1:
                    v = vehiculos[posicion]
                    print(f"Vehiculo encontrado en posicion {posicion}")
                    print(f"Modelo: {v['modelo']}")
                    print(f"Año : {v['año']}")
                    print(f"Precio : {v['precio']}")
                    print(f"Disponible: {v['disponible']}")
                else:
                    print(f"El vehiculo '{descripcion}' no se encuentra registrado.")

            elif opcion == 3:
                eliminar_vehiculo(vehiculos)

            elif opcion == 4:
                actualizar_disponibilidad(vehiculos)

            else:
                mostrar_vehiculos(vehiculos)

except ValueError:
    print("\nError: El valor que usted ingreso no concuerda con el tipo requerido.")