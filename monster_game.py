import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self, image, speed_x, speed_y, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y]

class Hero(Character):
    pass

class Goblin(Character):
    pass

class Monster(Character):
    def move(self, width, height):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.center = [self.x, self.y]
        if self.x > width:
            self.speed_x = 0
            self.speed_y = 5
        if self.y > height:
            self.speed_x = -5
            self.speed_y = 0
        if self.x < 0:
            self.speed_x = 0
            self.speed_y = -5
        if self.y < 0:
            self.speed_x = 5
            self.speed_y = 0
        print(self.x, self.y)

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')

    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()

    # Our hero and monster
    player = Hero(hero_image, 0, 0, 250, 250)
    monster = Monster(monster_image, 5, 0, 150, 120)

    # Create groups for monster and player to apply draw attribute
    player_group = pygame.sprite.Group()
    player_group.add(player)

    monster_group = pygame.sprite.Group()
    monster_group.add(monster)

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            
            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        monster.move(width, height)

        # Draw background
        screen.fill(blue_color)
        screen.blit(background_image, [0, 0])
        
        # Draw player and monster
        player_group.draw(screen)
        monster_group.draw(screen)

        # Game display
        pygame.display.update()

        # Monster movement
        #pygame.display.update()
        #monster.move()

    pygame.quit()

if __name__ == '__main__':
    main()
