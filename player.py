class Player:
    def __init__(self, sprite, x, y, speed, armor):
        self.sprite = sprite

        self.width = sprite.get_size()[0]
        self.height = sprite.get_size()[1]

        self.hit_box_x = self.width - 20
        self.hit_box_y = self.height - 20

        self.x = x
        self.y = y
        self.speed = speed

        self.armor = armor

        self.reload_time = 300
        self.last_time_shot = 0

        self.rush_reload = 10
        self.rush_duration = 5
        self.last_time_rushed = 0

        self.can_rush = False