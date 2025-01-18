def adunare(a, b):
    return a + b

def scadere(a, b):
    return a - b

def inmultire(a, b):
    return a * b

def impartire(a, b):
    if b != 0:
        return a / b
    else:
        return "Eroare: Împărțire la zero!"

# Funcția principală
def calculator():
    print("Bun venit la Calculatorul Simplu!")
    print("Selectează o operație:")
    print("1. Adunare (+)")
    print("2. Scădere (-)")
    print("3. Înmulțire (*)")
    print("4. Împărțire (/)")

    while True:
        try:
            # Alegerea operației
            optiune = input("\nAlege o opțiune (1/2/3/4) sau 'q' pentru a ieși: ")
            if optiune.lower() == 'q':
                print("La revedere!")
                break

            if optiune not in ['1', '2', '3', '4']:
                print("Opțiune invalidă. Încearcă din nou.")
                continue

            # Introducerea numerelor
            num1 = float(input("Introdu primul număr: "))
            num2 = float(input("Introdu al doilea număr: "))

            # Calcul și afișare rezultat
            if optiune == '1':
                print(f"Rezultatul: {num1} + {num2} = {adunare(num1, num2)}")
            elif optiune == '2':
                print(f"Rezultatul: {num1} - {num2} = {scadere(num1, num2)}")
            elif optiune == '3':
                print(f"Rezultatul: {num1} * {num2} = {inmultire(num1, num2)}")
            elif optiune == '4':
                print(f"Rezultatul: {num1} / {num2} = {impartire(num1, num2)}")

        except ValueError:
            print("Te rog introdu un număr valid.")

# Rularea calculatorului
calculator()
