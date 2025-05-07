from typing import List


class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self._is_hungry = True
        self._is_sick = False

    def make_sound(self):
        print(f"{self.name} издает звук")

    def eat(self):
        if self._is_hungry:
            print(f"{self.name} ест")
            self._is_hungry = False
        else:
            print(f"{self.name} не голоден(а)")

    def get_health_status(self):
        return "болен(а)" if self._is_sick else "здоров(а)"

    def set_sick(self, is_sick: bool):
        self._is_sick = is_sick


class Bird(Animal):
    def __init__(self, name: str, age: int, wingspan: float):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print(f"{self.name} поет: Чик-чирик!")


class Mammal(Animal):
    def __init__(self, name: str, age: int, fur_color: str):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит: Гррр!")


class Reptile(Animal):
    def __init__(self, name: str, age: int, scale_type: str):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит: Шшшш!")


class Employee:
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position

    def work(self):
        print(f"{self.name} ({self.position}) выполняет свои обязанности")


class ZooKeeper(Employee):
    def __init__(self, name: str):
        super().__init__(name, "Смотритель")

    def feed_animal(self, animal: Animal):
        print(f"{self.name} кормит {animal.name}")
        animal.eat()

    def clean_enclosure(self, animal: Animal):
        print(f"{self.name} убирает вольер для {animal.name}")


class Veterinarian(Employee):
    def __init__(self, name: str):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal: Animal):
        if animal.get_health_status() == "болен(а)":
            print(f"{self.name} лечит {animal.name}")
            animal.set_sick(False)
            print(f"{animal.name} теперь здоров(а)!")
        else:
            print(f"{animal.name} не нуждается в лечении")


class Zoo:
    def __init__(self, name: str):
        self.name = name
        self._animals: List[Animal] = []
        self._employees: List[Employee] = []

    def add_animal(self, animal: Animal):
        self._animals.append(animal)
        print(f"{animal.name} добавлен(а) в {self.name}")

    def add_employee(self, employee: Employee):
        self._employees.append(employee)
        print(f"{employee.name} принят(а) на работу как {employee.position}")

    def get_animals(self) -> List[Animal]:
        return self._animals

    def get_employees_by_position(self, position: str) -> List[Employee]:
        return [emp for emp in self._employees if emp.position == position]

    def daily_routine(self):
        print(f"\n--- Дневной режим в {self.name} ---")

        # Смотрители кормят животных и убирают вольеры
        for keeper in self.get_employees_by_position("Смотритель"):
            for animal in self._animals:
                keeper.feed_animal(animal)
                keeper.clean_enclosure(animal)

        # Ветеринары проверяют здоровье
        for vet in self.get_employees_by_position("Ветеринар"):
            for animal in self._animals:
                if animal.get_health_status() == "болен(а)":
                    vet.heal_animal(animal)


# Пример использования
if __name__ == "__main__":
    # Создаем зоопарк
    zoo = Zoo("Дикий мир")

    # Добавляем животных (некоторые больные)
    animals = [
        Bird("Воробей", 2, 15),
        Mammal("Лев", 5, "золотистый"),
        Reptile("Змея", 3, "гладкая")
    ]
    animals[1].set_sick(True)  # Лев болен

    for animal in animals:
        zoo.add_animal(animal)

    # Наняем сотрудников
    zoo.add_employee(ZooKeeper("Иван Петров"))
    zoo.add_employee(Veterinarian("Мария Сидорова"))
    zoo.add_employee(ZooKeeper("Алексей Павлов"))

    # Выполняем дневные обязанности
    zoo.daily_routine()

    # Проверяем здоровье животных после лечения
    print("\nСостояние здоровья животных:")
    for animal in zoo.get_animals():
        print(f"{animal.name}: {animal.get_health_status()}")