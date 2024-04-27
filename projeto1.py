import random
import sys

# Função principal que executa o programa
def main():
    dirs = (0, 0, 0, 0)  # Tipo de dados tuple para controlar as direções

    # Locais do Jedi's Housing
    entrada = {'name': 'Entrada', 'directions': dirs, 'msg': 'Você está na entrada'}
    sala_estar = {'name': 'Sala de Estar', 'directions': dirs, 'msg': 'Você está na sala de estar'}
    cozinha = {'name': 'Cozinha', 'directions': dirs, 'msg': 'Você está na cozinha'}
    salaEstudos = {'name': 'Sala de Estudos', 'directions': dirs, 'msg': 'Você está na sala de estudos'}
    quartoMeninos = {'name': 'Dormitório dos meninos Jedi', 'directions': dirs, 'msg': 'Você está no quarto dos meninos'}
    quartoMeninas = {'name': 'Dormitório das meninas Jedi', 'directions': dirs, 'msg': 'Você está no quarto das meninas'}

    # Definição das direções de cada local (N,L,S,O) conforme o mapa
    entrada['directions'] = (0, sala_estar, 0, 0)
    sala_estar['directions'] = (salaEstudos, quartoMeninas, cozinha, entrada)
    cozinha['directions'] = (sala_estar, 0, 0, 0)
    salaEstudos['directions'] = (0, quartoMeninos, sala_estar, 0)
    quartoMeninos['directions'] = (0, 0, quartoMeninas, salaEstudos)
    quartoMeninas['directions'] = (salaEstudos, 0, 0, sala_estar)

    # locais onde o sabre de luz pode estar
    room = [sala_estar, cozinha, salaEstudos, quartoMeninos, quartoMeninas]
   
    # colocar o sabre de luz em um local aleatório + darth vader em um local aleatório
    room_with_lightsaber = random.choice(room)
    room_with_vader = random.choice(room) 

    # Variável para verificar se o sabre de luz foi encontrado
    lightsaber_found = False
    local_atual = entrada

    print('Bem-vindo Padawan! Você consegue localizar onde está o seu sabre de luz?')

    # Função para ir para uma direção específica
    def mover(direction):
        nonlocal local_atual #se não for o local atual, segue

       # 'directions' contém as possíveis direções nas quais o jogador pode se mover
       # representa a direção escolhida pelo jogador
        proximo_local = local_atual['directions'][direction]
      
        if proximo_local:   #Verifica se há algo no próximo local
            local_atual = proximo_local
            print(local_atual['msg'])

            # se o próximo local for onde Darth Vader está, o jogo termina
            if local_atual == room_with_vader:
              print("Darth Vader te encontrou. Fim de jogo!")
              sys.exit() #módulo para encerrar bloco de comando dentro do if

              
            # se o próximo local for onde o sabre de luz está, o jogador vence o jogo
            elif local_atual == room_with_lightsaber:
                print("Você encontrou o sabre de luz! Parabéns, você venceu!") 
      
                nonlocal lightsaber_found
                lightsaber_found = True
          
        else:
          print("Você não pode ir nessa direção.")

    # Função para exibir o menu e permitir ao jogador escolher uma direção
    def menu():
        while not lightsaber_found: 
            print("------------------------ Jedi's Housing ------------------------")
            print("Você está em", local_atual['name'])
            print("N - Norte")
            print("S - Sul")
            print("L - Leste")
            print("O - Oeste")
            print("X - Encerrar jogo")

            opcao = input("Escolha uma direção: ").upper() #upper retorna os caracteres em maiúsculo

            if opcao == "N":
                mover(0)  # 0 representa o norte em Dirs 
            elif opcao == "L":
                mover(1)  # 1 representa o leste em Dirs
            elif opcao == "S":
                mover(2)  # 2 representa o sul em Dirs
            elif opcao == "O":
                mover(3)  # 3 representa o oeste em Dirs 
            elif opcao == "X":
                print("Programa Finalizado.")
                break 
            else:
                print("Escolha uma direção válida.")

    menu()

# Executa a função main
main()
