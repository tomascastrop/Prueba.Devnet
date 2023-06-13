import math

def calcular_circunferencia(radio):
    pi_evaluacion= round(math.pi,6)  
    circunferencia = radio * pi_evaluacion * 2
    return circunferencia

radios_soli = [3, 8, 10]

for radio in radios_soli:
    circunferencia = calcular_circunferencia(radio)
    print("La circunferencia de radio " + str(radio) + " es " + str(circunferencia))
