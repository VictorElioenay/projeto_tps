import random

class Mutacao(object):

    ## Com base na taxa é feita uma alteração numa posição aleatória 
    @staticmethod
    def mutar(populacao,taxa):
        chance_true = 100*taxa
        
        for i in range(len(populacao)):
            value = random.randrange(0,101)
            if value <= chance_true:
                index = random.randrange(1,len(populacao[0])-1)
                no = random.randrange(0,len(populacao[0]))
                populacao[i][index] = no


