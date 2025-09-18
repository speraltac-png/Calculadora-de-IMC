# 🧑‍💻 Sistema de Registro de Persona con Generación de Contraseña e IMC

Este proyecto en Python permite registrar a una persona, generar automáticamente una contraseña segura y realizar diferentes operaciones como mostrar información personal, verificar si es mayor de edad y calcular el **Índice de Masa Corporal (IMC)**.

---

## ✨ Funcionalidades

1. **Registro de usuario**  
   - Nombre  
   - Edad  
   - Género  
   - Peso (kg)  
   - Estatura (cm)  
   - Contraseña generada automáticamente

2. **Menú de opciones (requiere contraseña):**
   - `1`: Mostrar la información de la persona.  
   - `2`: Verificar mayoría de edad y calcular IMC.  
   - `3`: Salir del programa.  

3. **Generación de contraseñas seguras**  
   - Incluye letras minúsculas, mayúsculas y números.  
   - Longitud mínima de 10 caracteres.  

4. **Cálculo de IMC**  
   Fórmula utilizada:  

   \[
   IMC = \frac{peso \times 10000}{(estatura\_cm)^2}
   \]

   Se muestra el resultado con **un decimal**.

---

## 📂 Estructura del Proyecto
├── Contrasena.py # Clase para generar y validar contraseñas
├── main.py # Programa principal con la clase Persona
└── README.md # Este archivo


---

## ▶️ Ejecución

1. Clona el repositorio o copia los archivos.  
2. Ejecuta el programa principal:

```bash
python3 main.py

=== REGISTRARSE ===
NOMBRE: Juan
EDAD: 22
GENERO (Masculino o Femenino): Masculino
PESO (en kg): 70
ESTATURA (en cm): 175
Su contraseña es Xy7k3Pa9Qw. No la olvide, pues la necesitará luego.

Presione:
    1: para mostrar su información
    2: para calcular su IMC
    3: para salir del programa
>>> 2
<<<< INGRESE SU CONTRASEÑA >>>>
Xy7k3Pa9Qw
Juan es mayor de edad
El IMC de Juan es de 22.9

⚠️ Notas

El IMC está basado en rangos de adultos. Para menores de 18 años se necesitarían tablas de crecimiento especiales.

Las contraseñas se generan aleatoriamente, así que cada usuario tendrá una diferente en cada ejecución.

