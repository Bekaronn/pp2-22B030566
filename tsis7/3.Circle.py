import pygame

pygame.init()
pygame.display.set_caption('Ball')
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

x = 300
y = 300

while True:
    screen.fill((255,255,255))

    pygame.draw.circle(screen, (170, 74, 68), (y,x), 25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pressed = pygame.key.get_pressed()
    if x>0:
        if pressed[pygame.K_UP]: x -= 20
    if x<600:
        if pressed[pygame.K_DOWN]: x += 20
    if y<600:
        if pressed[pygame.K_RIGHT]: y += 20
    if y>0:
        if pressed[pygame.K_LEFT]: y -= 20
    
    pygame.display.flip()
    clock.tick(60)