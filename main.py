from populacao import Populacao
from selecao import Selecao
from crossover import Crossover
from mutacao import Mutacao

grafo = [   [0,1,1,0,0,9],#A
            [1,0,2,0,0,0],#B
            [1,2,0,1,4,0],#C
            [0,0,1,0,4,3],#D
            [0,0,4,4,0,0],#E
            [9,0,0,3,0,0] #F
        ]

def funcAptidao(populacao):
    global grafo
    valores_indv = []

    for indv in populacao:
        valor = 0
        for i in range(indv.__len__()-1):
            valor += grafo[indv[i]][indv[i+1]]
        valores_indv.append(valor)

    return valores_indv

tam_pop = int(input('tam_pop:'))
num_gen = int(input('num_gen:'))
corte_pos = int(input('corte_pos:'))
metd_sel = input('metd_sel:').lower()
tax_mut = float(input('tax_mut'))

populacao = Populacao.gerarPopulacaoIni(tam_pop,grafo.__len__())

print('População Inicial:')
for i in populacao:
    print(i)

for geracao in range(num_gen):
    print(geracao)

    valores_indv = funcAptidao(populacao)
    aptos = None

    if(metd_sel == 'roleta'):
        aptos = Selecao.roleta(populacao,valores_indv)
    elif(metd_sel == 'torneio'):
        aptos = Selecao.torneio(populacao,valores_indv,3)
    
    for i in aptos:
        print(i)

    populacao = Crossover.crossover(aptos,corte_pos)
    Mutacao.mutar(populacao,tax_mut)

    print(populacao)
# elitismo = int(input('elitismo:'))