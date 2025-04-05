import pygame
from pygame.locals import *
import sys
import datetime

pygame.init()

#Настройки окна
WIDTH, HEIGHT = 800, 600
TOOLBAR_HEIGHT = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Paint")

clock = pygame.time.Clock()
canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill((255, 255, 255))

#Переменные
drawing = False
last_pos = None
start_pos = None
brush_size = 5
eraser_size = 50  
color = (0, 0, 0)
tool = "brush"

#Цвета
colors = [
    (0, 0, 0),       # Черный
    (255, 0, 0),     # Красный
    (0, 255, 0),     # Зеленый
    (0, 0, 255),     # Синий
    (255, 255, 0),   # Желтый
    (255, 255, 255), # Белый(ластик)
]

#Кнопки 
font = pygame.font.SysFont(None, 24)

def draw_button(x, label, selected=False):
    color = (180, 180, 180) if selected else (220, 220, 220)
    rect = pygame.Rect(x, 5, 70, 40)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2)
    text = font.render(label, True, (0, 0, 0))
    screen.blit(text, (x + 10, 15))
    return rect

def draw_toolbar():
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, TOOLBAR_HEIGHT))
    buttons.clear()

    # Инструменты
    tools = [("Brush", "brush"), ("Rect", "rectangle"), ("Circle", "circle"), ("Eraser", "eraser")]
    for i, (label, name) in enumerate(tools):
        x = 10 + i * 80
        btn = draw_button(x, label, tool == name)
        buttons.append((btn, "tool", name))

    # Цвета
    for i, c in enumerate(colors):
        x = 350 + i * 35
        rect = pygame.Rect(x, 10, 30, 30)
        pygame.draw.rect(screen, c, rect)
        pygame.draw.rect(screen, (0, 0, 0), rect, 2)
        buttons.append((rect, "color", c))

    #Save и Clear
    save_btn = draw_button(650, "Save")
    clear_btn = draw_button(730, "Clear")
    buttons.append((save_btn, "save", None))
    buttons.append((clear_btn, "clear", None))

def handle_button_click(pos):
    global tool, color, canvas
    for rect, btn_type, value in buttons:
        if rect.collidepoint(pos):
            if btn_type == "tool":
                tool = value
            elif btn_type == "color":
                color = value
            elif btn_type == "save":
                filename = f"paint_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                pygame.image.save(canvas, filename)
                print(f"[💾] Saved as {filename}")
            elif btn_type == "clear":
                canvas.fill((255, 255, 255))
                print("[🧼] Canvas cleared")

#Основной цикл
buttons = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[1] < TOOLBAR_HEIGHT:
                    handle_button_click(event.pos)
                else:
                    drawing = True
                    start_pos = event.pos[0], event.pos[1] - TOOLBAR_HEIGHT
                    last_pos = start_pos

        elif event.type == MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos[0], event.pos[1] - TOOLBAR_HEIGHT
                if tool == "rectangle":
                    rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                    pygame.draw.rect(canvas, color, rect, brush_size)
                elif tool == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    pygame.draw.circle(canvas, color, start_pos, radius, brush_size)
                drawing = False

        elif event.type == MOUSEMOTION and drawing:
            current_pos = event.pos[0], event.pos[1] - TOOLBAR_HEIGHT
            if tool == "brush":
                pygame.draw.line(canvas, color, last_pos, current_pos, brush_size)
                last_pos = current_pos
            elif tool == "eraser":
                pygame.draw.line(canvas, (255, 255, 255), last_pos, current_pos, eraser_size)
                last_pos = current_pos

    screen.fill((220, 220, 220))
    draw_toolbar()
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))
    pygame.display.flip()
    clock.tick(60)
