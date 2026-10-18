from colorama import Fore, Style, init

init()

niveis = [1, 2, 3, 4, 5]

mensagens = [
    "Nivel 1 - Muito baixo (critico)",
    "Nivel 2 - Baixo",
    "Nivel 3 - Medio",
    "Nivel 4 - Alto",
    "Nivel 5 - Muito alto (alerta)"
]

def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE

for nivel in niveis:
    cor = definir_cor(nivel)
    mensagem = mensagens[nivel - 1]
    print(cor + mensagem + Style.RESET_ALL)
