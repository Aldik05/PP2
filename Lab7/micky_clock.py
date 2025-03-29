import pygame
import os
from datetime import datetime
import math

def get_clock_pos(clock_dict, clock_hand):
    x = 410 + 300 * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = 410 + 300 * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y

pygame.init()
screen = pygame.display.set_mode((820, 820))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

clock60 = dict(zip(range(60), range(0, 360, 6)))
font = pygame.font.SysFont('Verdana', 36)

base_path = r"C:\Users\ACER\Desktop\PP2\PP2-1\Lab7\images"

bg = pygame.image.load(os.path.join(base_path, "mic.png")).convert()
bg_rect = bg.get_rect()

image_left = pygame.image.load(os.path.join(base_path, "second.png"))
left_rect = image_left.get_rect(center=(410, 410))

image_right = pygame.image.load(os.path.join(base_path, "minute.png"))
right_rect = image_right.get_rect(center=(410, 410))

running = True
while running:
    screen.fill((255, 255, 255))  
    screen.blit(bg, bg_rect)

    t = datetime.now()
    minute, second = t.minute, t.second

    position_minute = get_clock_pos(clock60, minute)
    position_second = get_clock_pos(clock60, second)

    angle_minute = math.degrees(math.atan2(position_minute[1] - 410, position_minute[0] - 410)) + 90
    angle_second = math.degrees(math.atan2(position_second[1] - 410, position_second[0] - 410)) + 90

    right_hand_rot = pygame.transform.rotate(image_right, -angle_minute)
    left_hand_rot = pygame.transform.rotate(image_left, -angle_second)

    right_rect_rot = right_hand_rot.get_rect(center=(410, 410))
    left_rect_rot = left_hand_rot.get_rect(center=(410, 410))

    screen.blit(right_hand_rot, right_rect_rot.topleft)
    screen.blit(left_hand_rot, left_rect_rot.topleft)

    time_render = font.render(f"{t:%H:%M:%S}", True, (25, 100, 100), (255, 255, 255))
    screen.blit(time_render, (10, 10))

    pygame.display.update()
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
