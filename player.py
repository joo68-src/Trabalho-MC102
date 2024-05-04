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

cores_certas = [False, False, False, False, False, False, False]


def player(guess_hist, res_hist):
    global colors
    global cores_certas

    """
    As cores disponíveis são: RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE.

    Parâmetros:
    - guess_hist: lista de palpites anteriores
    - res_hist: lista de resultados anteriores

    Retorna:
    - lista de 4 cores
    """
    
    chute = []
    
    if len (guess_hist) < 4:
        chute = colors [len(guess_hist) : len(guess_hist) + 3]
    elif len (guess_hist) == 4:
        chute = colors [ORANGE, BLACK, WHITE, RED]
    else:
        for i in range(len(res_hist) - 1):
            if res_hist[i + 1] > res_hist[i]:
                cores_certas[colors.index(guess_hist[i + 1][3])] == True
            elif res_hist[i + 1] < res_hist[i]:
                cores_certas[colors.index(guess_hist[i][0])] == True
            else: 
                cores_certas[colors.index(guess_hist[i + 1][3])] == colors.index(guess_hist[i][0])

    return chute
    # return sample(colors, 4)  Exemplo: retorna um palpite aleatório
