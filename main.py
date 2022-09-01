import sys
import pygame

pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Meteor asteroid")

clock = pygame.time.Clock()

ship_surf = pygame.image.load('./assets/images/playerShip1_red.png').convert_alpha()
ship_rect = ship_surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
bg_surf = pygame.image.load('./assets/images/bg/purple.png').convert()

# font = pygame.font.Font('')
# text_surf = font.render('Space', True, (255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)

    display_surface.fill((0,0,0))
    display_surface.blit(bg_surf, (0, 0))

    if ship_rect.top > 0:
        ship_rect.y -= 4
    display_surface.blit(ship_surf, ship_rect)

    pygame.display.update()
