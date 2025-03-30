import pygame
import sys
import random
import time
import os

pygame.init()
pygame.mixer.init()

# Получаем путь к текущей папке
BASE_DIR = os.path.dirname(__file__)

# Загрузка фоновой музыки
music_path = os.path.join(BASE_DIR, "music", "background.wav")
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)  # Бесконечное воспроизведение

# Константы
FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

# Цвета
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Загрузка изображений
background = pygame.image.load(os.path.join(BASE_DIR, "images", "AnimatedStreet.png"))

# Создание экрана
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(BASE_DIR, "images", "Enemy.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, enemy_pos):
        super().__init__()
        self.image = pygame.image.load(os.path.join(BASE_DIR, "images", "coin.png"))
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        while self.rect.collidelist(enemy_pos) != -1:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global COINS_COLLECTED
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        elif pygame.sprite.spritecollideany(self, players):
            COINS_COLLECTED += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(BASE_DIR, "images", "Player.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

# Создание спрайтов
P1 = Player()
E1 = Enemy()
C1 = Coin([E1.rect])

# Группы спрайтов
enemies = pygame.sprite.Group(E1)
coins = pygame.sprite.Group(C1)
all_sprites = pygame.sprite.Group(P1, E1, C1)
players = pygame.sprite.Group(P1)

# Увеличение скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        crash_sound = pygame.mixer.Sound(os.path.join(BASE_DIR, "music", "crash.wav"))
        crash_sound.play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    coins_collected_text = font_small.render(f"Coins Collected: {COINS_COLLECTED}", True, BLACK)
    coins_collected_rect = coins_collected_text.get_rect()
    coins_collected_rect.topright = (SCREEN_WIDTH - 10, 10)
    DISPLAYSURF.blit(coins_collected_text, coins_collected_rect)

    pygame.display.update()
    pygame.time.Clock().tick(FPS)
