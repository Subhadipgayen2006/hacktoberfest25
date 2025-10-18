# zombie_survival.py
import pygame, random, sys
pygame.init()

W, H = 800, 600
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("🧟‍♂️ Zombie Survival")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect(center=(W//2, H//2))
        self.speed = 6

    def update(self, keys):
        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_s]: self.rect.y += self.speed
        if keys[pygame.K_a]: self.rect.x -= self.speed
        if keys[pygame.K_d]: self.rect.x += self.speed

        self.rect.clamp_ip(pygame.Rect(0, 0, W, H))

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(random.randint(0, W), random.randint(-50, -10)))
        self.speed = random.randint(2, 5)

    def update(self, keys):
        self.rect.y += self.speed
        if self.rect.top > H:
            self.kill()

player = Player()
all_sprites = pygame.sprite.Group(player)
zombies = pygame.sprite.Group()

score = 0
spawn_time = 0

while True:
    keys = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    spawn_time += 1
    if spawn_time > 25:
        spawn_time = 0
        z = Zombie()
        all_sprites.add(z)
        zombies.add(z)

    all_sprites.update(keys)

    if pygame.sprite.spritecollideany(player, zombies):
        print(f"💀 Game Over! Final Score: {score}")
        pygame.quit()
        sys.exit()

    score += 1
    win.fill(BLACK)
    all_sprites.draw(win)
    pygame.display.flip()
    clock.tick(60)
