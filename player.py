#!/usr/bin/env python3

from colors import *
from random import sample

# Cores disponíveis para o palpite
colors = [RED, GREEN, BLUE, YELLOW, ORANGE, BLACK, WHITE]

# Dicionário com as relações das cores. As com chave "True" são cores que estão na senha, e as com chave "False" não estão na senha
relacoes = {True : [], False : [], "dependencias" : []}

def player(guess_hist, res_hist):
    
    if len (guess_hist) < 4:
        chute = colors[len(guess_hist) : len(guess_hist) + 4]
    elif len (guess_hist) == 4:
        chute = [ORANGE, BLACK, WHITE, RED]
    elif res_hist[len(res_hist) - 1][0] == 4:
        cores_codigo = guess_hist[len(guess_hist) - 1]
        chute = sample(cores_codigo)
    else:    
        chute = analise(guess_hist, res_hist)

    return chute 


def analise (hist_chutes, hist_result):

    for i in range(len(hist_result) - 1):
        '''
        Análise dos resultados das 5 primeiras jogadas que a função player fez. Usamos como lógica a função jogar todas as cores em uma ordem específica, sempre trocando a última da linha do código pela próxima na lista completa das cores, e então ver se a quantidade de cores certas aumentou, diminuiu ou permaneceu constante.
        Se tiver aumentado: a cor que entrou está na senha e a cor que saiu, não.
        Se tiver diminuído: a cor que entrou não está na senha e a cor que saiu está.
        Se permanecer constante: as cores que entrou e que saiu são interdependentes. Se uma estiver na senha a outra também está, e vice-versa.
        '''
        if hist_result[i + 1][0] > hist_result[i][0]:
            relacoes[True].append(colors.index(hist_chutes[i + 1][3]))
            relacoes[False].append(colors.index(hist_chutes[i][0]))
        elif hist_result[i + 1][0] < hist_result[i][0]:
            relacoes[True].append(colors.index(hist_chutes[i][0]))
            relacoes[False].append(colors.index(hist_chutes[i+1][3]))
        else:
            repeticao = False

            for l in range(len(relacoes["dependencias"])):
                for k in range(len(relacoes["dependencias"][l])):
                    if relacoes["dependencias"][l][k] == hist_chutes[i + 1][3]:
                        relacoes["dependencias"][l].append(hist_chutes[i][0])
                        repeticao = True
                    
            for l in range(len(relacoes[True])):
                if relacoes[True][l] == hist_chutes[i][0]:
                    relacoes[True].append(hist_chutes[i + 1][3])
                    repeticao = True
                elif relacoes[True][l] == hist_chutes[i + 1][3]:
                    relacoes[True].append(hist_chutes[i][0])
                    repeticao = True

            if not repeticao:
                relacoes["dependencias"].append([colors.index(hist_chutes[i][0]), colors.index(hist_chutes[i+1][3])])

    for i in range(len(relacoes["dependencias"])):
        if len(relacoes[True]) + len(relacoes["dependencias"][i]) == 4:
            relacoes[True].extend(relacoes["dependencias"][i])
            relacoes["dependencias"].remove(relacoes["dependencias"][i])

            return list(relacoes[True]) 
