#Variables generales para este codigo
codigosID=[]
estaciones=[]
nombres=[]
apellidos=[]
nacimientos=[]
contraseñas=[]
#Codigo
continuar=True
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

    