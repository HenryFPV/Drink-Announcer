import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH = 600
HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Countdown Timer")

# Set up fonts
font = pygame.font.Font(None, 36)

# Button dimensions
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 20

# Create buttons
start_button = pygame.Rect(BUTTON_MARGIN, HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT)
stop_button = pygame.Rect((BUTTON_MARGIN + BUTTON_WIDTH + BUTTON_MARGIN), HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT)
end_button = pygame.Rect((BUTTON_MARGIN + BUTTON_WIDTH + BUTTON_MARGIN + BUTTON_WIDTH + BUTTON_MARGIN), HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT)

# Initialize variables
countdown = 0
play_alarm = False

# Function to play audio
def play_audio():
    print("Playing audio...")
    # Play your audio file here

# Function to reset countdown
def reset_countdown():
    global countdown
    countdown = random.randint(900, 2700)  # Random time between 15 and 45 minutes

# Set initial countdown
reset_countdown()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Check if start button clicked
                if start_button.collidepoint(event.pos):
                    play_alarm = True
                # Check if stop button clicked
                elif stop_button.collidepoint(event.pos):
                    play_alarm = False
                # Check if end button clicked
                elif end_button.collidepoint(event.pos):
                    running = False

    # Update countdown
    if play_alarm:
        countdown -= 1
        if countdown == 0:
            play_audio()
            play_alarm = False
            reset_countdown()

    # Clear the window
    window.fill(BLACK)

    # Draw buttons
    pygame.draw.rect(window, WHITE, start_button)
    pygame.draw.rect(window, WHITE, stop_button)
    pygame.draw.rect(window, WHITE, end_button)

    # Draw button labels
    start_text = font.render("Start", True, BLACK)
    window.blit(start_text, (start_button.x + 20, start_button.y + 15))

    stop_text = font.render("Stop", True, BLACK)
    window.blit(stop_text, (stop_button.x + 25, stop_button.y + 15))

    end_text = font.render("End", True, BLACK)
    window.blit(end_text, (end_button.x + 30, end_button.y + 15))

    # Draw countdown timer
    countdown_text = font.render(f"Countdown: {countdown}", True, WHITE)
    window.blit(countdown_text, (WIDTH // 2 - countdown_text.get_width() // 2, HEIGHT // 2 - countdown_text.get_height() // 2))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
