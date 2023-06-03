import pygame
import random
import time

# Initialize Pygame
pygame.init()
pg = pygame
musica = pg.mixer.music.load
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
now_button = pygame.Rect((WIDTH - BUTTON_WIDTH - BUTTON_MARGIN), HEIGHT - BUTTON_HEIGHT - BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT)

# Initialize variables
countdown = 0
play_alarm = False
display_message = False
remaining_time = 0

def music_on():
    pg.mixer.music.play()

# Function to play audio
def play_audio():
    print("Playing audio...")
    global display_message
    display_message = True
    musica('sock1.wav')
    music_on()

# Function to reset countdown
def reset_countdown():
    global countdown, remaining_time
    countdown = random.randint(900, 2700)  # Random time between 15 and 45 minutes
    remaining_time = countdown

# Set initial countdown
reset_countdown()

# Game loop
running = True
start_time = time.time()
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
                    start_time = time.time()
                # Check if stop button clicked
                elif stop_button.collidepoint(event.pos):
                    play_alarm = False
                    reset_countdown()
                # Check if end button clicked
                elif end_button.collidepoint(event.pos):
                    running = False
                # Check if now button clicked
                elif now_button.collidepoint(event.pos):
                    play_audio()
                    reset_countdown()

    # Update countdown
    if play_alarm:
        elapsed_time = int(time.time() - start_time)
        remaining_time = max(0, countdown - elapsed_time)
        if remaining_time == 0:
            play_audio()
            play_alarm = False
            reset_countdown()

    # Clear the window
    window.fill(BLACK)

    # Draw buttons
    pygame.draw.rect(window, WHITE, start_button)
    pygame.draw.rect(window, WHITE, stop_button)
    pygame.draw.rect(window, WHITE, end_button)
    pygame.draw.rect(window, WHITE, now_button)

    # Draw button labels
    start_text = font.render("Start", True, BLACK)
    window.blit(start_text, (start_button.x + 20, start_button.y + 15))

    stop_text = font.render("RESET", True, BLACK)
    window.blit(stop_text, (stop_button.x + 10, stop_button.y + 15))

    end_text = font.render("End", True, BLACK)
    window.blit(end_text, (end_button.x + 30, end_button.y + 15))

    now_text = font.render("Now", True, BLACK)
    window.blit(now_text, (now_button.x + 30, now_button.y + 15))

    # Draw countdown timer
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    countdown_text = font.render(f"Countdown: {minutes:02d}:{seconds:02d}", True, WHITE)
    window.blit(countdown_text, (WIDTH // 2 - countdown_text.get_width() // 2, HEIGHT // 2 - countdown_text.get_height() // 2))

    # Draw message
    if display_message:
        message_text = font.render("Playing audio...", True, WHITE)
        window.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, HEIGHT // 2 - message_text.get_height() // 2 - 50))
        display_message = False

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
