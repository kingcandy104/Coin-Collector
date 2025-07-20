import pygame
import sys
import random

pygame.init()

WIDTH = 400
HEIGHT = 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Coin Collector')

player_size = 60
player_x = WIDTH // 2
player_y = HEIGHT - (player_size + 20)
player_speed = 7

coin_radius = 30
coin_speed = 5
coins = []

score = 0
lives = 5
spawn_delay = 30
frame_count = 0

font = pygame.font.SysFont("Times New Roman", 40)
clock = pygame.time.Clock()

def spawn_coin():
    x = random.randint(coin_radius, WIDTH - coin_radius)
    y = 0 - coin_radius
    coins.append([x, y])

def display_text(text, x, y, size=40, colour=(255, 255, 255)):
    font_object = pygame.font.SysFont("Times New Roman", size)
    surface = font_object.render(text, True, colour)
    WINDOW.blit(surface, (x, y))

running = True
while running:
    WINDOW.fill((0, 0, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_x += player_speed

    if player_x - player_size // 2 < 0:
        player_x = player_size // 2
    if player_x + player_size // 2 > WIDTH:
        player_x = WIDTH - player_size // 2

    frame_count += 1
    if frame_count % spawn_delay == 0:
        spawn_coin()

    pygame.draw.circle(WINDOW, (0, 0, 255), (player_x, player_y), player_size // 2)
    player_rect = pygame.Rect(player_x - player_size // 2, player_y - player_size // 2, player_size, player_size)

    for coin in coins[:]:
        coin[1] += coin_speed
        pygame.draw.circle(WINDOW, (255, 255, 0), (coin[0], coin[1]), coin_radius)

        coin_rect = pygame.Rect(coin[0] - coin_radius, coin[1] - coin_radius, coin_radius * 2, coin_radius * 2)
        if player_rect.colliderect(coin_rect):
            coins.remove(coin)
            score += 1
            
        elif coin[1] > HEIGHT + coin_radius:
            coins.remove(coin)
            lives -= 1

    display_text(f"Score: {score}", 10, 10)
    display_text(f"Lives: {lives}", WIDTH - 150, 10)

    if lives <= 0:
        display_text("GAME OVER", WIDTH // 2 - 100, HEIGHT // 2, size=50, colour=(255, 0, 0))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
