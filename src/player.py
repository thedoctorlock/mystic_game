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
        self.jump_strength = -12
        self.gravity = 0.5

        # Double jump variables
        self.max_jumps = 2
        self.jumps_done = 0

    def handle_input_movement_only(self):
        """Check left/right each frame."""
        keys = pygame.key.get_pressed()
        self.x_vel = 0

        if keys[pygame.K_LEFT]:
            self.x_vel = -self.speed
        elif keys[pygame.K_RIGHT]:
            self.x_vel = self.speed

    def try_jump(self):
        """
        Called once per KEYDOWN event if player presses jump key.
        This ensures we only jump once per press.
        """
        if self.jumps_done < self.max_jumps:
            self.y_vel = self.jump_strength
            self.jumps_done += 1
            self.on_ground = False

    def apply_gravity(self):
        self.y_vel += self.gravity

    def update(self, platforms):
        # --- Move horizontally first ---
        self.x += self.x_vel
        self.resolve_collisions(platforms, axis='x')

        # --- Move vertically ---
        self.y += self.y_vel
        self.resolve_collisions(platforms, axis='y')

    def resolve_collisions(self, platforms, axis):
        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        for pf in platforms:
            if player_rect.colliderect(pf):
                if axis == 'x':
                    # Horizontal collisions
                    if self.x_vel > 0:
                        self.x = pf.left - self.width
                    elif self.x_vel < 0:
                        self.x = pf.right
                    player_rect.x = self.x

                elif axis == 'y':
                    if self.y_vel > 0:
                        # Landed on top
                        self.y = pf.top - self.height
                        self.on_ground = True
                        self.jumps_done = 0  # reset jumps on landing
                    elif self.y_vel < 0:
                        # Hit your head
                        self.y = pf.bottom

                    self.y_vel = 0
                    player_rect.y = self.y

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 50, 50), (self.x, self.y, self.width, self.height))

    def draw_with_camera(self, surface, camera_x, camera_y):
        pygame.draw.rect(
            surface,
            (200, 50, 50),
            (self.x - camera_x, self.y - camera_y, self.width, self.height)
        )