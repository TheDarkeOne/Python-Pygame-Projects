# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 15:12:06 2019

@author: ammon.zerkle
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:30:17 2019

@author: ammon.zerkle
"""
colors = []
mines = 0
squares = []
import pygame,sys, random
class cell:
        def __init__(self, x, y):
                self.rect = pygame.Rect(100*x, 100*y, 100, 100)
                self.isVisible = False
                self.isMine = False
                self.isFlag = False
                self.lose = False
                
        
    
        def click(self, pos):
                if self.isVisible:
                    return False
                if self.rect.collidepoint(pos):
                        self.isVisible = True
                        return True
                return False
        
        def flag(self, pos):
                if not self.isVisible and self.isFlag:
                    self.isFlag = False
                    return False
                if self.rect.collidepoint(pos) and not self.isVisible:
                        self.isFlag = True
                return False
            
        def mine(self):
            self.isMine = True
        
        def draw(self, screen):
                if self.isVisible and not self.lose:
                    if not self.isMine:
                        screen.blit(colors[1], self.rect)
                    if self.isMine:
                        screen.blit(colors[2], self.rect)
                        exit()
                
                if self.isFlag and not self.lose:
                    screen.blit(colors[3], self.rect)
                pygame.draw.rect(screen, (128,128,128), self.rect, 10)           


def exit():
     pygame.display.quit()
     sys.exit() 

def main():
    global colors
    global mines
    global sqaures
    pygame.init()
    mines = 10
    screen = pygame.display.set_mode((800, 800))
    squares = [[cell(x,y)for y in range(0,8)]for x in range(0,8)]
    
    availPos = list(range((7) * (7)))
    for i in range(mines):
        newPosX = random.choice(availPos)
        newPosY = random.choice(availPos)
        if newPosX != newPosY:
            availPos.remove(newPosX)
            availPos.remove(newPosY)
        
        (rowId, colId) = (newPosX %7, newPosY % 7)
        squares[rowId][colId].mine()
    
    font = pygame.font.SysFont('Papyrus', 70, bold =True)
    colors = [font.render("",True, (255,255,255)), font.render("X",True, (255,255,255)), font.render("O",True, (255,255,255)), font.render("4",True, (255,255,255)), font.render("Q",True, (255,255,255))]
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in range(0,8):
                    for y in range(0,8):
                       squares[x][y].click(event.pos)
                           
            if event.type == pygame.KEYDOWN:
                for x in range(0,8):
                    for y in range(0,8):
                        if event.key == pygame.K_SPACE:
                            temp = pygame.mouse.get_pos()
                            squares[x][y].flag(temp)

        screen.fill((0,0,255))

        for x in range(0,8):
                for y in range(0,8):
                    squares[x][y].draw(screen)
        
        pygame.display.flip()
        
main()