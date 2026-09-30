# Programa Evolutivo
# Version 4.0

# --- CONSTANTES ---
TARIFA_MINIMA = 8.50
HORAS_REGULARES_MAXIMAS = 40
FACTOR_TIEMPO_EXTRA = 1.5
DIAS_TRABAJADOS = 5
DIAS_SEMANA = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]


def pedir_datos_empleado():
    """Pide nombre y pago por hora. (v1.0/v2.0/v3.0, sin cambios)"""
    nombre = input("Nombre del empleado: ")
    pago_por_hora = float(input("Pago por hora ($): "))
    return nombre, pago_por_hora


# ---------------------------------------------------------------------
# 2. ARREGLO UNIDIMENSIONAL
# Las horas de cada dia ahora se guardan en una lista (arreglo),
# en vez de solo sumarse como en v2.0/v3.0. Esto permite acceder,
# mostrar y modificar un dia especifico despues de haberlo registrado.
# ---------------------------------------------------------------------

def registrar_horas_semana(dias_trabajados):
    """
    Pide las horas de cada dia con un ciclo while (se conserva de v2.0)
    y las va guardando en una lista. Retorna el arreglo completo.
    """
    horas_por_dia = []          # arreglo unidimensional vacio
    dia = 1
    while dia <= dias_trabajados:
        horas_dia = float(input("Horas trabajadas el " + DIAS_SEMANA[dia - 1] + ": "))
        horas_por_dia.append(horas_dia)   # se agrega al arreglo
        dia = dia + 1
    return horas_por_dia


def mostrar_arreglo_horas(horas_por_dia):
    """
    Muestra el contenido completo del arreglo y lo recorre con un
    ciclo for, mostrando cada valor junto al dia que representa.
    """
    print("\nArreglo completo de horas:", horas_por_dia)
    print("Recorrido dia por dia:")
    for i in range(len(horas_por_dia)):
        print(" -", DIAS_SEMANA[i] + ":", horas_por_dia[i], "horas")


def acceder_horas_especificas(horas_por_dia):
    """Accede a por lo menos dos elementos del arreglo mediante su indice."""
    primer_dia = horas_por_dia[0]          # acceso por indice 0
    ultimo_dia = horas_por_dia[-1]         # acceso al ultimo indice
    print("\nHoras del primer dia (indice 0):", primer_dia)
    print("Horas del ultimo dia (indice -1):", ultimo_dia)


def modificar_horas_dia(horas_por_dia, indice_dia, horas_corregidas):
    """Modifica un elemento existente del arreglo (ej. corregir un dato)."""
    horas_por_dia[indice_dia] = horas_corregidas
    print("\nSe corrigieron las horas del " + DIAS_SEMANA[indice_dia] +
          " a " + str(horas_corregidas) + " horas.")


# ---------------------------------------------------------------------
# 3. ARREGLO MULTIDIMENSIONAL
# Registro semanal de varios empleados: cada FILA es un empleado y
# cada COLUMNA es un dia de la semana (Lunes a Viernes).
# ---------------------------------------------------------------------

def registrar_multiples_empleados(nombres_empleados, dias_trabajados):
    """
    Pide las horas de cada dia para cada empleado y arma un arreglo
    multidimensional (lista de listas): registro[fila][columna].
    """
    registro_semanal = []
    for nombre in nombres_empleados:
        print("\n--- Horas de " + nombre + " ---")
        horas_empleado = registrar_horas_semana(dias_trabajados)  # una fila
        registro_semanal.append(horas_empleado)
    return registro_semanal


def recorrer_registro_multiempleados(registro_semanal, nombres_empleados):
    """Recorre la estructura de dos dimensiones con ciclos anidados."""
    print("\n----- REGISTRO SEMANAL DE TODOS LOS EMPLEADOS -----")
    for fila in range(len(registro_semanal)):
        print(nombres_empleados[fila] + ":")
        for columna in range(len(registro_semanal[fila])):
            dato = registro_semanal[fila][columna]   # acceso [fila][columna]
            print("   " + DIAS_SEMANA[columna] + " -> " + str(dato) + " horas")


