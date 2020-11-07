import random

# O indivíduo no caso é o caminho que sai do primeiro potno do grafo e vai até o último ponto.
class Individo(object):

#O indivíduo é gerado aleatóriamente, o que pode acabar gerando um caminho impossível.
    @staticmethod
    def gerar(n):
        indv = [0]
        for i in range(n-2):
            indv.append(random.randrange(0,n))
        indv.append(n-1)
        return indv
        