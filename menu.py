import pygame
import sys

# Menu inicial
def menu_inicial(WIDTH, HEIGHT, FPS, tam_populacao, num_geracoes, tipo_selecao):
    pygame.init()
    pygame.display.set_caption("Sistema Pastejo Rotacionado - Configuração Inicial")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)

    selecionado = 0
    opcoes = [
        "Iniciar",
        f"Tamanho População: {tam_populacao}",
        f"Número Gerações: {num_geracoes}",
        f"Tipo Seleção: {tipo_selecao}"
    ]
    tipos_selecao = ["Aleatoria", "Probabilidade", "Roleta", "Torneio"]

    while True:
        screen.fill((255, 255, 255))
        
        # Título do menu
        titulo = pygame.font.SysFont("Arial", 28, bold=True).render("Configuração Inicial", True, (0, 0, 0))
        screen.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, 50))
        
        # Exibir opções
        for i, opcao in enumerate(opcoes):
            cor = (255, 0, 0) if i == selecionado else (0, 0, 0)
            texto = font.render(opcao, True, cor)
            screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, 150 + i * 40))
        
        # Resumo das teclas
        instrucoes = [
            "Use as setas ↑ e ↓ para navegar",
            "Pressione ENTER para editar ou iniciar"
        ]
        for i, instrucao in enumerate(instrucoes):
            texto_instrucao = pygame.font.SysFont("Arial", 16).render(instrucao, True, (0, 0, 0))
            screen.blit(texto_instrucao, (WIDTH // 2 - texto_instrucao.get_width() // 2, HEIGHT - 80 + i * 20))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selecionado = (selecionado - 1) % len(opcoes)
                elif event.key == pygame.K_DOWN:
                    selecionado = (selecionado + 1) % len(opcoes)
                elif event.key == pygame.K_RETURN:
                    if selecionado == 0:  # Iniciar
                        return tam_populacao, num_geracoes, tipo_selecao
                    elif selecionado == 1:  # Alterar população
                        tam_populacao += 50
                        if tam_populacao > 500:
                            tam_populacao = 100
                        opcoes[1] = f"População: {tam_populacao}"
                    elif selecionado == 2:  # Alterar gerações
                        num_geracoes += 100
                        if num_geracoes > 1000:
                            num_geracoes = 100
                        opcoes[2] = f"Gerações: {num_geracoes}"
                    elif selecionado == 3:  # Alterar tipo de seleção
                        idx = (tipos_selecao.index(tipo_selecao) + 1) % len(tipos_selecao)
                        tipo_selecao = tipos_selecao[idx]
                        opcoes[3] = f"Seleção: {tipo_selecao}"

        clock.tick(FPS)