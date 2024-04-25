from sumaEREW import sumaEREW
from OrdenamientoEREW import merge_sort_pram
from MulMatrices import MatMultCREW
from busquedaEREW import busquedaEREW
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
            # Agrega un 0 al inicio del vector
            vector.insert(0, 0)
            sumaEREW(vector)
            print(f"Resultado: {vector}")
            pass
        elif option == "2":
            # Suma CREW
            pass
        elif option == "3":
            # Busqueda EREW
            vector = defineVector()
            x = int(input("Ingrese el valor a buscar: "))

            busquedaEREW(vector, x)
            print(f"Resultado: {vector}")
            pass
        elif option == "4":
            # Busqueda y Ordenamiento CRCW
            pass
        elif option == "5":
            # Ordenamiento EREW
            arr1 = [1, 8 , 4, 7, 5 , 6, 2, 3]
            merge_sort_pram(arr1,len(arr1))
            arr1.sort()
            print(arr1)
            pass
        elif option == "6":
            # Multiplicacion de Matrices CREW
            matrix1 = defineMatrix(x = 1)
            matrix2 = defineMatrix(x = 2)
            matrixResul = []
            l = len(matrix1)
            print(f"Matriz 1: {matrix1}")
            print(f"Matriz 2: {matrix2}")
            MatMultCREW(matrix1,matrix2,matrixResul,l)
            print("Matriz Resultado:")
            for row in matrixResul:
                print(row)
            
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

def defineMatrix(x):
    matrix = []
    if x == 0:
        n = input("Ingrese el número de filas y columnas de la matriz: ")
        n = int(n)
        m = n
        for i in range(n):
            row = []
            for j in range(m):
                row.append(int(input(f"Ingrese el valor de la posición ({i+1},{j+1}): ")))
            matrix.append(row)
    else:
        print("Matriz por defecto")
        if x == 2:
            matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
                ]
        elif x == 1:
            matrix = [
                [9, 8, 7],
                [6, 5, 4],
                [3, 2, 1]
                ]
    return matrix

if __name__ == "__main__":
    main()