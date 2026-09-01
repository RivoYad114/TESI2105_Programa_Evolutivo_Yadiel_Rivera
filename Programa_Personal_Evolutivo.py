
# Programa Personal Evolutivo - TESI 2105
# Registro de Horas de Trabajo
# Version 2.0 

# --- CONSTANTES ---
TARIFA_MINIMA = 8.50
HORAS_REGULARES_MAXIMAS = 40      # Limite semanal antes de pagar tiempo extra
FACTOR_TIEMPO_EXTRA = 1.5         # Las horas extra pagan 1.5 veces la tarifa
DIAS_TRABAJADOS = 5               # Se registran 5 dias de trabajo

# --- ENTRADAS (input) ---
nombre_empleado = input("Nombre del empleado: ")
pago_por_hora = float(input("Pago por hora ($): "))

# --- CICLO: se repite la misma tarea (pedir horas) por cada dia ---
# Esto evita escribir 5 veces el mismo input() como se haria manualmente.
total_horas = 0.0
dia = 1
while dia <= DIAS_TRABAJADOS:
    horas_dia = float(input("Horas trabajadas el dia " + str(dia) + ": "))
    total_horas = total_horas + horas_dia
    dia = dia + 1

# --- PROCESAMIENTO base (igual que en v1.0) ---
pago_total = total_horas * pago_por_hora
diferencia_tarifa_minima = pago_por_hora - TARIFA_MINIMA

# --- DECISION: calcular si hay tiempo extra ---
if total_horas > HORAS_REGULARES_MAXIMAS:
    horas_regulares = HORAS_REGULARES_MAXIMAS
    horas_extra = total_horas - HORAS_REGULARES_MAXIMAS
    pago_extra = horas_extra * pago_por_hora * FACTOR_TIEMPO_EXTRA
    pago_total = (horas_regulares * pago_por_hora) + pago_extra
    mensaje_tiempo = "Se trabajaron " + str(horas_extra) + " horas extra esta semana."
elif total_horas == HORAS_REGULARES_MAXIMAS:
    horas_extra = 0
    pago_extra = 0
    mensaje_tiempo = "Se completo exactamente la semana regular, sin horas extra."
else:
    horas_extra = 0
    pago_extra = 0
    mensaje_tiempo = "No se alcanzaron las " + str(HORAS_REGULARES_MAXIMAS) + " horas regulares."

# --- SALIDA ---
print("\n----- REGISTRO DE HORAS DE TRABAJO (v2.0) -----")
print("Empleado:", nombre_empleado)
print("Total de horas trabajadas en la semana:", total_horas)
print("Pago por hora: $" + str(pago_por_hora))
print(mensaje_tiempo)
print("Pago por horas extra: $" + str(pago_extra))
print("Pago total de la semana: $" + str(round(pago_total, 2)))
print("Diferencia respecto a la tarifa minima ($" + str(TARIFA_MINIMA) + "): $" + str(diferencia_tarifa_minima))