import pygame

pygame.init()
tela = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
rodando= True

objeto_1 = pygame.image.load('fases/ViniParado1.png').convert_alpha()
objeto_1 = pygame.transform.scale(objeto_1, (128, 128))




objeto_1_colocado = False

while rodando:
   
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill("purple")

    tela.blit(objeto_1, (100, 100))

    pygame.display.flip()

    clock.tick(60)  
pygame.quit()