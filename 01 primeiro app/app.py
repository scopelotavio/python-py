#bibliotecas
import os

#definição
restaurantes = ['Yalla Habib', 'Madero', 'Sky Burger']

def exibir_nome_do_programa():
      print('''

      ██████████████████████████████████████████████████████████████████████████
      █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
      █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
      █▄▄▄▄▄█▄▄█▄▄█▄▄▄▄██▄▄▄▄█▄▄█▄▄███▄▄▄▄▄█▄▄█▄▄█▄▄▄███▄▄█▄▄█▄▄▄▄▄█▄▄▄▄▄█▄▄▄▄▄█
      
            ''')

def exibir_opcoes():
      print('1. Cadastrar restaurante')
      print('2. Listar restaurante')
      print('3. Ativar restaurante')
      print('4. Sair\n')

def opcao_invalida():
      print('Opção inválida!\n')
      voltar_ao_menu_principal()

def cadastrar_restaurante():
      exibir_subtitulos('Cadastro de novos restaurantes:')
      nome_restaurante = input('Digite o nome do restaurante: ')
      restaurantes.append(nome_restaurante)
      print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso.')
      voltar_ao_menu_principal()

def listar_restaurantes():
      exibir_subtitulos('Listando restaurantes:')
      # para cada restaurante na lista de restaurantes
      for restaurante in restaurantes:
            print(f'.{restaurante}')
      voltar_ao_menu_principal()

def escolher_opcao():
      try:
            opcao_escolhida = int(input('Escolha uma opção: \n'))
            print(f'Você escolheu a opção {opcao_escolhida}:')
            if opcao_escolhida == 1:
                  cadastrar_restaurante()
            elif opcao_escolhida == 2:
                  listar_restaurantes()
            elif opcao_escolhida ==3:
                  print('Ativar restaurante')
            elif opcao_escolhida == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      
      except ValueError:
            print('Erro: por favor, insira um número válido.')

def finalizar_app():
    exibir_subtitulos('Finalizado o app:')

def voltar_ao_menu_principal():
      input('\nDigite uma tecla para voltar ao menu principal')
      main()

def exibir_subtitulos(texto):
      os.system('cls')
      print(f'{texto}\n')
      

# CHAMAR FUNCAO

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()