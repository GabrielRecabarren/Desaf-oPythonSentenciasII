from string import ascii_lowercase
import getpass
import sys

def fuerza_bruta(password):
    intentos = 0
    for letra_password in password:
        for letra in ascii_lowercase:
            intentos += 1
            if letra_password == letra:
                break
    return intentos

def main():
    if len(sys.argv) == 2:
        password = sys.argv[1].lower()
    else:
        password = getpass.getpass("Ingrese la contraseña: ").lower()
    intentos = fuerza_bruta(password)
    print(f"La contraseña fue forzada en {intentos} intentos")

if __name__ == "__main__":
    main()
