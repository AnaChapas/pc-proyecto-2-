import random

# Definir los vectores para almacenar la cantidad de Dolorín procesada
dolorin_estacion_1 = []
dolorin_estacion_2 = []
dolorin_estacion_3 = []

# Simular 5 días
for dia in range(5):
    # Generar 3 números aleatorios para cada estación de trabajo
    dolorin_estacion_1.append(random.randint(75, 120))
    dolorin_estacion_2.append(random.randint(75, 120))
    dolorin_estacion_3.append(random.randint(75, 120))

# Mostrar un mensaje indicando que la simulación ha finalizado
print("\nSimulación finalizada.")

# Control de calidad (opcional)
while True:
    opcion = input("¿Desea realizar control de calidad? (si/no): ")

    if opcion.lower() == "si":
        # Validar que la simulación haya finalizado
        if not dolorin_estacion_1 or not dolorin_estacion_2 or not dolorin_estacion_3:
            print("Error: La simulación del paso del tiempo no ha sido realizada.")
            break

        # Solicitar porcentajes de productos defectuosos
        porcentaje1 = int(input("Ingrese porcentaje de productos defectuosos en estación 1 (solo colocar el número): "))
        porcentaje2 = int(input("Ingrese porcentaje de productos defectuosos en estación 2 (solo colocar el número): "))
        porcentaje3 = int(input("Ingrese porcentaje de productos defectuosos en estación 3 (solo colocar el número): "))

        # Calcular productos defectuosos
        productosdefectuosos_1 = int(dolorin_estacion_1[1] * (porcentaje1 / 100))
        productosdefectuosos_2 = int(dolorin_estacion_2[-1] * (porcentaje2 / 100))
        productosdefectuosos_3 = int(dolorin_estacion_3[-1] * (porcentaje3 / 100))

        # Mostrar resultados
        print("\nResultados de control de calidad:")
        print(f"Estación 1: {dolorin_estacion_1[1]} unidades producidas, {productos_defectuosos_1} unidades defectuosas ({porcentaje_defectuoso_1:.2f}%).")
        print(f"Estación 2: {dolorin_estacion_2[1]} unidades producidas, {productos_defectuosos_2} unidades defectuosas ({porcentaje_defectuoso_2:.2f}%).")
        print(f"Estación 3: {dolorin_estacion_3[1]} unidades producidas, {productos_defectuosos_3} unidades defectuosas ({porcentaje_defectuoso_3:.2f}%).")
