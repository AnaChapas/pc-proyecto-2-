estacion1=[]
estacion2=[]
estacion3=[]
continuar=True
while continuar:
    print("Bienvenidos")
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
    eleccion=int(input("Ingrese una de las opciones anteriores (solo coloque el número): "))
    if eleccion==3:
        import random

        for dia in range(5):
            estacion1.append(random.randint(75,120))
            estacion2.append(random.randint(75,120))
            estacion3.append(random.randint(75,120))
        print("")
        print("¡La simulacion se realizo de manera exitosa!")
        print("")
        
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