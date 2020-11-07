## Sobre

Este é um trabalho da disciplina Tópicos de Sistemas Inteligentes, com o tema de algoritmos genéticos. A aplicação no caso é utilizada para encontrar o melhor caminho em um grafo, utilizando diferentes parâmetros para obtenção de um melhor resultado, sendo eles:
* Tamanho da população
* Número de gerações
* Posição de corte para crossover
* Método de seleção (roleta/torneio)
* Taxa de mutação
* Elitismo

> O tamanho da população, o numero de gerações são números inteiros, a posição do crossover também, contanto que não exceda o tamanho dos genes do individuos. O metodo de seleção é inserido por meio de uma string `roleta` ou `torneio`. A taxa de mutação é um numero de ponto flutuante que pode ir de 0 até 1 (Ex: 0.03). O elitismo é um número inteiro (contanto que não exceda o tamanho da população)

Integrantes do projeto:
* Luiz Gustavo Chinelato Setten
* Pedro Henrique Borges Prado
* Victor Elioenay Santos Narciso

## Instalação

Para executar o código é necesário ter baixado e instalado o python

> Foi utilizada a versão mais recente para a confecção deste trabalho `Python 3.9.0`.

[Download Python](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)

## Execução

A execução é feita a partir do arquivo `main.py`, sendo assim é só executar no terminal

```python
python main.py
```

