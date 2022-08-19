import os
import random

import pygame

tela_widht = 400
tela_height = 600

img_cano = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
img_chao = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
imagem_background = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
imgs_passaro = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]

pygame.font.init()
pygame.display.init()
pygame.init()
fonte_pontos = pygame.font.SysFont('arial', 50)


# Se der certo eu mudo para essa Bitstream Vera Sans Mono

class Passaro:
    img = imgs_passaro
    # animações
    rotacao_max = 25
    vel_rotacao = 20
    tempo_anima = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.vel = 0
        self.height = self.y
        self.time = 0
        self.imagem = self.img[0]
        self.cont_img = 0

    def jump(self):
        self.vel = -10.5
        self.time = 0
        self.height = self.y

    def move(self):
        # calcular deslocamento
        self.time += 1
        deslocamento = 1.5 * (self.time ** 2) + self.vel * self.time
        # restringir movimento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2
        self.y += deslocamento
        # o angulo do passáro
        if deslocamento < 0 or self.y < (self.height + 50):
            if self.angulo < self.rotacao_max:
                self.angulo = self.rotacao_max
        else:
            if self.angulo > -90:
                self.angulo -= self.vel_rotacao

    def desenhar(self, tela):
        # definir a imagem do passáro a ser usada

        self.cont_img += 1

        if self.cont_img < self.tempo_anima:
            self.imagem = self.img[0]
        elif self.cont_img < self.tempo_anima * 2:
            self.imagem = self.img[1]
        elif self.cont_img < self.tempo_anima * 3:
            self.imagem = self.img[2]
        elif self.cont_img < self.tempo_anima * 4:
            self.imagem = self.img[1]
        elif self.cont_img >= self.tempo_anima * 4 + 1:
            self.imagem = self.img[0]
            self.cont_img = 0
        # se o passáro estiver a cair eu não vou bater asa

        if self.angulo <= -80:
            self.imagem = self.img[1]
            self.cont_img = self.tempo_anima * 2
        # o desenho em si

        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.imagem)


class Cano:
    ditancia = 200
    vel = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.cano_topo = pygame.transform.flip(img_cano, False, True)
        self.cano_base = img_cano
        self.passou = False
        self.definir_height()

    def definir_height(self):
        self.height = random.randrange(50, 450)
        self.pos_base = self.height + self.ditancia
        self.pos_topo = self.height - self.cano_base.get_height()

    def mover(self):
        self.x -= self.vel

    def desenhar(self, tela):
        tela.blit(self.cano_topo, (self.x, self.pos_topo))
        tela.blit(self.cano_base, (self.x, self.pos_base))

    def colidir(self, passaro):
        passaro_mask = passaro.get_mask()
        topo_mask = pygame.mask.from_surface(self.cano_topo)
        base_mask = pygame.mask.from_surface(self.cano_base)

        distancia_topo = (self.x - passaro.x, self.pos_topo - round(passaro.y))
        distancia_base = (self.x - passaro.x, self.pos_base - round(passaro.y))

        base_ponto = passaro_mask.overlap(base_mask, distancia_base)
        topo_ponto = passaro_mask.overlap(topo_mask, distancia_topo)

        if base_ponto or topo_ponto:
            return True
        else:
            return False


class Chao:
    vel = 5
    widht = img_chao.get_width()
    img = img_chao

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.widht

    def mover(self):
        self.x1 -= self.vel
        self.x2 -= self.vel

        if self.x1 + self.widht < 0:
            self.x1 = self.x1 + self.widht
        if self.x2 + self.widht < 0:
            self.x2 = self.x2 + self.widht

    def desenhar(self, tela):
        tela.blit(self.img, (self.x1, self.y))
        tela.blit(self.img, (self.x2, self.y))


def desenhar_tela(tela, passaros, canos, chao, pontos):
    tela.blit(imagem_background, (0, 0))
    for passaro in passaros:
        passaro.desenhar(tela)
    for cano in canos:
        cano.desenhar(tela)

    texto = fonte_pontos.render(f'Pontos: {pontos}', 1, (255, 255, 255))
    tela.blit(texto, (tela_widht - 10 - texto.get_width(), 10))
    chao.desenhar(tela)
    pygame.display.update()
    # pygame.display.flip()


def main():
    passaros = [Passaro(230, 350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((tela_widht, tela_height))
    # pygame.display.set_caption('Flappy Passaro')
    # pygame.display.flip()
    pontos = 0
    relogio = pygame.time.Clock()
    rodando = True
    while rodando:
        relogio.tick(30)
        # pygame.display.init()
        for events in pygame.event.get():
            if events.type == pygame.quit():
                rodando = False
                pygame.quit()
                quit()

            elif events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:  # or events.key == pygame.K_UP:
                    for passaro in passaros:
                        passaro.jump()
                # if events.key == pygame.K_ESCAPE:
                #  rodando = False
                #  pygame.quit()
                #  quit()
        for passaro in passaros:
            passaro.move()
        chao.mover()

        adicionar_cano = False
        remover_cano = []
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    passaros.pop(i)
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True
            cano.mover()
            if cano.x + cano.cano_topo.get_width() < 0:
                remover_cano.append(cano)

        if adicionar_cano:
            pontos += 1
            canos.append(Cano(600))
        for cano in remover_cano:
            canos.remove(cano)
        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                passaros.pop(i)
    #pygame.display.flip()
        desenhar_tela(tela, passaros, canos, chao, pontos)


if __name__ == '__main__':
    main()
