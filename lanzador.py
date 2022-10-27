from clases.torrehanoi import *
from clases.reglasarrus import *
from clases.polinomios import *


def iniciar():
    while True:
        print("========================")
        print("  Bienvenido a los ejercicios")  
        print("========================")
        print("[1] Torre de hanoi ")
        print("[2] regla de sarrows ")
        print("[3] TDA polinomio con linkelist ")
        print("[4] Salir")
        print("========================")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            torre = Pila()
            torre.hanoi(4, "1", "2", "3")
        elif opcion == "2":
            matriz = Matriz([[0,0,0],[0,0,0],[0,0,0]])
            matriz.rellenar()
            matriz.mostrar()
            print(matriz.regladesarrows())
        elif opcion == "3":
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
        elif opcion == "4":
            break
        else:
            print("Opcion incorrecta")
        
iniciar()
                
