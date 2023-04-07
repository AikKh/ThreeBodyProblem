import pygame

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set the dimensions of the window
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Create the window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the font for the text
font = pygame.font.Font(None, 36)

# Define the slider properties
slider_width = 200
slider_height = 20
slider_x = (WINDOW_WIDTH - slider_width) / 2
slider_y = (WINDOW_HEIGHT - slider_height) / 2
slider_value = 50
slider_min = 0
slider_max = 100

# Define the slider bar
slider_bar_rect = pygame.Rect(slider_x, slider_y, slider_width, slider_height)

# Define the slider knob
slider_knob_width = 20
slider_knob_height = 30
slider_knob_x = slider_x + (slider_value - slider_min) / (slider_max - slider_min) * (slider_width - slider_knob_width)
slider_knob_y = slider_y - (slider_knob_height - slider_height) / 2
slider_knob_rect = pygame.Rect(slider_knob_x, slider_knob_y, slider_knob_width, slider_knob_height)

# Define a function to draw the slider
def draw_slider():
    # Draw the slider bar
    pygame.draw.rect(screen, GRAY, slider_bar_rect)
    
    # Draw the slider knob
    pygame.draw.rect(screen, WHITE, slider_knob_rect)
    
    # Draw the slider value text
    text = font.render(str(slider_value), True, WHITE)
    text_rect = text.get_rect(center=(slider_knob_rect.centerx, slider_knob_rect.centery + slider_knob_height))
    screen.blit(text, text_rect)

# Define the game loop
running = True
dragging = False
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse clicked on the slider knob
            if slider_knob_rect.collidepoint(event.pos):
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            # Check if the slider knob is being dragged
            if dragging:
                slider_knob_rect.centerx = min(max(event.pos[0], slider_x), slider_x + slider_width)
                slider_value = int(slider_min + (slider_knob_rect.centerx - slider_x) / slider_width * (slider_max - slider_min))
                slider_value = min(max(slider_value, slider_min), slider_max)
    
    # Clear the screen
    screen.fill(BLACK)
    
    # Draw the slider
    draw_slider()
    
    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
