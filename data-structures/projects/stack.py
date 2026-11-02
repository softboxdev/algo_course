#!/usr/bin/env python3
# Стек (LIFO)

print("=== Стек ===")

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавить элемент на вершину стека"""
        self.items.append(item)

    def pop(self):
        """Снять и вернуть верхний элемент"""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """Посмотреть верхний элемент, не удаляя"""
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return "Stack: " + str(self.items)

# Использование
stack = Stack()
stack.push("Первый")
stack.push("Второй")
stack.push("Третий")
print(stack)

print("Верхний элемент:", stack.peek())
print("Снимаем:", stack.pop())
print("Снимаем:", stack.pop())
print("После двух pop:", stack)
print("Размер:", stack.size())
