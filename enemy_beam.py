class EnemyBeam:
    def __init__(self, sprite, x, y, speed):
        self.sprite = sprite

        self.width = sprite.get_size()[0]
        self.height = sprite.get_size()[1]

        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.y += self.speed