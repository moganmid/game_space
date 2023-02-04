import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, ship):
        """Создаем пулю в позиции корабля"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 255, 255, 255
        self.speed = 1.5
        self.rect.centerx = ship.rect.centerx
        self.rect.center = ship.rect.center
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Отрисовка пули"""
        pygame.draw.rect(self.screen, self.color, self.rect)