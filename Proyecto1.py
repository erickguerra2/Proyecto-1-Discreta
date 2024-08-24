"""
Universidad del Valle de Guatemala
Nombres: Diego Fabián Morales Dávila | Erick Antonio Guerra Illescas
Última versión: 23/08/24

Proyecto 1 Mate Discreta

Proyecto1.py
Version de Python: 3.11.9
"""

#importamos la libreria para validar que el usuario solo ingresara letras de A a Z y numero de 0 a 9
import re

#Función para construir los conjuntos.
def construir_conjunto():
    nombre = input("Introduce el nombre del conjunto: ")
    conjunto = []
    datos = input(f"Introduce los elementos del conjunto {nombre} separados por comas (solo letras A-Z y números 0-9): ")
    datos = datos.lower()
    
    
    if universe(datos):
        for element in datos.split(','):
            element = element.strip()
            if element not in conjunto:  
                conjunto.append(element)
    else:
        print("Uno o más datos no son válidos. Intentelo de nuevo.\n")
    
    return nombre, conjunto


#Conjunto universo (solo letras A-Z y números 0-9) para compararlo con los elementos ingresados.
def universe(datos):
    return re.fullmatch(r'([a-z0-9]+)(,[a-z0-9]+)*', datos) is not None

#Realiza la union de los conjuntos y los muestra.
def union(conjunto1, conjunto2):
    resultado = conjunto1[:]
    for element in conjunto2:
        if element not in resultado:
            resultado.append(element)
    return resultado

#Realiza la interseccion de los conjuntos y lo smuestra.
def interseccion(conjunto1, conjunto2):
    return [element for element in conjunto1 if element in conjunto2]


#Los elementos del primer conjunto que no estén en el segundo.
def diferencia(conjunto1, conjunto2):
    return [element for element in conjunto1 if element not in conjunto2]

#Diferencia simetrica debería devolver los elementos presentes en los conjuntos pero no contenidos en ambos.
def diferencia_simetrica(conjunto1, conjunto2):
    union_r = union(conjunto1, conjunto2)
    inter_r = interseccion(conjunto1, conjunto2)
    return diferencia(union_r, inter_r)


#Complemetno del conjunto elejido.
def complemento(conjunto):
    
    universo = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]  #Especificar el conjunto universo con letras mayusculas según su asignación en ASCII y números enteros de 0 a 9.
    return [element for element in universo if element not in conjunto]


#Elegir el conjunto existente.
def elegir_conjunto(conjuntos):
    print("Conjuntos creados:")

    for nombre in conjuntos:
        print(f"- {nombre}")
    nombre = input("Elige un conjunto: ")
    return nombre if nombre in conjuntos else None


# Menu de Operaciones de conjuntos. 
def menu_operaciones(conjuntos):
    while True:
        print("\nOperaciones disponibles:")
        print("1. Unión")
        print("2. Intersección")
        print("3. Diferencia")
        print("4. Diferencia Simétrica")
        print("5. Complemento")
        print("6. Volver al menú principal")
        
        opcion = input("Elige una operación: ")
        
        if opcion in ['1', '2', '3', '4']:
            nombre1 = elegir_conjunto(conjuntos)
            if nombre1 == None:
                print("Conjunto no encontrado. Pruebe otra vez.")
            else:
                nombre2 = elegir_conjunto(conjuntos)
                if nombre2 == None:
                    print("Conjunto no encontrado. Pruebe otra vez.")

            if nombre1 and nombre2:
                if opcion == '1':
                    resultado = union(conjuntos[nombre1], conjuntos[nombre2])
                    print(f"Unión de {nombre1} y {nombre2}: {resultado}")
                elif opcion == '2':
                    resultado = interseccion(conjuntos[nombre1], conjuntos[nombre2])
                    print(f"Intersección de {nombre1} y {nombre2}: {resultado}")
                elif opcion == '3':
                    resultado = diferencia(conjuntos[nombre1], conjuntos[nombre2])
                    print(f"Diferencia entre {nombre1} y {nombre2}: {resultado}")
                elif opcion == '4':
                    resultado = diferencia_simetrica(conjuntos[nombre1], conjuntos[nombre2])
                    print(f"Diferencia Simétrica entre {nombre1} y {nombre2}: {resultado}")
        elif opcion == '5':
            nombre1 = elegir_conjunto(conjuntos)
            if nombre1:
                resultado = complemento(conjuntos[nombre1])
                print(f"Complemento de {nombre1}: {resultado}")
        elif opcion == '6':
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

#Menu principal de opciones.
def menu_principal():
    conjuntos = {}

    while True:
        print("\nMenú principal:")
        print("1. Construir conjunto")
        print("2. Operar conjunto")
        print("3. Finalizar")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            nombre, conjunto = construir_conjunto()
            conjuntos[nombre] = conjunto
            if conjuntos[nombre]:
                print(f"Conjunto {nombre} construido: {conjunto}")
            
            
        elif opcion == '2':
            if not conjuntos:
                print("Primero debes construir al menos un conjunto.")
            else:
                menu_operaciones(conjuntos)
        elif opcion == '3':
            print("Finalizando programa.")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

#Llamada al menu principal.
menu_principal()