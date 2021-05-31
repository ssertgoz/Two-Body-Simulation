import pygame
from pygame.locals import *
import time



class TwoBodyView:
    """Create a single-window app with multiple scenes."""
    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        flags = RESIZABLE
        TwoBodyView.screen = pygame.display.set_mode((900, 600), flags)

        TwoBodyView.t = Text('Pygame App', pos=(20, 20))
        TwoBodyView.body1 = Body("earth.png",(200,20),0.1)
        TwoBodyView.body2 = Body("sun.png",(400,20),0.1)

        TwoBodyView.running = True
        TwoBodyView.playing = True

    def simulate(self):
        """Run the main event loop."""
        while TwoBodyView.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    TwoBodyView.running = False
            TwoBodyView.screen.fill(Color('black'))
            TwoBodyView.t.updatePosition()
            TwoBodyView.body1.draw()
            TwoBodyView.body2.draw()
            pygame.display.update()

        pygame.quit()


    def drawBodies(self, body1, body2, body1NewPos, body2NewPos):
        body1.setPosition(body1NewPos)
        body2.setPosition(body2NewPos)
        body1.draw()
        body2.draw()

    def drawOrbit(self, body1Pos, body2Pos):
        pass
    def oyle(self):
        TwoBodyView.t.updatePosition()



class Text:
    """Create a text object."""

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos
        self.count = 1

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('white')
        self.set_font()
        self.render()

    def set_font(self):
        """Set the Font object from name and size."""
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        """Render the text into an image."""
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        """Draw the text image to the screen."""
        TwoBodyView.screen.blit(self.img, self.rect)
    def updatePosition(self):
        self.count += 1
        self.pos = (self.count,20)
        self.render()
        self.draw()

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


def simulate():
    """Run the main event loop."""
    while TwoBodyView.running:
        for event in pygame.event.get():
            if event.type == QUIT:
                TwoBodyView.running = False
        TwoBodyView.screen.fill(Color('black'))
        TwoBodyView.t.updatePosition()
        TwoBodyView.body1.draw()
        TwoBodyView.body2.draw()
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    TwoBodyView()
    simulate()