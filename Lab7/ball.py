import pygame

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Movement")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

pos_x, pos_y = 200, 200
move = 20  

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (pos_x, pos_y), 25)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT] and pos_x < WIDTH - 25:
        pos_x += move
    if keys[pygame.K_LEFT] and pos_x > 25:
        pos_x -= move
    if keys[pygame.K_DOWN] and pos_y < HEIGHT - 25:
        pos_y += move
    if keys[pygame.K_UP] and pos_y > 25:
        pos_y -= move

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
