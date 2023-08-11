from InquirerPy import prompt, inquirer
from InquirerPy.separator import Separator
from pprint import pprint
import time
import os
import sys

def quizHardwareClassico(perguntas_hardware):
    nome_equipe = str(input("Digite um nome para equipe: "))
    print(f"\n\nOlá {nome_equipe} vamos iniciar o quiz!! \n\n")
    pontuacao = 0
    for dic in perguntas_hardware:
        print(dic["pergunta"])
        for opcao in dic["opcoes"]:
            print(opcao)

        resposta = input("Digite sua respota: ").lower()
        if resposta == dic["resposta"]:
            pontuacao+=100
            print("\nResposta Certa\n")
        else:
            print("\nResposta Errada\n")
    
    print("Sua pontuação foi: ", pontuacao)


global ranking
ranking = {"Pedro":9999}

def main():

    menu = inquirer.select(
        message= "\n\ \Quiz de Hardware/ / \n",
        choices=[
            "Jogar",
            "Ranking",
            "Créditos",
            Separator(),
            "Sair"
        ]
    )

    perguntas_hardware = [
        {
            "type":"rawlist",       
            "message": "Qual componente do computador é responsável por armazenar dados permanentemente?",
            "choices": ["a) CPU", "b) RAM", "c) Disco rígido", "d) Placa de vídeo"]
        },
        {
            "type":"rawlist",       
            "message": "Que tipo de conexão é comum para conectar periféricos como teclado e mouse?",
            "choices": ["a) USB", "b) HDMI", "c) Ethernet", "d) VGA"]
        },
        {
            "type":"rawlist",   
            "message": "Qual componente do computador é responsável por executar instruções e realizar cálculos?",
            "choices": ["a) Monitor","b) Teclado","c) Mouse","d) CPU"]
        },
        {
            "type":"rawlist",   
            "message":"Qual é a função principal da memória RAM?",
            "choices": ["a) Armazenar permanentemente os dados","b) Controlar a temperatura interna do computador","c) Fornecer energia ao sistema","d) Armazenar temporariamente dados e programas em execução"]
        },
        {
            "type":"rawlist",   
            "message":"Qual é a função da placa-mãe em um computador?",
            "choices":["a) Fornecer energia elétrica","b) Armazenar programas e dados permanentemente","c) Conectar e comunicar todos os componentes de hardware","d) Controlar a temperatura interna"]
        },
        {
            "type":"rawlist",  
            "message":"Qual é o dispositivo de saída que exibe informações visuais na tela?",
            "choices":["a) Mouse","b) Teclado","c) Monitor","d) Impressora"]
        },
        {
            "type":"input",
            "message":"Digite seu nome:",
            "name":"name"
        }
    ]

    def answers(result, index, correct):
        return 100 if result[index] == correct else 0

    def typeprint(string):
        for char in string:
            time.sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()


    action = menu.execute()
    if action:
        match action:
            case "Jogar":
                os.system("cls")
                result = prompt(perguntas_hardware)

                points = 0
                points += answers(result, 0, "c) Disco rígido")
                points += answers(result, 1, "a) USB")
                points += answers(result, 2, "d) CPU")
                points += answers(result, 3, "d) Armazenar temporariamente dados e programas em execução")
                points += answers(result, 4, "c) Conectar e comunicar todos os componentes de hardware")
                points += answers(result, 5, "c) Monitor")
                ranking[result['name']] = points

                print(f"Você fez {points} pontos!")
                time.sleep(5)

            case "Ranking":
                print(f"{'Nome':<8} {'Pontos':<15}")
                for key, value in ranking.items():
                    print(f"{key:<8} {value:<15}")
            case "Créditos":
                typeprint("Desenvolvedores: Wesley Vieira e Pedro Lucas Simões\n")
                typeprint("Designers: Pedro Lucas Simões, Wesley Vieira e Carlos Vitor\n")
                typeprint("Apoio moral: Ryan Ribeiro e Humberto Nunes\n")
                typeprint("Logística e Transporte: André Maxwell\n")
            case "Sair":
                exit()


if __name__ == "__main__":
    while True:
        main()