import random
import pygame
pygame.init()
width=600
height = 400
block_s = 10
dis=pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
pygame.display.update()
red = (128, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
dis.fill(white)
game_over = False
x = 300
y = 200
x_c = 0
y_c = 0
clock = pygame.time.Clock()
game_close = False
font_style=pygame.font.SysFont('freesans', 25)
lost_img = font_style.render('You Lost! Press P to play again or Q to quit.', True, red)
def score(c_score):
    value = font_style.render('Your Score: ' + str(c_score), True, black)
    dis.blit(value, [0, 0])
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, (x[0], x[1], snake_block, snake_block))
    pygame.draw.rect(dis, (128, 0, 128), (snake_list[-1][0], snake_list[-1][1], snake_block, snake_block))
    
def game_loop():
    game_over=False
    game_close=False
    x=int(width/2)
    y=int(height/2)
    x_c=0
    y_c=0
    foodx = block_s*random.randint(0, int(width/block_s) - 1) 
    foody = block_s* random.randint(0, int(height/block_s) - 1)
    snake_list = []
    snake_length = 1
    while(game_over==False):
        while(game_close == True):
            dis.fill(white)
            dis.blit(lost_img, [100, 100])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    game_over=True
                    game_close=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_p:
                        game_loop()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_c = 0
                    y_c = -block_s
                elif event.key == pygame.K_DOWN:
                    x_c = 0
                    y_c = block_s
                elif event.key == pygame.K_LEFT:
                    x_c = -block_s
                    y_c = 0
                elif event.key == pygame.K_RIGHT:
                    x_c = block_s
                    y_c = 0
        if x>= width or x<0 or y>= height or y < 0:
            game_close=True

        x = x + x_c
        y = y + y_c
        dis.fill(white)
        #pygame.draw.rect(dis, red, (x, y, 10, 10))
        pygame.draw.rect(dis, blue, (foodx, foody, block_s, block_s))
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True
        snake(10, snake_list)
        if x==foodx and y ==foody:
            snake_length+=1
            foodx = random.randint(0, int(width / block_s)-1)*block_s
            foody = random.randint(0, int(height / block_s)-1)*block_s
        score(snake_length-1)
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
game_loop()