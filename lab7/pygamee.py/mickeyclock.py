import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800,800),pygame.RESIZABLE)
done=True
fon=pygame.image.load("image/mickey.png")
rigthhand=pygame.image.load("image/righthand.png")
lefthand=pygame.image.load("image/lefthand.png")
while done:
        now = datetime.datetime.now()
        min= now.minute *6
        sec = now.second * 6 
        rotaterigth=pygame.transform.rotate(rigthhand,-min)
        rotateleft=pygame.transform.rotate(lefthand,-sec)
        screen.blit(fon, fon.get_rect(center = screen.get_rect().center))

        screen.blit(rotaterigth, rotaterigth.get_rect(center=(450,450)))
        screen.blit(rotateleft, rotateleft.get_rect(center=(450,450)))
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done=False
                        pygame.quit()