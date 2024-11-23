import pygame

fps = 60
width, height = (800,600)
backgroundColor = (0, 0, 0)
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("mar io")

class Fighter(pygame.sprite.Sprite):

    def __init__(self, health, xpos, ypos):
        self.health = 1000
        self.xpos = 10
        self.ypos = 10
    
    def move(self, dx, dy):
        pass

def draw(window):
    window.fill(backgroundColor)

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw(window)
        
    pygame.quit()

main()