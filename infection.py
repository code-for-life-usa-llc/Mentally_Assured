import pygame
import random
import sys
# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20  # Size of each entity (human or zombie)
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE
# Colors
ZOMBIE_COLOR = (152, 251, 152)  # Mint
HUMAN_COLOR = (255, 223, 231)   # Lumber (changed from white for better visibility)
POLICE_COLOR =(144, 224, 247)   #Arctic blue
APOTHECARY_COLOR =(149, 125, 173)  #Lavender
BACKGROUND_COLOR = (0, 0, 0) # Black
FPS = 40 # Frames per second, adjusted for smoother movement
# --- Base Entity Class ---
class Entity(pygame.sprite.Sprite):
   """
   Base class for all moving entities in the simulation.
   Handles basic movement and screen boundary checks.
   """
   def __init__(self, x, y, color):
       super().__init__()
       self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
       self.image.fill(color)
       self.rect = self.image.get_rect()
       # Position entities on the grid
       self.rect.x = x * CELL_SIZE
       self.rect.y = y * CELL_SIZE
       # Movement direction (dx, dy) - can be -1, 0, or 1 for grid movement
       self.dx = random.choice([-1, 0, 1])
       self.dy = random.choice([-1, 0, 1])
   def update(self):
       """
       Updates the entity's position and handles screen boundaries.
       """
       # Move the entity by one CELL_SIZE in its current direction
       self.rect.x += self.dx * CELL_SIZE
       self.rect.y += self.dy * CELL_SIZE
       # Boundary checks: Reverse direction if hitting screen edges
       if self.rect.left < 0:
           self.rect.left = 0
           self.dx = 1 # Move right
       elif self.rect.right > SCREEN_WIDTH:
           self.rect.right = SCREEN_WIDTH
           self.dx = -1 # Move left
       if self.rect.top < 0:
           self.rect.top = 0
           self.dy = 1 # Move down
       elif self.rect.bottom > SCREEN_HEIGHT:
           self.rect.bottom = SCREEN_HEIGHT
           self.dy = -1 # Move up
       # Randomly change direction occasionally for more dynamic movement
       if random.random() < 0.1: # 10% chance to change direction each frame
           self.dx = random.choice([-1, 0, 1])
           self.dy = random.choice([-1, 0, 1])
# --- Human Class ---
class Human(Entity):
   """
   Represents a human entity.
   Can be converted into a zombie.
   """
   def __init__(self, x, y):
       super().__init__(x, y, HUMAN_COLOR)
       self.is_zombie = False # Track if the human has become a zombie
   def turn_into_zombie(self):
       """
       Changes the human's appearance and state to a zombie.
       """
       self.image.fill(ZOMBIE_COLOR)
       self.is_zombie = True
# --- Police Class ---
class Police(Entity):
    """
    Represents a police entity.
    """
    def __init__(self, x, y):
        super().__init__(x, y, POLICE_COLOR)
# --- Apothecary Class ---
class Apothecary(Entity):
    """
    Represents a apothecary entity.
    Infects zombies on collison.
    """
    def __init__(self, x, y ):
        super().__init__(x, y,APOTHECARY_COLOR )     
# --- Zombie Class ---
class Zombie(Entity):
   """
   Represents a zombie entity.
   Infects humans on collision.
   """
   def __init__(self, x, y):
       super().__init__(x, y, ZOMBIE_COLOR)
       self.is_human = False # Track if the human has become a zombie
   def turn_into_human(self):
       """
       Changes the human's appearance and state to a zombie.
       """
       self.image.fill(HUMAN_COLOR)
       self.is_human = True
# --- Main Game Function ---
def main():
   """
   Initializes Pygame, sets up the game window, and runs the main game loop.
   """
   pygame.init() # Initialize all the Pygame modules
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set up the display window
   pygame.display.set_caption("Infection Simulator") # Set the window title
   clock = pygame.time.Clock() # Create a clock object to control frame rate
   # Sprite groups for managing entities
   all_entities = pygame.sprite.Group() # Group for all entities (for drawing and updating)
   humans = pygame.sprite.Group()       # Group specifically for human entities
   polices = pygame.sprite.Group()      # Group specifically for police entities
   apothecarys = pygame.sprite.Group()
   zombies = pygame.sprite.Group()      # Group specifically for zombie entities
   # --- Game Setup: Create Initial Entities ---
   # Create initial zombies
   for _ in range(1): # Start with 1 zombies
       x = random.randint(0, GRID_WIDTH - 1)
       y = random.randint(0, GRID_HEIGHT - 1)
       zombie = Zombie(x, y)
       all_entities.add(zombie)
       zombies.add(zombie)
   # Create initial humans
   for _ in range(5): # Start with 10 humans
       x = random.randint(0, GRID_WIDTH - 1)
       y = random.randint(0, GRID_HEIGHT - 1)
       human = Human(x, y)
       all_entities.add(human)
       humans.add(human)
    # Create initial polices
   for _ in range(1): # Start with 10 polices
       x = random.randint(0, GRID_WIDTH - 1)
       y = random.randint(0, GRID_HEIGHT - 1)
       police = Police(x, y)
       all_entities.add(police)
       polices.add(police)
    # Create initial apothecary
   for _ in range(4): # Start with 4 apothecary
       x = random.randint(0, GRID_WIDTH - 1)
       y = random.randint(0, GRID_HEIGHT - 1)
       apothecary = Apothecary(x, y)
       all_entities.add(apothecary)
       apothecarys.add(apothecary)
   # --- Game Loop ---
   running = True
   while running:
       # Event handling
       for event in pygame.event.get():
           if event.type == pygame.QUIT: # Check if the user clicked the close button
               running = False
       # Update all entities' positions
       all_entities.update()
       # --- Collision Detection and Infection Logic ---
       # Iterate through each zombie to check for collisions with humans
       for zombie in zombies:
           # spritecollide returns a list of all sprites in a group that have collided with the given sprite
           # The 'True' argument means that the collided human sprites will be removed from the 'humans' group
           collided_humans = pygame.sprite.spritecollide(zombie, humans, False) # Don't remove immediately
           for human in collided_humans:
               if not human.is_zombie: # Only infect if the human is not already a zombie
                   human.turn_into_zombie() # Change the human's state and color
                   humans.remove(human)     # Remove from humans group
                   zombies.add(human)       # Add to zombies group (now it's a zombie)
       for apothecary in apothecarys:
           collided_zombies = pygame.sprite.spritecollide(apothecary,zombies,False)
           for zombie in collided_zombies:
               if not zombie.is_human:
                   zombie.turn_into_human()
                   zombies.remove(zombie)
                   apothecarys.add(zombie)
       screen.fill(BACKGROUND_COLOR) # Fillthe screen with black each frame
       all_entities.draw(screen)     # Draw all entities to the screen
       pygame.display.flip() # Update the full display Surface to the screen
       clock.tick(FPS)       # Control the frame rate
   pygame.quit() # Uninitialize Pygame modules
   sys.exit()    # Exit the program
# --- Run the Game ---
if __name__ == "__main__":
   main()