# Calendario 2024


Dias_de_la_semana = ["L", "M", "M", "J", "V", "S", "D" ]

# Dias junto con su mes (año bisiesto)
Dias_mes = {
    "Enero": 31,
    "Febrero": 29, # Año bisiesto
    "Marzo": 31,
    "Abril": 30,
    "Mayo": 31,
    "Junio": 30,
    "Julio": 31,
    "Agosto": 31,
    "Septiembre": 30,
    "Octubre": 31,
    "Noviembre": 30,
    "Diciembre": 31,
}

# Definir el primer dia del año 2024 (01/01/2024 es Lunes)
Primer_dia_del_año = 0  # 0 = Lunes, 1 Martes, 2 Miercoles, 3 Jueves, 4 Viernes, 5 Sabado, 6 Domingo


Primer_dia_mes = {}
Dias_anteriores = Primer_dia_del_año

for mes, dias in Dias_mes.items():
    Primer_dia_mes[mes] = Dias_anteriores
    Dias_anteriores = (Dias_anteriores + dias) % 7

# Codigos de Ansi 
Color_Domingo = "\033[91m"
Color_Especial = "\033[95m"
Color_Reset = "\033[0m"
Negrilla = "\033[1m"
Color_Domingo_Negrilla = Color_Domingo + Negrilla
Color_Especial_Negrilla = Color_Especial + Negrilla

# Fechas especiales
Fechas_especiales = {
    "Abril": [7],
    "Octubre": [21],
    "Noviembre": [20, 28],
}


Mes_usuario = input("Ingrese el mes que desea ver (Ejemplo: Mayo): ").capitalize()


if Mes_usuario in Dias_mes:

    Inicio_mes = Primer_dia_mes[Mes_usuario]
    Dias_en_mes = Dias_mes[Mes_usuario]

    print("  ".join(Dias_de_la_semana))

    Semana = ["  "] * 7

    for dia in range(1,  Dias_en_mes + 1):
        if Inicio_mes == 6: # Domingo
            Semana[Inicio_mes] = f"{Color_Domingo_Negrilla}{dia:2}{Color_Reset}"
        else:
            # Fechas especiales
            if dia in Fechas_especiales.get(Mes_usuario, []):
                Semana[Inicio_mes] = f"{Color_Especial_Negrilla}{dia:2}{Color_Reset}"
            else:
                 Semana[Inicio_mes] = f"{dia:2}"

        Inicio_mes = (Inicio_mes + 1) % 7
        
        if Inicio_mes == 0 or dia == Dias_en_mes:
            print(" ".join(Semana))
            Semana = ["  "] * 7
            
else:
    print("Mes no valido. Por favor, ingrese un mes valido.")

    