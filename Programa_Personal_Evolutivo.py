# Programa Personal Evolutivo - TESI 2105
# Registro de Horas de Trabajo
# Version 3.0 (Semana 4: funciones y modularidad)

# --- CONSTANTES ---
TARIFA_MINIMA = 8.50
HORAS_REGULARES_MAXIMAS = 40      # Limite semanal antes de pagar tiempo extra
FACTOR_TIEMPO_EXTRA = 1.5         # Las horas extra pagan 1.5 veces la tarifa
DIAS_TRABAJADOS = 5               # Se registran 5 dias de trabajo


def pedir_datos_empleado():

    # Responsabilidad: ENTRADA.
    # Pide el nombre del empleado y su pago por hora.
    # No recibe parametros. Devuelve (return) dos valores para que
    # el resto del programa los use.

    nombre = input("Nombre del empleado: ")
    pago_por_hora = float(input("Pago por hora ($): "))
    return nombre, pago_por_hora


def registrar_horas_semana(dias_trabajados):

    # Responsabilidad: ENTRADA + CICLO.
    # Recibe un parametro (dias_trabajados) y pide, mediante un ciclo while,
    # las horas trabajadas cada dia. Devuelve (return) el total de horas.

    total_horas = 0.0
    dia = 1
    while dia <= dias_trabajados:
        horas_dia = float(input("Horas trabajadas el dia " + str(dia) + ": "))
        total_horas = total_horas + horas_dia
        dia = dia + 1
    return total_horas


def calcular_pago(total_horas, pago_por_hora):
    # Responsabilidad: PROCESAMIENTO + DECISION.
    # Recibe dos parametros. Usa if/elif/else para decidir si hay tiempo
    # extra y calcula el pago correspondiente. Devuelve (return) varios
    # valores que la funcion de salida necesitara mostrar.
    if total_horas > HORAS_REGULARES_MAXIMAS:
        horas_extra = total_horas - HORAS_REGULARES_MAXIMAS
        pago_extra = horas_extra * pago_por_hora * FACTOR_TIEMPO_EXTRA
        pago_total = (HORAS_REGULARES_MAXIMAS * pago_por_hora) + pago_extra
        mensaje_tiempo = "Se trabajaron " + str(horas_extra) + " horas extra esta semana."
    elif total_horas == HORAS_REGULARES_MAXIMAS:
        pago_extra = 0
        pago_total = total_horas * pago_por_hora
        mensaje_tiempo = "Se completo exactamente la semana regular, sin horas extra."
    else:
        pago_extra = 0
        pago_total = total_horas * pago_por_hora
        mensaje_tiempo = "No se alcanzaron las " + str(HORAS_REGULARES_MAXIMAS) + " horas regulares."

    return pago_total, pago_extra, mensaje_tiempo


def mostrar_resultados(nombre, total_horas, pago_por_hora, pago_total, pago_extra, mensaje_tiempo):

    # Responsabilidad: SALIDA.
    # Recibe varios parametros y solo realiza una accion (imprimir en
    # pantalla). No necesita devolver ningun valor, por eso no usa return.

    diferencia_tarifa_minima = pago_por_hora - TARIFA_MINIMA

    print("\n----- REGISTRO DE HORAS DE TRABAJO (v3.0) -----")
    print("Empleado:", nombre)
    print("Total de horas trabajadas en la semana:", total_horas)
    print("Pago por hora: $" + str(pago_por_hora))
    print(mensaje_tiempo)
    print("Pago por horas extra: $" + str(pago_extra))
    print("Pago total de la semana: $" + str(pago_total))
    print("Diferencia respecto a la tarifa minima ($" + str(TARIFA_MINIMA) + "): $" + str(diferencia_tarifa_minima))


def main():
    # Responsabilidad: ORQUESTAR.
    # Llama a las demas funciones en orden para ejecutar el programa
    # completo. Es el unico lugar donde se arma el flujo principal.

    nombre, pago_por_hora = pedir_datos_empleado()
    total_horas = registrar_horas_semana(DIAS_TRABAJADOS)
    pago_total, pago_extra, mensaje_tiempo = calcular_pago(total_horas, pago_por_hora)

    # Funcion incorporada (built-in) de Python usada de forma util:
    # round() para presentar el pago total con solo 2 decimales.
    pago_total = round(pago_total, 2)

    mostrar_resultados(nombre, total_horas, pago_por_hora, pago_total, pago_extra, mensaje_tiempo)


# Punto de entrada del programa
if __name__ == "__main__":
    main()