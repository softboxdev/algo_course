Решение задачи "Частичный разворот" односвязного списка:

## **Решение на C++**

---

## **Компактное решение**

```cpp
#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int val = 0) : data(val), next(nullptr) {}
};

Node* Reverse(Node* head, int from, int to) {
    if (head == nullptr || from == to) {
        return head;
    }

    Node dummy(0);
    dummy.next = head;
    Node* prev = &dummy;

    // Идём к узлу перед from
    for (int i = 1; i < from; ++i) {
        prev = prev->next;
    }

    Node* current = prev->next;
    Node* next = nullptr;
    Node* tail = current;
    Node* temp = nullptr;

    // Стандартный разворот участка
    int count = to - from + 1;
    for (int i = 0; i < count; ++i) {
        next = current->next;
        current->next = temp;
        temp = current;
        current = next;
    }

    // Соединяем развёрнутый участок
    prev->next = temp;
    tail->next = current;

    return dummy.next;
}
```

---

## **Решение с использованием стека**

```cpp
#include <iostream>
#include <stack>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int val = 0) : data(val), next(nullptr) {}
};

Node* Reverse(Node* head, int from, int to) {
    if (head == nullptr || from == to) {
        return head;
    }

    Node dummy(0);
    dummy.next = head;
    Node* prev = &dummy;

    // Находим узел перед from
    for (int i = 1; i < from; ++i) {
        prev = prev->next;
    }

    // Собираем узлы для разворота в стек
    stack<Node*> st;
    Node* current = prev->next;
    for (int i = from; i <= to; ++i) {
        st.push(current);
        current = current->next;
    }
    Node* after_end = current;

    // Перестраиваем список, доставая узлы из стека
    current = prev;
    while (!st.empty()) {
        current->next = st.top();
        st.pop();
        current = current->next;
    }
    current->next = after_end;

    return dummy.next;
}
```

---

## **Объяснение алгоритма**

### **Основная идея**
Разбиваем список на три части:
1. **До from** (не меняется)
2. **Участок [from, to]** (разворачивается)
3. **После to** (не меняется)

### **Пошаговый алгоритм**

1. **Находим узел перед from**:
   - Идём от головы до `from - 1` шагов
   - Запоминаем его как `prev`

2. **Находим границы участка**:
   - `start` = узел на позиции `from`
   - `end` = узел на позиции `to`
   - `next_after_end` = узел после `end`

3. **Разворачиваем участок**:
   - Используем стандартный алгоритм разворота связного списка
   - Меняем указатели `next` для каждого узла на участке

4. **Соединяем части**:
   - `prev->next` указывает на новый первый узел (бывший `end`)
   - `start->next` указывает на `next_after_end`

### **Визуализация**

**Исходный список:**
```
[1] -> [2] -> [3] -> [4] -> [5]
        ↑             ↑
       from           to
```

**После разворота (from=2, to=4):**
```
[1] -> [4] -> [3] -> [2] -> [5]
```

---

## **Важные моменты**

1. **Проверка границ**:
   - Если `from == to`, разворот не нужен
   - Если `from == 1`, нужно менять голову списка

2. **Фиктивная голова** (dummy node):
   - Упрощает обработку случая `from == 1`
   - Не нужно обрабатывать особый случай для головы

3. **Сложность**:
   - Время: O(to) ≈ O(n)
   - Память: O(1) (без стека)

4. **Ограничения**:
   - Нельзя создавать новые вершины
   - Нумерация с 1 (не с 0)

---

## **Тестирование**

```cpp
// Тест 1: Нормальный случай
vector<int> v1 = {1, 2, 3, 4, 5};
// Reverse(v1, 2, 4) -> {1, 4, 3, 2, 5}

// Тест 2: Разворот с головы
vector<int> v2 = {1, 2, 3, 4, 5};
// Reverse(v2, 1, 3) -> {3, 2, 1, 4, 5}

// Тест 3: Разворот до конца
vector<int> v3 = {1, 2, 3, 4, 5};
// Reverse(v3, 3, 5) -> {1, 2, 5, 4, 3}

// Тест 4: Весь список
vector<int> v4 = {1, 2, 3, 4, 5};
// Reverse(v4, 1, 5) -> {5, 4, 3, 2, 1}

// Тест 5: Один элемент
vector<int> v5 = {1};
// Reverse(v5, 1, 1) -> {1}
```

---

## **Сравнение подходов**

| Подход | Преимущества | Недостатки |
|--------|--------------|------------|
| **Прямой разворот** | • O(1) памяти<br>• Быстрый<br>• Стандартный подход | • Сложнее понять |
| **Со стеком** | • Проще понять<br>• Интуитивный | • O(k) памяти<br>• Медленнее |
