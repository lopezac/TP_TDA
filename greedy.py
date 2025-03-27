def es_culpable(transacciones,tiempos_sospechosos):
    resultado=[]
    valores=dic_transacciones(transacciones)
    transacciones_ord=ordenar_tiempos(transacciones)  
    for i in range(len(tiempos_sospechosos)): 
        for j in range(len(transacciones_ord)):
            cota_inferior=transacciones_ord[j][0]-transacciones_ord[j][1]
            cota_superior=transacciones_ord[j][0]+transacciones_ord[j][1]

            if  (tiempos_sospechosos[i]>=cota_inferior and tiempos_sospechosos[i]<=cota_superior and valores[transacciones_ord[j]] > 0):
                valores[transacciones_ord[j]]-=1
                resultado.append((tiempos_sospechosos[i],transacciones_ord[j]))
                break
           
    return resultado

def dic_transacciones(t):
    dic={}
    for tran in t:
        dic[tran] = dic.get(tran,0)+1
    return dic

def ordenar_tiempos(t):
    t=sorted(t, key=lambda punto: (punto[0]+punto[1]))
    return t




def main():
#caso_5_es
    t=[(599,12),(727,49),(892,82),(856,70),(229,45)]
    s=[213,607,711,806,816]
   
    respuesta=es_culpable(t,s)
    for i in range(len(respuesta)):
        print(str(respuesta[i][0])+"-->"+str(respuesta[i][1][0])+"±"+str(respuesta[i][1][1]))
    
#     print("Deberia ser True", es_culpable(intervalos,s))
# #caso_5_no_es
#     t1=[(908,66),(845,30),(728,97),(807,97),(624,40)]
#     s1=[46,560,600,890,998]
#     intervalos=(parsear_a_intervalos(t1))
#     print("Deberia ser False", es_culpable(intervalos,s1))

#caso 50_es
    t3 = [(117, 35), (627, 27), (963, 58), (568, 77), (342, 88),(140, 81), (230, 76), (663, 31), (940, 70), (409, 73),(349, 22), (144, 57), (622, 25), (502, 10), (905, 65),(112, 90), (856, 51), (890, 78), (906, 41), (740, 45),(668, 77), (698, 82), (181, 10), (670, 29), (955, 17),(935, 68), (710, 10), (257, 98), (108, 31), (989, 75),(392, 46), (921, 92), (107, 96), (208, 61), (490, 55),(248, 70), (709, 76), (519, 76), (429, 20), (734, 63),(688, 20), (976, 29), (650, 38), (674, 86), (980, 79),(846, 31), (132, 48), (171, 57), (502, 86), (891, 33)]

    s3=[75, 92, 99, 107, 116, 118, 131, 152, 178, 179,261, 275, 334, 339, 349, 350, 421, 446, 475, 486,500, 563, 563, 600, 625, 626, 630, 652, 661, 696,701, 716, 723, 734, 743, 774, 846, 852, 861, 890,908, 909, 916, 918, 937, 946, 950, 983, 1001, 1042]

    #intervalos,dic=parsear_a_intervalos(t3)
    respuesta=es_culpable(t3,s3)
    for i in range(len(respuesta)):
        print(str(respuesta[i][0])+"-->"+str(respuesta[i][1][0])+"±"+str(respuesta[i][1][1]))
    
    
# #caso 50_no_es
    # t4=[(831,42),(164,34),(100,69),(483,75),(316,21),(961,80),(550,95),(330,69),(944,92),(139,87),(258,39),(970,61),(765,25),(332,27),(519,17),(417,88),(540,22),(164,21),(432,60),(755,90),(871,79),(269,59),(549,29),(462,88),(483,36),(640,41),(999,80),(109,48),(468,42),(124,90),(177,29),(751,32),(271,94),(432,43),(841,67),(148,50),(258,50),(698,61),(730,98),(834,54),(841,55),(604,49),(648,78),(655,96),(496,94),(746,56),(766,25),(875,82),(455,78),(194,10)]
    # s4=[5,17,29,31,44,46,54,58,64,82,109,113,207,291,340,343,347,354,376,384,388,477,499,510,516,517,531,588,590,656,692,692,704,722,743,752,785,840,917,953,964,1030,1052,1069,1167,1178,1243,1257,1295,1354]
    # intervalos=parsear_a_intervalos(t4)
    # print("Deberia ser False:", es_culpable(intervalos,s4))
    
main()
