class Pila():
    def __init__(self):
        self.superior = None
    def hanoi(self, n, origen, auxiliar, destino):
        if n == 1:
            print(f"mover disco de {origen} a {destino}")
            return
        else:
            self.hanoi(n-1, origen, destino, auxiliar)
            print(f"Mueve el disco de la torre", {origen} ,"a la torre",{destino})
            self.hanoi(n-1, auxiliar, origen, destino)

