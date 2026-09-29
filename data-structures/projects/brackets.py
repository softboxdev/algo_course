#!/usr/bin/env python3
# Проверка правильности скобок

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def check_brackets(text):
    """Возвращает True, если скобки расставлены правильно."""
    stack = Stack()

    for char in text:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.pop() is None:   # закрывающая без открывающей
                return False

    return stack.is_empty()            # все открывающие закрыты


# ---------- Проверка ----------
tests = [
    "(2 + 3) * 4",          # правильно
    "((a + b) * c)",        # правильно
    "(2 + 3)) * 4",         # лишняя закрывающая
    "((2 + 3) * 4",         # не хватает закрывающей
    "2 + 3 * 4",            # скобок нет — тоже правильно
]

for t in tests:
    result = "OK" if check_brackets(t) else "ОШИБКА"
    print(f"{result:8} | {t}")
