import random
from typing import List

# Funções do algoritmo genético
# Função para gerar população de forma aleatória
def gerar_populacao(num_piquetes: int, tam_populacao: int) -> List[List[int]]:
    return [[random.randint(0, 50) for _ in range(num_piquetes)] for _ in range(tam_populacao)]

# Função para cálculo da aptidão dos indivíduos. A aptidão será o somatório das vacas distribuídas nos piquetes.
def calcular_aptidao(individuo, qtde_capim_inicio, num_piquetes, num_rotacoes, consumo_por_vaca_dia, dias_por_rotacao, crescimento_capim, qtde_capim_mínima, chuva, temperatura):
    # Variáveis para cálculos dos limitadores do problema
    disponibilidade = [qtde_capim_inicio] * num_piquetes
    total_vacas = sum(individuo)
    rotacao = individuo[:]

    for _ in range(num_rotacoes):
        for i in range(num_piquetes):
            crescimento_ajustado = crescimento_capim * chuva[i]
            consumo_ajustado = rotacao[i] * consumo_por_vaca_dia * dias_por_rotacao * temperatura[i]
            disponibilidade[i] -= consumo_ajustado
            disponibilidade[i] += crescimento_ajustado

            # Se a disponibilidade de capim ficar abaixo do parâmetro mínimo o indivíduo terá a aptidão zerada.
            if disponibilidade[i] < qtde_capim_mínima:
                return 0

        # Rotação das vacas entre os piquetes da esquerda para direita. O gado do último piquete[9] vai para o primeiro piquete[0].
        rotacao = [rotacao[-1]] + rotacao[:-1]

    return total_vacas

# Função para ordenação das listas de indivíduos e suas aptidões
def ordenar(populacao, aptidoes):
    combinados = list(zip(populacao, aptidoes))
    combinados.sort(key=lambda x: x[1], reverse=True)
    populacao_ordenada, aptidoes_ordenadas = zip(*combinados)
    return list(populacao_ordenada), list(aptidoes_ordenadas)

# Função de cruzamento. Utilizei dois pontos aleatórios para definir quais genes serão repassados para o filho.
def crossover(pai1, pai2, num_piquetes):
    ponto1 = random.randint(1, num_piquetes - 1)
    ponto2 = random.randint(ponto1, num_piquetes)
    return pai1[:ponto1] + pai2[ponto1:ponto2] + pai1[ponto2:]
    
# Função de mutação. Utiliza a Mutação Adaptativa, onde a taxa de mutação é maior nas gerações iniciais e menor nas finais.
def mutacao(individuo, taxa_mutacao):

    indices_mutacao = random.sample(range(len(individuo)), 2)

    for i in indices_mutacao:
        if random.random() < taxa_mutacao:
            individuo[i] = random.randint(0, 50)  # Define um novo valor aleatório para o gene
    
    return individuo


# Métodos de seleção
# Função para seleção aleatória. Dois indivíduos serão selecionados.
def selecionar_aleatorio(populacao_ordenada):
    return random.sample(populacao_ordenada, 2)

# Função para seleção por probabilidade. Dois indivíduos serão selecionados.
def selecionar_por_probabilidade(populacao_ordenada):
    aptidoes = [individuo[1] for individuo in populacao_ordenada]
    total_aptidao = sum(aptidoes)
    probabilidades = [aptidao / total_aptidao for aptidao in aptidoes]
    return random.choices(populacao_ordenada, weights=probabilidades, k=2)

# Função para seleção por roleta. Dois indivíduos serão selecionados.
def selecionar_por_roleta(populacao_ordenada):
    aptidoes = [individuo[1] for individuo in populacao_ordenada]
    soma_aptidao = sum(aptidoes)
    limite = random.uniform(0, soma_aptidao)
    acumulado = 0
    for individuo in populacao_ordenada:
        acumulado += individuo[1]
        if acumulado >= limite:
            return [individuo, random.choice(populacao_ordenada)]
        
# Função para seleção por torneio. Apenas um indivíduo é selecionado.
def selecionar_por_torneio(populacao_ordenada, tamanho_torneio=2):
    torneio = random.sample(populacao_ordenada, tamanho_torneio)
    vencedor = max(torneio, key=lambda individuo: individuo[1])  # Seleciona o indivíduo com maior aptidão
    return vencedor

# Função para seleção dos pais
def selecionar_pais(populacao_ordenada, tipo_selecao):
    if tipo_selecao == "Aleatoria":
        return selecionar_aleatorio(populacao_ordenada)
    elif tipo_selecao == "Probabilidade":
        return selecionar_por_probabilidade(populacao_ordenada)
    elif tipo_selecao == "Roleta":
        return selecionar_por_roleta(populacao_ordenada)
    elif tipo_selecao == "Torneio":
        pai1 = selecionar_por_torneio(populacao_ordenada)
        pai2 = selecionar_por_torneio(populacao_ordenada)
        return [pai1, pai2]
    else:
        raise ValueError(f"Tipo de seleção '{tipo_selecao}' inválido.")
    
# Função para cálculo da diversidade. Mede a diversidade da população calculando a média das distâncias entre os indivíduos.
def calcular_diversidade(populacao):
    total_distancia = 0
    num_individuos = len(populacao)
    
    for i in range(num_individuos):
        for j in range(i + 1, num_individuos):
            # Soma as diferenças absolutas entre os genes dos indivíduos
            distancia = sum(abs(gene1 - gene2) for gene1, gene2 in zip(populacao[i], populacao[j]))
            total_distancia += distancia
    
    # Calcula a distância média
    num_combinacoes = (num_individuos * (num_individuos - 1)) // 2  # Total de pares únicos
    return total_distancia / num_combinacoes if num_combinacoes > 0 else 0

# Função para introduzir novos indivíduos na população. Substitui uma fração da população por indivíduos aleatórios para aumentar a diversidade.
def introduzir_novos_individuos(populacao, num_piquetes, num_novos):  
    novos_individuos = gerar_populacao(num_piquetes, num_novos)
    populacao[-num_novos:] = novos_individuos  # Substitui os últimos indivíduos
    return populacao