def es_culpable(transacciones,tiempos_sospechosos):

    transacciones_ord=ordenar_tiempos(transacciones)  
    for i in range(len(tiempos_sospechosos)):
        if not (tiempos_sospechosos[i]>=transacciones_ord[i][0]and tiempos_sospechosos[i]<=transacciones_ord[i][1]):

                return False
    return True 
def ordenar_tiempos(t):

    t=sorted(t, key=lambda punto: (punto[1],punto[0]))
    return t


def parsear_a_intervalos(t):
    intervalos=[]
    for i in range(len(t)):
        intervalos.append((t[i][0]-t[i][1],t[i][0]+t[i][1]))
    return intervalos

def main():
#caso_5_es
    t=[(599,12),(727,49),(892,82),(856,70),(229,45)]
    s=[213,607,711,806,816]
    intervalos=(parsear_a_intervalos(t))
    
    print("Deberia ser True", es_culpable(intervalos,s))
#caso_5_no_es
    t1=[(908,66),(845,30),(728,97),(807,97),(624,40)]
    s1=[46,560,600,890,998]
    intervalos=(parsear_a_intervalos(t1))
    print("Deberia ser False", es_culpable(intervalos,s1))

#caso 50_es
    t3 = [(117, 35), (627, 27), (963, 58), (568, 77), (342, 88),(140, 81), (230, 76), (663, 31), (940, 70), (409, 73),(349, 22), (144, 57), (622, 25), (502, 10), (905, 65),(112, 90), (856, 51), (890, 78), (906, 41), (740, 45),(668, 77), (698, 82), (181, 10), (670, 29), (955, 17),(935, 68), (710, 10), (257, 98), (108, 31), (989, 75),(392, 46), (921, 92), (107, 96), (208, 61), (490, 55),(248, 70), (709, 76), (519, 76), (429, 20), (734, 63),(688, 20), (976, 29), (650, 38), (674, 86), (980, 79),(846, 31), (132, 48), (171, 57), (502, 86), (891, 33)]

    s3=[75, 92, 99, 107, 116, 118, 131, 152, 178, 179,261, 275, 334, 339, 349, 350, 421, 446, 475, 486,500, 563, 563, 600, 625, 626, 630, 652, 661, 696,701, 716, 723, 734, 743, 774, 846, 852, 861, 890,908, 909, 916, 918, 937, 946, 950, 983, 1001, 1042]

    intervalos=parsear_a_intervalos(t3)
    print("Deberia ser True:", es_culpable(intervalos,s3))
    

main()
