import os
import sys
import random

def es_culpable(transacciones,tiempos_sospechosos):
    resultado=[]
    valores=dic_transacciones(transacciones)
    transacciones_ord=ordenar_tiempos(transacciones)  
    for i in range(len(tiempos_sospechosos)): 
        
        hay_candidato=False

        for j in range(len(transacciones_ord)):
            cota_inferior=transacciones_ord[j][0]-transacciones_ord[j][1]
            cota_superior=transacciones_ord[j][0]+transacciones_ord[j][1]

            if (tiempos_sospechosos[i]>=cota_inferior and tiempos_sospechosos[i]<=cota_superior and valores[transacciones_ord[j]] > 0):
                valores[transacciones_ord[j]]-=1
                resultado.append((tiempos_sospechosos[i],transacciones_ord[j]))
                hay_candidato=True
                break
    
        if not hay_candidato:
            return None
           
    return resultado

def dic_transacciones(t):
    dic={}
    for tran in t:
        dic[tran] = dic.get(tran,0)+1
    return dic

def ordenar_tiempos(t):
    t=sorted(t, key=lambda punto: (punto[0]+punto[1]))
    return t


def parsear_a_tuplas(t):
    intervalos = []
    for i in range(len(t)):
        intervalos.append((t[i][0], t[i][1],))
    return intervalos


def main():
    # caso_5_es
    t = [(599, 12), (727, 49), (892, 82), (856, 70), (229, 45)]
    s = [213, 607, 711, 806, 816]
    intervalos = (parsear_a_tuplas(t))

    print("Deberia ser True", es_culpable(intervalos, s))
    # caso_5_no_es
    t1 = [(908, 66), (845, 30), (728, 97), (807, 97), (624, 40)]
    s1 = [46, 560, 600, 890, 998]
    intervalos = (parsear_a_tuplas(t1))
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

    intervalos = parsear_a_tuplas(t3)
    print("Deberia ser True:", es_culpable(intervalos, s3))

    rata,sospechoso=leer_archivo("5000-es.txt")
    respuesta=es_culpable(rata,sospechoso)
    if not respuesta:
        print("False")
    else:
        print("True")

def generate_intervals(n, center_range, error_range):
    """
    Generate a set of intervals.
    
    Args:
        n (int): Number of intervals to generate.
        center_range (tuple): Range for the center values (min, max).
        error_range (tuple): Range for the error values (min, max).
    
    Returns:
        list: A list of intervals in the format (center, error).
    """
    intervals = []
    for _ in range(n):
        center = random.randint(*center_range)
        error = random.randint(*error_range)
        intervals.append((center, error))
    return intervals

def generate_guesses(length, intervals):
    guesses = []
    for _ in range(length):
        # Randomly pick an interval and its error
        interval, error = random.choice(intervals)
        # Generate a guess within the range [interval - error, interval + error]
        guess = random.randint(interval - error, interval + error)
        guesses.append(guess)
    guesses.sort()
    return guesses

def crear_archivo(n, rata, sospechoso, es=True):
    with open("tests/"+str(n)+f"-{'es' if es else 'no-es'}.txt", 'w') as f:
        f.write("# Primero viene la cantidad (n) de timestamps para ambos, luego n líneas que son un timestamp aproximado cada uno separado por una coma (',') del error, y luego n lineas de las transacciones del sospechoso\n")
        f.write(str(n)+"\n")
        for i in range(len(rata)):
            f.write(str(rata[i][0])+","+str(rata[i][1])+"\n")
        for i in range(len(sospechoso)):
            f.write(str(sospechoso[i])+"\n")

def probar_generador():
    respuesta = None
    seed = 0
    while respuesta is None:
        seed += 1
        random.seed(seed)
        n = 10000  # Number of intervals
        center_range = (100, 1000)  # Range for center values
        error_range = (10, 100)  # Range for error values
        
        # Generate intervals
        new_intervals = generate_intervals(n, center_range, error_range)
        guesses = generate_guesses(n, new_intervals)
        respuesta = es_culpable(new_intervals, guesses)
    print("Intervals:", new_intervals)
    print("Guesses:", guesses)
    print("Respuesta:", respuesta)
    print("Seed:", seed)
    crear_archivo(n, new_intervals, guesses)

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
                rata.append((int(datos[0]), int(datos[1])))
            elif 2 + n <= index < len(lines):
                sospechoso.append(int(line))

    return rata, sospechoso


# validamos que los tests que terminen en "es-txt" retornen que el sospechoso es la rata (pero no nos fijamos si estan
# bien los datos), y los que terminan en "no-es.txt" retornen que el sospechoso no es la rata
def validar_tests_aproximado(carpeta):
    # Si no existe la carpeta Resultados la creamos
    if not os.path.exists("Resultados"):
        os.makedirs("Resultados")

    for file in os.listdir(carpeta):
        if file == "Resultados Esperados.txt" or file == "Esperados":
            continue

        rata, sospechoso = leer_archivo(carpeta + "/" + file)

        respuesta = es_culpable(rata, sospechoso)
        if (respuesta is None and "no-es" in file) or (respuesta is not None and "es" in file):
            print("Test " + file + " OK")
            if respuesta is not None:
                with open("Resultados/"+file, 'w') as f:
                    for i in range(len(respuesta)):
                        f.write(str(respuesta[i][0]) + " --> " + str(respuesta[i][1][0]) + " ± " + str(respuesta[i][1][1]) + "\n")
                    # print(str(respuesta[i][0]),"-->",str(respuesta[i][1][0]),"±",str(respuesta[i][1][1]))
        else:
            print("Test " + file + " FAIL")

if __name__ == "__main__":
    # Si pasamos un archivo por parametro, leemos ese archivo y le mostramos al usuario si el sospechoso es o no la rata
    if len(sys.argv) > 1:
        archivo = sys.argv[1]
        rata, sospechoso = leer_archivo(archivo)
        respuesta = es_culpable(rata, sospechoso)
        if respuesta is None:
            print("El sospechoso no es la rata")
        else:
            for i in range(len(respuesta)):
                print(str(respuesta[i][0]), "-->", str(respuesta[i][1][0]), "±", str(respuesta[i][1][1]))
    # Si no pasamos un archivo por parametro, corremos los tests aproximados
    else:
        # main()
        # validar_tests_aproximado("tests")
        probar_generador()
