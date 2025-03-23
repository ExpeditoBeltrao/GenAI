import pygame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
pygame.init()
font = pygame.font.SysFont("Arial", 18)

# Gráficos e interface
# Função para criação do gráfico "Evolução da Aptidão".
def desenhar_grafico(screen, x, y, x_label="Gerações", y_label="Aptidão - Quantidade de Vacas"):
    fig, ax = plt.subplots(figsize=(8, 4), dpi=100)
    ax.plot(x, y, label="Melhor Aptidão", color="blue", linewidth=2)
    media_aptidao = sum(y) / len(y)
    ax.plot(x, [media_aptidao] * len(x), label="Média Aptidão", linestyle="--", color="green")
    ax.set_title("Evolução da Aptidão", fontsize=14, color="red", fontweight="bold")
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    ax.legend()
    plt.tight_layout()

    canvas = FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_argb()
    size = canvas.get_width_height()
    surf = pygame.image.fromstring(raw_data, size, "ARGB")
    screen.blit(surf, (50, 50))
    plt.close(fig)

# Função para criação da representação do melhor indivíduo, maior aptidão, exibindo os piquetes com o respectivo número de vacas.
def desenhar_piquetes(screen, melhor_individuo, x_center, y_start=550, square_size=80):
    espaco = 10
    total_largura = len(melhor_individuo) * (square_size + espaco) - espaco
    x_start = x_center - total_largura // 2

    texto_titulo = pygame.font.SysFont("Arial", 24, bold=True).render("Melhor Resultado", True, (255, 0, 0))
    text_rect_titulo = texto_titulo.get_rect(center=(x_center, y_start - 70))
    screen.blit(texto_titulo, text_rect_titulo)

    for i, vacas in enumerate(melhor_individuo):
        x_pos = x_start + i * (square_size + espaco)
        y_pos = y_start
        cor = (200, 0, 0) if vacas > 25 else (0, 200, 0)
        pygame.draw.rect(screen, cor, (x_pos, y_pos, square_size, square_size))
        pygame.draw.rect(screen, (0, 0, 0), (x_pos, y_pos, square_size, square_size), 2)

        texto_piquete = font.render(f"Piquete {i + 1}", True, (0, 0, 0))
        text_rect_piquete = texto_piquete.get_rect(center=(x_pos + square_size // 2, y_pos - 20))
        screen.blit(texto_piquete, text_rect_piquete)

        texto_vacas = font.render(str(vacas), True, (0, 0, 0))
        text_rect_vacas = texto_vacas.get_rect(center=(x_pos + square_size // 2, y_pos + square_size // 2 - 10))
        screen.blit(texto_vacas, text_rect_vacas)

        texto_label = font.render("vacas", True, (0, 0, 0))
        text_rect_label = texto_label.get_rect(center=(x_pos + square_size // 2, y_pos + square_size // 2 + 20))
        screen.blit(texto_label, text_rect_label)

# Funções para inclusão das instruções de navegação.
def incluir_instrucoes(screen, WIDTH, HEIGHT):
    # Resumo das teclas
    instrucoes = [
         "Navegação: Pressione as teclas",
         "r - Reiniciar | p - Pausar | m - Voltar ao Menu"
        ]
    for i, instrucao in enumerate(instrucoes):
        texto_instrucao = pygame.font.SysFont("Arial", 16).render(instrucao, True, (0, 0, 0))
        screen.blit(texto_instrucao, (WIDTH // 2 - texto_instrucao.get_width() // 2, HEIGHT - 60 + i * 20))