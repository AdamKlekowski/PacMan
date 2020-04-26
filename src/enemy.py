import pygame
import time

class Enemy(object):
    def __init__(self):
        self.positionEnemy=(0,0)
        self.image=pygame.image.load("images/enemy.png")
        self.step=0

    def move(self, game, graph):
        if len(graph.path)==0:
            return
        v=graph.path[0]
        xy=graph.vertex[v]
        newX=xy[0]
        newY=xy[1]
        x=self.positionEnemy[0]
        y=self.positionEnemy[1]
        if game.map[newY][newX]=="p":
            game.isPacmanDead=True
            time.sleep(1)
        game.map[newY][newX], game.map[y][x] = game.map[y][x], game.map[newY][newX]
        self.positionEnemy=newX, newY
        graph.path.pop(0)