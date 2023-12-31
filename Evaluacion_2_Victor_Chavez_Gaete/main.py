
import locale


locale.setlocale(locale.LC_ALL, "es_CL")


def agregar_compra(compra, compras):
    # Agrega a la lista compras la nueva compra
    compras.append(compra)

    # mensaje de exito al agregar la compra
    print("Compra agregada correctamente")


def mostrar_compras(compras):
    # Si la lista de compras está vacía, muestra un mensaje indicando el problema
    if not compras:
        print("No hay compras registradas")
        return

    # Recorre la lista de compras y muestra cada compra
    for i, compra in enumerate(compras):


        # Muestra el número y el monto de la compra, le sumamos +1 ya que parte en 0 y al monto de compra lo seteamos para tipo monetario

        print(f"Compra {i + 1}: {locale.currency(compra, grouping=True)}")


def mostrar_total(compras):
    # Si la lista de compras está vacía, muestra un mensaje indicando el problema
    if not compras:
        print("No hay compras registradas")
        return

    # Calcular el total
    total_gastado = 0

    for compra in compras:
        total_gastado += compra

    # seteamos el valor de total total gastado a tipo moneda
    total_gastado = locale.currency(total_gastado, grouping=True)

    # se imprime el total gastado
    print(f"Total gastado: {total_gastado}")


def main():
    # lista vacía de compras
    compras = []
    # variable para total gastado
    total_gastado = 0

    while True:
        # desplegams el menu
        print("")
        print("<<<      MENU       >>>")
        print("")
        print("1.- AGREGAR COMPRA")
        print("2.- MOSTRAR COMPARAS")
        print("3.- MOSTRAR TOTAL GASTADO")
        print("4.- SALIR")

        # Solicitar al usuario el ingreso de una opcion
        opcion = input("Seleccione una accion: ")

        # Opcion 1, Ingreso compra
        if opcion == "1":
            # Solicitar al usuario el monto de la compra
            monto = int(input("Ingrese el monto de compra: "))

            # Agregamos la compra a la lista llamando a la funcion creada
            agregar_compra(monto, compras)

        # Opcion 2, llamamos a la funcion creada para que muestre las copras realizadas
        elif opcion == "2":
            # Muestra las compras
            mostrar_compras(compras)

        # Opcion 3, Llamamos la funcion creada para mostrar el total gastado en formato moneda local (chile)
        elif opcion == "3":
            # Muestra el total gastado
            mostrar_total(compras)

        # Opcion 4, Salir del programa
        elif opcion == "4":

            break

        else:
            # si no es una opcion valida, mostramos el mjs de error
            print("Opción invalida")

if __name__ == "__main__":
    main()
