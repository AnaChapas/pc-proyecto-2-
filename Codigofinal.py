# Variables generales
continuar=True
#Variables para ingresar operarios 
codigosID=[]
estaciones=[]
nombres=[]
apellidos=[]
nacimientos=[]
contraseñas=[]
#Variables para simular paso de tiempo
estacion1=[]
estacion2=[]
estacion3=[]
#Variables para historial de produccion
#Variables para control de calidad
#Variables para pago a operarios
#Variables para restablecer contraseña
#Variables para cambiar contraseña
#CODIGOS
while continuar:
    print("Bienvenido")
    print("Escoja una de las siguientes opciones:")
    print("1. Ingresar operarios")
    print("2. Mostrar equipo de trabajo")
    print("3. Simular paso del tiempo")
    print("4. Historia de producción")
    print("5. Control de calidad")
    print("6. Pago a operarios")
    print("7. Restablecer contraseña")
    print("8. Cambiar contraseña")
    print("9. Salir")
    print("")
    eleccion=int(input("Ingrese una de las opciones anteriores (solo coloque el número): "))

#Codigo de ingresar operarios
    if eleccion==1:
        
        for i in range(4):
                print("")
                codigosID.append(input("Ingrese el codigo ID del operario "+ str(i+1)+": "))
                estaciones.append(input("Ingrese a que estacion pertenece el operario "+ str(i+1)+": "))
                nombres.append(input("Ingrese el nombre del operario " + str(i+1)+": "))
                apellidos.append(input("Ingrese el apellido del operario " + str(i+1)+": "))
                nacimientos.append(input("Ingrese la fecha de nacimiento del operario "+ str(i+1)+" (DD-MM-AAAA): "))
                contraseñas.append(input("Ingrese la contraseña del operario "+ str(i+1)+": "))
                print("")
            
        siguiente=input("¿Desea terminar la simulacion definitivamente? (si/no): ")
        print("")
        if siguiente == "si":
            continuar=False
        else:
           continuar=True
#Codigo de Mostrar equipo de trabajo
    elif eleccion==2:
        if len(codigosID)== 0:
            print("")
            print("Debe de entar en el apartado de ingresar operarios para que se puedan mostrar los datos")
            print("")
            continuar=True
        else:
            print("")
            print(f"{"Código ID":15} {"Estación":20} {"Nombre":20} {"Apellido":20} {"Fecha Nac.":15} {"Contraseña":15}")
            for i in range(len(codigosID)):
                print(f"{codigosID[i]:15} {estaciones[i]:20} {nombres[i]:20} {apellidos[i]:20} {nacimientos[i]:15} {contraseñas[i]:15}")
            print("")

#Codigo de Simular paso del tiempo
    elif eleccion==3:
        import random

        for dia in range(5):
            estacion1.append(random.randint(75,120))
            estacion2.append(random.randint(75,120))
            estacion3.append(random.randint(75,120))
        print("")
        print("¡La simulacion se realizo de manera exitosa!")
        print("")
#Codigo de historial de produccion
    elif eleccion==4:
        if len(estacion1)==0:
            print("")
            print("Debe de entar en el apartado de simular tiempo para que se puedan mostrar los datos")
            print("")
            continuar=True
        else:
            print("")
            print("Historial de producción:")
            print("")
            print(f"{"Estación 1":15} {estacion1[0]:5} {estacion1[1]:5} {estacion1[2]:5} {estacion1[3]:5} {estacion1[4]:5}")
            print(f"{"Estación 2":15} {estacion2[0]:5} {estacion2[1]:5} {estacion2[2]:5} {estacion2[3]:5} {estacion2[4]:5}")
            print(f"{"Estación 3":15} {estacion2[0]:5} {estacion2[1]:5} {estacion3[2]:5} {estacion3[3]:5} {estacion3[4]:5}")
            print("")
#Codigo de control de calidad
#Codigo de pago a operarios
#Codigo de restablecer contraseña
#Codigo de cambiar contraseña
#Codigo de salir
