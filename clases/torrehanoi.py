

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class Pila:
    def __init__(self):
        self.superior = None

    def hanoi(self, n, origen, auxiliar, destino):
        if n == 1:
            print(f"Mover disco de {origen} a {destino}")
            return
        else:
            self.hanoi(n-1, origen, destino, auxiliar)
            print(f"Mover disco de {origen} a {destino}")
            self.hanoi(n-1, auxiliar, origen, destino)
    def jugarhanoi(self):
        n = int(input("Ingrese el numero de discos: "))
        self.hanoi(n, "1", "2", "3")
            

       

    def imprimir(self):
        print("Imprimiendo pila:")
        # Recorrer la pila e imprimir valores
        nodo_temporal = self.superior
        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}", end=",")
            nodo_temporal = nodo_temporal.siguiente
        print("")
