import random

class Mutacao(object):

    @staticmethod
    def mutar(populacao,taxa):
        chance_true = 100*taxa
        
        for i in range(len(populacao)):
            value = random.randrange(0,101)
            if value <= chance_true:
                index = random.randrange(0,len(populacao))
                no = random.randrange(0,len(populacao))
                populacao[i][index] = no


