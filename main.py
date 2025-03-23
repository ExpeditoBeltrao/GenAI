import pygame
import sys
from menu import menu_inicial
from funcoes_genai import *
from graficos import *

# Configurações do Pygame
WIDTH = 1000
HEIGHT = 700
FPS = 60
pygame.init()
font = pygame.font.SysFont("Arial", 18)

# variáveis Globais
tam_populacao = 300
num_geracoes = 500
tipo_selecao = "Aleatoria"

# Configurações do problema (valores padrão)
num_piquetes = 10
qtde_capim_inicio = 3000  # Quantidade inicial de capim por piquete
qtde_capim_mínima = 100   # Quantidade mínima de capim por piquete
qtde_capim_diario = 50    # Incremento diário de capim
dias_por_rotacao = 2      # Dias por rotação
num_rotacoes = 10         # Número de rotações no ciclo
consumo_por_vaca_dia = 15 # Consumo diário de capim por vaca
crescimento_capim = qtde_capim_diario * dias_por_rotacao

# Fatores Climáticos
chuva = [1.0, 0.8, 1.2, 0.9, 1.1, 1.3, 0.7, 1.0, 0.6, 1.1]  # Multiplicador para o crescimento do capim
temperatura = [1.0, 0.9, 0.85, 0.8, 1.1, 1.2, 0.75, 0.9, 0.7, 1.0]  # Fator que ajusta o consumo de capim



# Loop principal
def executar_algoritmo():
    global tam_populacao, num_geracoes, tipo_selecao
    populacao = gerar_populacao(num_piquetes, tam_populacao)
    lista_melhores_aptidoes = []
    geracao = 0

    running = True
    paused = False

    pygame.display.set_caption("Sistema Pastejo Rotacionado - Resultado Análises")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    limite_baixo_diversidade = 50  # Limite crítico de diversidade

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pausar
                    paused = not paused
                elif event.key == pygame.K_r:  # Reiniciar
                    populacao = gerar_populacao(num_piquetes, tam_populacao)
                    lista_melhores_aptidoes = []
                    geracao = 0
                elif event.key == pygame.K_m:  # Voltar ao menu inicial
                    return  # Sai do loop e volta ao início do programa

        if not paused:

            # Taxa de mutação adaptativa
            taxa_mutacao_adaptativa = max(0.1, 1.0 - (geracao / num_geracoes))

            # Avaliação da população
            aptidoes = [calcular_aptidao(ind, qtde_capim_inicio, num_piquetes, num_rotacoes,
                                         consumo_por_vaca_dia, dias_por_rotacao, crescimento_capim,
                                         qtde_capim_mínima, chuva, temperatura) for ind in populacao]
            
            populacao_ordenada, aptidoes_ordenadas, populacao_aptidao = ordenar(populacao, aptidoes)
            
            melhor_aptidao = aptidoes_ordenadas[0]
            melhor_individuo = populacao_ordenada[0]
            lista_melhores_aptidoes.append(melhor_aptidao)

            # Calcular a diversidade da população
            diversidade = calcular_diversidade([ind for ind in populacao])

            # Introduzir novos indivíduos aleatórios se necessário
            if diversidade < limite_baixo_diversidade:
                populacao = introduzir_novos_individuos(populacao, num_piquetes, tam_populacao // 10)

            # Geração da nova população
            nova_populacao = [populacao_ordenada[0]]  # Elitismo
            while len(nova_populacao) < tam_populacao:
                pais = selecionar_pais(populacao_ordenada, tipo_selecao)
                filho = crossover(pais[0], pais[1], num_piquetes)
                filho = mutacao(filho, taxa_mutacao_adaptativa)
                nova_populacao.append(filho)

            populacao = nova_populacao
            geracao += 1

            # Renderização da interface
            screen.fill((255, 255, 255))
            font = pygame.font.SysFont("Arial", 16, bold=True)
            texto = font.render(f"Geração: {geracao} | Melhor Aptidão: {melhor_aptidao} | Diversidade: {diversidade:.2f} | Taxa Mutação: {taxa_mutacao_adaptativa:.2f} | Tipo Seleção: {tipo_selecao}", True, (0, 0, 0))
            screen.blit(texto, (50, 20))
            desenhar_grafico(screen, list(range(1, geracao + 1)), lista_melhores_aptidoes)
            desenhar_piquetes(screen, melhor_individuo, WIDTH // 2)
            incluir_instrucoes(screen, WIDTH, HEIGHT)

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

        if geracao == num_geracoes:
            paused = True

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    while True:
        tam_populacao, num_geracoes, tipo_selecao = menu_inicial(WIDTH, HEIGHT, FPS, tam_populacao, num_geracoes, tipo_selecao)  # Exibe o menu inicial
        executar_algoritmo()  # Executa o algoritmo genético com as configurações escolhidas
