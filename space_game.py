import pygame, controls
from main_ship import Ship
from pygame.sprite import Group

def run():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Space Invaders")
    bg_color = (0, 0, 0)
    ship = Ship(screen)
    bullets = Group()

    while True:
        controls.events(screen, ship, bullets)
        ship.update_ship()
        controls.update(bg_color, screen, ship, bullets)
        controls.update_bullets(bullets)

run()