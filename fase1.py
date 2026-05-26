#                                ***PROJETO BIPEX. FASE 2 ☠  ***

from inputimeout import inputimeout, TimeoutOccurred

oi = input("digita: ")

if oi == "oi":
    try:
        mensagem = inputimeout(
            prompt="digite um negocio ae: ",
            timeout=15
        )
    except TimeoutOccurred:
        exit()

    if mensagem == "oi":
        exit()

    nome = input("digite seu nome: ")
    idade = int(input(f"digite sua idade, {nome}: "))

    if idade <= 18:
        print(f"Menor de idade: {idade} anos")
        exit()

    print("Acesso liberado")

    locked = input("Digite o acesso: ")

    contador = 0

    while contador < 3:
        locked = input("Digite seu acesso: ")

        if locked == "2233":
            print("PARABÉNS acesso liberado")
            print("agora voce pode")
            print(f"Bem-vindo {nome}, idade {idade}")
            break

        else:
            contador += 1
            print("Senha incorreta")

    if contador == 3:
        print("Número máximo de tentativas atingido")
        exit()

else:
    usuarios = []
    usuarios.extend(["Guilherme","baiano","juninho"])

    print(usuarios)

    usuarios.append(input("LISTA DE SABADO: "))
    print(usuarios)

    alertas = []
    alerta = input("agora vamos a lista de alerta: ")
    alertas.extend([alerta, "alerta1", "alerta2", "alerta3"])

    print(alertas)
    for usuario in usuarios:
        print (usuario)
















