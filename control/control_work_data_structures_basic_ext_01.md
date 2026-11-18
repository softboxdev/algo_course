# Проверочная работа №2 по Python: списки, кортежи, стек, очередь

**Продолжительность:** 90 минут  
**Максимальный балл:** 40

---

## Часть A. Выберите правильный вариант (5 × 2 = 10 баллов)

**A1.** Что выведет данный код?

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a, b)
```

- а) `[1, 2, 3, 4] [1, 2, 3, 4]`
- б) `[1, 2, 3] [1, 2, 3, 4]`
- в) `[1, 2, 3, 4] [1, 2, 3]`
- г) Ошибка

---

**A2.** Что произойдёт при выполнении кода?

```python
t = (1, 2, 3)
t[0] = 10
```

- а) Кортеж станет `(10, 2, 3)`
- б) Будет создан новый кортеж
- в) Возникнет `TypeError`
- г) Возникнет `IndexError`

---

**A3.** Какой метод списка реализует поведение очереди (FIFO) при использовании только этого списка?

- а) `append()` / `pop()`
- б) `append()` / `pop(0)`
- в) `insert(0, x)` / `pop()`
- г) `sort()` / `pop()`

---

**A4.** Что выведет код?

```python
from collections import deque
d = deque([1, 2, 3])
d.rotate(1)
print(d)
```

- а) `deque([3, 1, 2])`
- б) `deque([2, 3, 1])`
- в) `deque([1, 2, 3])`
- г) Ошибка

---

**A5.** Что выведет код?

```python
t = (1, 2, [3, 4])
t[2][0] = 100
print(t)
```

- а) `TypeError`
- б) `(1, 2, [100, 4])`
- в) `(1, 2, [3, 4])`
- г) `(100, 2, [3, 4])`

---

## Часть B. Что покажет код? (5 × 3 = 15 баллов)

**B1.**
```python
lst = [10, 20, 30, 40, 50]
print(lst[-3:])
print(lst[::2])
print(lst.index(30))
```

**B2.**
```python
t = (5, 10, 15)
a, b, c = t
print(a + b + c)
print(t * 2)
print(max(t), min(t))
```

**B3.**
```python
stack = []
stack.append("a")
stack.append("b")
stack.append("c")
print(stack[-1])
print(stack.pop())
print(stack.pop())
print(stack)
```

**B4.**
```python
from collections import deque
q = deque()
q.append(1)
q.append(2)
q.appendleft(0)
print(q)
print(q.popleft())
q.append(3)
print(q)
```

**B5.**
```python
a = [1, [2, 3], 4]
b = a[:]
b[1][0] = 99
b[0] = 100
print(a)
print(b)
```

---

## Часть C. Допишите код (4 × 3 = 12 баллов)

**C1.** Допишите функцию, которая возвращает список квадратов чисел, **больших 5**.

```python
def squares_over_five(lst):
    result = []
    for x in lst:
        # допишите условие и добавление
        ...
    return result

print(squares_over_five([2, 6, 3, 8, 1]))  # [36, 64]
```

**C2.** Реализуйте очередь на основе списка. Допишите методы `enqueue`, `dequeue` и `is_empty`.

```python
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        # допишите: добавить в конец
        ...

    def dequeue(self):
        # допишите: вернуть первый элемент и удалить его
        ...

    def is_empty(self):
        # допишите
        ...

q = Queue()
q.enqueue(1); q.enqueue(2); q.enqueue(3)
print(q.dequeue())   # 1
print(q.is_empty())  # False
```

**C3.** Допишите функцию, которая проверяет, является ли список **палиндромом**, используя `deque`.

```python
from collections import deque

def is_list_palindrome(lst):
    d = deque(lst)
    while len(d) > 1:
        # допишите сравнение
        ...
    return True

print(is_list_palindrome([1, 2, 3, 2, 1]))  # True
print(is_list_palindrome([1, 2, 3, 4]))     # False
```

**C4.** Допишите код: из списка строк создайте **кортеж** строк, длина которых больше 3.

```python
words = ["cat", "hello", "dog", "python", "sun"]
long_words = tuple(
    # допишите генератор
    ...
)
print(long_words)  # ('hello', 'python')
```

---

## Часть D. Задача (3 балла)

**D1.** Напишите функцию `remove_duplicates(t)`, которая принимает **кортеж** и возвращает **кортеж** без повторяющихся элементов, сохраняя порядок первого появления. Используйте список как вспомогательную структуру.

Примеры:
```python
print(remove_duplicates((1, 2, 2, 3, 1, 4)))  # (1, 2, 3, 4)
print(remove_duplicates((5, 5, 5)))           # (5,)
print(remove_duplicates(()))                  # ()
```

---

### Критерии оценивания
- Часть A: 2 балла за верный ответ
- Часть B: по 1 баллу за каждый правильный вывод (в B1–B5 по 3 вывода)
- Часть C: 3 балла за полностью верный код, 1–2 — при частичном решении
- Часть D: 3 балла за корректную реализацию с сохранением порядка и возвратом кортежа

**Оценка:** 36–40 — «5», 28–35 — «4», 20–27 — «3», менее 20 — «2».
