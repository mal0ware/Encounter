import subprocess
subprocess.run(['pip', 'install', 'pygame']) #installs pygame
import pygame
from fighter import Fighter

#stops python from writing .pyc files after running code
import sys
sys.dont_write_bytecode = True

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

#clock stuff
clock = pygame.time.Clock()
FPS = 60
#colors
GREEN = (0,255,0)
BLACK = (0,0,0)

# fighter variables
sprite1Size = 0.25
sprite1Scale = 1
sprite2Size = 0.25
sprite2Scale = 1
p1Offset = [72, 56]
p2Offset = [112, 107]
spriteData1 = [sprite1Size, sprite1Scale, p1Offset]
spriteData2 = [sprite2Size, sprite2Scale, p2Offset]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("enCOUNTER")

# game loop
bg_image = pygame.image.load("assets/louispngs/backgroundv2.jpg").convert_alpha()
louisSheet = pygame.image.load("assets/louispngs/p1SpriteSheet.png").convert_alpha()
louisSheet2 = pygame.image.load("assets/louispngs/p2SpriteSheet.png").convert_alpha()

#animation steps
p1AnimationSteps = [2, 1, 1, 1, 1]
p2AnimationSteps = [1,1,1,1,2]

# #load 

# def spriteTransform(img):
#     sprite = pygame.transform.scale(img, (spriteSize * spriteScale, spriteSize * spriteScale))
#     return sprite

# sprites = []
# player1Sprite = spriteTransform(pygame.image.load("playerNuetralv2.png"))
# sprites.append(player1Sprite)

# player2Sprite = pygame.image.load(nuetral_stance)


#fighters

def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))


#health bars
def drawHealthBar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, BLACK, (x - 2, y-2, 404, 34))
    pygame.draw.rect(screen, GREEN, (x, y, 400*ratio, 30))

def drawBlackBar(x,y):
    pygame.draw.rect(screen, (255,0,0), (x, y, 400,30))

# the two fighters
fighter1 = Fighter(200, 500, spriteData1, louisSheet, p1AnimationSteps)
fighter2 = Fighter(600, 400, spriteData2, louisSheet2, p2AnimationSteps)

run = True
while run:
    clock.tick(FPS)
    draw_bg()
    drawBlackBar(20,20)
    drawHealthBar(fighter1.health, 20, 20)
    drawBlackBar(580,20)
    drawHealthBar(fighter2.health, 580, 20)
    #move fighters
    fighter1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter2)
    #fighter2.move(SCREEN_WIDTH, SCREEN_HEIGHT)

    fighter1.draw(screen)
    fighter2.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #display updater
    pygame.display.update()

#exits game
pygame.quit()