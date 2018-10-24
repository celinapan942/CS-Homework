import pygame 

screen = pygame.display.set_mode ((660, 660))
screen.fill((255,0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range (1,6):
        if i%2 == 1:
            for j in range (1,6):
                if j%2 == 1:
                    pygame.draw.rect(screen, (0,0,0), ((100*j,100*i), (100,100)))
                    pygame.display.update()
                elif j%2 == 0:
                    pygame.draw.rect(screen, (255,255,255), ((100*j,100*i), (100,100)))
                    pygame.display.update()
        if i%2 == 0:
            for n in range (1,6):
                if n%2 == 1:
                    pygame.draw.rect(screen, (255,255,255), ((100*n,100*i), (100,100)))
                    pygame.display.update()
                elif n%2 == 0:
                    pygame.draw.rect(screen, (0,0,0), ((100*n,100*i), (100,100)))  
                    pygame.display.update()
           
pygame.quit()