import pygame

Width = 500         # Windows width
Height = 500        # Window height
BGColor = (0,0,0)   # Window background color
DisplaySpeed = 10   # Display update speed
Running = True      # True to keep running else exit
PlayerSpd = 1       # Player velocity
PlayerLives = 3      # Player lives

# Set up the main window
pygame.font.init()
Font = pygame.font.SysFont("Courier", 24)
pygame.init()
Screen = pygame.display.set_mode((Width, Height))
Screen.fill((BGColor))
game_icon = pygame.image.load('assets/SpaceInvader.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Space Invaders")

# Load the graphics
PlayerSprite = pygame.image.load('assets/Ship@2x.png')

def RedrawWindow():
    Screen.fill((BGColor))
    LivesLabel = Font.render("Lives : "+str(PlayerLives), 1, (255,255,255))

    Screen.blit(LivesLabel, (10,10))
    Screen.blit(PlayerSprite, (50,Height-35))
    pygame.display.update()

# Loop until the window is closes
while Running:
    pygame.display.flip()
    pygame.time.wait(DisplaySpeed)  # Higher for slower animation

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] and Ship.x - PlayerSpd > 0):
        Ship.x -= PlayerSpd
    if (keys[pygame.K_d] and Ship.x + PlayerSpd < Width):
        Ship.x += PLayerSpd

    RedrawWindow()