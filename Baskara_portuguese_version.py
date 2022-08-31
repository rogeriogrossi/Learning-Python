import math
from typing import Any
from time import sleep
def linhas(mensagem):
    print('\33[92m-=\33[m'*15)
    print(f'{mensagem:^30}\33[m')
    print('\33[92m-=\33[m'*15)



def baskara():
    m_ini = '\33[35mBem vindo ao Baskara\33[m'
    print('*'*30,'\n')
    print(f'{m_ini:^30}','\n')
    print('*' * 30, '\n')
    sleep(2)
    print('Vamos resolver uma equação do tipo \33[1;34m ax^2 + bx + c = 0\33[m\n')
    sleep(2)
    print('Você vai precisar digitar os coeficientes da equação. Vamos começar?')
    simb = '.'
    for p in range(0,3):
        print(f'{simb:^50}')
        sleep(1)
    del simb
    try:
        a = int(input('Digite o coeficiente de x^2 (a):'))
        b = int(input('Digite o coeficiente de x (b):'))
        c = int(input('Digite a constante (c):'))
    except:
        linhas('Ops... algo deu errado. Verifique se você digitou apenas números.')

    if a == 0 and b==0:
        linhas('Essa não é uma equação válida. Tente novamente.')
        baskara()
    else:
        if a == 0 and b!=0:
            while True:
                linhas('Você está tentando resolver uma equação do primeiro grau')
                continua = input('Deseja continuar? [S/N]').upper()
                if continua == 'S':
                    print('#' * 30, '\n')
                    print(f'\33[91m A resposta é x = {c/b}\33[m','\n')
                    print('#' * 30, '\n')
                    break
                elif continua == 'N':
                    baskara()
                    break
                else:
                    linhas('Você não digitou um valor valido. Digite S ou N')

        else:
            bq = b**2
            if bq < 4*a*c:
                linhas('Delta complexo!')
                delta = round(math.sqrt(abs(b ** 2 - 4 * a * c)),2)
                print('#' * 30, '\n')
                print('\33[91mAs raizes são: ', -b,'+-',delta,'j','\n\33[m')
                print('#' * 30, '\n')
            else:
                delta = math.sqrt(b**2 - 4*a*c)
                xmais = (-b + delta)/(2*a)
                xmenos = xmais -delta/a
                print('#'*30,'\n')
                print('\33[91mAs raizes são: ', round(xmais,2), 'e', round(xmenos,2),'\n\33[m')
                print('#' * 30,'\n')
    linhas('Obrigado e volte sempre')



baskara()

