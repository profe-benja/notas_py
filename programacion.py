PONDERACIONES = [.3, .3, .3, .1]

def obtener_nota_presentacion(notas):
    nota_parcial = 0
    for p, nota in enumerate(notas):
        nota_p = notas[p] * PONDERACIONES[p]
        nota_parcial += nota_p
    
    return nota_parcial

def porcentaje_nota(nota, porc):
    return nota * porc

def print_resultado(nota_final):
    if nota_final < 4:
        print('😭')
    else:
        print('🎉😎🎉')

def calcular_nota(notas, nota_examen):   
    nota_presentacion = obtener_nota_presentacion(notas)
    nota_presentacion_final = porcentaje_nota(nota_presentacion, 0.6)
    nota_examen_final = porcentaje_nota(nota_examen, 0.4)
    nota_final = nota_presentacion_final + nota_examen_final 
    return nota_final

######
notas = [7, 3, 6 , 7]
examen = 6
nota = calcular_nota(notas, examen)
print(nota)
print_resultado(nota)



