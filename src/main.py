import pygame
import sys

def main():
    pygame.init()

    # Set up the display
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mystic Adventure")

    # Clock to cap FPS
    clock = pygame.time.Clock()

    # Example player (a simple rectangle)
    player_rect = pygame.Rect(100, 100, 50, 50)

    # Main game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game state (if any)

        # Clear screen with a background color
        screen.fill((30, 30, 60))

        # Draw the player
        pygame.draw.rect(screen, (200, 50, 50), player_rect)

        # Refresh the display
        pygame.display.flip()

        # Cap the frame rate at 60 FPS
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()