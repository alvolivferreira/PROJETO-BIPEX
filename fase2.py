from inputimeout import inputimeout, TimeoutOccurred
import json


# -----------------------------
# LOGIN SIMPLES
# -----------------------------
def login():
    try:
        mensagem = inputimeout(
            prompt="digite um negocio ae: ",
            timeout=15
        )
    except TimeoutOccurred:
        print("Tempo esgotado")
        return False

    if mensagem == "oi":
        print("Encerrando login...")
        return False

    nome = input("digite seu nome: ")
    idade = int(input(f"digite sua idade, {nome}: "))

    if idade <= 18:
        print(f"Menor de idade: {idade} anos")
        return False

    print("Acesso liberado")
    return nome, idade


# -----------------------------
# SISTEMA DE SENHA
# -----------------------------
def sistema_senha(nome, idade):
    contador = 0

    while contador < 3:
        senha = input("Digite seu acesso: ")

        if senha == "2233":
            print("PARABÉNS acesso liberado")
            print(f"Bem-vindo {nome}, idade {idade}")
            return True
        else:
            contador += 1
            print("Senha incorreta")

    print("Número máximo de tentativas atingido")
    return False


# -----------------------------
# MODO ALTERNATIVO (LISTAS)
# -----------------------------
def modo_alternativo():
    usuarios = ["Guilherme", "baiano", "juninho"]

    print("\nLista inicial:", usuarios)

    novo_usuario = input("LISTA DE SABADO: ")
    usuarios.append(novo_usuario)

    print("Lista atualizada:", usuarios)

    alertas = []

    alerta = input("agora vamos a lista de alerta: ")
    alertas.extend([alerta, "alerta1", "alerta2", "alerta3"])

    print("Alertas:", alertas)

    for usuario in usuarios:
        print("Usuário:", usuario)


# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------
def main():
    oi = input("digita: ")

    if oi == "oi":
        resultado = login()

        if not resultado:
            return

        nome, idade = resultado
        sistema_senha(nome, idade)

    else:
        modo_alternativo()


# -----------------------------
# EXECUÇÃO
# -----------------------------
main()

# ------------------
# SALVAR USUARIO
# ------------------
def salvar_usuario(nome, idade):

    usuario = {
        "nome": nome,
        "idade": idade
    }
    try:
        with open ("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
    except FileNotFoundError:
        usuarios = []
    usuarios.append(usuario)

    with open("usuarios.json", "w") as arquivo
        json.dump(usuarios, arquivo, indent=4)