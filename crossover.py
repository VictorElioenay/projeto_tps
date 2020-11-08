import random

class Crossover(object):

    ## Com base na posição de corte dois individuos aptos são elegidos aleatoriamento para fazerem crossover
    @staticmethod
    def crossover(aptos,corte,tam_pop):
        tam = len(aptos)
        populacao = []
        indvs = []

        for i in range(tam_pop):
            index = random.randrange(0,tam)
            index2 = random.randrange(0,tam)
                        
            while index2==index:
                index2 = random.randrange(0,tam)
        
            part1 = aptos[index][0:corte]
            part2 = aptos[index][corte:]
            part3 = aptos[index2][0:corte]    
            part4 = aptos[index2][corte:]

            part1.extend(part4)
            part3.extend(part2)

            indvs.append(part1)
            indvs.append(part3)
        
        for i in range(tam_pop):
            populacao.append(indvs[i])

        return populacao