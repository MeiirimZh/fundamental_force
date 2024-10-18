import random
from enemy_beam import EnemyBeam

class CommonEnemy:
    def __init__(self, sprite, beams_list, beam_sprite, speed):
        self.sprite = sprite
        self.beams_list = beams_list
        self.beam_sprite = beam_sprite

        self.width = sprite.get_size()[0]
        self.height = sprite.get_size()[1]

        self.has_collied = False

        self.x = random.randint(100, 800)
        self.y = -20
        self.speed = speed

        self.shoot()

    def move(self):
        self.y += self.speed

    def shoot(self):
        self.beams_list.append(EnemyBeam(self.beam_sprite, self.x + 23, self.y, 1))