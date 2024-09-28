'''
Exercícios
1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
'''
import os

def exercicio_01():
    nome_exercicio('2')
    listaNumeros = [1,2,3,4,5,6,7,8,9,10]
    listaNomes = ['Bruno', 'Danilo', 'Otavio', 'Lucas']
    listaAnos = [1993, 2024]
    print(listaNumeros)
    print(listaNomes)
    print(listaAnos)




def exercicio_02():
    nome_exercicio('2')
    listaEx02 = [1,2,3,4,5,6,7,8,9,10]
    for elemento in listaEx02:
        print(f'{elemento}')

def exercicio_03():
    nome_exercicio('3')
    listaNumeros = [1,2,3,4,5,6,7,8,9,10]
    soma = 0
    for numero in listaNumeros:
        if numero % 2 != 0:
            soma = soma + numero 
        else:
            soma = soma
    print(soma)

def exercicio_04():
    nome_exercicio('4')
    listaNumeros = [1,3,2,4,5,6,7,8,9,10]
    listaNumeros_decrescente = sorted(listaNumeros, reverse=True)
    try:
        for numero in listaNumeros_decrescente:
            print(f'{numero}')
    except ValueError:
            print('Erro.')

def exercicio_05():
    tabuada = [1,2,3,4,5,6,7,8,9,10]
    try:
        numero_do_usuario = int(input('Escolha um número: '))
    
        #Calcular a tabuada
        for numero in tabuada:
            resultado = numero * numero_do_usuario
            print(f'{numero_do_usuario} x {numero} = {resultado}' )

    except ValueError:
        print('Erro. Digite um número.')
        exercicio_05()

def exercicio_06():
    listaNumeros = [1,2,3,4,5,6,7,8,9,10]
    soma = 0
    try:
        for elemento in listaNumeros:
            soma = soma + elemento
    except ValueError:
        print('Erro.')
    print(f'A soma dos valores da lista é {soma}')

def exercicio_07(lista):
    try:
        soma = sum(lista)
        solucao = soma / len(lista)
        return solucao
    except ZeroDivisionError:
        print
        return 'Erro. Divisão por 0'
    except ValueError:
        return 'Erro. Digite um valor válido'



def nome_exercicio(titulo):
    print(f'\nExercício {titulo}:')

# CHAMAR FUNCAO

def main():
    os.system('cls')
    
    #Exercicio 01
    exercicio_01()
    
    exercicio_02()
    exercicio_03()
    exercicio_04()
    exercicio_05()
    exercicio_06()
    
    #Exercicio 07
    minha_lista = [1,2,3,4,5,6,7,8,9]
    media = exercicio_07(minha_lista)
    print(f'A média é: {media}')

if __name__ == '__main__':
    main()