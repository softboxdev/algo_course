# Разбор основных структур данных на Python: практическая работа для РОСА Линукс

**Цель работы:** Изучить базовые структуры данных в Python 3.8, разобрать их реализацию и запустить примеры в операционной системе РОСА Линукс.

**Требования:** Компьютер с установленной ОС РОСА Линукс, терминал, встроенный Python 3.8.

---

## Подготовка: проверка Python

Откройте терминал (`Ctrl+Alt+T`) и убедитесь, что Python на месте:

```bash
python3 --version
```

Ожидаемый вывод:
```
Python 3.8.13
```

В РОСА Python 3.8 — системный, и обновлять его глобально **не рекомендуется**, чтобы не сломать зависимости системы . Для новых версий Python (например, 3.11) его устанавливают отдельно через `sudo dnf install python3.11` и вызывают как `/usr/libexec/python3.11` .

---

## Способ 1. Запуск через интерпретатор (самый простой)

Это основной способ. Вы явно говорите системе: «запусти Python и передай ему мой файл».

### 1.1. Создайте скрипт

Перейдите в папку, где будет лежать скрипт, и создайте файл:

```bash
cd ~
nano hello.py
```

Введите код:

```python
print("Hello, Rosa Linux!")
```

Сохраните: `Ctrl+O`, `Enter`, `Ctrl+X`.

### 1.2. Запустите

```bash
python3 hello.py
```

**Результат:**
```
Hello, Rosa Linux!
```

В РОСА для Python 2 используется команда `python`, для Python 3 — `python3` . Всегда используйте `python3`, чтобы не запустить старый Python 2.

---

## Способ 2. Запуск как исполняемый файл (с `./`)

Этот способ позволяет запускать скрипт как обычную программу, без указания `python3` каждый раз.

### 2.1. Добавьте shebang

Shebang — это первая строка файла, которая говорит системе, чем интерпретировать скрипт . Для Python:

```python
#!/usr/bin/env python3
print("Hello, Rosa Linux!")
```

Используйте `/usr/bin/env python3`, а не жёсткий путь `/usr/bin/python3` — это надёжнее, если Python установлен в нестандартном месте или используется виртуальное окружение .

### 2.2. Дайте право на выполнение

Созданный файл не является исполняемым по умолчанию. Проверить:

```bash
ls -l hello.py
# -rw-r--r-- 1 user user 33 ... hello.py   ← нет «x»
```

Добавить право:

```bash
chmod +x hello.py
```

Теперь:

```bash
ls -l hello.py
# -rwxr-xr-x 1 user user 33 ... hello.py   ← есть «x»
```

Без `chmod +x` при запуске `./hello.py` будет ошибка `Permission denied` .

### 2.3. Запустите

```bash
./hello.py
```

Точка и слэш `./` обязательны: они означают «ищи файл в текущей папке». Без них Linux ищет программу в системных директориях и не находит.

---

## Способ 3. Запуск из любой папки (через `PATH`)

Если скрипт нужен постоянно, его можно поместить в директорию, которая уже есть в `PATH`, и вызывать по имени из любого места.

### 3.1. Создайте личную папку для скриптов

```bash
mkdir -p ~/.local/bin
```

### 3.2. Переместите или скопируйте скрипт

```bash
cp hello.py ~/.local/bin/hello
```

Обратите внимание: убрали расширение `.py` — теперь это команда `hello`.

### 3.3. Проверьте, что папка в `PATH`

```bash
echo $PATH
```

