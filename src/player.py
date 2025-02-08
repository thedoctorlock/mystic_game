import pygame

class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_vel = 0
        self.y_vel = 0
        self.on_ground = False

        self.speed = 5
        self.jump_strength = -10
        self.gravity = 0.5

    def handle_input(self):
        keys = pygame.key.get_pressed()
        self.x_vel = 0

        if keys[pygame.K_LEFT]:
            self.x_vel = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.x_vel = self.speed

        # Jump only if on_ground
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.y_vel = self.jump_strength
            self.on_ground = False

    def apply_gravity(self):
        self.y_vel += self.gravity

    def update(self, platforms):
        # --- Move horizontally first ---
        self.x += self.x_vel
        # Resolve horizontal collisions
        self.resolve_collisions(platforms, axis='x')

        # --- Move vertically ---
        self.y += self.y_vel
        # Resolve vertical collisions
        self.resolve_collisions(platforms, axis='y')

    def resolve_collisions(self, platforms, axis):
        """
        Check and resolve collisions along a single axis (x or y)
        so we don't 'tunnel' through platforms.
        """
        # Create a player rect for collision checks
        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # Check each platform
        for pf in platforms:
            if player_rect.colliderect(pf):
                # We have a collision
                if axis == 'x':
                    # If moving right
                    if self.x_vel > 0:
                        self.x = pf.left - self.width
                    # If moving left
                    elif self.x_vel < 0:
                        self.x = pf.right
                    # Update the rect so further checks are accurate
                    player_rect.x = self.x

                elif axis == 'y':
                    # If moving down
                    if self.y_vel > 0:
                        self.y = pf.top - self.height
                        self.on_ground = True
                    # If moving up
                    elif self.y_vel < 0:
                        self.y = pf.bottom

                    # Reset vertical velocity if we collided vertically
                    self.y_vel = 0
                    player_rect.y = self.y

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 50, 50), (self.x, self.y, self.width, self.height))