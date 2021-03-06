class Entity(object):
    """The base class that all characters/mobs follow."""

    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop("name")


class Character(Entity):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Stats
        self.hp = kwargs.pop("hp")
        self.attack = kwargs.pop("attack")
        self.defence = kwargs.pop("defence")
        self.magic = kwargs.pop("magic")
        self.speed = kwargs.pop("speed")

        self.attack_points = self.attack * 4
        self.magic_points = self.magic * 3

    def basic_attack(target, rune=None):
        power = rune.basic_attack_bonus if rune is not None else 1
        damage = target.defence - (0.5 * self.attack) + power

    def special_attack(target, attack):
        damage = target.defence - (0.5 * self.attack) + attack.power

    def magic_attack(target, attack):
        pass


class Mob(Entity):
    def __init__(self, hp, attack, defence, speed, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.speed = speed
