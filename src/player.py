# player.py
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

        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.y_vel = self.jump_strength
            self.on_ground = False

    def apply_gravity(self):
        self.y_vel += self.gravity

    def update(self, floor_y):
        self.x += self.x_vel
        self.y += self.y_vel

        # Check collision with the "floor"
        if self.y + self.height > floor_y:
            self.y = floor_y - self.height
            self.y_vel = 0
            self.on_ground = True

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 50, 50), (self.x, self.y, self.width, self.height))