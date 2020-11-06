from populacao import Populacao
from selecao import Selecao
from crossover import Crossover
from mutacao import Mutacao
from elitismo import Elitismo

B = float('inf') #Infinito de pé B
grafo = [   [B,1,1,B,B,9],#A
            [1,B,2,B,B,B],#B
            [1,2,B,1,4,B],#C
            [B,B,1,B,4,3],#D
            [B,B,4,4,B,B],#E
            [9,B,B,3,B,B] #F
        ]

f = open("relatorio.txt", "a")

def funcAptidao(populacao):
    global grafo
    valores_indv = []

    for indv in populacao:
        valor = 0
        for i in range(indv.__len__()-1):
            v = grafo[indv[i]][indv[i+1]]
            if not(v == B):
                valor += v
            else:
                valor = B
        valores_indv.append(valor)

    return valores_indv

tam_pop = int(input('tam_pop:'))
num_gen = int(input('num_gen:'))
corte_pos = int(input('corte_pos:'))
metd_sel = input('metd_sel:').lower()
tax_mut = float(input('tax_mut:'))
elitismo = int(input('elitismo:'))

populacao = Populacao.gerarPopulacaoIni(tam_pop,grafo.__len__())

print('\nPopulação Inicial:')
f.write('\nPopulação Inicial:')
for i in populacao:
    print(i)
    f.write(str(i))
    f.write('\n')



for geracao in range(num_gen):

    valores_indv = funcAptidao(populacao)
    aptos = None

    # Retirar ind infinitos

    for i in range(len(valores_indv)):
        if valores_indv[i] == B:
            populacao[i] = -1
            valores_indv[i] = -1
    
    populacao = list(filter(lambda x : x != -1,populacao))
    valores_indv = list(filter(lambda x : x != -1,valores_indv))

    elite = Elitismo.escolher(populacao,valores_indv,elitismo)
    
    if(metd_sel == 'roleta'):
        aptos = Selecao.roleta(populacao,valores_indv)
    elif(metd_sel == 'torneio'):
        aptos = Selecao.torneio(populacao,valores_indv,3)
    
    if aptos == None:
        break

    aptos.extend(elite)
    
    populacao = Crossover.crossover(aptos,corte_pos,tam_pop)
    Mutacao.mutar(populacao,tax_mut)
    valores_indv = funcAptidao(populacao)

    print('\nGeração:',geracao)
    f.write('\nGeração:')
    f.write(str(geracao))
    f.write('\n')


    for i in range(len(populacao)):
        print(populacao[i],valores_indv[i])
        f.write(str(populacao[i]))
        f.write(str(valores_indv[i]))
        f.write('\n')

        


# print('\nResultado final:')
# for indv in populacao:
#     index = 0
#     for i in range(len(indv)):
#         if indv[i] == 0:
#             index=i
#     print(indv[index:])

# elitismo = int(input('elitismo:'))