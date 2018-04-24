import pygame
import random
pygame.init()

SIZE = (800, 600)
TITLE = "Road -Ethan M"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
GRAY = (90, 90, 90)
LIGHT_GRAY = (150, 150, 150)
YELLOW = (255, 255, 40)
RED = (255, 100, 100)


light_color = GREEN

def draw_light(color):
    pygame.draw.rect(screen, YELLOW, [565, 285, 40, 50])
    pygame.draw.rect(screen, GRAY, [580, 335, 10, 70])
    pygame.draw.ellipse(screen, GRAY, [573, 298, 25, 25])
    pygame.draw.ellipse(screen, color, [575, 300, 20, 20])


def draw_car(cord):
    x = cord[0]
    y = cord[1]
    pygame.draw.rect(screen, WHITE, [x, y, 60, 40])
    car.append(cord)

def determine_light_color(light_timer):
    if 500 >= light_timer >= 300:
        light_color = GREEN
    if 299 >= light_timer >= 200:
        light_color = YELLOW
    if 199 >= light_timer >= 0:
        light_color = RED
    
        
   

def timer():
    light_timer = 500
    while light_timer >= 0:
        light_timer -= 1
        determine_light_color(light_timer)
        if light_timer == 0:
            light_timer = 500



'''makes car'''
car_amount = 1
car = []
for i in range(car_amount):  
    x = 10
    y = 360
    cord = [x, y]
    car.append(cord)




# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                light_color = RED
            if event.key == pygame.K_g:
                light_color = GREEN
            if event.key == pygame.K_y:
                light_color = YELLOW
        
      

    # Game logic

    ''' move car '''
    for c in car:
        if light_color == GREEN:
            c[0] += 0.02
        if light_color == RED:
            c[0] += 0
        if light_color == YELLOW:
            c[0] += 0.0005
        if c[0] > 850:
            c[0] = -30
            c[1] = 360

            
    ''' time stuff '''
    timer()
            
    # Drawing code
    ''' sky '''
    screen.fill(BLUE)

    ''' light '''
    draw_light(light_color)
    
    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' road '''
    pygame.draw.rect(screen, LIGHT_GRAY, [0, 400, 800, 20])

    ''' car '''
    draw_car(cord)
    
    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
