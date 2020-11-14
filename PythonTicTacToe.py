colors = []
squares = []
import pygame,sys
class cell:
        def __init__(self, x, y):
                self.rect = pygame.Rect(265*x, 265*y, 265, 265)
                self.isVisible = False
                self.isCounted = False
                self.Circle = False
                self.Cross = False
                self.lose = False
                
        
    
        def click(self, pos, circle, cross):
                if self.isVisible:
                    return False
                if self.rect.collidepoint(pos):
                        self.isVisible = True
                        if circle:
                            self.Circle = True
                        if cross:
                            self.Cross = True
                        return True
                return False
        
        def draw(self, screen):
                if self.isVisible and not self.lose:
                    if self.Cross:
                        screen.blit(colors[1], self.rect)
                    if self.Circle:
                        screen.blit(colors[2], self.rect)
                
                pygame.draw.rect(screen, (128,128,128), self.rect, 10)           


def exit():
     pygame.display.quit()
     sys.exit() 

def main():
    global colors
    global sqaures
    pygame.init()
    circle = False
    cross = True
    count = 0
    screen = pygame.display.set_mode((800, 800))
    squares = [[cell(x,y)for y in range(0,3)]for x in range(0,3)]
    
    pygame.display.set_caption("Ammon's Tic Tac Toe")
    
    font = pygame.font.SysFont('Papyrus', 200, bold =True)
    colors = [font.render("",True, (255,255,255)), font.render("X",True, (255,255,255)), font.render("O",True, (255,255,255)), font.render("Hello",True, (255,255,255))]
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for x in range(0,3):
                    for y in range(0,3):
                        squares[x][y].click(event.pos, circle, cross)
                
                if circle:
                    circle = False
                    cross = True
                else:
                    circle = True
                    cross = False

        screen.fill((0,0,255))

        for x in range(0,3):
            for y in range(0,3):
                squares[x][y].draw(screen)
        
        for x in range(0,3):
            for y in range(0,3):
                if squares[x][y].isVisible == True and squares[x][y].isCounted == False:
                    count += 1
                    squares[x][y].isCounted = True
        

        pygame.display.flip()

main()