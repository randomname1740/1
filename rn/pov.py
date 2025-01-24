def poveste():
    print("Bun venit la povestea interactivă!")
    print("Tu vei decide cursul acțiunii. Fă alegerile cu grijă!\n")

    print("Ești un aventurier care a ajuns în fața unei păduri misterioase.")
    print("Ce vei face?")
    print("1. Intri în pădure.")
    print("2. Ocolești pădurea.")

    alegere1 = input("\nAlege 1 sau 2: ")

    if alegere1 == "1":
        print("\nIntri în pădure și descoperi un castel vechi și înfricoșător.")
        print("Ce faci mai departe?")
        print("1. Intri în castel.")
        print("2. Îți continui drumul prin pădure.")

        alegere2 = input("\nAlege 1 sau 2: ")

        if alegere2 == "1":
            print("\nIntri în castel și descoperi o cameră plină de comori!")
            print("Dar... din spatele tău apare un dragon care păzește comoara.")
            print("Ce faci?")
            print("1. Încerci să te lupți cu dragonul.")
            print("2. Fugi cât de repede poți.")

            alegere3 = input("\nAlege 1 sau 2: ")

            if alegere3 == "1":
                print("\nÎți înfrunți frica și reușești să învingi dragonul. Ești un adevărat erou!")
                print("Povestea ta devine o legendă în regatul apropiat.")
            elif alegere3 == "2":
                print("\nFugi cât de repede poți și scapi cu viață, dar pierzi șansa de a lua comoara.")
                print("Trăiești să povestești altora despre aventura ta.")
            else:
                print("\nAlegere invalidă. Povestea ta se încheie aici.")
        elif alegere2 == "2":
            print("\nContinui drumul prin pădure, dar te pierzi în întunericul dens.")
            print("Din păcate, povestea ta se termină într-o notă misterioasă.")
        else:
            print("\nAlegere invalidă. Povestea ta se încheie aici.")
    elif alegere1 == "2":
        print("\nOcolești pădurea și ajungi la un sat liniștit.")
        print("Oamenii de aici îți spun povești despre pădurea blestemată.")
        print("Ce faci?")
        print("1. Te întorci să explorezi pădurea.")
        print("2. Rămâi în sat și trăiești o viață pașnică.")

        alegere2 = input("\nAlege 1 sau 2: ")

        if alegere2 == "1":
            print("\nTe întorci în pădure și îți încerci norocul. Cine știe ce aventuri te așteaptă!")
        elif alegere2 == "2":
            print("\nRămâi în sat și devii un povestitor renumit, relatând aventuri imaginare.")
        else:
            print("\nAlegere invalidă. Povestea ta se încheie aici.")
    else:
        print("\nAlegere invalidă. Povestea ta se încheie aici.")

# Pornim povestea
poveste()
