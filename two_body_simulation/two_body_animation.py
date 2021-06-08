import pygame
from pygame.locals import *
import time



class TwoBodyView:
    """Create a single-window app with multiple scenes."""
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        flags = RESIZABLE
        TwoBodyView.screenWidth = 1200
        TwoBodyView.screenHeight = 700
        TwoBodyView.screen = pygame.display.set_mode((TwoBodyView.screenWidth, TwoBodyView.screenHeight), flags)
        TwoBodyView.body1 = Body("earth.png",(200,20),0.04) # you can change size of bodies by changing last parameter
        TwoBodyView.body2 = Body("sun.png",(400,20),0.1)

        TwoBodyView.running = True
        TwoBodyView.playing = True
        TwoBodyView.reload = False



    def drawBodies(self, body1NewPos, body2NewPos):
        TwoBodyView.body1.setPosition(body1NewPos)
        TwoBodyView.body2.setPosition(body2NewPos)
        TwoBodyView.body1.draw()
        TwoBodyView.body2.draw()





class Body:
    def __init__(self, image, pos, scale):
        self.image = pygame.image.load(image)
        self.image.convert()
        self.rect = self.image.get_rect()
        self.setScale(scale)
        self.setPosition(pos)
        self.draw()


    def setScale(self, scale):
        self.image = pygame.transform.rotozoom(self.image, 0, scale)

    def draw(self):
        TwoBodyView.screen.blit(self.image, self.rect)

    def setPosition(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class App:
    def __init__(self):
        self.startIndex = 0

    def readFile(self):
        file = open("locationVectorC.txt","r")
        lines = file.readlines()
        file.close()
        return lines

    def run(self):
        view = TwoBodyView()
        lines = self.readFile()
        clock = pygame.time.Clock()

        while TwoBodyView.running:
            self.getEvent()
            while TwoBodyView.playing:
                TwoBodyView.reload = False
                for i in range(self.startIndex,len(lines)):
                    self.getEvent()
                    if (not TwoBodyView.running or not TwoBodyView.playing or TwoBodyView.reload):
                        break
                    pygame.display.flip()
                    clock.tick(60)

                    splittedLine = lines[i].split(",")
                    TwoBodyView.screen.fill(Color('black')) # you can see the orbit when you make comment this line
                    view.drawBodies(self.transformPosition((float(splittedLine[0]),float(splittedLine[1]))),self.transformPosition((float(splittedLine[2]),float(splittedLine[3]))))
                    pygame.display.update()
                    self.startIndex += 1
                #self.startIndex = 0

        pygame.quit()

        
    def transformPosition(self, rawPos):
        origin = (int(TwoBodyView.screenWidth/2-200),int(TwoBodyView.screenHeight/2-0))
        transformParameter = 150
        transformedPos = (int(rawPos[0]*transformParameter + origin[0]), int(rawPos[1]*transformParameter + origin[1]))
        return  transformedPos

    def getEvent(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                TwoBodyView.running = False
                TwoBodyView.playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    TwoBodyView.running = False
                    TwoBodyView.playing = False
                elif event.key == pygame.K_SPACE:
                    TwoBodyView.playing = not TwoBodyView.playing
                elif event.key == pygame.K_r:
                    TwoBodyView.reload = True
                    TwoBodyView.playing = True
                    self.startIndex = 0



if __name__ == '__main__':
    App().run()