import re

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

def validar_conjunto(entrada):
    patron = r'^[A-Z0-9](,[A-Z0-9])*$'
    return re.match(patron, entrada) is not None

def crear_conjunto(nombre):
    while True:
        elementos = input(f"Ingrese los elementos del conjunto {nombre} separados por comas (A-Z, 0-9): ")
        if validar_conjunto(elementos):
            conjunto = [elemento.strip() for elemento in elementos.split(",")]
            return conjunto
        else:
            print("Entrada inválida. Asegúrese de usar solo letras (A-Z) y números (0-9), separados por comas.")

def union(A, B):
    resultado = A.copy()
    for elemento in B:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def interseccion(A, B):
    return [elemento for elemento in A if elemento in B]

def diferencia(A, B):
    return [elemento for elemento in A if elemento not in B]

def diferencia_simetrica(A, B):
    return union(diferencia(A, B), diferencia(B, A))

def complemento(A, U):
    return [elemento for elemento in U if elemento not in A]

def operar_conjuntos(opcion, A, B, U):
    if opcion == 1:
        print(f"Complemento de A: {complemento(A, U)}")
    elif opcion == 2:
        print(f"Unión: {union(A, B)}")
    elif opcion == 3:
        print(f"Intersección: {interseccion(A, B)}")
    elif opcion == 4:
        print(f"Diferencia A - B: {diferencia(A, B)}")
    elif opcion == 5:
        print(f"Diferencia Simétrica: {diferencia_simetrica(A, B)}")
    else:
        print("Opción no válida.")

def main():
    A, B = [], []
    U = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]  # Universo: A-Z y 0-9
    opcion1 = 0

    while opcion1 != 3:
        mostrar_menu_principal()
        opcion1 = int(input("Seleccione una opción: "))

        match opcion1:
            case 1:
                A = crear_conjunto("A")
                B = crear_conjunto("B")
                print(f"Conjunto A: {A}")
                print(f"Conjunto B: {B}")
                print(f"Conjunto Universo (A-Z y 0-9): {U}")
            case 2:
                operando = True
                while operando:
                    mostrar_menu_operaciones()
                    opcion2 = int(input("Seleccione una operación: "))

                    match opcion2:
                        case 6:
                            operando = False
                        case _:
                            operar_conjuntos(opcion2, A, B, U)
            case 3:
                print("Saliendo del programa.")
            case _:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()