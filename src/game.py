from pacman import PacMan

import pygame
import time
import re
import linecache
import os

class Game(object):
    def __init__(self):
        self.map=[]
        self.score=0
        self.bestScores=[]
        self.totalAmountFood=0
        self.isPlayerWin=False
        self.isPacmanDead=False
        self.downloadMapFromFile()
        self.downloadBestScoresFromFile()

    def downloadMapFromFile(self):
        try:
            file=open("files/pacman.map", "rb")
            for line in file:
                mapLine=[]
                for char in line:
                    mapLine.append(chr(char))
                    if chr(char) == "f":
                        self.totalAmountFood+=1
                self.map.append(mapLine)
            file.close()
        except FileNotFoundError:
            self.map.append("FileNotFoundError")

    def downloadBestScoresFromFile(self):
        try:
            for num in range(1, 4):
                line=linecache.getline('files/bestScores.txt', num)
                line=int(re.sub('[\n]','' ,line))
                self.bestScores.append(line)
        except FileNotFoundError:
            self.bestScores.append("FileNotFoundError", '0', '0')
        except:
            self.bestScores=[0,0,0]

    def drawingSurface(self, screen, pacman, enemy, CEILSIZE):
        screen.fill ((0,0,0))

        if self.map[0] == 'FileNotFoundError':
            font = pygame.font.SysFont(None, 2*CEILSIZE)
            text = font.render('Nie odnaleziono pliku z mapą', True, (255, 0, 0))
            errorText = text.get_rect()
            errorText.centerx = screen.get_rect().centerx
            errorText.centery = screen.get_rect().centery
            screen.blit(text, errorText)

            pygame.display.flip()
            time.sleep(1)
            return

        y=0
        for line in self.map:
            x=0
            for char in line:
                if char=="w":
                    pygame.draw.rect(screen, (0,100,250), (x,y,CEILSIZE, CEILSIZE))
                elif char=="f":
                    center=(x+CEILSIZE//2, y+CEILSIZE//2)
                    radius=CEILSIZE//8
                    pygame.draw.circle(screen, (255,0,0), center, radius, 0)
                elif char=="p":
                    pacman.image=pygame.transform.scale(pacman.image, (CEILSIZE,CEILSIZE))
                    screen.blit(pacman.image, (x,y))
                    pacman.positionPacman=(x//CEILSIZE,y//CEILSIZE)
                elif char=="e":
                    enemy.image=pygame.transform.scale(enemy.image, (CEILSIZE,CEILSIZE))
                    screen.blit(enemy.image, (x,y))
                    enemy.positionEnemy=(x//CEILSIZE,y//CEILSIZE)
                x+=CEILSIZE
            y+=CEILSIZE

        basicfont = pygame.font.SysFont(None, 2*CEILSIZE)
        text = basicfont.render('PacMan', True, (255, 255, 0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = CEILSIZE
        screen.blit(text, textrect)

        basicfont2 = pygame.font.SysFont(None, CEILSIZE)
        text = basicfont2.render('Score: ' + str(self.score), True, (255, 255, 0))
        screen.blit(text, (CEILSIZE,2*CEILSIZE))
        
        pygame.display.flip()

    def drawButtonInMenu(self, CEILSIZE, screen, textOnButton, y, x=0, size=2, col=(0,0,0), bCol=(0,100,250),):
        menuFont = pygame.font.SysFont(None, size*CEILSIZE)
        text = menuFont.render(textOnButton, True, col, bCol)
        button = text.get_rect()
        if x==0:
            button.centerx = screen.get_rect().centerx
        else:
            button.centerx = CEILSIZE*x
        button.centery = CEILSIZE*y
        screen.blit(text, button)
        return button

    def saveBestScore(self):
        self.bestScores.append(self.score)
        self.bestScores.sort(reverse=True)
        self.bestScores.pop()
        try:
            os.remove('files/bestScores.txt')
        except:
            pass
        file=open('files/bestScores.txt', 'w+')
        for num in range(3):
            file.writelines(str(self.bestScores[num]) + "\n")
        file.close()

    def reload(self):
        self.map=[]
        self.score=0
        self.totalAmountFood=0
        self.isPlayerWin=False
        self.isPacmanDead=False
        self.downloadMapFromFile()