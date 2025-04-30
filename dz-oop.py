class Task:
    def __init__(self, description, due_date, status=False):
        self.description = description
        self.due_date = due_date
        self.status = status  # False - не выполнено, True - выполнено

    def mark_as_done(self):
        self.status = True

    def __str__(self):
        status = "Выполнено" if self.status else "Не выполнено"
        return f"Описание: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print(f"Задача добавлена: {description}")

    def mark_task_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_as_done()
                print(f"Задача отмечена как выполненная: {description}")
                return
        print(f"Задача не найдена: {description}")

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.status]
        if not current_tasks:
            print("Нет текущих задач.")
        else:
            print("Текущие задачи (не выполненные):")
            for task in current_tasks:
                print(task)


# Пример использования
if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task("Потестить отчет", "2025-04-30")
    manager.add_task("Сделать презентацию", "2025-04-30")
    manager.add_task("Сделать домашку", "2025-04-30")

    print("\nТекущие задачи:")
    manager.show_current_tasks()

    print("\nОтмечаем задачу как выполненную...")
    manager.mark_task_done("Сделать домашку")

    print("\nОбновленный список задач:")
    manager.show_current_tasks()
