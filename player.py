#!/usr/bin/env python3
"""
Implemente aqui o seu código para o jogador.

Seu principal objetivo é implementar a função `player`, que deve retornar uma lista de 4 cores, o seu próximo palpite.
Como exemplo, a função abaixo retorna um palpite aleatório.

Dicas:
- Você pode implementar outras funções para auxiliar a função `player`.
- Você pode salvar informações entre os palpites usando variáveis globais (fora de qualquer função).
"""
from colors import *
from random import sample

# Cores disponíveis para o palpite
colors = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]

'''
Lista com as cores da lista acima (as posições nessa lista refletem as posições das cores na lista "colors
True significa que a cor está na senha, False indica que a cor não está na senha
Por padrão, todas as cores estão definidas como False para análise posterior
'''

cores_certas = [0, 1, 2, 3, 4, 5, 6] # Valores iniciais que serão modificados ao longo das tentativas. Eles representam meramente a posição, na lista "colors", das cores representadas.

# Cores que a função "analise" irá retornar para a função player usar como chute, e que posteriormente será usada para armazenr as cores que sabidamente fazem parte da senha
cores_codigo = []

opcoes_pares = [] # Variável para o caso extremamente específico em que, após análise preliminar, sabemos que duas cores estão na senha e uma delas é o vermelho



 
def player(guess_hist, res_hist):
    """
    As cores disponíveis são: RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE.

    Parâmetros:
    - guess_hist: lista de palpites anteriores
    - res_hist: lista de resultados anteriores

    Retorna:
    - lista de 4 cores
    """

    global cores_codigo
    global cores_certas

    chute = []

    if len (guess_hist) < 4:
        chute = colors[len(guess_hist) : len(guess_hist) + 4]
    elif len (guess_hist) == 4:
        chute = [ORANGE, BLACK, WHITE, RED]
    elif res_hist[len(res_hist) - 1][0] != 4:
        chute = analise(guess_hist, res_hist)
    else:
        cores_codigo = guess_hist[len(guess_hist) - 1]
        chute = sample(cores_codigo)


    return chute 


def analise (hist_chutes, hist_result):
    global cores_codigo
    global opcoes_pares

    for i in range(len(hist_result) - 1):
            '''
            Análise dos resultados das 5 primeiras jogadas que a função player fez. Usamos como lógica a função jogar todas as cores em uma ordem específica, sempre trocando a última da linha do código pela próxima na lista completa das cores, e então ver se a quantidade de cores certas aumentou, diminuiu ou permaneceu constante.
            Se tiver aumentado: a cor que entrou está na senha e a cor que saiu, não.
            Se tiver diminuído: a cor que entrou não está na senha e a cor que saiu está.
            Se permanecer constante: as cores que entrou e que saiu são interdependentes. Se uma estiver na senha a outra também está, e vice-versa.
            '''
            if hist_result[i + 1][0] > hist_result[i][0]:
                cores_certas[colors.index(hist_chutes[i + 1][3])] == True
                cores_certas[colors.index(hist_chutes[i][0])] == False
            elif hist_result[i + 1][0] < hist_result[i][0]:
                cores_certas[colors.index(hist_chutes[i][0])] == True
                cores_certas[colors.index(hist_chutes[i+1][3])] == False
            else:
                cores_certas[colors.index(hist_chutes[i][0])] == colors.index(hist_chutes[i + 1][3])
    
    for i in range(len(cores_certas)):
        if cores_certas[i] == True:
            cores_codigo.append(colors[i])

    '''
    Análise posterior da quantidade de cores que sabemos que estão na senha para definirmos, pela lógica, se as cores interdependentes também estão ou não. Avaliamos caso a caso nessa situação, ao que não encontramos solução melhor.'''

    if cores_certas.count(True) == 1:
        cores_certas[cores_certas[0]] = True
        cores_certas[0] = True
        for i in range(len(cores_certas)):
            if cores_certas[i] == 0:
                cores_certas[i] = True
        
        cores_codigo = cores_na_senha(cores_certas)
        return cores_codigo
    elif cores_certas.count(True) == 3:
        for i in range(len(cores_certas)):
            if type(cores_certas[i]) == int and cores_certas[cores_certas[i]] == True:
                cores_certas[i] = True
        
        cores_codigo = cores_na_senha(cores_certas)
        return cores_codigo
    else:
        return sample(colors, 4)
                
                    
        

def cores_na_senha (suposicoes):
    senha = []

    for i in range(len(suposicoes)):
        if suposicoes[i] == True:
            senha.append(colors[i])

    return senha
