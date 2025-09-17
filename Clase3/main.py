#comentario

"""
comentario en bloque

edad = 23 #int
altura = 1.57 #float
nombre = "Daniel"
liciencia_conducir = False #boolean --- letter in capitals


x, y, z, = 0, 2, 5 #se declaran multiples valores.... PYTHON no tiene array como tipo


#suma
resultado_suma = x + y


#resta
resultado_resta = 8 - 2


#multiplicacion 
resultado_multiplicacion= 8 * 2


#division

resultado_division= 8 / 2



#las constantes se escriben en mayusculas




print(resultado_suma)



print(5 !=6 )

print(edad >= 18 and liciencia_conducir == True)

print(not False)





nombre = input("ingrese su nombre: ")  #input siempre asume el input que es string
edad = input("ingrese su edad: ") #input siempre asume el input que es string
print("bienvenido" , nombre) #" , " concatena diferente tipos de datos y genera un espacio. "+" concantena mismo tipo de datos


print(type(edad)) 

#mayoria_de_edad =  edad >= 18

if edad.isdigit():  #isdigit() is true and false that checks is a number
    edad = int(edad)

    if (edad >= 18):     
        print(nombre + " es mayor de edad? = " + str(edad))        #los espacios son muy importantes en python. la indentacion define los bloques. parecido a las {} en java
    elif (edad < 18):
     print(nombre + " es menor de edad")
else:
    print("la edad no es valida")
   """

##### BUCKLES #####


# while
"""
contador = 0

while contador < 5:
   print (contador)
   contador += 1  # los contadores o acumuladores en python son unicamente " += 1"


"""





"""
# for
frutas = [ "manzana" , "pera", "durazno"]

## for  in range (3):  #for i in range (5) == for(i=0; 0<i; i++)
  
for elementos in frutas:
    print(frutas)

"""

"""
nombre = input("ingres tu nombre:")
edad = input("ingresa tu edad:")
profession = input(" ingresa tu profesion : ")

print(f"hola {nombre}, tienes {edad}, y tu profesion es {profession}")  # f is a string formatter/

"""


########


for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)
        


