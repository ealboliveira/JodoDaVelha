def inicio():
    jogador = 1
    linha, coluna = 0, 0
    numeroJogadas = 0
    vencedor = 0
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

    print("Olá! Este é um jogo da velha! Você deve jogar com outra pessoa!")
    print("Digite a posição da sua jogada na seguinte forma: (linha,coluna).")
    print("Ou seja, linha 2 e coluna 2 será: (1,1)")
    print("Antes de começarmos, veja as posições para as jogadas:")
    print("[ (0,0) ]\t[ (0,1) ]\t[ (0,2) ]")
    print("[ (1,0) ]\t[ (1,1) ]\t[ (1,2) ]")
    print("[ (2,0) ]\t[ (2,1) ]\t[ (2,2) ]")
    print()
    print("A primeira pessoa que jogar será (X) e a segunda pessoa que jogar será (O).")
    print("Ganha quem fizer linha, coluna ou diagonal. Bom jogo!")

    for i in range(3):
        for j in range(3):
            tabuleiro[i][j] = ' '

    print("#####################################################")
    print("Este é o nosso tabuleiro, por favor, inicie a jogada!")
    print("#####################################################")

    for i in range(3):
        for j in range(3):
            print("[", tabuleiro[i][j], "]", end="")
        print()

    while vencedor == 0 and numeroJogadas < 9:
        if jogador == 1:
            print("\nVocê é o jogador", jogador, ". Por favor escolha sua jogada:")
            linha = int(input("\nDigite uma linha: "))
            coluna = int(input("Digite uma coluna: "))

            if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' ':
                print("Você digitou:", linha, ",", coluna, ".")
                tabuleiro[linha][coluna] = 'X'
                print("A posição (", linha, ",", coluna, ") será preenchida com (X).\n")

                jogador = 2

                for i in range(3):
                    for j in range(3):
                        print("[", tabuleiro[i][j], "]", end="")
                    print()
            else:
                print("#################################")
                print("Você digitou: uma opção inválida!")
                print("#################################")

                for i in range(3):
                    for j in range(3):
                        print("[", tabuleiro[i][j], "]", end="")
                    print()
        else:
            print("\nVocê é o jogador", jogador, ". Por favor escolha sua jogada:")
            linha = int(input("\nDigite uma linha: "))
            coluna = int(input("Digite uma coluna: "))

            if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' ':
                print("Você digitou:", linha, ",", coluna, ".")
                tabuleiro[linha][coluna] = 'O'
                print("A posição (", linha, ",", coluna, ") será preenchida com (O).\n")

                jogador = 1

                for i in range(3):
                    for j in range(3):
                        print("[", tabuleiro[i][j], "]", end="")
                    print()
            else:
                print("#################################")
                print("Você digitou: uma opção inválida!")
                print("#################################")

                for i in range(3):
                    for j in range(3):
                        print("[", tabuleiro[i][j], "]", end="")
                    print()

        print("\n\n")

        if vencedor == 0:
            for i in range(3):
                if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == 'X':
                    vencedor = 1
                elif tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == 'O':
                    vencedor = 2

            for i in range(3):
                if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == 'X':
                    vencedor = 1
                elif tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == 'O':
                    vencedor = 2

            if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'X' or \
                    tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'X':
                vencedor = 1
            elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == 'O' or \
                    tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == 'O':
                vencedor = 2

            numeroJogadas += 1

    if vencedor == 1:
        print("\nA pessoa que escolheu (X) venceu!")
    elif vencedor == 2:
        print("\nA pessoa que escolheu (O) venceu!")
    else:
        print("\nDeu VELHA! Jogue novamente!")

inicio()
