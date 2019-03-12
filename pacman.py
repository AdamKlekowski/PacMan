import pygame

class PacMan(object):
    def __init__(self):
        self.positionPacman=(0,0)
        self.image=pygame.image.load("images/pacman.png")

    def movePacman(self, direction, game):
        x=self.positionPacman[0]
        y=self.positionPacman[1]
        if direction=="down":
            newX=x
            newY=y+1
        elif direction=="up":
            newX=x
            newY=y-1
        elif direction=="left":
            newX=x-1
            newY=y
        elif direction=="right":
            newX=x+1
            newY=y

        if game.map[newY][newX] == "f":
            game.map[newY][newX] = "p"
            game.map[y][x] = "b"
            self.positionPacman=newX, newY
            game.score+=1
        elif game.map[newY][newX] == "b":
            game.map[newY][newX] = "p"
            game.map[y][x] = "b"
            self.positionPacman=newX, newY