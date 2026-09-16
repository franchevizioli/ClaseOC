while True:
    mp="piedra"
    s=input("ingrese piedra, papel o tijera:")
    piedra="piedra"
    papel="papel"
    tijera="tijera"
    if s== papel :
        print("ganaste")
        break
    elif s==piedra :
        print("empate")
        break
    elif s==tijera :
        print("perdiste")
        break
    else:
        print("error,ingrese un argumento valido")