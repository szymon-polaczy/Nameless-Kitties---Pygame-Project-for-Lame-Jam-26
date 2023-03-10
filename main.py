import sys, pygame

pygame.init()

size = width, height = 1280, 720
BLACK = 0, 0, 0
WHITE = 255, 255, 255

screen = pygame.display.set_mode(size)

font = pygame.font.Font('PatrickHandSC-Regular.ttf', 72)

random_text = 'lucy'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    img = font.render(random_text, True, WHITE)

    img_rect = img.get_rect() 

    center_cords = (
        (1280 / 2 - (img_rect.height / 2)),
        (720 / 2 - (img_rect.width / 2))
    )

    screen.fill(BLACK)
    screen.blit(img, center_cords)

    pygame.display.flip()