from individuos import Individo

class Populacao(object):

    ## Gera individuos (chama o metodo gerar do individuo e vai agregando o individuo à população) até atingir o tamanho da população
    @staticmethod
    def gerarPopulacaoIni(tam,n):
        populacao = []
        for i in range(tam):
            populacao.append(Individo.gerar(n))

        return populacao