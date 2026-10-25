import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_ang = random.uniform(20, 50)
            #split1_vector = pygame.Vector2(0, 1)
            rotated_split1 = self.velocity.rotate(rand_ang)
            #split2_vector = pygame.Vector2(0, 1)
            rotated_split2 = self.velocity.rotate(-rand_ang)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split_1 = Asteroid(self.position.x, self.position.y, new_radius)
            split_2 = Asteroid(self.position.x, self.position.y, new_radius)
            split_1.velocity = rotated_split1 * 1.2
            split_2.velocity = rotated_split2 * 1.2