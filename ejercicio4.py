sa = False
while sa == False:
    print("la fabulosa maravillosa alocada \n extrafalaria hermosa \n y fantastica maquina \n para definir impar par")
    c = int(input("ingresa un numero criatura del señor \n si quieres salir pulsa 0 \n >>"))
    if c == 0:
        sa = True
        print("adiosito wiwiwiwiwiwiwi")
    else:
        if c % 2 == 0:
            print("el numero es par")
        else:
            print("este numero no es par tun tun tun tuuuuun")