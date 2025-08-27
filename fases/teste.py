import pygame

pygame.init()
tela = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
rodando= True

objeto_1 = pygame.image.load('fases/ViniParado1.png').convert_alpha()
objeto_1 = pygame.transform.scale(objeto_1, (128, 128))

objeto_2 = pygame.image.load('fases/ViniParado1.png').convert_alpha()
objeto_2 = pygame.transform.scale(objeto_2, (128, 128))

objeto_3 = pygame.image.load('fases/ViniParado1.png').convert_alpha()
objeto_3 = pygame.transform.scale(objeto_3, (128, 128))

objeto_4 = pygame.image.load('fases/ViniParado1.png').convert_alpha()
objeto_4 = pygame.transform.scale(objeto_4, (128, 128))

jogador = pygame.image.load('fases/AlmaParado.png').convert_alpha()
jogador = pygame.transform.scale(jogador, (64, 64))

jogador_para_direita = pygame.image.load('fases/AlmaCorrendo1.png').convert_alpha()
jogador_para_direita = pygame.transform.scale(jogador_para_direita, (64, 64))

imagem_atual_jogador = jogador


objeto_1_colocado = False

jogador_para_direita_bool = False

tocando_em_uma_estatua = False

coordenada_y_jogador = 300
coordenada_x_jogador = 300

while rodando:
   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill("purple")

    tela.blit(objeto_1, (100, 100))
    tela.blit(objeto_2, (700, 100))
    tela.blit(objeto_3, (100, 500))
    tela.blit(objeto_4, (700, 500))

    tela.blit(imagem_atual_jogador, (coordenada_x_jogador, coordenada_y_jogador))

    tecla = pygame.key.get_pressed()

    if tecla[pygame.K_w]:
        coordenada_y_jogador -= 5
        jogador_para_direita_bool = False
    if tecla[pygame.K_s]:
        coordenada_y_jogador += 5
        jogador_para_direita_bool = False
    if tecla[pygame.K_d]:
        coordenada_x_jogador += 5
        jogador_para_direita_bool = True
    if tecla[pygame.K_a]:
        coordenada_x_jogador -= 5
        jogador_para_direita_bool = False

    if jogador_para_direita_bool:
        imagem_atual_jogador = jogador_para_direita
    else:
        imagem_atual_jogador = jogador

    pygame.display.flip()

    clock.tick(60)  
pygame.quit()