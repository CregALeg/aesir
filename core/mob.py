from entity import Entity


class Mob(Entity):
    def __init__(self, hp, attack, defence, speed, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.speed = speed
