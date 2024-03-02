import pygame
import socket
import pickle

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pong")

# Initialize paddle position
paddle_y = (SCREEN_HEIGHT - 100) // 2  # Initial position for the paddle

# Function to draw the paddle
def draw_paddle(y):
    pygame.draw.rect(screen, WHITE, (10, y, 10, 100))

# Function to send and receive data over TCP
def send_receive_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('20.163.17.66', 12345))  # Replace 'server_ip_address' with the actual IP address of the server
        s.sendall(pickle.dumps(data))
        received_data = pickle.loads(s.recv(1024))
    return received_data

# Main game loop
running = True
while running:
    screen.fill(BLACK)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle_y -= 5
    if keys[pygame.K_DOWN]:
        paddle_y += 5

    # Send paddle position to the server and receive opponent's position
    opponent_paddle_y = send_receive_data(paddle_y)

    # Draw paddles
    draw_paddle(paddle_y)
    draw_paddle(opponent_paddle_y)

    pygame.display.update()

# Quit Pygame
pygame.quit()