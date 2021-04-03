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
PlayerBullet = pygame.image.load('assets/PlayerBullet.png');

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
        xmin = 9; xmax = 0; ymax = 0
        for y in range(0, 5):
            for x in range(0 , 10):
                if (self.Population[y,x]):
                # Find the limits of invaders
                    if (x<xmin):    xmin=x
                    elif (x>xmax):  xmax=x
                    elif (y>ymax):  ymax=y
                # Draw the invaders
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
        return(xmin, xmax, ymax)


def Main():
    DisplaySpeed = 20  # Display update speed
    Running = True     # True to keep running else exit
    PlayerSpd = 5      # Player velocity
    PlayerLives = 3    # Player lives
    PlayerX = int(Width/2)

    PlayerBulletSpd = 20    # Player bullet velocity
    PlayerBulletPosX = 0    # Player bullet X
    PlayerBulletPosY = -1   # Player bullet Y

    InvaderAnim = 0
    InvaderFrame=False
    InvaderFrameRate=20



    InvaderX=0; InvaderY=50; InvaderSpdX=5; InvaderSpdY=10

    MyInvaders=Invaders()
    MyInvaders.Init()

    # Loop until the window is closes
    while Running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False

    # Handle Player movement and firing
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] and PlayerX - PlayerSpd > 0):
            PlayerX -= PlayerSpd
        if (keys[pygame.K_d] and PlayerX + PlayerSpd < (Width-32)):
            PlayerX += PlayerSpd
        if (keys[pygame.K_SPACE] and PlayerBulletPosY<0):
            PlayerBulletPosX = PlayerX + 14
            PlayerBulletPosY = Height - 28

        Screen.fill((BGColor))
        LivesLabel = Font.render("Lives : " + str(PlayerLives), 1, (255, 255, 255))

    # Add lives and score
        Screen.blit(LivesLabel, (10, 10))
    # Add player
        Screen.blit(PlayerSprite, (PlayerX, Height - 20))
    # If a Player Bullet is in play update it
        if (PlayerBulletPosY >= 0):
            Screen.blit(PlayerBullet, (PlayerBulletPosX, PlayerBulletPosY))
            PlayerBulletPosY -= PlayerBulletSpd
    # Update the invaders
        InvaderRange=MyInvaders.Draw(Screen, InvaderX, InvaderY, InvaderFrame)
        print (InvaderRange)

    # Update the space invaders
        InvaderAnim = (InvaderAnim+1)%InvaderFrameRate
        InvaderFrame=False
        if (InvaderAnim < (InvaderFrameRate/2)):InvaderFrame=True

        InvaderXMax=(Width-((InvaderRange[1]+1)*30))
        InvaderXMin=-((InvaderRange[0])*30)
        if (InvaderX > InvaderXMax):
            InvaderY += InvaderSpdY
            InvaderX = InvaderXMax
            InvaderSpdX *= -1
        elif(InvaderX < InvaderXMin):
            InvaderY += InvaderSpdY
            InvaderX = InvaderXMin
            InvaderSpdX *= -1
        InvaderYMax=(Height-((InvaderRange[2]+1)*20))
        if (InvaderY >= InvaderYMax):
            InvaderSpdY=0
            InvaderSpdX=0

        InvaderX+=InvaderSpdX

    # Finally update the display
        pygame.display.flip()
        pygame.time.wait(DisplaySpeed)  # Higher for slower animation
Main()