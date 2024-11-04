def eh_positivo(numero: float):
    ele_eh_positivo = None
    if numero > 0:
       ele_eh_positivo = True
    else:
        ele_eh_positivo = False
    return ele_eh_positivo

numero_1 = 2
resultado_1 = eh_positivo(numero_1)
print(resultado_1)


print(eh_positivo(-65))
