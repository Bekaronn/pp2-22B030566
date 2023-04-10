import pygame

def main():
    #init and display
    pygame.init()
    pygame.display.set_caption("Paint")
    screen = pygame.display.set_mode((700,700))

    #fps
    FPS = pygame.time.Clock()

    #var
    x = 0
    y = 0
    color = (255,0,0)
    ls_sqr = []
    figure = 0
    real = True
    radius = 30

    #color
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)

    while True:
        #pressed
        pressed = pygame.mouse.get_pressed()
        if pressed[0]:
            y = position
            if figure == 2:
                ls_sqr += ("Era",event.pos,radius),

        for event in pygame.event.get():
            #quit
            if event.type == pygame.QUIT:
                return
            #mousemotion and pos
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
            #button down
            if event.type == pygame.MOUSEBUTTONDOWN:
                y = position
                x = position
                real = True
                if figure == 1:
                    ls_sqr += ("Cir",event.pos,color,radius),
            #button up
            if event.type == pygame.MOUSEBUTTONUP:
                if figure == 0:
                    y = position
                    ls_sqr += ("Rec",x,y,color),
                    real = False
            #keydown
            if event.type == pygame.KEYDOWN:
                #change_color
                if event.key == pygame.K_1:
                    color = RED
                if event.key == pygame.K_2:
                    color = GREEN
                if event.key == pygame.K_3:
                    color = BLUE
                #select figure
                if event.key == pygame.K_q:
                    figure = 0
                if event.key == pygame.K_w:
                    figure = 1
                if event.key == pygame.K_e:
                    figure = 2
                #change circle size
                if event.key == pygame.K_UP:
                    radius += 5
                if event.key == pygame.K_DOWN:
                    radius -= 5

        #display and draw
        screen.fill((255,255,255))

        draw("self",ls_sqr,screen)
        if figure == 0:
            if x!=0 and y!=0 and real == True:
                if x[0] > y[0]:
                    if x[1] > y[1]:
                        pygame.draw.rect(screen, color, (y[0], y[1], x[0]-y[0], x[1]-y[1]))
                    if x[1] < y[1]:
                        pygame.draw.rect(screen, color, (y[0], x[1], x[0]-y[0], y[1]-x[1]))
                if x[0] < y[0]:
                    if x[1] > y[1]:
                        pygame.draw.rect(screen, color, (x[0], y[1], y[0]-x[0], x[1]-y[1]))
                    if x[1] < y[1]:
                        pygame.draw.rect(screen, color, (x[0], x[1], y[0]-x[0], y[1]-x[1]))

        pygame.display.update()
        #FPS
        FPS.tick(60)

#draw funtion
def draw(self,ls,screen):
    for x in ls:
        #Rectangle draw
        if x[0] == "Rec":
            if x[1][0] > x[2][0]:
                if x[1][1] > x[2][1]:
                    pygame.draw.rect(screen, x[3], (x[2][0], x[2][1], x[1][0]-x[2][0], x[1][1]-x[2][1]))
                if x[1][1] < x[2][1]:
                    pygame.draw.rect(screen, x[3], (x[2][0], x[1][1], x[1][0]-x[2][0], x[2][1]-x[1][1]))
            if x[1][0] < x[2][0]:
                if x[1][1] > x[2][1]:
                    pygame.draw.rect(screen, x[3], (x[1][0], x[2][1], x[2][0]-x[1][0], x[1][1]-x[2][1]))
                if x[1][1] < x[2][1]:
                    pygame.draw.rect(screen, x[3], (x[1][0], x[1][1], x[2][0]-x[1][0], x[2][1]-x[1][1]))
        #Erase draw
        if x[0] == "Era":
            pygame.draw.circle(screen, (255,255,255), (x[1][0],x[1][1]), x[2])
        #Circle draw
        if x[0] == "Cir":
            pygame.draw.circle(screen, x[2], (x[1][0],x[1][1]), x[3])


main()