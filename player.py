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

def analise (hist_chutes, hist_result):
    cores_codigo = []
    for i in range(len(hist_result) - 1):
            if hist_result[i + 1][0] > hist_result[i][0]:
                cores_certas[colors.index(hist_chutes[i + 1][3])] == True
                cores_certas[colors.index(hist_chutes[i][0])] == False
            elif hist_result[i + 1][0] < hist_result[i][0]:
                cores_certas[colors.index(hist_chutes[i][0])] == True
                cores_certas[colors.index(hist_chutes[i+1][3])] == False
            else: 
                cores_certas[colors.index(hist_chutes[i + 1][3])] == colors.index(hist_chutes[i][0])
    if cores_certas.count(True) == 1:
        cores_certas[cores_certas[0]] = True
        cores_certas[0] = True
        for i in range(len(cores_certas)):
            if cores_certas[i] == 0:
                cores_certas[i] = True
    elif cores_certas.count(True) == 2:
        cores_dependentes = 0
        for i in range(len(cores_certas)):
            if type(cores_certas[i]) == int and cores_certas[i] != i:
                cores_dependentes += 1

def player(guess_hist, res_hist):
    """
    As cores disponíveis são: RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE.

    Parâmetros:
    - guess_hist: lista de palpites anteriores
    - res_hist: lista de resultados anteriores

    Retorna:
    - lista de 4 cores
    """

    global cores_certas

    chute = []

    if len (guess_hist) < 4:
        chute = colors[len(guess_hist) : len(guess_hist) + 4]
    elif len (guess_hist) == 4:
        chute = [ORANGE, BLACK, WHITE, RED]
    else:
        chute = sample(analise(guess_hist, res_hist))

    return chute
