from clases.torrehanoi import *
from clases.reglasarrus import *
from clases.polinomios import *


def iniciar():
        print("========================")
        print("  Bienvenido al examen  ")
        print("========================")
        print("[1] Torre de hanoi ")
        print("[2] regla de sarrows ")
        print("[3] Añadir un cliente   ")
        print("[4] TDA polinomio con linkelist")
        print("[5] Borrar un cliente   ")
        print("========================")

        opcion = input("> ")
        while opcion != "0":
            if opcion == "1":
                pila= Pila()
                pila.hanoi(3, "A", "B", "C")
            elif opcion == "2":
              matriz = Matriz([[0,0,0],[0,0,0],[0,0,0]])
              matriz.rellenar()
              matriz.mostrar()
              matriz.regladesarrows()
              print(matriz.regladesarrows())
            elif opcion == "4":
               x = Polinomio()
               x.agregar(2, 3)
               x.agregar(3, 2)
               y = Polinomio()
               y.agregar(1, 2)
               y.agregar(5, 1)
               print("x = ", end="")
               x.mostrar()
               print("y = ", end="")
               y.mostrar()
               z = x.suma(y)
               print ("Suma polinomica:")
               z.mostrar()
               print ("Multiplicacion polinomica:")
               g = x.multiplicacion(y)
               g.mostrar()
iniciar()
                
