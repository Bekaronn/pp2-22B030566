#Imports
import pygame, sys, time, random
from pygame.locals import *
import psycopg2

#postgreSQL
def connect(username, score, level):
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", database="snake", user="postgres", password="1234")
        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_score (
            username VARCHAR(32) NOT NULL,
            score VARCHAR(100) NOT NULL,
            level VARCHAR(100) NOT NULL
            )""")
        
        if score != -1:
            with conn.cursor() as cursor:
                cursor.execute("INSERT INTO user_score (username, score, level) VALUES('{}','{}',{})".format(username, score, level))
        else:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM user_score WHERE username = '{}'".format(username))
                data = cursor.fetchone()
                print(data[0],"max score",data[1])
                print(data[0],"max level",data[2])

    except:
        print("Error to connect")
    finally:
        if conn is not None:
            pass


print("Print your username:")
username = input()
connect(username, -1, -1)

#Initialzing
pygame.init()

#Setting up FPS
FramePerSec = pygame.time.Clock()

#Snake speed
Snake_speed = 6

#Creating colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

#Other Variables for use in the program
Pixel = 10
Direction = 'NONE'
SCREEN_WIDTH = Pixel*41
SCREEN_HEIGHT = Pixel*41
Score = 0
Level = 0
TIME = 0

#Create a screen 
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Snake')

#Snake
Snake_body = [[Pixel*20, Pixel*20]]
Snake_head = [Pixel*20, Pixel*20]

#Fruit
Eat = False
Food_position = [0,0]

def Food_position_generate():
    global Food_position

    Position = [random.randint(0, 40)*Pixel,random.randint(0, 40)*Pixel]
    for pos in Snake_body:
        if Position[0] == pos[0] and Position[1] == pos[1]:
            Food_position_generate()
    Food_position = Position

Food_position_generate()

# displaying Score and Level function
def show_score(self, color, font, size):
   
    # creating font object score_font
    Font = pygame.font.SysFont(font, size)
    
    # create the display surface object
    # score_surface
    score_surface = Font.render('Score : ' + str(Score), True, color)
    level_surface = Font.render('Level : ' + str(Level), True, color)
    
     
    # displaying text
    screen.blit(score_surface, (0,0))
    screen.blit(level_surface, (100,0))

#Game Loop
while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            connect(username, Score, Level)
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN  and event.key == K_UP and Direction!='DOWN':
            Direction = 'UP'
        if event.type == pygame.KEYDOWN  and event.key == K_DOWN and Direction!='UP':
            Direction = 'DOWN'
        if event.type == pygame.KEYDOWN  and event.key == K_RIGHT and Direction!='LEFT':
            Direction = 'RIGHT'
        if event.type == pygame.KEYDOWN  and event.key == K_LEFT and Direction!='RIGHT':
            Direction = 'LEFT'


    if Direction == 'UP':
        Snake_head[0] -= Pixel
    if Direction == 'DOWN':
        Snake_head[0] += Pixel
    if Direction == 'LEFT':
        Snake_head[1] -= Pixel
    if Direction == 'RIGHT':
        Snake_head[1] += Pixel

    #Check wall
    if Snake_head[0] < 0 or Snake_head[0] > 40*Pixel or Snake_head[1] < 0 or Snake_head[1] > 40*Pixel:
        connect(username, Score, Level)
        pygame.quit()
        sys.exit()
    for pos in Snake_body:
        if pos[0] == Snake_body[0][0] and pos[1] == Snake_body[0][1]:
            continue
        if Snake_head[0] == pos[0] and Snake_head[1] == pos[1]:
            connect(username, Score, Level)
            pygame.quit()
            sys.exit()
    
    TIME += 1
    if TIME % 100 == 0:
        Food_position_generate()
        TIME = 0

    #Snake growth
    Snake_body.insert(0, list(Snake_head))
    if Snake_head[0] == Food_position[0] and Snake_head[1] == Food_position[1]:
        Eat = True
        Snake_body.insert(0, list(Snake_head))
        Score += random.randint(0,5)
        if Score%3==0:
            Snake_speed += 3
            Level += 1
    Snake_body.pop()
    
    #Draw
    for pos in Snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[1], pos[0], Pixel, Pixel))
    
    if Eat == True:
        TIME = 0
        Food_position_generate()
    Eat = False

    pygame.draw.rect(screen, RED, pygame.Rect(Food_position[1], Food_position[0], Pixel, Pixel))

    show_score(1, WHITE, 'times new roman', 20)

    #Update and FPS
    pygame.display.update()
    FramePerSec.tick(Snake_speed)