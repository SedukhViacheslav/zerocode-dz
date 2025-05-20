import time
import random


class Hero:
    """
    Класс, представляющий героя для игры в битву.

    Атрибуты:
        name (str): Имя героя
        health (int): Уровень здоровья (по умолчанию 100)
        attack_power (int): Сила атаки (по умолчанию 20)
    """

    def __init__(self, name: str, health: int = 100, attack_power: int = 20):
        """
        Инициализация героя.

        Параметры:
            name: Имя героя
            health: Начальное здоровье
            attack_power: Сила атаки

        Проверки:
            - Имя не должно быть пустым
            - Здоровье и атака должны быть положительными числами
        """
        if not name:
            raise ValueError("Имя героя не может быть пустым")
        if health <= 0:
            raise ValueError("Здоровье должно быть положительным числом")
        if attack_power <= 0:
            raise ValueError("Сила атаки должна быть положительным числом")

        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other: 'Hero') -> None:
        """
        Атаковать другого героя.

        Параметры:
            other: Экземпляр класса Hero для атаки

        Проверки:
            - Цель атаки должна быть экземпляром Hero
            - Герой не может атаковать себя
            - Оба героя должны быть живы
        """
        if not isinstance(other, Hero):
            raise TypeError("Цель атаки должна быть экземпляром класса Hero")
        if self is other:
            raise ValueError("Герой не может атаковать себя")
        if not self.is_alive():
            raise ValueError("Мертвый герой не может атаковать")
        if not other.is_alive():
            raise ValueError("Нельзя атаковать мертвого героя")

        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self) -> bool:
        """Проверить, жив ли герой."""
        return self.health > 0


class Game:
    """
    Класс, управляющий игровым процессом.

    Атрибуты:
        player (Hero): Герой игрока
        computer (Hero): Герой компьютера
    """

    def __init__(self, player_name: str):
        """
        Инициализация игры.

        Параметры:
            player_name: Имя героя игрока
        """
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер", attack_power=18)  # Немного слабее игрока

    def _print_status(self) -> None:
        """Вывести текущий статус боя."""
        print("\n" + "=" * 30)
        print(f"{self.player.name}: {max(0, self.player.health)} HP")
        print(f"{self.computer.name}: {max(0, self.computer.health)} HP")
        print("=" * 30 + "\n")

    def start(self) -> None:
        """
        Начать игру и управлять ходом боя.

        Логика:
            1. Выводит информацию о начале боя
            2. По очереди вызывает атаки героев
            3. Проверяет состояние героев после каждого раунда
            4. Объявляет победителя
        """
        print("\n⚔️ Начинается битва героев! ⚔️")
        print(f"{self.player.name} (Здоровье: {self.player.health}) vs "
              f"{self.computer.name} (Здоровье: {self.computer.health})")

        # Определяем, кто атакует первым (случайный выбор)
        current_attacker, current_defender = random.choice(
            [(self.player, self.computer), (self.computer, self.player)]
        )
        print(f"\nПервым атакует {current_attacker.name}!\n")

        round_num = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"🌀 Раунд {round_num} 🌀")
            self._print_status()

            # Атака
            current_attacker.attack(current_defender)

            # Проверка состояния после атаки
            if not current_defender.is_alive():
                current_defender.health = 0  # Не допускаем отрицательного здоровья
                self._print_status()
                print(f"\n💀 {current_defender.name} повержен!")
                print(f"🎉 Победил {current_attacker.name}!")
                break

            # Смена атакующего и защищающегося
            current_attacker, current_defender = current_defender, current_attacker

            # Пауза для удобства чтения
            time.sleep(1.5)
            round_num += 1


def main():
    """Основная функция для запуска игры."""
    try:
        print("Добро пожаловать в игру 'Битва героев'!")
        player_name = input("Введите имя вашего героя: ").strip()
        if not player_name:
            player_name = "Безымянный"

        game = Game(player_name)
        game.start()

        # Предложение сыграть еще раз
        while True:
            choice = input("\nХотите сыграть еще раз? (да/нет): ").lower()
            if choice in ('нет', 'н', 'no', 'n'):
                print("Спасибо за игру! До свидания!")
                break
            elif choice in ('да', 'д', 'yes', 'y'):
                game = Game(player_name)
                game.start()
            else:
                print("Пожалуйста, введите 'да' или 'нет'.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        print("Игра завершена.")


if __name__ == "__main__":
    main()