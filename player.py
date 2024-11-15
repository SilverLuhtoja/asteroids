import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

        self.momentum = 0
        self.moving = False

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update_position(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # self.position += forward * PLAYER_MAX_SPEED * dt
        self.position += forward * self.momentum

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(
            self.rotation) * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        self.shoot_timer -= dt
        if self.momentum > 0 and not self.moving:
            self.momentum -= dt

        self.player_action_mapping(dt)
        self.update_position()

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def player_action_mapping(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_s]:
            self.moving = True
        else:
            self.moving = False

        if keys[pygame.K_w]:
            self.momentum += dt
        if keys[pygame.K_s]:
            self.momentum -= dt

        # ROTATE
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()