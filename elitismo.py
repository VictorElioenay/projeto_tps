class Elitismo(object):

    ## Elege nos n individuos mais aptos para a próxima geração
    @staticmethod
    def escolher(populacao,valores_indv,elitismo):
        aux = []
        elite = []

        for i in range(len(populacao)):
            aux.append({'indv':populacao[i].copy(),'valor':valores_indv[i]})
        
        aux.sort(key=lambda x : x['valor'])

        try:
            for i in range(elitismo):
                elite.append(aux[i]['indv'])
        except IndexError as e:
            pass
        
        return elite
