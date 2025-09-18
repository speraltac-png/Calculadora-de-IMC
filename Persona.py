from Contrasena import Contrasena

class Persona:
    def __init__(self, nombre, edad,  genero, peso, estatura):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.peso = peso
        self.estatura = estatura

    def calcularIMC(self):
        imc = (self.peso / (self.estatura ** 2))*10000
        print(f"El IMC de {self.nombre} es de {imc:.1f}")

    def verificarMayoriaEdad(self):
        if(self.edad >= 18):
            print(f"{self.nombre} es mayor de edad")    
        else:
            print(f"{self.nombre} no es mayor de edad")    

    def mostrarInfo(self):
        print(f"nombre: {self.nombre} \n edad: {self.edad} \n genero: {self.genero} \n peso: {self.peso} \n estatura: {self.estatura}")

def main():
    print("REGISTRARSE")
    nombre = input("NOMBRE: ")
    edad = int(input("EDAD: "))
    genero = input("GENERO (Masculino o Femenino): ")
    peso = int(input("PESO (en kg): "))
    estatura = int(input("ESTATURA (en cm):"))  
    contrasena = Contrasena("")
    contrasenaGenerada = contrasena.generarContrasena()
    print(f" su contraseña es {contrasenaGenerada} no la olvide pues la necesitara luego") 

    persona1 = Persona(nombre,edad, genero, peso, estatura)
    
    
    while True:
        eleccionMenu = int(input("Presione \n\t1: para mostrar su información \n\t2: para calcular su IMC \n\t3: Para salir del programa\n >>>"))
        contrasenaIngresada = input("<<<< INGRESE SU CONTRASEÑA >>>> \n")
        
        if eleccionMenu == 1 and contrasenaIngresada == contrasenaGenerada:
            persona1.mostrarInfo()

        elif eleccionMenu == 2 and contrasenaIngresada == contrasenaGenerada:
            persona1.verificarMayoriaEdad()
            persona1.calcularIMC()

        elif eleccionMenu == 3:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida o contraseña equivocada")

      

if __name__ == "__main__":
    main()    