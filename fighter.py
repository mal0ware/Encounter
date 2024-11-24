import pygame

class Fighter():

    def __init__(self, x, y, data, sprite_sheet, animation_steps):
        self.size = data[0]
        self.image_scale = data[1]
        self.flip = False
        self.offset = data[2]
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0 # (0 idle, 1 attack, 2 jump, 4 hit, 6 death)
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect((x,y, 80, 150))
        self.vel_y = 0
        self.action = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0
        self.health = 100

    def load_images(self, sprite_sheet, animation_steps):
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
        for x in range(animation):
            temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size+100, self.size+300)
            pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size* self.image_scale))
            temp_img_list.append(temp_img)
        animation_list.append(temp_img_list)
        return animation_list
        

    # def imageScaler(self, img, size, scale):
    #     img = pygame.transform.scale(img, (self.size * self.scale, self.size * self.scale))
    #     return img


    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        #key presses
        key = pygame.key.get_pressed()

        #performs conditionals


        #movement
        if self.attacking == False:
            #movement 
            if key[pygame.K_a]:
                dx = -SPEED
            if key[pygame.K_d]:
                dx = SPEED
            if key[pygame.K_w] and self.jump == False:
                self.vel_y = -20
                self.jump == True
            
            #attack
            if key[pygame.K_e] or key[pygame.K_q]:
                self.attack(surface, target)
                #determines attack type
                if key[pygame.K_e]:
                    self.attack_type = 1
                if key[pygame.K_q]:
                    self.attack_type = 2
            
        
        #gravity
        self.vel_y += GRAVITY
        dy += self.vel_y


        #stays on screen stuff
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 110 - self.rect.bottom
        
        #players face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        
        
        #jump 

        
        #update player pos
        self.rect.x += dx
        self.rect.y += dy


    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2*self.rect.width * self.flip), self.rect.y, 2*self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10


        pygame.draw.rect(surface, (0,255,0), attacking_rect)


    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
        surface.blit(self.image, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
        #surface.blit(self.image, (self.rect.x, self.rect.y))
        