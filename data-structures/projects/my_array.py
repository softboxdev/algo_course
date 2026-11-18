#!/usr/bin/env python3
# Мой динамический массив

class MyArray:
    def __init__(self):
        """Создаём пустой массив с начальной ёмкостью 2."""
        self.capacity = 2           # сколько всего ячеек
        self.size = 0               # сколько занято
        self.data = [None] * self.capacity

    def append(self, value):
        """Добавить элемент в конец."""
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1

    def _resize(self):
        """Увеличить массив в 2 раза."""
        print(f"  [расширение: {self.capacity} -> {self.capacity * 2}]")
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def get(self, index):
        """Получить элемент по индексу."""
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне диапазона")
        return self.data[index]

    def set(self, index, value):
        """Изменить элемент по индексу."""
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне диапазона")
        self.data[index] = value

    def length(self):
        """Сколько элементов в массиве."""
        return self.size

    def __str__(self):
        """Красивый вывод для print()."""
        elements = [str(self.data[i]) for i in range(self.size)]
        return "[" + ", ".join(elements) + "]"


# ---------- Проверка ----------
print("=== Динамический массив ===")

arr = MyArray()
print("Создали пустой массив:", arr)
print("Размер:", arr.length())
print()

# Добавляем элементы и следим за расширением
for i in range(1, 6):
    print(f"append({i})")
    arr.append(i)
    print("  Массив:", arr)
    print("  size =", arr.size, ", capacity =", arr.capacity)
    print()

# Доступ по индексу
print("Элемент с индексом 2:", arr.get(2))
arr.set(2, 100)
print("После set(2, 100):", arr)
