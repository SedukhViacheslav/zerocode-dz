class Warrior():
    # new
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color
    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2
    def eat(self):
        print(f"{self.name} сел есть")
        self.power += 1
    def hit(self):
        print(f"{self.name} бьёт")
        self.endurance -= 1
        self.power -= 1
    def walk(self):
        print(f"{self.name} ходит")
        self.endurance -= 1
        self.power -= 1

    def info(self):
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")