import random
import string
class Contrasena:
    def __init__(self, contrasena):
        self.contrasena = contrasena

    def generarContrasena(self):

        minusculas = list(string.ascii_lowercase)  
        mayusculas = list(string.ascii_uppercase)  
        numeros = list(string.digits)  

        caracteres = minusculas + mayusculas + numeros
        contrasena = []
        for i in range(10):
            contrasena.append(random.choice(caracteres))

        self.contrasena = "".join(contrasena)
        return self.contrasena    
        
    def revisarContrasena(self):
        if(len(self.contrasena) >= 10 and any(m.isupper() for m in self.contrasena) and any(m.islower() for m in self.contrasena)) and any(m.isdigit() for m in self.contrasena):
            print("La contraseña es segura")
            
        else:    
            print("La contraseña debe tener minimo 10 caracteres, contener una mayuscula, una minuscula y un numero")  
              
