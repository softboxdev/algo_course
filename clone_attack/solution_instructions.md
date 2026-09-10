
## **Решение на C++**

```cpp
#include "solution.h"
#include <unordered_map>
#include <queue>

/** Comment it before submitting
struct Node {
    int val;
    std::vector<Node*> neighbours;
    Node(int val_) {
        val = val_;
        neighbours = {};
    }
};
**/

Node* cloneGraph(Node* node) {
    if (node == nullptr) {
        return nullptr;
    }

    // Хэш-таблица: оригинал -> копия
    std::unordered_map<Node*, Node*> visited;

    // Создаём копию стартовой вершины
    Node* clone = new Node(node->val);
    visited[node] = clone;

    // BFS-обход
    std::queue<Node*> q;
    q.push(node);

    while (!q.empty()) {
        Node* current = q.front();
        q.pop();

        for (Node* neighbour : current->neighbours) {
            // Если сосед ещё не клонирован — создаём копию
            if (visited.find(neighbour) == visited.end()) {
                visited[neighbour] = new Node(neighbour->val);
                q.push(neighbour);
            }

            // Добавляем копию соседа в список соседей копии текущей вершины
            visited[current]->neighbours.push_back(visited[neighbour]);
        }
    }

    return clone;
}
```

---

## **Почему именно так**

### 1. **`#include "solution.h"`**
В шаблоне уже есть этот инклюд — он подключает структуру `Node` и объявление функции `cloneGraph`. Не удаляйте его.

### 2. **Имя поля — `val`, а не `value`**
В вашем шаблоне:
```cpp
struct Node {
    int val;
    ...
};
```
Значит, обращаться нужно к `node->val`, а не `node->value`.

### 3. **Свободная функция**
Объявление:
```cpp
Node* cloneGraph(Node* node);
```
Это **не метод класса**, поэтому определение должно быть **без** `class Solution` и без `Solution::`.

### 4. **BFS вместо DFS**
Рекурсивный DFS может переполнить стек при глубине 10^5. BFS безопаснее.

### 5. **`std::` префиксы**
В шаблоне используется `std::vector`, значит, `using namespace std;` не подключён. Пишем `std::unordered_map`, `std::queue` явно.

---

## **Альтернатива — рекурсивный DFS (короче, но рискованно)**

```cpp
#include "solution.h"
#include <unordered_map>

Node* cloneGraph(Node* node) {
    if (node == nullptr) {
        return nullptr;
    }

    static std::unordered_map<Node*, Node*> visited;
    visited.clear();  // на случай повторного вызова

    // Если копия уже есть — вернуть её
    if (visited.find(node) != visited.end()) {
        return visited[node];
    }

    // Создаём копию и СРАЗУ записываем в таблицу (защита от циклов)
    Node* clone = new Node(node->val);
    visited[node] = clone;

    // Рекурсивно клонируем соседей
    for (Node* neighbour : node->neighbours) {
        clone->neighbours.push_back(cloneGraph(neighbour));
    }

    return clone;
}
```

⚠️ **Минус:** при глубине рекурсии ~10^5 возможен stack overflow.
**Решение:** оставить BFS-вариант.

---

## **Ещё вариант — итеративный DFS**

```cpp
#include "solution.h"
#include <unordered_map>
#include <vector>

Node* cloneGraph(Node* node) {
    if (node == nullptr) {
        return nullptr;
    }

    std::unordered_map<Node*, Node*> visited;

    Node* clone = new Node(node->val);
    visited[node] = clone;

    std::vector<Node*> stack;
    stack.push_back(node);

    while (!stack.empty()) {
        Node* current = stack.back();
        stack.pop_back();

        for (Node* neighbour : current->neighbours) {
            if (visited.find(neighbour) == visited.end()) {
                visited[neighbour] = new Node(neighbour->val);
                stack.push_back(neighbour);
            }
            visited[current]->neighbours.push_back(visited[neighbour]);
        }
    }

    return clone;
}
```

---

## **Проверка корректности**

**Пример 1: одна вершина**
```
Вход:  Node(1), neighbours = {}
Выход: новый Node(1), neighbours = {}
```

**Пример 2: две связанные вершины**
```
Вход:  A(1) <-> B(2)
Выход: A'(1) <-> B'(2), где A' != A, B' != B
```

**Пример 3: треугольник**
```
Вход:  1 — 2
       \  /
        3
Выход: 1' — 2'
        \  /
         3'
```

---

## **Итоговый ответ**

```cpp
#include "solution.h"
#include <unordered_map>
#include <queue>

/** Comment it before submitting
struct Node {
    int val;
    std::vector<Node*> neighbours;
    Node(int val_) {
        val = val_;
        neighbours = {};
    }
};
**/

Node* cloneGraph(Node* node) {
    if (node == nullptr) {
        return nullptr;
    }

    std::unordered_map<Node*, Node*> visited;

    Node* clone = new Node(node->val);
    visited[node] = clone;

    std::queue<Node*> q;
    q.push(node);

    while (!q.empty()) {
        Node* current = q.front();
        q.pop();

        for (Node* neighbour : current->neighbours) {
            if (visited.find(neighbour) == visited.end()) {
                visited[neighbour] = new Node(neighbour->val);
                q.push(neighbour);
            }
            visited[current]->neighbours.push_back(visited[neighbour]);
        }
    }

    return clone;
}
```
