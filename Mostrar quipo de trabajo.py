continuar=True
codigosID=[]
estaciones=[]
nombres=[]
apellidos=[]
nacimientos=[]
contraseñas=[]
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