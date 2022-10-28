
class Matriz():
    
    def __init__(self, matriz):
        self.matriz = matriz
        matriz = [[0,0,0],[0,0,0],[0,0,0]]
    def rellenar(self):
        for i in range(3):
            for j in range(3):
                self.matriz[i][j] = int(input("Ingrese el valor de la matriz: "))
    def mostrar(self):
        print("La matriz es: ")
        for i in range(3):
            for j in range(3):
                print(self.matriz[i][j], end=" ")
            print()
    def regladesarrows(self):
        print(" El determinante de la matriz es: ")
        determinate = self.matriz[0][0] * self.matriz[1][1] * self.matriz[2][2] + self.matriz[0][1] * self.matriz[1][2] * self.matriz[2][0] + self.matriz[0][2] * self.matriz[1][0] * self.matriz[2][1] - self.matriz[0][2] * self.matriz[1][1] * self.matriz[2][0] - self.matriz[0][1] * self.matriz[1][0] * self.matriz[2][2] - self.matriz[0][0] * self.matriz[1][2] * self.matriz[2][1]
        print(determinate)

