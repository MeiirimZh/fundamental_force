class EnemyBeam:
    def __init__(self, sprite, x, y, speed):
        self.sprite = sprite

        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y += self.speed