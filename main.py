import pygame
import numpy as np

Width = 500         # Windows width
Height = 500        # Window height
BGColor = (0,0,0)   # Window background color

# Set up the main window
pygame.font.init()
Font = pygame.font.SysFont("Courier", 18)
pygame.init()
Screen = pygame.display.set_mode((Width, Height))
Screen.fill((BGColor))
game_icon = pygame.image.load('assets/SpaceInvader.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Space Invaders")
# Load the graphics
PlayerSprite = pygame.image.load('assets/Ship.png')
InvaderAA = pygame.image.load('assets/InvaderA_00.png'); InvaderAB = pygame.image.load('assets/InvaderA_01.png')
InvaderBA = pygame.image.load('assets/InvaderB_00.png'); InvaderBB = pygame.image.load('assets/InvaderB_01.png')
InvaderCA = pygame.image.load('assets/InvaderC_00.png'); InvaderCB = pygame.image.load('assets/InvaderC_01.png')

class Invaders:
    def __init__(self):
        self.Population=None

    def Init(self):
        self.Population = np.array([
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True],
            [True, True, True, True, True, True, True, True, True, True]
        ])

    def Draw(self, scn, X, Y, Anim):
        for y in range(0, 5):
            for x in range(0 , 10):
                if (self.Population[y,x]):
                    if (y==0):
                        if (Anim): DrawInvader = InvaderCA
                        else: DrawInvader = InvaderCB
                    elif (y==1):
                        if (Anim): DrawInvader = InvaderBA
                        else: DrawInvader = InvaderBB
                    else:
                        if (Anim): DrawInvader = InvaderAA
                        else: DrawInvader = InvaderAB

                    scn.blit(DrawInvader, (X+(x*30), Y+(y*20)))


def Main():
    DisplaySpeed = 100  # Display update speed
    Running = True     # True to keep running else exit
    PlayerSpd = 5      # Player velocity
    PlayerLives = 3    # Player lives
    PlayerX = int(Width/2)
    InvaderAnim = True

    MyInvaders=Invaders()
    MyInvaders.Init()

    # Loop until the window is closes
    while Running:
        pygame.display.flip()
        pygame.time.wait(DisplaySpeed)  # Higher for slower animation

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] and PlayerX - PlayerSpd > 0):
            PlayerX -= PlayerSpd
        if (keys[pygame.K_d] and PlayerX + PlayerSpd < (Width-32)):
            PlayerX += PlayerSpd

        Screen.fill((BGColor))
        LivesLabel = Font.render("Lives : " + str(PlayerLives), 1, (255, 255, 255))

        Screen.blit(LivesLabel, (10, 10))
        Screen.blit(PlayerSprite, (PlayerX, Height - 20))
        MyInvaders.Draw(Screen, 20,50, InvaderAnim)
        pygame.display.update()

        InvaderAnim = not InvaderAnim

Main()