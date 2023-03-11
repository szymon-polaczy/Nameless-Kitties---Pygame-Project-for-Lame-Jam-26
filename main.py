import sys, pygame
from random import seed
from random import randint
from datetime import datetime

pygame.init()

seed(datetime.now())

BLACK = 0, 0, 0
WHITE = 255, 255, 255
SCREEN_SIZE = width, height = 1280, 720
SCREEN = pygame.display.set_mode(SCREEN_SIZE)
MAIN_FONT = pygame.font.Font('PatrickHandSC-Regular.ttf', 72)
MEDIUM_FONT = pygame.font.Font('PatrickHandSC-Regular.ttf', 36)

MAX_TORSO = 7
MAX_TAIL = 6
MAX_REAR = 6
MAX_LEAR = 6
MAX_FACE = 15

def display_in_the_center(element):
    element_rect = element.get_rect()

    return [
        ((SCREEN_SIZE[0] / 2) - (element_rect.width / 2)),
        ((SCREEN_SIZE[1] / 2) - (element_rect.height / 2))
    ]

def generate_random_cat():
    cat = []

    torso_number = randint(1, MAX_TORSO)
    tail_numer = randint(1, MAX_TAIL)
    rear_number = randint(1, MAX_REAR)
    lear_number = randint(1, MAX_LEAR)
    face_number = randint(1, MAX_FACE)

    cat.append(pygame.image.load(f'torso/{torso_number}.png'))
    cat.append(pygame.image.load(f'tail/{tail_numer}.png'))
    cat.append(pygame.image.load(f'rear/{rear_number}.png'))
    cat.append(pygame.image.load(f'lear/{lear_number}.png'))
    cat.append(pygame.image.load(f'face/{face_number}.png'))

    return cat

def start_game_loop():

    generated_cat = generate_random_cat()

    task = 'Name the kitty'
    task_text = MAIN_FONT.render(task, True, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: generated_cat = generate_random_cat()
            
        SCREEN.fill(BLACK)
        
        for part in generated_cat:
            SCREEN.blit(part, display_in_the_center(part)) 

        center_position_task_text = display_in_the_center(task_text)
        SCREEN.blit(task_text, (center_position_task_text[0], -10 ))

        pygame.display.flip()

def initialize_game():

    title = 'Nameless Kitties'
    title_text = MAIN_FONT.render(title, True, WHITE)

    info = 'Click space to start..'
    continue_text = MEDIUM_FONT.render(info, True, WHITE)

    print(display_in_the_center(title_text))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: start_game_loop()

        SCREEN.fill(BLACK)

        center_title_text_position = display_in_the_center(title_text)
        center_title_text_position[1] = center_title_text_position[1] + -50        
        SCREEN.blit(title_text, display_in_the_center(title_text))

        center_continue_text_position = display_in_the_center(continue_text)
        center_continue_text_position[1] = center_continue_text_position[1] + 75
        SCREEN.blit(continue_text, center_continue_text_position)

        pygame.display.flip()
    
initialize_game()