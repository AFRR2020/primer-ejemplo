import json
import logging

# ==========================================================
# CONFIGURACIÓN DEL LOGGING
# ==========================================================

logging.basicConfig(
    filename="operaciones.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ==========================================================
# CLASE OPERACION
# ==========================================================

class Operacion:

    def __init__(self, nombre, cantidad):
        self.__nombre = nombre
        self.__cantidad = cantidad

    # -------------------------
    # GETTERS
    # -------------------------

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    # -------------------------
    # SETTERS
    # -------------------------

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        self.__cantidad = cantidad


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

operaciones = []

logging.info("Sistema iniciado")


while True:

    print("\n==============================")
    print("1. Registrar operación")
    print("2. Consultar operaciones")
    print("3. Guardar operaciones")
    print("0. Salir")
    print("==============================")

    try:

        opcion = int(input("Seleccione una opción: "))

        # --------------------------------------------------
        # REGISTRAR OPERACIÓN
        # --------------------------------------------------

        if opcion == 1:

            nombre = input("Nombre de la operación: ")
            cantidad = int(input("Cantidad producida: "))

            if cantidad <= 0:
                logging.warning("Se intentó registrar una cantidad inválida")
                raise ValueError("La cantidad debe ser mayor que cero")

            operacion = Operacion(nombre, cantidad)

            operaciones.append(operacion)

            logging.info(
                f"Operación registrada: {nombre} - Cantidad: {cantidad}"
            )

            logging.debug(
                f"Cantidad de operaciones almacenadas: {len(operaciones)}"
            )

            print("Operación registrada correctamente")


        # --------------------------------------------------
        # CONSULTAR OPERACIONES
        # --------------------------------------------------

        elif opcion == 2:

            logging.info("Consulta de operaciones")

            if len(operaciones) == 0:

                logging.warning("No existen operaciones registradas")
                print("No hay operaciones registradas")

            else:

                for operacion in operaciones:

                    print(
                        operacion.get_nombre(),
                        "-",
                        operacion.get_cantidad()
                    )


        # --------------------------------------------------
        # GUARDAR EN JSON
        # --------------------------------------------------

        elif opcion == 3:

            datos = []

            for operacion in operaciones:

                datos.append({
                    "nombre": operacion.get_nombre(),
                    "cantidad": operacion.get_cantidad()
                })

            with open("operaciones.json", "w") as archivo:

                json.dump(datos, archivo, indent=4)

            logging.info("Operaciones guardadas en operaciones.json")

            print("Información guardada correctamente")


        # --------------------------------------------------
        # SALIR
        # --------------------------------------------------

        elif opcion == 0:

            logging.info("Sistema finalizado")
            print("Programa finalizado")

            break

        else:

            logging.warning(f"Opción inválida: {opcion}")
            print("Opción inválida")


    except ValueError as error:

        logging.error(f"Error de entrada: {error}")
        print("Error:", error)

    except Exception as error:

        logging.error(f"Error inesperado: {error}")
        print("Se presentó un error inesperado")