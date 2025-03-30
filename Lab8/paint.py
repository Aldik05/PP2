import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    points = []
    is_drawing_rect = False
    rect_start_pos = None
    rectangles = []

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Изменение цвета
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_d:
                    is_drawing_rect = True
                    rect_start_pos = pygame.mouse.get_pos()

            # Обработка нажатий мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Mouse clicked at {event.pos} with button {event.button}")

                if event.button == 1:  # Левая кнопка увеличивает радиус
                    radius = min(200, radius + 5)
                elif event.button == 3:  # Правая кнопка уменьшает радиус
                    radius = max(1, radius - 5)

            if event.type == pygame.MOUSEMOTION:
                buttons = pygame.mouse.get_pressed()
                if buttons[0] and not is_drawing_rect:  # Левая кнопка зажата
                    position = event.pos
                    points.append(position)
                    points = points[-256:]  # Ограничиваем количество точек
                    print(f"Points list: {points}")  # Отладка

            if event.type == pygame.MOUSEBUTTONUP:
                if is_drawing_rect:
                    is_drawing_rect = False
                    rect_end_pos = pygame.mouse.get_pos()
                    rect = pygame.Rect(rect_start_pos, 
                                       (rect_end_pos[0] - rect_start_pos[0], rect_end_pos[1] - rect_start_pos[1]))
                    rectangles.append(rect)

        # Очистка экрана
        screen.fill((0, 0, 0))

        # Рисуем все прямоугольники
        for rect in rectangles:
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)

        # Рисуем линии
        if not is_drawing_rect:
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
                i += 1

        # Предпросмотр прямоугольника
        if is_drawing_rect:
            rect_end_pos = pygame.mouse.get_pos()
            rect = pygame.Rect(rect_start_pos, 
                               (rect_end_pos[0] - rect_start_pos[0], rect_end_pos[1] - rect_start_pos[1]))
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()
