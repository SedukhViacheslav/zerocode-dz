from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "наносит удар мечом"

    def get_name(self):
        return "меч"


class Bow(Weapon):
    def attack(self):
        return "наносит удар из лука"

    def get_name(self):
        return "лук"


class Axe(Weapon):
    def attack(self):
        return "рубит топором"

    def get_name(self):
        return "топор"


class Fighter:
    def __init__(self, name="Боец"):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.get_name()}.")

    def attack(self):
        if self.weapon:
            print(f"{self.name} {self.weapon.attack()}.")
        else:
            print(f"{self.name} не имеет оружия!")


class Monster:
    def __init__(self, name="Монстр"):
        self.name = name

    def defeated(self):
        print(f"{self.name} побежден!")


def battle(fighter: Fighter, monster: Monster):
    fighter.attack()
    monster.defeated()
    print()


if __name__ == "__main__":
    fighter = Fighter()
    monster = Monster()

    fighter.change_weapon(Sword())
    battle(fighter, monster)

    fighter.change_weapon(Bow())
    battle(fighter, monster)

    fighter.change_weapon(Axe())  # Исправлено на change_weapon
    battle(fighter, monster)