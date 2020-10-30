import random
class Selecao(object):

    @staticmethod
    def roleta(populacao,valores_indv):
        valorMax = 0
        tam = len(populacao)
        aptos = []
        aux_values = []
        
        for i in valores_indv:
            value = max(valores_indv)+min(valores_indv)-i
            valorMax += value
            aux_values.append(value)

        print('len:',tam)
        if not(valorMax == 0):
            for i in range(tam):
                aux = 0
                value = random.randrange(0,valorMax)
                
                for j in range(len(valores_indv)):
                    aux += aux_values[j]
                    if(value<=aux):
                        aptos.append(populacao[j].copy())
                        break
        else:
            return None
        return aptos

    @staticmethod
    def torneio(populacao,valores_indv,n):
        aptos = []
        tam = len(populacao)

        for i in range(tam):
            selecionados = []
            selecionados_values = []

            for j in range(n):
                index = random.randrange(0,tam)
                selecionados.append(populacao[index].copy())
                selecionados_values.append(valores_indv[index])
            
            min_value = min(selecionados_values)
            aptos.append(selecionados[selecionados_values.index(min_value)])
        
        return aptos