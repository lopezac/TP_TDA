import os

def es_culpable(transacciones, tiempos_sospechosos):
    candidatos = set()
    cantidad_transacciones = len(transacciones)
    for i in range(cantidad_transacciones):
        for j in range(cantidad_transacciones):
            if (tiempos_sospechosos[i] >= transacciones[j][0] and tiempos_sospechosos[i] <= transacciones[j][1]):
                candidatos.add(transacciones[i])

    return len(candidatos) == len(tiempos_sospechosos)


def parsear_a_intervalos(t):
    intervalos = []
    for i in range(len(t)):
        intervalos.append((t[i][0] - t[i][1], t[i][0] + t[i][1]))
    return intervalos


def main():
    # caso_5_es
    t = [(599, 12), (727, 49), (892, 82), (856, 70), (229, 45)]
    s = [213, 607, 711, 806, 816]
    intervalos = (parsear_a_intervalos(t))

    print("Deberia ser True", es_culpable(intervalos, s))
    # caso_5_no_es
    t1 = [(908, 66), (845, 30), (728, 97), (807, 97), (624, 40)]
    s1 = [46, 560, 600, 890, 998]
    intervalos = (parsear_a_intervalos(t1))
    print("Deberia ser False", es_culpable(intervalos, s1))

    # caso 50_es
    t3 = [(117, 35), (627, 27), (963, 58), (568, 77), (342, 88), (140, 81), (230, 76), (663, 31), (940, 70), (409, 73),
          (349, 22), (144, 57), (622, 25), (502, 10), (905, 65), (112, 90), (856, 51), (890, 78), (906, 41), (740, 45),
          (668, 77), (698, 82), (181, 10), (670, 29), (955, 17), (935, 68), (710, 10), (257, 98), (108, 31), (989, 75),
          (392, 46), (921, 92), (107, 96), (208, 61), (490, 55), (248, 70), (709, 76), (519, 76), (429, 20), (734, 63),
          (688, 20), (976, 29), (650, 38), (674, 86), (980, 79), (846, 31), (132, 48), (171, 57), (502, 86), (891, 33)]

    s3 = [75, 92, 99, 107, 116, 118, 131, 152, 178, 179, 261, 275, 334, 339, 349, 350, 421, 446, 475, 486, 500, 563,
          563, 600, 625, 626, 630, 652, 661, 696, 701, 716, 723, 734, 743, 774, 846, 852, 861, 890, 908, 909, 916, 918,
          937, 946, 950, 983, 1001, 1042]

    intervalos = parsear_a_intervalos(t3)
    print("Deberia ser True:", es_culpable(intervalos, s3))


main()

# rata es de la forma [[timestamp, error], ...]
# sospechoso es de la forma [timestamp, ...]
# ejemplo el archivo 5-es.txt devuelve:
# Rata = [[599, 12], [727, 49], [892, 82], [856, 70], [229, 45]]
# Sospechoso = [213, 607, 711, 806, 816]
def leer_archivo(archivo):
    rata = []
    sospechoso = []
    n = 0

    with open(archivo, 'r') as f:
        lines = f.readlines()
        for index, line in enumerate(lines):
            if index == 1:
                n = int(line)
            elif 2 <= index < 2 + n:
                datos = line.split(",")
                rata.append([int(datos[0]), int(datos[1])])
            elif 2 + n <= index < len(lines):
                sospechoso.append(int(line))

    return rata, sospechoso


# validamos que los tests que terminen en "es-txt" retornen que el sospechoso es la rata (pero no nos fijamos si estan
# bien los datos), y los que terminan en "no-es.txt" retornen que el sospechoso no es la rata
def validar_tests_aproximado(carpeta):
    for file in os.listdir(carpeta):
        if file == "Resultados Esperados.txt":
            continue

        rata, sospechoso = leer_archivo(carpeta + "/" + file)
        intervalos = (parsear_a_intervalos(rata))
        esperado = True
        if "no-es" in file:
            esperado = False
        culpabilidad = es_culpable(intervalos, sospechoso)
        if culpabilidad == esperado:
            print(("exito:     " + file).ljust(30), "es", esperado, "y nos da", culpabilidad)
        else:
            print(("FALLO!!!:  " + file).ljust(30), "es", esperado, "pero nos da", culpabilidad)


validar_tests_aproximado("tests")