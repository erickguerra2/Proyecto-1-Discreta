def mostrar_menu_principal():
    print("\nMenú Principal")
    print("1. Crear conjuntos")
    print("2. Operar conjuntos")
    print("3. Salir")

def mostrar_menu_operaciones():
    print("\nOperaciones con conjuntos")
    print("1. Complemento")
    print("2. Unión")
    print("3. Intersección")
    print("4. Diferencia")
    print("5. Diferencia Simétrica")
    print("6. Regresar al menú principal")

def crear_conjunto(nombre):
    elementos = input(f"Ingrese los elementos del conjunto separados por comas: ")
    return conjunto

def operar_conjuntos(opcion, A, B):
    if opcion == 1:
        print(f"Complemento de")
    elif opcion == 2:
        print(f"Unión: ")
    elif opcion == 3:
        print(f"Intersección: ")
    elif opcion == 4:
        print(f"Diferencia: ")
    elif opcion == 5:
        print(f"Diferencia Simétrica: ")
    else:
        print("Opción no válida.")

def main():
    A, B = set(), set()
    opcion1 = 0
    opcion2 = 0

    while opcion1 != 3:
        mostrar_menu_principal()
        opcion_principal = int(input("Seleccione una opción: "))

        match opcion1:
            case 1:
                A = crear_conjunto("A")
                B = crear_conjunto("B")
                print(f"Conjunto A: {A}")
                print(f"Conjunto B: {B}")
            case 2:
                operando = True
                while operando:
                    mostrar_menu_operaciones()
                    opcion_operacion = int(input("Seleccione una operación: "))

                    match opcion2:
                        case 6:
                            operando = False
                        case _:
                            operar_conjuntos(opcion2, A, B)
            case 3:
                print("Saliendo del programa.")
            case _:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()