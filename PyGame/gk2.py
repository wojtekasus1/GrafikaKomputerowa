import pygame
import sys
pygame.init()
szer, wys = 800, 600
ekran = pygame.display.set_mode((szer, wys))
class BlackCircleWithYellowSquare:
    def __init__(self, circle_radius, square_side_length):
        self.x = szer // 2
        self.y = wys // 2
        self.circle_radius = circle_radius
        self.square_side_length = square_side_length
    def draw(self):
        ekran.fill((255, 255, 255))
        pygame.draw.circle(ekran, (0, 0, 0), (self.x, self.y), self.circle_radius)
        square_x = self.x - self.square_side_length / 2
        square_y = self.y - self.square_side_length / 2
        pygame.draw.rect(ekran, (255, 255, 0), (square_x, square_y, self.square_side_length, self.square_side_length))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    figura = BlackCircleWithYellowSquare(100, 80)
    figura.draw()
    pygame.display.flip()