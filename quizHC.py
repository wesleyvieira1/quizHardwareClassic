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
        },
        {
            "pergunta": "Qual componente do computador é responsável por executar instruções e realizar cálculos?",
            "opcoes": ["a) Monitor","b) Teclado","c) Mouse","d) CPU (Unidade Central de Processamento)"],
            "resposta":"d"
        },
        {
            "pergunta":"Qual é a função principal da memória RAM?",
            "opcoes": ["a) Armazenar permanentemente os dados","b) Controlar a temperatura interna do computador","c) Fornecer energia ao sistema","d) Armazenar temporariamente dados e programas em execução"],
            "reposta": "d"
        },
        {
            "pergunta":"Qual é a função da placa-mãe em um computador?",
            "opcoes":["a) Fornecer energia elétrica","b) Armazenar programas e dados permanentemente","c) Conectar e comunicar todos os componentes de hardware","d) Controlar a temperatura interna"],
            "reposta": "c"
        },
        {
            "pergunta":"Qual é o dispositivo de saída que exibe informações visuais na tela?",
            "opcoes":["a) Mouse","b) Teclado","c) Monitor","d) Impressora"],
            "reposta":"c"
        }
    ]

    quizHardwareClassico(perguntas_hardware)
if __name__ == "__main__":
    main()