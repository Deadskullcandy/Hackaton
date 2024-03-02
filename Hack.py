import pygame
import os  

pygame.init()

# Set screen dimensions
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up clock for frame rate control
clock = pygame.time.Clock()

# Define colors
white = (255, 255, 255)

# Set player starting position
player_pos = (screen_width // 2, screen_height // 2)


class Fighter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Load the image and get its rectangle
        for i in range(8):
          self.image = [pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat1.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat2.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat3.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat4.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat5.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat6.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat7.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat8.png")]
          
          self.image_inverse = [pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat1.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat2.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat3.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat4.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat5.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat6.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat7.png"),
                        pygame.image.load("/Users/darrenmathewjacob/Documents/GitHub/Hackaton/cat sheet/cat8.png")]



        self.rect = self.image[1].get_rect()

        # Set initial position
        self.rect.x = x
        self.rect.y = y
        self.image_num = 0
        self.side = 1 
        self.gravity = -5

    def update(self):
        # Check for key presses and move the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.rect.y >= 370:
              self.rect.y -= 100
        if keys[pygame.K_s]:
            self.rect.y += 30
        if keys[pygame.K_a]:
            self.rect.x -= 30
            self.side = -1
            self.image_num += 0.3
            if self.image_num >=8:
              self.image_num = 0
        if keys[pygame.K_d]:
            self.rect.x += 30
            self.side = 1
            self.image_num += 0.3
            if self.image_num >=8:
              self.image_num = 0

        if self.rect.y <=400:
           self.rect.y -= self.gravity

        # Keep the player within screen bounds
        self.rect.clamp_ip(screen.get_rect())
        # Draw the player on the screen
        if self.side == 1:
          screen.blit(self.image[int(self.image_num)], self.rect)
        if self.side == -1:
          screen.blit(pygame.transform.flip(self.image[int(self.image_num)],1,0), self.rect)


# Create a single player instance
player = Fighter(player_pos[0], player_pos[1])

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(white)

    # Update and draw the player
    player.update()

    # Update the display
    pygame.display.flip()

    # Set frame rate to 60 fps
    clock.tick(30)

# Quit pygame
pygame.quit()
