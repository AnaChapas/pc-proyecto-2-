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
        estacion1=[]
        estacion2=[]
        estacion3=[]
        for dia in range(5):
            estacion1.append(random.randint(75,120))
            estacion2.append(random.randint(75,120))
            estacion3.append(random.randint(75,120))
        print("")
        print("¡La simulacion se realizo de manera exitosa!")
        print("")
        
