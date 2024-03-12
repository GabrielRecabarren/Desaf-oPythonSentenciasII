# mayor_a.py

import sys

# Diccionario con los balances de ventas por mes
ventas = {
 "Enero": 15000,
 "Febrero": 22000,
 "Marzo": 12000,
 "Abril": 17000,
 "Mayo": 81000,
 "Junio": 13000,
 "Julio": 21000,
 "Agosto": 41200,
 "Septiembre": 25000,
 "Octubre": 21500,
 "Noviembre": 91000,
 "Diciembre": 21000,
}

# Función para filtrar los meses que superan el umbral especificado
def filtrar_meses_sobre_umbral(umbral):
    meses_sobre_umbral = {}
    for mes, venta in ventas.items():
        if venta > umbral:
            meses_sobre_umbral[mes] = venta
    return meses_sobre_umbral

# Función principal
def main():
    if len(sys.argv) != 2:
        print("Uso: python mayor_a.py <umbral>")
        return

    umbral = int(sys.argv[1])

    # Filtrar los meses que superan el umbral especificado
    meses_sobre_umbral = filtrar_meses_sobre_umbral(umbral)

    # Imprimir el resultado
    print(meses_sobre_umbral)

if __name__ == "__main__":
    main()