Если `~/.local/bin` там нет — добавьте в `~/.bashrc`:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
exec bash
```

### 3.4. Запустите из любого места

```bash
cd /tmp
hello
```

**Результат:**
```
Hello, Rosa Linux!
```

---

## Способ 4. Запуск в интерактивном режиме (для экспериментов)

Если нужно быстро проверить кусок кода, можно запустить Python без файла:

```bash
python3
```

Появится приглашение `>>>`. Введите код:

```python
>>> print("Привет из РОСА!")
>>> 2 + 2
```

Выход: `exit()` или `Ctrl+D` .

---

## Способ 5. Запуск через `-c` (одна строка без файла)

Для коротких команд:

```bash
python3 -c "print('Hello from command line!')"
```

Это удобно для быстрых проверок, но не для больших скриптов .

---


## 1. Введение

### Что такое структуры данных?

**Структура данных** — это способ организации и хранения информации, который позволяет эффективно её использовать: добавлять, искать, удалять элементы.

В Python есть **встроенные** структуры (список, словарь) и **реализуемые вручную** (стек, очередь, связный список). В этой работе мы разберём оба типа.

### Проверка Python в РОСА Линукс

В РОСА Линукс Python 3.8 уже установлен по умолчанию . Откройте терминал (`Ctrl+Alt+T`) и проверьте:

```bash
python3 --version
```

Ожидаемый вывод:
```
Python 3.8.13
```

Если Python не найден, установите его:
```bash
sudo dnf install python3
```

### Как запускать скрипты

Создайте файл с расширением `.py` и запустите его командой:

```bash
python3 имя_файла.py
```

Например, файл `test.py`:
```python
print("Hello, Rosa Linux!")
```

Запуск:
```bash
python3 test.py
```

Подробнее о способах запуска см. в разделе 9.

---

## 2. Динамический массив (список `list`)

### Теория

**Динамический массив** — это массив, который может автоматически расширяться при добавлении элементов. В Python это встроенный тип `list`.

**Характеристики:**
- Доступ по индексу: **O(1)** — мгновенно
- Добавление в конец (`append`): **O(1)** амортизированно
- Вставка/удаление в середину: **O(n)** — нужно сдвигать элементы
- Поиск: **O(n)** в общем случае

### Пример кода

Создайте файл `01_dynamic_array.py`:

```python
#!/usr/bin/env python3
# Динамический массив (список) в Python

print("=== Динамический массив ===")

# Создание списка
numbers = [10, 20, 30]
print("Исходный список:", numbers)

# Добавление в конец
numbers.append(40)
numbers.append(50)
print("После append(40), append(50):", numbers)

# Доступ по индексу
print("Элемент с индексом 2:", numbers[2])

# Изменение элемента
numbers[0] = 100
print("После numbers[0] = 100:", numbers)

# Вставка в середину (дорого по времени!)
numbers.insert(1, 15)
print("После insert(1, 15):", numbers)

# Удаление
numbers.remove(15)
print("После remove(15):", numbers)

# Длина
print("Длина списка:", len(numbers))

# Срез (slice)
print("Срез numbers[1:3]:", numbers[1:3])
```

**Запуск:**
```bash
cd ~/python_structures
python3 01_dynamic_array.py
```

---

## 3. Стек (Stack)

### Теория

**Стек** — структура данных, работающая по принципу **LIFO** (Last In, First Out): «последним пришёл — первым вышел».

**Аналогия:** стопка тарелок. Кладёшь сверху, берёшь сверху.

**Операции:**
- `push` — добавить на вершину
- `pop` — снять с вершины
- `peek` — посмотреть верхний элемент

**Реализация в Python:** можно использовать `list` (методы `append` и `pop`).

### Пример кода

Создайте файл `02_stack.py`:

```python
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
```

**Запуск:**
```bash
python3 02_stack.py
```

---

## 4. Очередь (Queue)

### Теория

**Очередь** — структура данных, работающая по принципу **FIFO** (First In, First Out): «первым пришёл — первым вышел».

**Аналогия:** очередь в магазине. Кто первый встал, тот первый уйдёт.

**Операции:**
- `enqueue` — добавить в конец
- `dequeue` — извлечь из начала

**Реализация:** используем `collections.deque` — он эффективнее списка для извлечения из начала.

### Пример кода

Создайте файл `03_queue.py`:

```python
#!/usr/bin/env python3
# Очередь (FIFO)

