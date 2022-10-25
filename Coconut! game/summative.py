'''
By Jeniton Augustinpillai
2020/06/13
'''
import pygame, time, sys
pygame.init()

# Game instruction
print('Welcome to Coconut!\nIn this game you move your player with the arrow keys\nThe goal of this game is to not get hit by the coconuts!\nYou only have 3 lives in total\n      Good Luck!')

# These are my variables
walk_count = 0   # This stores the number of sprites being displayed to make the animation
clock = pygame.time.Clock()  # Stores the pygame clock
size = (400, 400)  # Stores the size of the screen
vel = 30  # Stores the velocity of the player's movement
x = 120  # Stores the x coordinates of the player
y = 200  # Stores the y coordinates of the player
right = False  # Stores a boolean value for player direction
left = False  # Stores a boolean value for player direction
stillL = True  # Stores a boolean value for the player's facing direction
stillR = False  # Stores a boolean value for the player's facing direction
coconutY = 110 # Stores the x coordinates if the coconut
coconutX = 0  # Stores the Y coordinates of the coconut
score = 0 # This stores the score that the player gets
lives = 3  # This stores the amount of lives that the player has
font = pygame.font.SysFont('comicsans', 25, True) # This Stores the font of the letter

# These variables are for my music and sound effect
hit_sound = pygame.mixer.Sound('hitSound.wav')
music = pygame.mixer.music.load('bgMusic.mp3')
pygame.mixer.music.play(-1)


# These are the variable that will store my png images
walkRight = [pygame.image.load('playerR1.png'),pygame.image.load('playerR2.png'),pygame.image.load('playerR3.png'),pygame.image.load('playerR4.png')]
walkLeft = [pygame.image.load('playerL1.png'), pygame.image.load('playerL2.png'),pygame.image.load('playerL3.png'),pygame.image.load('playerL4.png')]
standingL = pygame.image.load('playerStill.png')
standingR = pygame.image.load('playerStillR.png')
bg = pygame.image.load('palmTreeBg.png')
coconut = pygame.image.load('coconutObstacle.png')


# Window
window = pygame.display.set_mode(size)
# Caption
pygame.display.set_caption("Coconut!")

# This function stores the window update and the player animation
def redrawWindow():
    global walk_count
    window.blit(bg, (0,0))
    window.blit(coconut, (coconutX, coconutY))
    score_text = font.render('Score: '+ str(score), 1, (255, 255, 255)) # Stores the string for the score
    lives_text = font.render('Lives: '+ str(lives), 1, (255,255,255))
    window.blit(score_text, (300, 10))
    window.blit(lives_text, (5, 10))
    if walk_count +1 >= 4:
        walk_count = 0
    if left == True:
        window.blit(walkLeft[walk_count//2], (x,y))
        walk_count+=1
    elif right == True:
        window.blit(walkRight[walk_count//2], (x,y))
        walk_count += 1
    else:
        if stillL == True:
            window.blit(standingL, (x,y))
        elif stillR == True:
            window.blit(standingR, (x,y))
    pygame.display.update()
    

# Game loop
running = True
while running == True:
    clock.tick(9)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # keys: Stores what key is being pressed        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > -85:
        x -= vel
        left = True
        stillL = True
        right = False
        stillR = False
            
    elif keys[pygame.K_RIGHT] and x < 400 - 146:
        x += vel
        left = False
        stillL = False
        right = True
        stillR = True
    else:
        left = False
        right = False
    coconutY += 30
    if coconutY > 399:
        score += 1
        coconutY = 110
        coconutX = x + 100

    if coconutY > y + 72 and coconutX > x + 90 and coconutX < x + 132 or coconutY + 20 > y + 72 and coconutX > x + 90 and coconutX <x + 132:
        lives -= 1
        coconutY = 110
        coconutX = 192
        hit_sound.play()
        pygame.time.delay(200)
    if lives == 0:
        print('You lost!')
        pygame.mixer.music.pause()
        running = False
        
    redrawWindow()
quit()





    
