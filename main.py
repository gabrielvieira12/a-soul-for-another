import pygame
from pygame.locals import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
import random

pygame.init()

#Janela
janela_largura = 1200
janela_altura = 675
janela = pygame.display.set_mode((janela_largura, janela_altura))
pygame.display.set_caption('One soul for another')

#Game variables
tile_size_largura = 50
tile_size_altura = 50
clock = pygame.time.Clock()
fps = 30
scroll = [0,0]

#Load Sounds


#Load Images
clouds_img = pygame.image.load("clouds.png")

sky_img = pygame.image.load("sky.jpg")

sea_img = pygame.image.load("sea.png")

far_ground_img = pygame.image.load("far-grounds.png")

fundo_menu_img = pygame.image.load("FundoMenuTeste.jpg")

#def draw_grid():
    #for linha in range(0,18):
        #pygame.draw.line(janela, (255, 255, 255), (0, linha * tile_size_largura), (janela_largura, linha * tile_size_largura))
    #for linha in range(0, 24):
        #pygame.draw.line(janela, (255, 255, 255), (linha * tile_size_altura, 0), (linha * tile_size_altura, janela_altura))

#Estágios do Jogo
class GameStage():
    def __init__(self):
        self.state = "Menu"

    def Menu(self):
        janela.blit(fundo_menu_img, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.state = "Fase1"

    def Fase1(self):
        janela2 = pygame.display.set_mode((janela_largura, janela_altura))
        janela2.blit(sky_img, (0, 0))
        janela2.blit(clouds_img, (0, -10))
        janela2.blit(sea_img, (0, 100))
        janela2.blit(far_ground_img, (0, 410))




        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            self.state = "Menu"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        world.__init__(world_data)
        #olhosvoadores_g.draw(janela)
        #olhosvoadores_g.update()
        player.update()

        #draw_grid()


    def controla_Fase(self):
        if self.state == "Menu":
            #pygame.mixer.music.load("musicamenu.mp3")
            self.Menu()
            #pygame.mixer.music.play()
            #pygame.event.wait()


        if self.state == "Fase1":
            #pygame.mixer.music.load("musicafase1.mp3")
            self.Fase1()
            #pygame.mixer.music.play()
            #pygame.event.wait()'''

class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []

        self.images_parada_right = []
        self.images_parada_left = []

        self.images_pulando_right = []
        self.images_pulando_left = []

        self.images_caindo_right = []
        self.images_caindo_left = []

        self.index = 0
        self.counter = 0



        #Parada
        for num in range(1,12):
            kaorip_img = pygame.image.load(f"Kaoriparada{num}.png")
            kaorip_img = pygame.transform.scale(kaorip_img, (87, 100))
            kaoripleft_img = pygame.transform.flip(kaorip_img, True, False)
            self.images_parada_right.append(kaorip_img)
            self.images_parada_left.append(kaoripleft_img)

        #Correndo
        for num in range(1, 9):
            kaoric_img = pygame.image.load(f"Kaoricorrendo{num}.png")
            kaoric_img = pygame.transform.scale(kaoric_img, (87, 100))
            kaoricleft_img = pygame.transform.flip(kaoric_img, True, False)
            self.images_right.append(kaoric_img)
            self.images_left.append(kaoricleft_img)

        #Pulando
        for num in range(1,4):
            kaorij_img = pygame.image.load(f"Kaoripulando{num}.png")
            kaorij_img = pygame.transform.scale(kaorij_img, (87, 100))
            kaorijleft_img = pygame.transform.flip(kaorij_img, True, False)
            self.images_pulando_right.append(kaorij_img)
            self.images_pulando_left.append(kaorijleft_img)

        #Caindo
        for num in range(1,4):
            kaorif_img = pygame.image.load(f"Kaoripulando{num}.png")
            kaorif_img = pygame.transform.scale(kaorif_img, (87, 100))
            kaorifleft_img = pygame.transform.flip(kaorif_img, True, False)
            self.images_caindo_right.append(kaorif_img)
            self.images_caindo_left.append(kaorifleft_img)

        self.image = self.images_parada_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def Correndo(self,dx):
        walk_cooldown = 1

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= 7
            self.counter += 1
            self.direction = -1
            scroll[0] += 10
        if key[pygame.K_d]:
            dx += 7
            self.counter += 1
            self.direction = 1
            scroll[0] -= 10
        if key[pygame.K_LEFT]:
            dx -= 7
            self.counter += 1
            self.direction = -1
            scroll[0] += 10
        if key[pygame.K_RIGHT]:
            dx += 7
            self.counter += 1
            self.direction = 1
            scroll[0] -= 10

            # Adicionar Animações
        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 1
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

    def Parada(self,dx):
        parada_cooldown = 5
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == False and key[pygame.K_d] == False and key[pygame.K_RIGHT] == False and key[
            pygame.K_LEFT] == False:
            self.counter += 1
            self.index += 1
            if self.index >= len(self.images_parada_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_parada_right[self.index]
            if self.direction == -1:
                self.image = self.images_parada_left[self.index]


        # Adicionar Animações
        if self.counter > parada_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_parada_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_parada_right[self.index]
            if self.direction == -1:
                self.image = self.images_parada_left[self.index]

    def Pulando(self):
        pulando_cooldown = 5
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.counter += 1
            self.index += 1
        if self.index >= len(self.images_pulando_right):
            self.index = 0
        if self.direction == 1:
            self.image = self.images_pulando_right[self.index]
        if self.direction == -1:
            self.image = self.images_pulando_left[self.index]

        # Adicionar Animações
        if self.counter > pulando_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_pulando_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_pulando_right[self.index]
            if self.direction == -1:
                self.image = self.images_pulando_left[self.index]

    def Caindo(self):
        caindo_cooldown = 3
        self.counter += 1
        self.index += 1
        if self.index >= len(self.images_caindo_right):
            self.index = 0
        if self.direction == 1:
            self.image = self.images_caindo_right[self.index]
        if self.direction == -1:
            self.image = self.images_caindo_left[self.index]

        # Adicionar Animações
        if self.counter > caindo_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_caindo_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_caindo_right[self.index]
            if self.direction == -1:
                self.image = self.images_caindo_left[self.index]

    def update(self):
        dx = 0
        dy = 0


        # Movimento Player
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == False and key[pygame.K_d] == False and key[pygame.K_RIGHT] == False and key[
            pygame.K_LEFT] == False and key[pygame.K_SPACE] == False :
            self.Parada(dx)

        if key[pygame.K_a] == True or key[pygame.K_d] == True or key[pygame.K_RIGHT] == True or key[
        pygame.K_LEFT] == True and key[pygame.K_SPACE] == False:
            self.Correndo(dx)

        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -20
            self.Pulando()
            self.jumped = True

        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -20
            self.Pulando()
            self.jumped = True

        if key[pygame.K_SPACE] == False:
            self.jumped = False




        #Adicionar Gravidade
        self.vel_y +=1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        #Check se Colide com algo
        for tile in world.tile_list:
            #Colisão em x
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                if self.direction == 1:
                    self.rect.right = tile[1].left
                elif self.direction == -1:
                    self.rect.left = tile[1].right

            #Colisão em y
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                #Check se bellow um chão e pula
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                # Check se above um chão e caindo
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0

        #Update posição Player
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > janela_altura:
            self.rect.bottom = janela_altura
            dy = 0


        #Desenha player na tela
        janela.blit(self.image,self.rect)
        pygame.draw.rect(janela, (255,255,255), self.rect, 2)
        pygame.draw.rect(janela, (255, 255, 255), self.rect, 2)

class World():
    def __init__(self,data):
        self.tile_list = []

        #Load Images
        chao_padrao_img = pygame.image.load("chão padrão.png")
        chao_pedra1_img = pygame.image.load("chão pedra 1.jpg")
        chao_pedra2_img = pygame.image.load("chão pedra 2.jpg")

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(chao_padrao_img,(tile_size_largura,tile_size_altura))
                    janela.blit(img, (col_count * 50 + scroll[0], row_count * 50 + scroll[1]))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_largura + scroll[0]
                    img_rect.y = row_count * tile_size_altura + scroll[1]
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(chao_pedra1_img,(tile_size_largura,tile_size_altura))
                    janela.blit(img, (col_count * 50 + scroll[0], row_count * 50 + scroll[1]))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_largura + scroll[0]
                    img_rect.y = row_count * tile_size_altura + scroll[1]
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(chao_pedra2_img,(tile_size_largura,tile_size_altura))
                    janela.blit(img,(col_count * 50 + scroll[0],row_count * 50 + scroll[1]))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size_largura + scroll[0]
                    img_rect.y = row_count * tile_size_altura + scroll[1]
                    tile = (img,img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    olho_voador = Enemy(col_count * tile_size_largura + scroll[0], row_count * tile_size_altura + scroll[1])
                    olhosvoadores_g.add(olho_voador)
                col_count += 1
            row_count += 1

    '''def draw(self):
        for tile in self.tile_list:
            janela.blit(tile[0],tile[1])'''
        # pygame.draw.rect(janela, (255,255,255), tile[1], 1)'''

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("olhovoador.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 5
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 10:
            self.move_direction *= -1
            self.move_counter *= -1
        janela.blit(self.image, self.rect)

world_data = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
[2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,],
[2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,3,2,2,3,2,2,2,3,2,3,2,2,2,2,2,3,2,2,2,2,3,2,2,2,2,2,2,2,3,2,],
[2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,3,2,2,3,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,2,2,2,2,2,3,]
]

olhosvoadores_g = pygame.sprite.Group()
world = World(world_data)
player = Player(100,400)
game_states = GameStage()

#Game Loop
run = True
while run:
    clock.tick(fps)
    game_states.controla_Fase()
    pygame.display.update()

