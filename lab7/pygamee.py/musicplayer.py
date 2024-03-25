import pygame
import datetime

pygame.init()
pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)
musics = ['music/eminem.mp3',
        'music/kairatnurtas.mp3',
        'music/raim.mp3']
w = 800
h = 800
nextsong = 0
clock = pygame.time.Clock()
pause = False
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Music")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pause = True
                pygame.mixer.music.load(musics[nextsong])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                nextsong -= 1
                if nextsong == -1:
                    nextsong = len(musics) - 1
                pygame.mixer.music.load(musics[nextsong])
                pygame.mixer.music.play()

            elif event.key == pygame.K_RIGHT:
                nextsong += 1
                if nextsong == len(musics):
                    nextsong = 0
                pygame.mixer.music.load(musics[nextsong])
                pygame.mixer.music.play()

            elif event.key == pygame.K_SPACE and pause == False:
                pause = True
                pygame.mixer.music.pause()

            elif event.key == pygame.K_SPACE and pause == True:
                pause = False
                pygame.mixer.music.unpause()
    pygame.display.flip()
    clock.tick(60)

