# encoding=utf-8
# Programado el 16 y 19 de sept 2019 desde el Lab. de la facultad. También conocido como "la cueva del hamster en la ruedita eterna"
# Versión 1.60: Retocado el 26 de enero 2020, en mi laptop con Linux, en casa.
# Copyright (C) Alejandro Moliné, 2019

autoria="\nEste programa calcula el gasto calórico del *METABOLISMO BASAL* | (C) 2019-09-16 Ale Moliné."

defMBR = """
El METABOLISMO BASAL es el gasto energético diario, es decir, lo que un cuerpo necesita diariamente para seguir funcionando. 
A ese cálculo hay que añadir las actividades extras que se pueden hacer cada día. 
La tasa metabólica disminuye con la edad y con la pérdida de masa corporal. 

Los siguientes factores AUMENTAN el metabolismo basal:

    * Mayor masa muscular
    * Mayor superficie corporal total
    * Género masculino (Los varones casi siempre tienen mayor masa corporal magra que las mujeres)
    * Temperatura corporal, (fiebre o condiciones ambientales frías)
    * Hormonas tiroideas (un regulador clave del metabolismo basal las concentraciones altas aumentan la BMR)
    * Aspectos de la actividad del sistema nervioso (liberación de hormonas de estrés)
    * Etapas de crecimiento en el ciclo vital
    * Consumo de cafeína o tabaco. 
"""
def cls():
    sistema="nulo"
    import os
    import platform
    # Ver si estoy en Windows o en un posix
    if (platform.system() == "Windows"):
        sistema="Windows"
        os.system('cls')
    else:
        sistema="Unix"
        os.system('clear')
    return

def tdee(bmr):
    # Segunda parte: cálculo del TDEE (Total Daily Energy Expenditure).

    """
    * Factores para calcular el TDEE *
    
    Sedentary = BMR x 1.2
    Light Active = BMR x 1.375
    Moderately Active = BMR x 1.55
    Very Active = BMR x 1.725
    """
    factortxt = """
    ** Segunda parte: cálculo del gasto calórico total **
    
    Elija el número, de acuerdo a su nivel *REAL* de actividad física DIARIA:

    OBS: "ejercicio intenso" significa correr o levantar pesas.
    
    [1] Sedentario.........: Mucho Netflix y redes sociales. No te ejercitás intencionalmente.
    [2] Actividad liviana..: 30 minutos de caminata diaria o 15 minutos de ejercicio intenso.
    [3] Actividad moderada.: 1hora 45 minutos diarios de caminata, o 50 minutos de ejercicio intenso.
    [4] Actividad intensa..: 4 horas 15 minutos de caminata, o dos horas de ejercicio intenso.

    Ante la duda, elegir el nivel de actividad *más bajo* de lo que pensamos.
    
    """
    print(factortxt)
    fAct = raw_input("¿Número [1/4]?:")
    if   fAct == '1': 
        numfact = 1.2
    elif fAct == '2': 
        numfact = 1.375
    elif fAct == '3': 
        numfact = 1.55
    elif fAct == '4': 
        numfact = 1.725
    else:
        numfact = 0
    
    a = bmr*numfact
    print("\nTDEE [Gasto diario calórico total]: "+str(a)+"\n")
    return a

cls()

print(autoria)
print(defMBR)
peso=raw_input("¿Peso? (en kg):"); peso=float(peso)
altura=raw_input("¿Altura? (En centímetros. Ej. 176):"); altura=int(altura)
sexo=raw_input("¿Sexo? (M/F):")
if  sexo.upper() == "M":  # Transforma el sexo en el coeficiente usado en la fórmula
    sexf = 5
else:
    sexf = -161
edad=raw_input("¿Edad? (en años):"); edad=int(edad)
BMR = 10 * peso + 6.25 * altura - 5 * edad + sexf # Ecuación Mifflin-St Jeor de MBR
BMR = int(BMR)
print("\nBMR [Metabolismo Basal] = "+str(BMR)+" calorías.\n") 

tdee(BMR) # Lo implementé como función porque es más facil el debug

