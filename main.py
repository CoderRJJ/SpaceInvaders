import pygame

Width = 500         # Windows width
Height = 500        # Window height
BGColor = (0,0,0)   # Window background color
DisplaySpeed = 10   # Display update speed
Running = True      # True to keep running else exit
PlayerSpd = 1

# Set up the main window
pygame.init()
Screen = pygame.display.set_mode((Width, Height))
Screen.fill((BGColor))
game_icon = pygame.image.load('assets/SpaceInvader.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Space Invaders")

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
