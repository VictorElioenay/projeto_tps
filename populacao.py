from individuos import Individo

class Populacao(object):

    @staticmethod
    def gerarPopulacaoIni(tam,n):
        populacao = []
        for i in range(tam):
            populacao.append(Individo.gerar(n))

        return populacao