class Familia:
    def __init__(self, edad_juan):
        self.edad_juan = edad_juan
        self.edad_alberto = 0
        self.edad_ana = 0
        self.edad_mama = 0

    def calcular_edades(self):
        self.edad_alberto = 2 * self.edad_juan / 3
        self.edad_ana = 4 * self.edad_juan / 3
        self.edad_mama = self.edad_juan + self.edad_alberto + self.edad_ana

    def mostrar_edades(self):
        print("LAS EDADES SON:")
        print("ALBERTO:", self.edad_alberto)
        print("JUAN:", self.edad_juan)
        print("ANA:", self.edad_ana)
        print("MAMÁ:", self.edad_mama)


edad_juan = float(input("Ingrese la edad de Juan: "))

familia = Familia(edad_juan)
familia.calcular_edades()
familia.mostrar_edades()
