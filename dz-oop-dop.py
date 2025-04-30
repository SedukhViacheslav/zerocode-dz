class Store:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.items: dict[str, float] = {}  # Словарь товаров (название: цена)

    def add_item(self, item_name: str, price: float) -> None:
        """Добавляет товар в ассортимент магазина."""
        self.items[item_name] = price
        print(f'Товар "{item_name}" добавлен в {self.name}.')

    def remove_item(self, item_name: str) -> None:
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]
            print(f'Товар "{item_name}" удален из {self.name}.')
        else:
            print(f'Товар "{item_name}" не найден в {self.name}.')

    def get_price(self, item_name: str) -> float | None:
        """Возвращает цену товара. Если товара нет, возвращает None."""
        return self.items.get(item_name)

    def update_price(self, item_name: str, new_price: float) -> None:
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f'Цена товара "{item_name}" обновлена в {self.name}.')
        else:
            print(f'Товар "{item_name}" не найден в {self.name}.')

    def __str__(self) -> str:
        """Возвращает строковое представление магазина."""
        items_str = "\n  ".join(f"{name}: {price}Руб" for name, price in self.items.items())
        return (
            f"Магазин: {self.name}\n"
            f"Адрес: {self.address}\n"
            f"Товары:\n  {items_str if items_str else 'Нет товаров'}"
        )


# Создаем несколько магазинов
store1 = Store("Фруктовый рай", "ул. Пушкина, 10")
store2 = Store("Овощной дворик", "ул. Лермонтова, 5")
store3 = Store("Молочная ферма", "ул. Гоголя, 15")

# Добавляем товары в магазины
store1.add_item("Яблоки", 350)
store1.add_item("Бананы", 250)
store1.add_item("Апельсины", 350)

store2.add_item("Картофель", 120)
store2.add_item("Морковь", 60)
store2.add_item("Лук", 25)

store3.add_item("Молоко", 100)
store3.add_item("Сыр", 250)
store3.add_item("Йогурт", 180)

# Тестируем методы на одном из магазинов (например, store1)
print("\n--- Тестирование методов ---")
print("Исходное состояние магазина:")
print(store1)

print("\nДобавляем новый товар:")
store1.add_item("Виноград", 450)

print("\nОбновляем цену товара:")
store1.update_price("Яблоки", 360)

print("\nПытаемся обновить цену несуществующего товара:")
store1.update_price("Груши", 900)

print("\nЗапрашиваем цену товара:")
price = store1.get_price("Бананы")
print(f'Цена бананов: {price}Руб' if price is not None else "Товар не найден")

print("\nЗапрашиваем цену несуществующего товара:")
price = store1.get_price("Киви")
print(f'Цена киви: {price}Руб' if price is not None else "Товар не найден")

print("\nУдаляем товар:")
store1.remove_item("Апельсины")

print("\nПытаемся удалить несуществующий товар:")
store1.remove_item("Манго")

print("\nФинальное состояние магазина:")
print(store1)