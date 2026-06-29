import math

# Imagen binaria de ejemplo
# 1 = borde de la circunferencia
# 0 = fondo

imagen = [
    [0,0,0,0,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,1,0,0,0,1,0],
    [0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0]
]

alto = len(imagen)
ancho = len(imagen[0])

# Radio conocido
radio = 2

# Acumulador
acumulador = {}

print("Buscando posibles centros de la circunferencia...\n")

for y in range(alto):
    for x in range(ancho):
        if imagen[y][x] == 1:

            for angulo in range(0, 360, 45):

                rad = math.radians(angulo)

                xc = round(x - radio * math.cos(rad))
                yc = round(y - radio * math.sin(rad))

                if (xc, yc) not in acumulador:
                    acumulador[(xc, yc)] = 1
                else:
                    acumulador[(xc, yc)] += 1

# Buscar el centro con mayor cantidad de votos
mejor_centro = max(acumulador, key=acumulador.get)

print("Centro encontrado:")
print(f"X = {mejor_centro[0]}")
print(f"Y = {mejor_centro[1]}")
print(f"Votos = {acumulador[mejor_centro]}")
