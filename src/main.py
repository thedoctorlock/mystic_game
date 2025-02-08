import pygame
import sys

from player import Player  # or put Player class in the same file if you prefer

def main():
    pygame.init()

    # Set up the display
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mystic Adventure")

    # Clock to cap FPS
    clock = pygame.time.Clock()

    # Create a player instance
    # Let's say the 'floor' is near the bottom of the screen: floor_y = 550
    floor_y = 550
    player = Player(x=100, y=100, width=50, height=50)

    # Main game loop
    running = True
    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # --- Input ---
        player.handle_input()

        # --- Physics Updates ---
        player.apply_gravity()
        player.update(floor_y)  # Check for collision with the floor

        # --- Draw ---
        screen.fill((30, 30, 60))           # background color
        player.draw(screen)
        pygame.display.flip()

        # Cap the frame rate at 60 FPS
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()