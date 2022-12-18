# Importing modules
import pygame
import time
import random

# Initiializing pygame 
pygame.init()
 
# Defining colours
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
# Defining dimensions of screen
dis_width = 800
dis_height = 600
 
# Creating screen
dis = pygame.display.set_mode((dis_width, dis_height))

#Caption of tab
pygame.display.set_caption('Snake Game')

# Creating an object to track time
clock = pygame.time.Clock()

#Defining snake size and snake frame times
snake_block = 20
snake_speed = 30
 
# Setting font styles
font_style = pygame.font.SysFont("Arial", 24)
score_font = pygame.font.SysFont("Arial", 34)
 

# Score function to show score and add score
def Your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    #Shows it on screen
    dis.blit(value, [10, 10])
 
 
# Snake function
def our_snake(snake_block, snake_list):
    for x in snake_list:
        #Creating snake
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
 
# Message function
def message(msg, color):
    #Creating messafe
    mesg = font_style.render(msg, True, color)
    #Showing message on screen
    dis.blit(mesg, [dis_width / 4, dis_height / 3])



#def wallsOn():
    #if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        #game_close = True
 
# Main game function
def gameLoop():
    #Setting game over and game close to false initially
    game_over = False
    game_close = False
    
    # Putting snake in the middle of the screen to star of with
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    #Setting speeds to 0 initially
    x1_change = 0
    y1_change = 0
 
    #Creaitng a snake list
    snake_List = []

    #Setting the initial lenght of the snake to 1
    Length_of_snake = 1
 
    # Spawning the food in a random position each time
    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
    
    # While the game_over is False
    while not game_over:
        
        # If game close is True show the reset message
        while game_close == True:
            dis.fill(black)
            message("You Lost ! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            #Give the option to press the Q or C screen in order to move on
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        # If the user clicks the exit button the game will quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            # If left is clicked move left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                # If right is clicked move right
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                # if up is clicked move up
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                # if down is clicked move down
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

        #Making snake teleport through walls     
        if x1 >= dis_width:
            x1 = 0
            
        elif x1 < 0:
            x1 = dis_width
            
        if y1 >= dis_height:
            y1 = 0
            
        if y1 < 0:
            y1 = dis_height          
        
        # Setting speed
        x1 += x1_change
        y1 += y1_change

        # Setting background
        dis.fill(black)

        #Creating food in screen
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        # Declaring snake head list
        snake_Head = []

        # Adding snake head into x1 and y1
        snake_Head.append(x1)
        snake_Head.append(y1)

        # Putting snake head into snake list
        snake_List.append(snake_Head)

        # If the lenght of the snake list is bigger than the lenght of the snake delete the first value in the list
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        # If the x is equal to the snake head you lose
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        # Making our snake
        our_snake(snake_block, snake_List)

        # The score is equalt to the lenght of the snake minus 1
        Your_score(Length_of_snake - 1)
 
        # Updating the screen
        pygame.display.update()
 
        # If the snake is touching the food spawn the food in a new spot and add lenght to the snake. This will also add to the score.
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        #Setting the frame rate to snake speed
        clock.tick(snake_speed)
 
    # Quitting the program when the user closes it
    pygame.quit()
    quit()
 
# Calling the main game loop function
gameLoop()