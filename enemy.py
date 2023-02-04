import pygame

class Enemy(pygame.sprite.Sprite):
    """класс одного корабля"""

    def __init__(self, screen):
        """инициализация и начальная позиция"""
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод корабля на экран"""
        self.screen.blit(self.image, self.rect)