import turtle
import random

# Função 1: Configura a tela
def configurar_tela():
    janela = turtle.Screen()
    janela.bgcolor("black")  # Fundo preto para destaque
    janela.title("Arte Generativa com Turtle")
    t = turtle.Turtle()
    t.speed(0)  # Velocidade máxima para a animação
    t.pensize(2)
    return t

# Função 2: Desenha o padrão principal
def desenhar_espiral(t, tamanho_maximo):
    cores = ["red", "purple", "blue", "green", "orange", "yellow"]
    tamanho = 0

    while tamanho < tamanho_maximo:
        # Muda a cor a cada iteração
        t.pencolor(random.choice(cores))

        # Desenha a linha e avança
        t.forward(tamanho)

        # Gira em um ângulo fixo (cria a espiral)
        t.right(91)

        # Aumenta o tamanho do passo
        tamanho += 1

# --- Programa Principal ---
tartaruga = configurar_tela()
desenhar_espiral(tartaruga, 300)

turtle.done()  # Mantém a janela aberta até ser fechada manualmente