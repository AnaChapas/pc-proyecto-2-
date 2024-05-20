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
        
    elif eleccion==5:
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

            porcentaje1 = int(input("Ingrese porcentaje de productos defectuosos en estación 1 (solo colocar el número): "))
            porcentaje2 = int(input("Ingrese porcentaje de productos defectuosos en estación 2 (solo colocar el número): "))
            porcentaje3 = int(input("Ingrese porcentaje de productos defectuosos en estación 3 (solo colocar el número): "))

            # Calcular productos defectuosos dia 1
            productos1dia1 = int(estacion1[0] * (porcentaje1 / 100))
            productos2dia1 = int(estacion2[0] * (porcentaje2 / 100))
            productos3dia1 = int(estacion3[0] * (porcentaje3 / 100))
            # Calcular productos defectuosos dia 2
            productos1dia2= int(estacion1[1] * (porcentaje1 / 100))
            productos2dia2 = int(estacion2[1] * (porcentaje2 / 100))
            productos3dia2 = int(estacion3[1] * (porcentaje3 / 100))
            # Calcular productos defectuosos dia 3
            productos1dia3 = int(estacion1[2] * (porcentaje1 / 100))
            productos2dia3 = int(estacion2[2] * (porcentaje2 / 100))
            productos3dia3 = int(estacion3[2] * (porcentaje3 / 100))
            # Calcular productos defectuosos dia 4
            productos1dia4 = int(estacion1[3] * (porcentaje1 / 100))
            productos2dia4 = int(estacion2[3] * (porcentaje2 / 100))
            productos3dia4 = int(estacion3[3] * (porcentaje3 / 100))
            # Calcular productos defectuosos dia 5
            productos1dia5 = int(estacion1[4] * (porcentaje1 / 100))
            productos2dia5 = int(estacion2[4] * (porcentaje2 / 100))
            productos3dia5 = int(estacion3[4] * (porcentaje3 / 100))
            print("")
            print("Resultados de control de calidad de cada dia:")
            print("")
            print("Dia 1:")
            print(f"Estación 1: {estacion1[0]} unidades producidas, {productos1dia1} unidades defectuosas")
            print(f"Estación 2: {estacion2[0]} unidades producidas, {productos2dia1} unidades defectuosas")
            print(f"Estación 3: {estacion3[0]} unidades producidas, {productos3dia1} unidades defectuosas")
            print("")
            print("Dia 2:")
            print(f"Estación 1: {estacion1[1]} unidades producidas, {productos1dia2} unidades defectuosas")
            print(f"Estación 2: {estacion2[1]} unidades producidas, {productos2dia2} unidades defectuosas")
            print(f"Estación 3: {estacion3[1]} unidades producidas, {productos3dia2} unidades defectuosas")
            print("")
            print("Dia 3:")
            print(f"Estación 1: {estacion1[2]} unidades producidas, {productos1dia3} unidades defectuosas")
            print(f"Estación 2: {estacion2[2]} unidades producidas, {productos2dia3} unidades defectuosas")
            print(f"Estación 3: {estacion3[2]} unidades producidas, {productos3dia3} unidades defectuosas")
            print("")
            print("Dia 4:")
            print(f"Estación 1: {estacion1[3]} unidades producidas, {productos1dia4} unidades defectuosas")
            print(f"Estación 2: {estacion2[3]} unidades producidas, {productos2dia4} unidades defectuosas")
            print(f"Estación 3: {estacion3[3]} unidades producidas, {productos3dia4} unidades defectuosas")
            print("")
            print("Dia 5:")
            print(f"Estación 1: {estacion1[4]} unidades producidas, {productos1dia5} unidades defectuosas")
            print(f"Estación 2: {estacion2[4]} unidades producidas, {productos2dia5} unidades defectuosas")
            print(f"Estación 3: {estacion3[4]} unidades producidas, {productos3dia5} unidades defectuosas")
            #Resta de productos producidos menos productos defectuosos 
            #dia1
            productos1dia1=estacion1[0]-productos1dia1
            productos2dia1=estacion2[0]-productos2dia1
            productos3dia1=estacion3[0]-productos3dia1
            #dia2
            productos1dia2=estacion1[1]-productos1dia2
            productos2dia2=estacion2[1]-productos2dia2
            productos3dia2=estacion3[1]-productos3dia2
            #dia3
            productos1dia3=estacion1[2]-productos1dia3
            productos2dia3=estacion2[2]-productos2dia3
            productos3dia3=estacion3[2]-productos3dia3
            #dia4
            productos1dia4=estacion1[3]-productos1dia4
            productos2dia4=estacion2[3]-productos2dia4
            productos3dia4=estacion3[3]-productos3dia4
            #dia5
            productos1dia5=estacion1[4]-productos1dia5
            productos2dia5=estacion2[4]-productos2dia5
            productos3dia5=estacion3[4]-productos3dia5
            print("")
            print("Historial de producción actualizado:")
            print("")
            print(f"{"Estación 1":15} {productos1dia1:5} {productos1dia2:5} {productos1dia3:5} {productos1dia4:5} {productos1dia5:5}")
            print(f"{"Estación 2":15} {productos2dia1:5} {productos2dia2:5} {productos2dia3:5} {productos2dia4:5} {productos2dia5:5}")
            print(f"{"Estación 3":15} {productos3dia1:5} {productos3dia2:5} {productos3dia3:5} {productos3dia4:5} {productos3dia5:5}")
            print("")