import pygame
import sys

from player import Player

def main():
    pygame.init()

    # Set up the display
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mystic Adventure")

    # Clock to cap FPS
    clock = pygame.time.Clock()

    # Platforms: hardcoded Rects for now (x, y, width, height)
    # The first rect is effectively your "ground."
    platforms = [
        pygame.Rect(0, 550, 800, 50),      # ground
        pygame.Rect(300, 400, 100, 20),    # floating platform
        # Add more as you wish
    ]

    # Create a player instance
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

        # --- Physics & Collision Updates ---
        # Pass in the platforms list so the player can check collisions
        player.apply_gravity()
        player.update(platforms)

        # --- Draw ---
        screen.fill((30, 30, 60))  # background color
       
        # Draw each platform (gray)
        for pf in platforms:
            pygame.draw.rect(screen, (100, 100, 100), pf)

        # Draw the player
        player.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()