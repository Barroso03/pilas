from clases.torrehanoi import *
from clases.reglasarrus import *



if __name__ == '__main__':
   def iniciar():
        print("========================")
        print("  Bienvenido al examen  ")
        print("========================")
        print("[1] Torre de hanoi ")
        print("[2] regla de sarrows ")
        print("[3] Añadir un cliente   ")
        print("[4] Modificar un cliente")
        print("[5] Borrar un cliente   ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("> ")
        while opcion != "0":
            if opcion == "1":
              pila = Pila()
              pila.hanoi(4, "1", "2", "3")
            elif opcion == "2":
              matriz = Matriz([[0,0,0],[0,0,0],[0,0,0]])
              matriz.rellenar()
              matriz.mostrar()
              print(matriz.regladesarrows())
                    
    