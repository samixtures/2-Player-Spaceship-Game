import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#CONSTANTS
FPS = 60
VEL = 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

# RGB COLORS:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Spaceship images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

def handle_yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_s] and yellow.y < HEIGHT-60:
        yellow.y += VEL
    if keys_pressed[pygame.K_d] and yellow.x + yellow.width < BORDER.x:
        yellow.x += VEL
def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_UP] and red.y > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_LEFT] and red.x > BORDER.x+20:
        red.x -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y < HEIGHT-60:
        red.y += VEL
    if keys_pressed[pygame.K_RIGHT] and red.x < WIDTH-60:
        red.x += VEL

def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    #when drawing a surface onto the screen. A surface is some item in pygame
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        handle_yellow_movement(keys_pressed, yellow)
        handle_red_movement(keys_pressed, red)
        draw_window(red, yellow)
    pygame.quit()
if __name__ == "__main__":
    main()