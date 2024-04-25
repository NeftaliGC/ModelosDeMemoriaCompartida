from sumaEREW import sumaEREW
from OrdenamientoEREW import merge_sort_pram
def main():
    print("---------------Modelos de memoria compartida---------------")

    while True:
        print("\nSeleccione una opción:")
        print("1. Suma EREW (Vector)")
        print("2. Suma CREW (Vector)")
        print("3. Busqueda EREW (Vector)")
        print("4. Busqueda y Ordenamiento CRCW (Vector)")
        print("5. Ordenamiento EREW (Vector)")
        print("6. Multiplicacion de Matrices CREW")
        print("7. Salir")

        option = input("Opción: ")

        if option == "1":
            # Suma EREW
            vector = defineVector()
            sumaEREW(vector)
            print(f"Resultado: {vector}")
            pass
        elif option == "2":
            # Suma CREW
            pass
        elif option == "3":
            # Busqueda EREW
            pass
        elif option == "4":
            # Busqueda y Ordenamiento CRCW
            pass
        elif option == "5":
            # Ordenamiento EREW
            arr1 = defineVector();
            merge_sort_pram(arr1,len(arr1))
            pass
        elif option == "6":
            # Multiplicacion de Matrices CREW
            pass
        elif option == "7":
            print("Saliendo...")
            break
        else:
            print("Opción no válida")
        
        print("\n")
    

def defineVector():
    vector = []
    n = int(input("Ingrese el tamaño del vector: "))
    for i in range(n):
        vector.append(int(input(f"Ingrese el valor del elemento {i+1}: ")))

    return vector

def defineMatrix():
    matrix = []
    n = int(input("Ingrese el número de filas de la matriz: "))
    m = int(input("Ingrese el número de columnas de la matriz: "))
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(input(f"Ingrese el valor de la posición ({i+1},{j+1}): ")))
        matrix.append(row)

    return matrix

if __name__ == "__main__":
    main()