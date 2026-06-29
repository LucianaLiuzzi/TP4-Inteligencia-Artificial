import math

# Imagen binaria de ejemplo (0 = fondo, 1 = línea)
imagen = [
    [0,0,0,0,0],
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,0],
    [0,0,0,0,1]
]

alto = len(imagen)
ancho = len(imagen[0])

print("Puntos detectados:")

for y in range(alto):
    for x in range(ancho):
        if imagen[y][x] == 1:
            print(f"Punto ({x},{y})")

print("\nTransformada de Hough")

for y in range(alto):
    for x in range(ancho):
        if imagen[y][x] == 1:
            for theta in [0,45,90,135]:
                rad = math.radians(theta)
                rho = x*math.cos(rad)+y*math.sin(rad)

                print(
                    f"Punto ({x},{y})  Theta={theta}°  Rho={rho:.2f}"
                )

print("\nFin del prototipo.")
