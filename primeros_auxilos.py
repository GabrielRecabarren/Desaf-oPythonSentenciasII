def primeros_auxilios():
    print("Inicio:")
    respuesta = input("- Responde a estímulo (si/no): ")
    if respuesta.lower() == "si":
        print("Evaluar si llevarlo al hospital más cercano.")
        return
    elif respuesta.lower() == "no":
        print("Abrir la vía aérea:")
        respira = input("- ¿Respira? (si/no): ")
        if respira.lower() == "si":
            print("Permitir suficiente ventilación.")
            return
        elif respira.lower() == "no":
            print("Administrar 5 ventilaciones y llamar a la ambulancia.")
            while True:
                signos_vida = input("- ¿Signos de vida? (si/no): ")
                if signos_vida.lower() == "no":
                    print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
                    llego_ambulancia = input("- ¿Llegó la ambulancia? (si/no): ")
                    if llego_ambulancia.lower() == "si":
                        return
                    elif llego_ambulancia.lower() == "no":
                        continue  # Vuelve a preguntar por los signos vitales
                    else:
                        print("Respuesta no válida.")
                elif signos_vida.lower() == "si":
                    print("Evaluar la espera de la ambulancia:")
                    llego_ambulancia = input("- ¿Llegó la ambulancia? (si/no): ")
                    if llego_ambulancia.lower() == "si":
                        return
                    elif llego_ambulancia.lower() == "no":
                        continue  # Vuelve a preguntar por los signos vitales
                    else:
                        print("Respuesta no válida.")
                else:
                    print("Respuesta no válida.")
        else:
            print("Respuesta no válida.")
    else:
        print("Respuesta no válida.")

# Ejecutar la función principal
primeros_auxilios()
