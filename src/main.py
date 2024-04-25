from sumaEREW import sumaEREW
from OrdenamientoEREW import merge_sort_pram
from MulMatrices import MulMatrices
import time
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
            arr1 = defineVector()
            merge_sort_pram(arr1,len(arr1))
            print(arr1)
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
    vector = list(map(int, input("Ingrese los valores del vector separados por espacios: ").split(" ")))
    return vector

def defineMatrix():
    matrix = []
    n = int(input("Ingrese el número de filas y columnas de la matriz: "))
    m = n
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(input(f"Ingrese el valor de la posición ({i+1},{j+1}): ")))
        matrix.append(row)

    return matrix

if __name__ == "__main__":
    main()