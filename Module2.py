import pygame
pygame.init()


win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First game")

screen_width = 500
screen_height = 500
x = 50
y= 50
width = 40
height = 60
velocity = 5
isjump = False
jumpcount=10

flag = True
while flag:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>velocity:
        x-= velocity
    if keys[pygame.K_RIGHT] and x< screen_width - width-velocity:
        x+= velocity
    if not isjump:
        if keys[pygame.K_UP] and y>velocity:
            y-=velocity
        if keys[pygame.K_DOWN] and y<screen_height-height-velocity:
            y+=velocity
        if keys[pygame.K_SPACE]:
            isjump = True
    else:
        if jumpcount > -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y-=(jumpcount**2)*.45 *neg
            jumpcount -= 1
        else:
            isjump = False
            jumpcount = 10


    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()

pygame.quit()