# ---------------------------------------------------------------------
# 4. CADENAS DE CARACTERES
# Operaciones sobre el nombre del empleado.
# ---------------------------------------------------------------------

def analizar_nombre_empleado(nombre):
    """
    Realiza varias operaciones sobre una cadena: longitud, acceso por
    indice, recorrido, busqueda y transformacion.
    """
    print("\n----- ANALISIS DEL NOMBRE -----")

    # Longitud de la cadena
    print("Longitud del nombre:", len(nombre))

    # Acceso a un caracter por indice
    print("Primer caracter (indice 0):", nombre[0])

    # Recorrido de los caracteres
    print("Recorrido caracter por caracter:")
    for caracter in nombre:
        print(" ", caracter)

    # Busqueda dentro del texto
    letra_buscada = "a"
    if letra_buscada in nombre.lower():
        print("La letra '" + letra_buscada + "' SI aparece en el nombre.")
    else:
        print("La letra '" + letra_buscada + "' NO aparece en el nombre.")

    # Transformacion de texto
    nombre_mayusculas = nombre.upper()
    print("Nombre en mayusculas:", nombre_mayusculas)


# ---------------------------------------------------------------------
# Logica de pago (se conserva de v2.0 / v3.0, sin cambios)
# ---------------------------------------------------------------------

def calcular_pago(total_horas, pago_por_hora):
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
    diferencia_tarifa_minima = pago_por_hora - TARIFA_MINIMA
    print("\n----- REGISTRO DE HORAS DE TRABAJO (v4.0) -----")
    print("Empleado:", nombre)
    print("Total de horas trabajadas en la semana:", total_horas)
    print("Pago por hora: $" + str(pago_por_hora))
    print(mensaje_tiempo)
    print("Pago por horas extra: $" + str(pago_extra))
    print("Pago total de la semana: $" + str(pago_total))
    print("Diferencia respecto a la tarifa minima ($" + str(TARIFA_MINIMA) + "): $" + str(diferencia_tarifa_minima))


def main():
    # --- Empleado principal (flujo normal de v1.0 a v3.0) ---
    nombre, pago_por_hora = pedir_datos_empleado()
    horas_por_dia = registrar_horas_semana(DIAS_TRABAJADOS)   # arreglo unidimensional

    mostrar_arreglo_horas(horas_por_dia)
    acceder_horas_especificas(horas_por_dia)
    modificar_horas_dia(horas_por_dia, 0, horas_por_dia[0] + 1)  # ejemplo de modificacion

    total_horas = sum(horas_por_dia)   # funcion incorporada sum()
    pago_total, pago_extra, mensaje_tiempo = calcular_pago(total_horas, pago_por_hora)
    pago_total = round(pago_total, 2)
    mostrar_resultados(nombre, total_horas, pago_por_hora, pago_total, pago_extra, mensaje_tiempo)

    # --- Analisis de cadena sobre el nombre del empleado ---
    analizar_nombre_empleado(nombre)

    # --- Demostracion de arreglo multidimensional (varios empleados) ---
    print("\n¿Deseas registrar empleados adicionales para el arreglo multidimensional? (s/n)")
    respuesta = input("> ")
    if respuesta.lower() == "s":
        nombres_empleados = [nombre]
        cantidad_adicionales = int(input("¿Cuantos empleados adicionales? "))
        contador = 1
        while contador <= cantidad_adicionales:
            nombre_extra = input("Nombre del empleado adicional " + str(contador) + ": ")
            nombres_empleados.append(nombre_extra)
            contador = contador + 1

        registro_semanal = registrar_multiples_empleados(nombres_empleados, DIAS_TRABAJADOS)
        recorrer_registro_multiempleados(registro_semanal, nombres_empleados)


if __name__ == "__main__":
    main()