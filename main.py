from time import sleep
from unidecode import unidecode
import os, random

palavras = ["gato", "cachorro", "vermelho", "sorriso", "python", "cantar", "carro"]

palavra_escolhida_form = random.choice(palavras).upper()
palavra_escolhida = list(unidecode(palavra_escolhida_form))

def restart():
    if jogando == False:
        os.system('cls')
        pergunta = str(input("Deseja jogar novamente? (s/n): "))
        if pergunta == "s":
            os.system('cls')
            print("Recomeçando jogo.....")
            jogo()
        elif pergunta == "n":
            print(f"Ok, tchau.\n"*5)
        else:
            restart()

def jogo():
    global jogando
    jogando = True

    chances = 6
    Palpites = []
    palavra_len = list("_" * len(palavra_escolhida))
    while jogando:
        if chances == 0:
            jogando = False
            print(f"Jogo finalizado você perdeu\n{chances}/6")
        else:
            palpite = input("Digite uma letra: ").upper()
            if not palpite.isalpha() or len(palpite) != 1:
                os.system('cls')
                print(f"Digite uma única letra e não adicione números ou outros caracteres.\n{chances}/6 Chances")
                print(palavra_len)
            else:
                if palpite in Palpites:
                    os.system('cls')
                    print(f"Você já usou essa letra.\n{chances}/6 Chances")
                    print(palavra_len)
                else:
                    Palpites.append(palpite)
                    if palpite in palavra_escolhida:
                        for i, letter in enumerate(palavra_escolhida):
                            if palpite == letter:
                                os.system('cls')
                                palavra_len[i] = letter
                                print(f"{chances}/6 Chances\n{palavra_len}")
                                if "_" not in palavra_len:
                                    jogando = False
                                    os.system('cls')
                                    print(f"{chances}/6 Chances\nJogo finalizado\nA palavra era {palavra_escolhida_form}.")
                    else:
                        chances -= 1
                        os.system('cls')
                        print(f"Letra não eencontrada na palavra {chances}/6 Chances")
                        print(palavra_len)
    else:
        restart()
                    
if __name__ == "__main__":
    jogo()
