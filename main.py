import pygame
import time
import sys

from game import Game
from pacman import PacMan
from enemy import Enemy
from graph import Graph

CEILSIZE = 30
FPS = 10

if __name__=="__main__":
    pygame.init()
    clock = pygame.time.Clock()
    game=Game()

    while True:
        graph=Graph()
        enemy=Enemy()
        pacman=PacMan()
        game.reload()

        graph.completeVertex(game)
        graph.shortestPath((pacman.positionPacman), (enemy.positionEnemy))

        if game.map[0] == 'FileNotFoundError':
            height=15*CEILSIZE
            width=30*CEILSIZE
        else:
            height=len(game.map)*CEILSIZE
            width=(len(game.map[0])-1)*CEILSIZE
        screen=pygame.display.set_mode((width, height))

        ############### MENU #################
        pygame.display.set_caption('PacMan')

        pacman.image=pygame.transform.scale(pacman.image, (5*CEILSIZE,5*CEILSIZE))
        screen.blit(pacman.image, (4*CEILSIZE,1.5*CEILSIZE))

        game.drawButtonInMenu(CEILSIZE, screen, "PacMan", 4, size=5, col=(255,255,0), bCol=(0,0,0))

        game.drawButtonInMenu(CEILSIZE, screen, "Top Scores:", 8, x=5, size=1, col=(255,0,0), bCol=(0,0,0))
        game.drawButtonInMenu(CEILSIZE, screen, str(game.bestScores[0]), 9, x=5, size=1, col=(255,0,0), bCol=(0,0,0))
        game.drawButtonInMenu(CEILSIZE, screen, str(game.bestScores[1]), 10, x=5, size=1, col=(255,0,0), bCol=(0,0,0))
        game.drawButtonInMenu(CEILSIZE, screen, str(game.bestScores[2]), 11, x=5, size=1, col=(255,0,0), bCol=(0,0,0))

        game.drawButtonInMenu(CEILSIZE, screen, "Wybierz poziom:", 8, col=(0,100,250), bCol=(0,0,0))
        button1=game.drawButtonInMenu(CEILSIZE, screen, "Bardzo łatwy", 10)
        button2=game.drawButtonInMenu(CEILSIZE, screen, "Normalny", 12)
        button3=game.drawButtonInMenu(CEILSIZE, screen, "Wyście z gry", 14)
        pygame.display.flip()

        wait=True
        mousePos=(0,0)
        while(wait):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()

            if button1.collidepoint(mousePos):
                DIFFICULTY=25
                wait=False
            elif button2.collidepoint(mousePos):
                DIFFICULTY=12
                wait=False
            elif button3.collidepoint(mousePos):
                sys.exit(0)
        ######################################

        while (not game.isPacmanDead and not game.isPlayerWin):
            clock.tick(FPS)
            game.drawingSurface(screen, pacman, enemy, CEILSIZE)
            
            if game.score == game.totalAmountFood:
                game.isPlayerWin = True
                time.sleep(1)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            key = pygame.key.get_pressed()
            if key[pygame.K_s]:
                pacman.movePacman("down", game)
            if key[pygame.K_w]:
                pacman.movePacman("up", game)
            if key[pygame.K_a]:
                pacman.movePacman("left", game)
            if key[pygame.K_d]:
                pacman.movePacman("right", game)
            if enemy.step==DIFFICULTY:
                graph.shortestPath(pacman.positionPacman, enemy.positionEnemy)
                enemy.step-=DIFFICULTY
            enemy.move(game, graph)
            enemy.step+=1
        
        if game.isPacmanDead==True:
            result="Przegrałeś!"
        elif game.isPlayerWin==True:
            result="Wygrałeś!"
        game.saveBestScore()

        screen.fill ((0,0,0))
        basicfont = pygame.font.SysFont(None, 2*CEILSIZE)
        text = basicfont.render(result, True, (255, 255, 0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery
        screen.blit(text, textrect)

        pygame.display.flip()
        time.sleep(2)