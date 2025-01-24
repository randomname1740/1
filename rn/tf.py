import random

# Întrebări și răspunsuri
intrebari = [
    {"intrebare": "Soarele este o stea.", "raspuns": True},
    {"intrebare": "Apa îngheață la 50°C.", "raspuns": False},
    {"intrebare": "Luna este mai mare decât Pământul.", "raspuns": False},
    {"intrebare": "Un an are 365 de zile.", "raspuns": True},
    {"intrebare": "Piramidele din Egipt au fost construite de romani.", "raspuns": False},
    {"intrebare": "Python este un limbaj de programare.", "raspuns": True},
    {"intrebare": "Delfinii sunt mamifere.", "raspuns": True},
]

# Funcția principală
def joc_adevarat_sau_fals():
    print("Bun venit la jocul Adevărat sau Fals!")
    print("Răspunde cu 'A' pentru Adevărat sau 'F' pentru Fals.\n")

    scor = 0  # Scorul inițial
    random.shuffle(intrebari)  # Amestecăm întrebările pentru diversitate

    for intrebare in intrebari:
        print(intrebare["intrebare"])
        raspuns_utilizator = input("Răspunsul tău (A/F): ").strip().upper()

        if raspuns_utilizator not in ["A", "F"]:
            print("Răspuns invalid! Trebuie să răspunzi cu 'A' sau 'F'.")
            continue

        # Verificăm răspunsul
        raspuns_corect = intrebare["raspuns"]
        if (raspuns_utilizator == "A" and raspuns_corect) or (raspuns_utilizator == "F" and not raspuns_corect):
            print("Corect!")
            scor += 1
        else:
            print("Greșit!")

        print(f"Scorul tău: {scor}\n")

    print(f"Joc terminat! Scorul final: {scor} din {len(intrebari)}")

# Pornim jocul
joc_adevarat_sau_fals()
