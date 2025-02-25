# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_rectangle(screen, rect, color, thickness, border_radius):
    pygame.draw.rect(screen, color, rect, thickness, border_radius)

def draw_circle(screen, center, radius, color, thickness):
    pygame.draw.circle(screen, color, center, radius, thickness)

def draw_line(surface, color, start_pos, end_pos, thickness):
    pygame.draw.line(surface, color, start_pos, end_pos, thickness)

def draw_polygon(screen, color, points, thickness=0):
    pygame.draw.polygon(screen, color, points, thickness)


def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initalize the clock here
    running = True
    while running:
        running = handle_events()
        screen.fill(config.GREEN) # Use color from config
        # man?
        my_rect = [200, 300, 200, 150]
        draw_rectangle(screen, my_rect, config.BLACK, 0, 0)

        circle_center = (300, 220)
        radius = 40
        draw_circle(screen, circle_center, radius, config.BLACK, 0)# Head

        draw_line(screen, config.BLACK, [200, 300], [150, 450], 10)# left arm
        draw_line(screen, config.BLACK, [400, 300], [450, 450], 10)# right arm

        draw_circle(screen, (280, 210), 6, config.RED, 0) # left eye
        draw_circle(screen, (320, 210), 6, config.RED, 0) # right eye
        pygame.draw.circle(screen, config.WHITE, (300, 230), 15, 5, draw_bottom_left=True, draw_bottom_right=True) #smile 
        my_rect = [280, 255, 40, 50] # neck
        draw_rectangle(screen, my_rect, config.BLACK, 0, 0)
       
    #     five_points = [
    #        (100, 50),
    #        (400, 50),
    #        (350, 200),
    #        (200, 100),
    #        (250, 75)
    #    ]
    #     three_points = [
    #        (300, 200),
    #        (500, 200),
    #        (400, 400)
    #     ]
    #     four_point = [
    #         (600, 100),
    #         (650, 50),
    #         (700 ,100),
    #         (650, 150)
    #     ]

    #     thickness = 0
    #     draw_polygon(screen, config.RED, five_points, thickness)
    #     draw_polygon(screen, config.BLUE, three_points, thickness=5)
    #     draw_polygon(screen, config.WHITE, four_point, thickness)
        pygame.display.flip()
        # Limit the frame rate to the specified frames per second
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()



