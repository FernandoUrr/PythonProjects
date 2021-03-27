#No se puede ser más preciso y más rápido con los algoritmos
objetivo = int(input("Escoge un número: "))
epsilon = 0.01 #Precisión
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f"No se encontró la raíz cuadrada de {objetivo}")
else:
    print(f"La raíz cuadrada de {objetivo} es {respuesta}")

