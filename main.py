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

populacoes_predefinidas = [[
 [12, 28, 1, 16, 50, 35, 26, 5, 39, 47], [46, 27, 1, 46, 20, 32, 23, 5, 30, 2], [41, 17, 17, 32, 44, 5, 10, 45, 24, 28], [21, 13, 26, 10, 22, 3, 7, 49, 5, 2], [16, 16, 16, 16, 16, 16, 16, 16, 16, 16], 
 [41, 8, 49, 2, 40, 14, 22, 32, 24, 48], [32, 29, 2, 47, 4, 30, 36, 46, 20, 50], [15, 15, 15, 15, 15, 15, 15, 15, 15, 15], [42, 22, 27, 40, 4, 43, 43, 30, 31, 4], [40, 7, 48, 27, 48, 45, 41, 50, 14, 9], 
 [42, 42, 42, 42, 42, 42, 42, 42, 42, 42], [14, 24, 35, 23, 22, 47, 35, 10, 33, 26], [26, 34, 30, 20, 8, 5, 20, 2, 0, 32], [16, 40, 6, 14, 41, 47, 21, 18, 28, 50], [16, 16, 16, 16, 16, 16, 16, 16, 16, 16], 
 [8, 41, 11, 39, 48, 22, 50, 13, 30, 50], [12, 39, 20, 29, 22, 35, 45, 17, 10, 8], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [8, 12, 27, 37, 27, 31, 46, 26, 40, 6], [40, 6, 24, 21, 32, 23, 15, 45, 38, 37], 
 [49, 21, 34, 8, 3, 22, 8, 49, 40, 4], [33, 17, 15, 50, 50, 34, 8, 26, 8, 49], [43, 8, 41, 43, 15, 13, 29, 27, 42, 17], [10, 2, 20, 16, 2, 19, 44, 25, 9, 26], [36, 50, 18, 18, 40, 11, 12, 28, 30, 28], 
 [46, 16, 47, 21, 5, 43, 26, 11, 22, 32], [7, 33, 32, 32, 40, 27, 21, 48, 10, 19], [19, 26, 15, 19, 45, 0, 14, 28, 44, 38], [28, 28, 28, 28, 28, 28, 28, 28, 28, 28], [48, 15, 22, 48, 42, 7, 29, 45, 22, 42], 
 [6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [14, 8, 2, 33, 30, 13, 41, 13, 4, 18], [17, 17, 17, 17, 17, 17, 17, 17, 17, 17], [0, 41, 43, 40, 33, 30, 13, 23, 42, 10], [10, 30, 33, 0, 26, 25, 12, 40, 8, 7], 
 [30, 30, 30, 30, 30, 30, 30, 30, 30, 30], [18, 27, 47, 35, 44, 35, 44, 33, 4, 27], [28, 28, 28, 28, 28, 28, 28, 28, 28, 28], [39, 11, 32, 2, 14, 11, 24, 18, 31, 34], [34, 13, 28, 25, 39, 48, 17, 33, 41, 48], 
 [42, 42, 42, 42, 42, 42, 42, 42, 42, 42], [37, 48, 21, 46, 16, 17, 18, 4, 17, 23], [21, 41, 47, 46, 37, 34, 13, 38, 13, 6], [50, 6, 14, 37, 10, 12, 25, 16, 20, 12], [2, 32, 37, 26, 22, 43, 32, 43, 3, 8], 
 [39, 38, 6, 40, 40, 37, 44, 30, 49, 11], [0, 31, 13, 45, 2, 22, 12, 46, 1, 40], [14, 32, 24, 22, 37, 15, 19, 48, 5, 45], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [6, 16, 29, 30, 4, 36, 20, 14, 33, 35], 
 [0, 31, 19, 28, 42, 8, 18, 23, 1, 24], [38, 19, 6, 18, 11, 37, 2, 20, 2, 27], [3, 26, 12, 49, 9, 6, 17, 49, 9, 14], [47, 23, 11, 4, 14, 50, 37, 47, 26, 20], [2, 10, 12, 20, 22, 45, 37, 28, 7, 1], 
 [2, 14, 46, 20, 32, 4, 3, 18, 15, 17], [33, 23, 15, 19, 21, 7, 23, 48, 42, 13], [43, 48, 22, 10, 19, 1, 30, 44, 43, 33], [21, 21, 21, 21, 21, 21, 21, 21, 21, 21], [35, 11, 37, 41, 39, 32, 20, 46, 41, 39], 
 [40, 22, 49, 1, 49, 33, 38, 16, 24, 29], [34, 26, 43, 10, 48, 42, 2, 41, 46, 11], [26, 38, 23, 45, 34, 34, 30, 35, 16, 47], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [39, 19, 11, 33, 22, 6, 8, 23, 15, 33], 
 [20, 20, 20, 20, 20, 20, 20, 20, 20, 20], [26, 4, 12, 4, 42, 13, 48, 24, 48, 19], [28, 47, 46, 46, 3, 19, 26, 12, 22, 37], [20, 40, 22, 3, 39, 38, 1, 14, 41, 20], [16, 32, 38, 42, 24, 49, 10, 20, 47, 33], 
 [7, 16, 17, 38, 11, 8, 25, 8, 41, 7], [35, 35, 35, 3, 12, 5, 23, 44, 30, 38], [48, 22, 8, 12, 2, 20, 48, 43, 43, 16], [49, 49, 49, 49, 49, 49, 49, 49, 49, 49], [6, 6, 6, 6, 6, 6, 6, 6, 6, 6], 
 [4, 19, 30, 42, 16, 27, 31, 19, 43, 42], [44, 20, 35, 6, 8, 8, 20, 26, 22, 12], [9, 38, 41, 49, 48, 28, 30, 47, 2, 12], [2, 50, 7, 34, 25, 29, 41, 18, 28, 30], [21, 35, 28, 26, 5, 12, 27, 41, 7, 2], 
 [13, 13, 13, 13, 13, 13, 13, 13, 13, 13], [24, 37, 37, 34, 8, 43, 36, 12, 49, 26], [33, 10, 11, 30, 22, 30, 21, 35, 44, 50], [1, 26, 7, 12, 36, 29, 28, 41, 29, 48], [30, 30, 30, 30, 30, 30, 30, 30, 30, 30], 
 [48, 43, 41, 46, 49, 6, 29, 3, 0, 20], [37, 37, 37, 37, 37, 37, 37, 37, 37, 37], [33, 33, 33, 33, 33, 33, 33, 33, 33, 33], [40, 26, 8, 30, 46, 23, 5, 42, 17, 5], [5, 38, 15, 23, 18, 8, 50, 27, 42, 24], 
 [28, 44, 46, 11, 22, 37, 38, 40, 48, 2], [29, 29, 29, 29, 29, 29, 29, 29, 29, 29], [5, 49, 31, 24, 18, 7, 14, 1, 23, 30], [34, 6, 27, 38, 36, 19, 4, 23, 8, 12], [42, 16, 43, 33, 16, 34, 15, 12, 18, 30], 
 [37, 3, 43, 16, 10, 41, 18, 3, 49, 44], [0, 34, 19, 9, 26, 20, 36, 5, 50, 25], [43, 7, 8, 35, 44, 48, 50, 20, 25, 33], [41, 22, 32, 40, 45, 34, 22, 28, 46, 35], [41, 50, 12, 47, 36, 27, 11, 48, 10, 17], 
 [25, 17, 34, 10, 0, 27, 27, 32, 3, 0], [19, 48, 50, 11, 0, 3, 29, 48, 12, 1], [34, 41, 4, 19, 44, 24, 32, 50, 9, 14], [50, 6, 10, 0, 28, 33, 45, 47, 9, 17], [12, 12, 12, 12, 12, 12, 12, 12, 12, 12], 
 [14, 28, 15, 41, 20, 49, 33, 32, 10, 37], [21, 30, 16, 14, 1, 31, 24, 3, 23, 18], [39, 13, 9, 4, 50, 8, 7, 49, 44, 9], [17, 22, 30, 7, 17, 28, 37, 39, 27, 0], [46, 22, 16, 50, 50, 18, 11, 32, 31, 42], 
 [5, 42, 46, 7, 20, 35, 48, 32, 20, 28], [27, 24, 40, 50, 42, 15, 47, 43, 21, 50], [41, 37, 23, 9, 25, 10, 36, 23, 48, 35], [18, 34, 24, 26, 29, 26, 0, 14, 50, 33], [30, 22, 48, 9, 10, 26, 19, 29, 13, 6], 
 [30, 24, 20, 21, 42, 36, 33, 7, 18, 41], [44, 44, 44, 44, 44, 44, 44, 44, 44, 44], [30, 30, 30, 30, 30, 30, 30, 30, 30, 30], [41, 41, 41, 41, 41, 41, 41, 41, 41, 41], [11, 15, 2, 24, 2, 14, 26, 13, 49, 35], 
 [48, 20, 12, 12, 45, 35, 19, 4, 27, 16], [46, 30, 15, 38, 33, 28, 48, 26, 31, 0], [25, 26, 18, 50, 24, 22, 24, 48, 11, 32], [45, 49, 16, 16, 47, 42, 16, 14, 27, 34], [16, 14, 29, 27, 1, 9, 20, 26, 6, 35], 
 [40, 19, 7, 43, 46, 2, 47, 36, 20, 24], [11, 13, 29, 22, 17, 38, 46, 10, 3, 46], [24, 26, 2, 41, 33, 16, 44, 17, 15, 30], [47, 17, 14, 47, 31, 13, 3, 15, 34, 19], [27, 44, 45, 39, 6, 3, 46, 29, 29, 14], 
 [12, 40, 29, 47, 9, 14, 16, 10, 3, 41], [43, 14, 40, 25, 9, 39, 49, 43, 38, 30], [30, 33, 32, 39, 30, 50, 19, 31, 27, 14], [29, 4, 42, 15, 30, 2, 34, 5, 40, 35], [17, 17, 17, 17, 17, 17, 17, 17, 17, 17], 
 [18, 28, 7, 17, 9, 33, 39, 21, 6, 13], [32, 0, 49, 7, 19, 29, 13, 26, 42, 13], [17, 48, 4, 25, 13, 21, 43, 24, 31, 15], [25, 43, 44, 2, 1, 38, 37, 45, 5, 0], [5, 33, 37, 47, 20, 36, 35, 28, 13, 34], 
 [41, 27, 15, 8, 9, 12, 12, 12, 36, 45], [37, 43, 33, 18, 1, 25, 13, 18, 4, 43], [20, 7, 3, 24, 41, 13, 38, 3, 27, 3], [17, 8, 5, 49, 3, 12, 41, 9, 36, 40], [10, 44, 19, 47, 10, 50, 5, 1, 37, 39], 
 [6, 38, 17, 10, 39, 31, 24, 40, 9, 15], [6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [45, 44, 33, 7, 50, 25, 8, 16, 30, 7], [28, 22, 34, 31, 19, 46, 8, 14, 40, 20], [17, 16, 39, 35, 14, 40, 39, 40, 30, 19], 
 [30, 8, 38, 16, 28, 36, 5, 24, 11, 29], [48, 32, 45, 43, 10, 22, 13, 42, 7, 9], [39, 12, 37, 0, 47, 36, 4, 41, 49, 16], [18, 6, 41, 8, 20, 6, 26, 18, 25, 34], [33, 32, 13, 16, 4, 11, 17, 24, 18, 30], 
 [32, 16, 0, 34, 45, 10, 19, 25, 19, 12], [2, 17, 32, 48, 20, 45, 39, 39, 43, 46], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [39, 32, 37, 20, 27, 12, 9, 24, 35, 40], [29, 2, 24, 18, 8, 48, 15, 23, 37, 14], 
 [8, 10, 39, 8, 14, 12, 48, 30, 34, 13], [18, 23, 11, 15, 26, 39, 33, 28, 7, 6], [9, 4, 26, 48, 41, 30, 24, 28, 37, 34], [42, 42, 42, 42, 42, 42, 42, 42, 42, 42], [47, 28, 32, 48, 46, 46, 34, 36, 35, 30], 
 [28, 40, 24, 4, 10, 2, 16, 46, 31, 16], [1, 42, 14, 24, 23, 40, 5, 15, 50, 9], [47, 7, 35, 48, 36, 30, 30, 36, 36, 10], [16, 16, 16, 16, 16, 16, 16, 16, 16, 16], [18, 33, 34, 8, 12, 13, 13, 14, 1, 35], 
 [38, 21, 43, 50, 48, 33, 41, 21, 37, 17], [5, 12, 26, 37, 12, 5, 26, 2, 8, 4], [16, 13, 17, 9, 31, 46, 44, 23, 47, 41], [31, 31, 31, 31, 31, 31, 31, 31, 31, 31], [42, 41, 27, 2, 50, 36, 30, 18, 18, 18], 
 [48, 48, 48, 48, 48, 48, 48, 48, 48, 48], [36, 36, 36, 36, 36, 36, 36, 36, 36, 36], [28, 38, 13, 35, 36, 5, 46, 27, 32, 15], [31, 31, 31, 31, 31, 31, 31, 31, 31, 31], [39, 27, 15, 48, 34, 16, 37, 4, 4, 0], 
 [38, 38, 38, 38, 38, 38, 38, 38, 38, 38], [14, 44, 29, 5, 39, 11, 19, 30, 4, 38], [44, 14, 23, 31, 38, 29, 17, 20, 18, 33], [8, 8, 8, 8, 8, 8, 8, 8, 8, 8], [48, 37, 9, 25, 27, 9, 30, 38, 45, 11], 
 [25, 25, 25, 25, 25, 25, 25, 25, 25, 25], [8, 7, 41, 7, 32, 12, 12, 8, 17, 9], [25, 46, 45, 23, 17, 40, 7, 15, 25, 2], [4, 43, 42, 18, 23, 23, 25, 28, 23, 42], [10, 46, 48, 48, 23, 8, 50, 24, 11, 9], 
 [22, 36, 13, 16, 47, 31, 29, 31, 8, 40], [45, 5, 38, 40, 35, 49, 2, 34, 50, 0], [33, 31, 9, 12, 10, 5, 15, 47, 10, 37], [32, 43, 0, 49, 22, 37, 12, 37, 9, 12], [27, 38, 29, 22, 31, 49, 49, 33, 23, 20], 
 [34, 32, 23, 17, 13, 36, 29, 42, 20, 28], [10, 21, 9, 27, 48, 39, 29, 21, 49, 37], [17, 17, 17, 17, 17, 17, 17, 17, 17, 17], [29, 13, 13, 30, 35, 11, 20, 7, 21, 20], [15, 11, 6, 7, 28, 29, 34, 21, 9, 22]],
[[11, 11, 11, 11, 11, 11, 11, 11, 11, 11]], [[100, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]

# Variáveis Algorítmo Genético
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
chuva = [1.0, 0.8, 1.2, 0.9, 1.1, 1.3, 0.7, 1.0, 0.6, 1.1]  # Multiplicador para o crescimento do capim
temperatura = [1.0, 0.9, 0.85, 0.8, 1.1, 1.2, 0.75, 0.9, 0.7, 1.0]  # Fator que ajusta o consumo de capim

# Loop principal
def executar_algoritmo(populacao_predefinida=None):
    global tam_populacao, num_geracoes, tipo_selecao

    if populacao_predefinida:
        populacao = populacao_predefinida
    else:
        # 1. Gerar população inicial
        populacao = gerar_populacao(num_piquetes, tam_populacao)
    
    lista_melhores_aptidoes = []
    limite_baixo_diversidade = 50  # Limite crítico de diversidade
    geracao = 0
    running = True
    paused = False
    
    pygame.display.set_caption("Sistema Pastejo Rotacionado - Resultado Análises")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

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
                elif event.key == pygame.K_ESCAPE:  # Encerrar e fechar ao pressionar ESC
                    running = False


        if not paused:

            # Cálculo da taxa de mutação adaptativa
            taxa_mutacao_adaptativa = max(0.1, 1.0 - (geracao / num_geracoes))

            # 2. Avaliação da aptidão dos indivíduos da população
            aptidoes = [calcular_aptidao(ind, qtde_capim_inicio, num_piquetes, num_rotacoes,
                                         consumo_por_vaca_dia, dias_por_rotacao, crescimento_capim,
                                         qtde_capim_mínima, chuva, temperatura) for ind in populacao]
            
            # Ordenação das listas de indivíduos e suas aptidões
            populacao_ordenada, aptidoes_ordenadas = ordenar(populacao, aptidoes)
            
            # Armazenamento dos melhores indivíduos e aptidões
            melhor_aptidao = aptidoes_ordenadas[0]
            melhor_individuo = populacao_ordenada[0]
            lista_melhores_aptidoes.append(melhor_aptidao)

            # Calcular a diversidade da população
            diversidade = calcular_diversidade([ind for ind in populacao])

            # Introduzir novos indivíduos aleatórios se baixa diversidade
            if diversidade < limite_baixo_diversidade:
                populacao = introduzir_novos_individuos(populacao, num_piquetes, tam_populacao // 10)

            # Geração da nova população utilizando Elitismo. O melhor indivíduo é replicado para a próxima população.
            nova_populacao = [populacao_ordenada[0]]

            # 3. Verifica condição de término
            while len(nova_populacao) < tam_populacao:
                # 4. Seleção
                pais = selecionar_pais(populacao_ordenada, tipo_selecao)
                # 5. Cruzamento
                filho = crossover(pais[0], pais[1], num_piquetes)
                # 6. Mutação
                filho = mutacao(filho, taxa_mutacao_adaptativa)
                nova_populacao.append(filho)

            # 7. Substitui população antiga
            populacao = nova_populacao
            geracao += 1

            # Renderização da interface gráfica
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

# Função Principal
if __name__ == "__main__":
# Adicione uma variável para armazenar a população pré-definida
    populacao_predefinida = None

    while True:
        # Menu inicial retorna a população pré-definida, se for escolhida
        resultado = menu_inicial(WIDTH, HEIGHT, FPS, tam_populacao, num_geracoes, tipo_selecao, populacoes_predefinidas)
        
        if isinstance(resultado, tuple) and len(resultado) == 4:  # Caso uma população pré-definida seja retornada
            tam_populacao, num_geracoes, tipo_selecao, populacao_predefinida = resultado
            executar_algoritmo(populacao_predefinida)
        else:  # Caso contrário, inicia com configurações padrão
            tam_populacao, num_geracoes, tipo_selecao = resultado
            executar_algoritmo()