print("=== Очередь ===")

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Добавить в конец очереди"""
        self.items.append(item)

    def dequeue(self):
        """Извлечь из начала очереди"""
        if self.is_empty():
            return None
        return self.items.popleft()

    def front(self):
        """Посмотреть первый элемент"""
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return "Queue: " + str(list(self.items))

# Использование
q = Queue()
q.enqueue("Задача 1")
q.enqueue("Задача 2")
q.enqueue("Задача 3")
print(q)

print("Первый в очереди:", q.front())
print("Выполняем:", q.dequeue())
print("Выполняем:", q.dequeue())
print("После двух dequeue:", q)
print("Размер:", q.size())
```

**Запуск:**
```bash
python3 03_queue.py
```

---

## 5. Связный список (Linked List)

### Теория

**Связный список** — структура, где каждый элемент (**узел**) хранит данные и **ссылку** на следующий элемент.

**Виды:**
- **Односвязный** — каждый узел ссылается на следующий
- **Двусвязный** — ссылки в обе стороны

**Плюсы:** быстрая вставка/удаление в любом месте (**O(1)**, если есть ссылка на узел).
**Минусы:** доступ по индексу — **O(n)** (нужно идти от начала).

### Пример кода

Создайте файл `04_linked_list.py`:

```python
#!/usr/bin/env python3
# Односвязный список

print("=== Связный список ===")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Добавить в конец"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Добавить в начало"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Удалить первый узел с указанными данными"""
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next

    def display(self):
        """Показать все элементы"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(str(e) for e in elements))

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Использование
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print("После append(10,20,30):")
ll.display()

ll.prepend(5)
print("После prepend(5):")
ll.display()

ll.delete(20)
print("После delete(20):")
ll.display()

print("Длина списка:", ll.length())
```

**Запуск:**
```bash
python3 04_linked_list.py
```

---

## 6. Хеш-таблица (Hash Table)

### Теория

**Хеш-таблица** — структура, которая хранит пары «ключ → значение» и обеспечивает **быстрый доступ** по ключу.

**Принцип:**
1. Ключ преобразуется в число с помощью **хеш-функции**.
2. Число определяет **индекс** в массиве.
3. По этому индексу хранится значение.

**В Python:** встроенный тип `dict`.

**Характеристики:**
- Вставка: **O(1)** в среднем
- Поиск: **O(1)** в среднем
- Удаление: **O(1)** в среднем

### Пример кода

Создайте файл `05_hash_table.py`:

```python
#!/usr/bin/env python3
# Хеш-таблица (словарь)

print("=== Хеш-таблица ===")

# Создание словаря
phonebook = {
    "Иван": "+7-900-123-45-67",
    "Мария": "+7-900-765-43-21",
    "Петр": "+7-900-111-22-33"
}

print("Исходный словарь:", phonebook)

# Добавление
phonebook["Анна"] = "+7-900-999-88-77"
print("После добавления Анны:", phonebook)

# Поиск
print("Телефон Ивана:", phonebook.get("Иван"))
print("Телефон Сергея:", phonebook.get("Сергей", "не найден"))

# Изменение
phonebook["Иван"] = "+7-900-000-00-00"
print("После изменения:", phonebook["Иван"])

# Удаление
del phonebook["Петр"]
print("После удаления Петра:", phonebook)

# Проверка наличия ключа
print("Есть ли Мария?", "Мария" in phonebook)
print("Есть ли Петр?", "Петр" in phonebook)

# Перебор
print("\nВсе контакты:")
for name, phone in phonebook.items():
    print(f"  {name}: {phone}")
```

**Запуск:**
```bash
python3 05_hash_table.py
```

---

## 7. Бинарная куча и приоритетная очередь

### Теория

**Бинарная куча** — это **двоичное дерево**, где каждый родитель меньше (min-heap) или больше (max-heap) своих потомков.

**Приоритетная очередь** — очередь, где элементы извлекаются по **приоритету**, а не по времени добавления.

**В Python:** модуль `heapq` реализует **min-heap** (минимальный элемент всегда наверху).

**Характеристики:**
- Вставка: **O(log n)**
- Извлечение минимума: **O(log n)**
- Просмотр минимума: **O(1)**

### Пример кода

Создайте файл `06_heap.py`:

```python
#!/usr/bin/env python3
# Бинарная куча (heapq) и приоритетная очередь

print("=== Бинарная куча ===")

import heapq

# Min-heap: минимальный элемент наверху
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

print("Куча (внутреннее представление):", heap)
print("Минимальный элемент (heap[0]):", heap[0])

# Извлечение минимума
print("\nИзвлекаем по одному:")
while heap:
    print("  Извлечено:", heapq.heappop(heap))

# Приоритетная очередь: (приоритет, значение)
print("\n=== Приоритетная очередь ===")

tasks = []
heapq.heappush(tasks, (3, "Низкий приоритет"))
heapq.heappush(tasks, (1, "Высокий приоритет"))
heapq.heappush(tasks, (2, "Средний приоритет"))

print("Задачи в очереди:")
while tasks:
    priority, task = heapq.heappop(tasks)
    print(f"  Приоритет {priority}: {task}")
```

**Запуск:**
```bash
python3 06_heap.py
```

---

## 8. Двоичное дерево поиска (BST)

### Теория

**Двоичное дерево поиска (Binary Search Tree, BST)** — дерево, где:
- Левое поддерево содержит **меньшие** элементы
- Правое поддерево содержит **большие** элементы

**Характеристики (в среднем):**
- Поиск: **O(log n)**
- Вставка: **O(log n)**
- Удаление: **O(log n)**

В **худшем случае** (несбалансированное дерево) — **O(n)**.

### Пример кода

Создайте файл `07_bst.py`:

```python
#!/usr/bin/env python3
# Двоичное дерево поиска

print("=== Двоичное дерево поиска ===")

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Вставить значение"""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        """Найти значение"""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """Симметричный обход (выдаёт отсортированный список)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

# Использование
bst = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

print("Симметричный обход (отсортировано):", bst.inorder())
print("Поиск 40:", bst.search(40))
print("Поиск 45:", bst.search(45))
print("Поиск 70:", bst.search(70))
```

**Запуск:**
```bash
python3 07_bst.py
```

---

## 9. Запуск скриптов в РОСА Линукс: три способа

### Способ 1. Через интерпретатор (самый простой)

```bash
python3 имя_файла.py
```

### Способ 2. Как исполняемый файл

Добавьте в начало файла **шебанг**:

```python
#!/usr/bin/env python3
```

Сделайте файл исполняемым и запустите:

```bash
chmod +x имя_файла.py
./имя_файла.py
```

Этот способ описан в документации для Linux .

### Способ 3. Интерактивный режим (для экспериментов)

```bash
python3
```

Введите код прямо в приглашении `>>>`:

```python
>>> print("Привет из РОСА!")
>>> 2 + 2
```

Выход: `exit()`

---

## 10. Итоговая таблица: структуры данных и их сложность

| Структура | Доступ по индексу | Поиск | Вставка | Удаление | Где применять |
|---|---|---|---|---|---|
| **Динамический массив (list)** | O(1) | O(n) | O(1) в конец / O(n) в середину | O(n) | Хранение упорядоченных данных |
| **Стек** | — | O(n) | O(1) | O(1) с вершины | Отмена действий, парсинг |
| **Очередь** | — | O(n) | O(1) | O(1) из начала | Обработка задач |
| **Связный список** | O(n) | O(n) | O(1) при известной позиции | O(1) | Частые вставки/удаления |
| **Хеш-таблица (dict)** | — | O(1) | O(1) | O(1) | Быстрый поиск по ключу |
| **Бинарная куча (heapq)** | — | — | O(log n) | O(log n) | Приоритетные очереди |
| **BST** | — | O(log n) ср. | O(log n) ср. | O(log n) ср. | Упорядоченные данные, диапазоны |

---

## 11. Практическое задание для самостоятельной работы

Создайте скрипт `task.py`, который:

1. **Динамический массив:** создаёт список из 5 чисел, добавляет ещё 3, выводит сумму.
2. **Стек:** проверяет, является ли строка палиндромом (читается одинаково в обе стороны), используя стек.
3. **Очередь:** моделирует очередь из 3 клиентов, обслуживает их по порядку.
4. **Хеш-таблица:** создаёт словарь «предмет → оценка» из 3 записей, выводит средний балл.
5. **Куча:** находит 3 наименьших числа в списке `[15, 3, 8, 1, 20, 5]` с помощью `heapq`.

**Подсказка для стека-палиндрома:**
```python
def is_palindrome(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)
    for ch in s:
        if ch != stack.pop():
            return False
    return True
```

---

## Контрольные вопросы

1. Чем отличается стек от очереди? Приведите примеры из жизни.
2. Почему доступ по индексу в списке — O(1), а в связном списке — O(n)?
3. Почему в хеш-таблице поиск в среднем O(1), но может деградировать?
4. В каком случае BST вырождается в связный список? Как это исправить?
5. Зачем нужна приоритетная очередь? Где она применяется в реальных системах?

---

**Отчёт должен содержать:** листинги всех скриптов, скриншоты терминала РОСА Линукс с результатами запуска, ответы на контрольные вопросы.

