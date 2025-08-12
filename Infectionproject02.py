#INFECTION GAME 0.2
from turtle import Screen
import pygame
import random

#SET UP GAME ENVIRONMENT
pygame.init()

#SCREEN DIMENSIONS
Width, Height = 800, 600
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Infection Survial Game")

#CHARACTER'S COLORS
ZOMBIE_COLOR = (152, 251, 152)# Mint
HUMAN_COLOR = (255, 223, 231)# Lumber (changed from white for better visibility)
POLICEFORCE_COLOR =(144, 224, 247)#Arctic blue
APOTHECARY_COLOR =(149, 125, 173)#Lavender
BACKGROUND_COLOR = (0, 0, 0) # Black
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)

#THE LOADING SCREEN THAT ALLOWS TO SHOW THE NPC'S AND GAME
human_img = pygame.image.load("static/human.png")
zombie_img = pygame.image.load("static/zombie.png")
policeforce_img = pygame.image.load("static/policeforce.png")
apothecary_img = pygame.image.load("static/apothecary.png")

#RESIZING CHARACTER'S
human_size = 50 
human_img = pygame.transform.scale(human_img,(human_size, human_size))
zombie_size = 50
zombie_img = pygame.transform.scale(zombie_img,(zombie_size, zombie_size))
policeforce_size = 50 
policeforce_img = pygame.transform.scale(policeforce_img,(policeforce_size, policeforce_size))
apothecary_size = 50
apothecary_img = pygame.transform.scale(apothecary_img,(apothecary_size,apothecary_size))

#CHARACTER'S SET UP
policeforce_x = Width //2
policeforce_y = Height -70
policeforce_speed = 5

#BULLET SETUP
bullets = []
bullet_speed = 7

#ZOMBIE SETUP
zombies = []
zombie_speed = 2
spawn_rate = 25 

#CHOOSEN FONT FOR SCREEN
font = pygame.font.Font(None,36)

#SCORE
def load_top_score():
   try:
     with open("Current_Score.txt","r") as file:#JUST HELPS RETURN SCORE IF THE FILE ISN'T WORKING
        return int(file.read().strip())
   except (FileNotFoundError,ValueError):
      return 0
   
def save_top_score(score):#THIS SAVES CURRENT SCORE
   with open("top_score.txt","w") as file:
      file.write(str(score))

top_score = load_top_score()#LOAD CURRENT SCORE

#GAME LOOP
running = True 
game_over = False
clock = pygame.time.Clock()#CONTROLS FRAME RATE
score = 0 #TRACKS PLAYER SCORE

def reset_game():#RESETS GAME
   global policeforce_x, policeforce_y,bullets,zombies,score,game_over
   policeforce_x = Width //2
   policeforce_y = Height -70
   bullets = []
   zombies = []
   score = 0
   game_over = False

while running:#MAIN GAME LOOP
   screen.fill(0, 0, 0) #BLACK

   if not game_over:#MAIN FUNCTION THAT HELPS PLAYER QUIT GAME
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                  bullets.append([policeforce_x + policeforce_size //2, policeforce_y])
            
#PLAYERS MOVEMENT
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT] and policeforce_x > 0:
   policeforce_x -= policeforce_speed
if keys[pygame.K_RIGHT] and policeforce_x < Width - policeforce_size:
   policeforce_x += policeforce_speed

#BULLET MOVEMENT 
for bullet in bullets[:]:
   bullet[1] -= bullet_speed
   if bullet[1] < 0:
      bullets.remove(bullet)

#SPAWN ZOMBIES
if random.randint(1,spawn_rate) == 1:
   zombies.appened([random.randint(0,Width - policeforce_size), 0])

#ZOMBIES MOVEMENT
for zombie in zombies[:]:
   zombie[1] += zombie_speed
   if zombie[1] > Height:
      game_over = True #GAME WILL END IF A ZOMBIES REACHES THE BOTTOM

#COLLISION DETECTION
   for bullet in bullets[:]:
    for zombie in zombies[:]:
       if zombie [0] < bullet[0] < zombie[0] + policeforce_size and \
          zombie [1] < bullet[1] <zombie[1] + policeforce_size:
           zombies.remove(zombie)
           score += 1

#DRAWS CURRENT MOVEMENTS
    screen.blit(policeforce_img,(policeforce_x,policeforce_y))
    for bullet in bullets: #DRAWS BULLETS ON SCREEN
       pygame.draw.rect(screen,WHITE,(bullet[0], bullet[1], 5, 10))
    for zombie in zombies: #DRAWS ZOMBIES ON SCREEN
       screen.blit(zombie_img, (zombie[0], zombie[1]))

#DISPLAYS SCORE
    if score > top_score:
        top_score = score
        save_top_score(top_score)

#DISPLAYS CURRENT AND TOP SCORE
    top_score_text = font.render(f"Top Score:{top_score}", True, RED)
    Screen.blit (top_score_text,(Width -200, 10))
    score_text = font.render(f"Score {score}", True, GREEN)
    Screen.blit (score_text,(Width -200, 10))

   else:
      #GAME OVER SCREEN
      game_over_text = font.render("GAME OVER! YOUR SCORE:" + str(score), True,WHITE)
      screen.blit(game_over_text,(Width //2 - 150, Height //2 -50))
      restart_text = font.render("PRESS R TO RESTART", True, WHITE)
      screen.blit(restart_text, (Width //2 -100, Height //2 +10))
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
               reset_game()

#UPDATES FRAME
      pygame.display.flip()
      clock.tick(30)

#EXIT PYGAME
pygame.quit()