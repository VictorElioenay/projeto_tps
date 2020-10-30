import random

class Individo(object):

    @staticmethod
    def gerar(n):
        indv = [0]
        for i in range(n-2):
            indv.append(random.randrange(0,n))
        indv.append(n-1)
        return indv
        