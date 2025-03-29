import pygame
import os

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (255, 255, 255)
FONT_SIZE = 35
FONT_COLOR = (0, 0, 0)

MUSIC_FILES = [
    r"C:\Users\ACER\Desktop\PP2\PP2-1\Lab7\music\Bruno Mars - Finesse.mp3",
    r"C:\Users\ACER\Desktop\PP2\PP2-1\Lab7\music\Jay Sean feat. Lil Wayne - Down.mp3",
    r"C:\Users\ACER\Desktop\PP2\PP2-1\Lab7\music\Mac Miller - Self Care.mp3"
]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player")
font = pygame.font.Font(None, FONT_SIZE)

current_music = 0
paused = False  

def play_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.load(MUSIC_FILES[current_music])
        pygame.mixer.music.play()

def stop_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global current_music, paused
    current_music = (current_music + 1) % len(MUSIC_FILES)
    paused = False
    pygame.mixer.music.load(MUSIC_FILES[current_music])
    pygame.mixer.music.play()

def prev_music():
    global current_music, paused
    current_music = (current_music - 1) % len(MUSIC_FILES)
    paused = False
    pygame.mixer.music.load(MUSIC_FILES[current_music])
    pygame.mixer.music.play()

play_music()

running = True
while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_RIGHT:
                next_music()
            elif event.key == pygame.K_LEFT:
                prev_music()

    text = font.render("SPACE: Play/Pause | LEFT/RIGHT: Change track", True, FONT_COLOR)
    text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    screen.blit(text, text_rect)

    pygame.display.update()

pygame.quit()
