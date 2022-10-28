from clases.torrehanoi import *
from clases.reglasarrus import *
from clases.polinomios import *
from clases.starwars import *
import unittest


def iniciar():
    while True:
        print("========================")
        print("  Bienvenido a los ejercicios")  
        print("========================")
        print("[1] Torre de hanoi ")
        print("[2] regla de sarrows ")
        print("[3] TDA polinomio con linkelist ")
        print("[4] Star Wars")
        print("[5] Salir")
        print("========================")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            torre = Pila()
            torre.jugarhanoi()
        elif opcion == "2":
            matriz = Matriz([[0,0,0],[0,0,0],[0,0,0]])
            matriz.rellenar()
            matriz.mostrar()
            matriz.regladesarrows()
            unittest.main()
            
        elif opcion == "3":
            Polinomio1 = Polinomio()
            Polinomio1.agregar(2, 3)
            Polinomio1.agregar(3, 2)
            print("El primer polinomio es: ")
            print(Polinomio1.mostrar())
            Polinomio2 = Polinomio()
            Polinomio2.agregar(1, 2)
            Polinomio2.agregar(1, 1)
            print("El segundo polinomio es: ")
            print(Polinomio2.mostrar())
            resta = Polinomio1.restar(Polinomio2)
            print("La resta de los polinomios es: ")
            print(resta.mostrar())
            division = Polinomio1.division(Polinomio2)
            print("La division de los polinomios es: ")
            division.mostrar()
            print("Eliminamos un termino: ")
            Polinomio1.eliminar(2)
            print(Polinomio1.mostrar())
            print("Verificamos si existe un termino: ")
            print(Polinomio1.existe(3))
        elif opcion == "4":
            
        
            while True:
                print("========================")
                print("  Bienvenido a starwars")  
                print("========================")
                print("[1] Ordenar naves por nombre: ")
                print("[2]Ordenar naves por largo:s ")
                print("[3] Mostrar info de Halcón Milenario y Estrella de la muerte:")
                print("[4] Cinco naves con mas pasajeros")
                print ("[5] Mostrar la nave con mayor tripulación: ")
                print("[6] Mostrar las naves que empiezan por AT: ")
                print("[7] Mostrar las naves que pueden llevar 6 o más pasajeros: ")
                print("[8] Mostrar la nave más pequeña: ")
                print("[9] Mostrar la nave más grande: ")
                print("[10] Salir") 
                print("========================")
                opcion2 = input("Ingrese una opcion: ")
                if opcion2 == "1":
                   ordenr_navesalfabetico()
                    
                elif opcion2 == "2":
                    ordenar_navesporlargo()
                    
                elif opcion2 == "3":
                    mostrarinfo()
                elif opcion2 == "4":
                    cinconavesconmaspasajeros()
                elif opcion2 == "5":
                    navesconmayortripulacion()
                elif opcion2 == "6":
                    navesempiezanporAT()
                elif opcion2 == "7":
                    navesconmasde6pasajeros()
                elif opcion2 == "8":
                    navesmaspequeña()
                elif opcion2 == "9":
                    navesmasgrande()
                elif opcion2 == "10":
                    break
                else:
                    print("Opcion no valida")
                unittest.main()
        elif opcion == "5":
            break
        else:
            print("Opcion incorrecta")
    
        

                
