# main.py
import pygame
import sys

from player import Player
from level_loader import load_tmx_map

def main():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mystic Adventure")

    clock = pygame.time.Clock()

    # 1) Load the TMX map you found
    # (Make sure the .tmx and .gif tileset are in your project folder)
    tmx_file = "MagicLand.tmx"  # or whatever the file is named
    map_surface, collision_rects = load_tmx_map(tmx_file)

    # 2) Create a player
    player = Player(x=100, y=100, width=50, height=50)

    # 3) Optional: If your map is bigger than the screen, we need a camera offset
    camera_x = 0
    camera_y = 0

    running = True  # Define running variable

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Check if SPACE or UP is pressed
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    player.try_jump()  # This method should be defined in your Player class

        # Player movement (if you’re still using handle_input for left/right, or update accordingly)
        player.handle_input_movement_only()  
        player.apply_gravity()
        player.update(collision_rects)
        
        if player.y > map_surface.get_height() + 200:
            player.x, player.y = 100, 100
            player.y_vel = 0

        # Simple camera: center on player.x, player.y
        camera_x = player.x - WIDTH // 2
        camera_y = player.y - HEIGHT // 2

        # Clamp camera so it doesn't scroll past map edges
        map_width = map_surface.get_width()
        map_height = map_surface.get_height()
        camera_x = max(0, min(camera_x, map_width - WIDTH))
        camera_y = max(0, min(camera_y, map_height - HEIGHT))

        # Draw everything
        screen.fill((0, 0, 0))
        screen.blit(map_surface, (-camera_x, -camera_y))
        player.draw_with_camera(screen, camera_x, camera_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()