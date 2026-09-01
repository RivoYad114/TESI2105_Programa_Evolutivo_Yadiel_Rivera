
# Programa Personal Evolutivo - TESI 2105
# Registro de Horas de Trabajo
# version 1.0


# --- CONSTANTE ---
# Tarifa minima de referencia 
TARIFA_MINIMA = 8.50

# --- ENTRADAS (input) ---
nombre_empleado = input("Nombre del empleado: ")
horas_trabajadas_texto = input("Horas trabajadas esta semana: ")
pago_por_hora_texto = input("Pago por hora ($): ")

# --- CONVERSION DE DATOS ---
horas_trabajadas = float(horas_trabajadas_texto)
pago_por_hora = float(pago_por_hora_texto)

# --- PROCESAMIENTO (operadores) ---
pago_total = horas_trabajadas * pago_por_hora
diferencia_tarifa_minima = pago_por_hora - TARIFA_MINIMA

# --- SALIDA ---
print("----- REGISTRO DE HORAS DE TRABAJO -----")
print("Empleado:", nombre_empleado)
print("Horas trabajadas:", horas_trabajadas)
print("Pago por hora: $" + str(pago_por_hora))
print("Pago total de la semana: $" + str(pago_total))
print("Diferencia respecto a la tarifa minima ($" + str(TARIFA_MINIMA) + "): $" + str(diferencia_tarifa_minima))