from whaaaaat import style_from_dict, Token, prompt, print_json, default_style


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


def main():
    perguntas_hardware = [
        {
            "pergunta": "Qual componente do computador é responsável por armazenar dados permanentemente?",
            "opcoes": ["a) CPU", "b) RAM", "c) Disco rígido", "d) Placa de vídeo"],
            "resposta": "c"
        },
        {
            "pergunta": "Que tipo de conexão é comum para conectar periféricos como teclado e mouse?",
            "opcoes": ["a) USB", "b) HDMI", "c) Ethernet", "d) VGA"],
            "resposta": "a"
        }
    ]

    quizHardwareClassico(perguntas_hardware)
if __name__ == "__main__":
    main()