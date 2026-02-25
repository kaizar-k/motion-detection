import pygame
import random
import math

class Particle:
    def __init__(self, width, height):
        self.x = random.uniform(0, width)
        self.y = random.uniform(0, height)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.size = random.uniform(2, 5)
        self.color = (255, 255, 255)

    def update(self, motion, width, height):
        # Increase speed based on motion
        speed_factor = 1 + motion * 0.0005
        self.x += self.vx * speed_factor
        self.y += self.vy * speed_factor

        # Wrap around screen edges
        if self.x < 0: self.x = width
        if self.x > width: self.x = 0
        if self.y < 0: self.y = height
        if self.y > height: self.y = 0

        # Color shifts with motion
        intensity = min(255, int(motion * 0.02))
        self.color = (intensity, 100, 255 - intensity)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))


class VisualEngine:
    def __init__(self, width=800, height=600, particle_count=200):
        pygame.init()
        self.pygame = pygame

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Motion Visuals")

        self.particles = [Particle(width, height) for _ in range(particle_count)]
        self.clock = pygame.time.Clock()

    def update_and_draw(self, motion_score):
        self.screen.fill((0, 0, 0))

        for p in self.particles:
            p.update(motion_score, self.width, self.height)
            p.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)
