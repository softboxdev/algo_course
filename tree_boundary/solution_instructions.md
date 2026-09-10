"Граница дерева" с использованием BFS по уровням:

## **Решение на C++**

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <set>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, root;
    cin >> n >> root;

    vector<int> left_child(n, -1), right_child(n, -1);

    for (int i = 0; i < n; i++) {
        cin >> left_child[i] >> right_child[i];
    }

    // Множество для хранения граничных вершин (без дубликатов)
    set<int> boundary;

    // BFS по уровням
    queue<int> q;
    q.push(root);

    while (!q.empty()) {
        int level_size = q.size();
        vector<int> current_level;

        // Собираем все вершины текущего уровня
        for (int i = 0; i < level_size; i++) {
            int node = q.front();
            q.pop();
            current_level.push_back(node);

            // Добавляем детей в очередь
            if (left_child[node] != -1) {
                q.push(left_child[node]);
            }
            if (right_child[node] != -1) {
                q.push(right_child[node]);
            }
        }

        // Самая левая и самая правая вершина уровня — граничные
        boundary.insert(current_level.front());
        boundary.insert(current_level.back());
    }

    // Для листьев — отдельная проверка (они все на границе)
    for (int i = 0; i < n; i++) {
        if (left_child[i] == -1 && right_child[i] == -1) {
            boundary.insert(i);
        }
    }

    // Вывод
    bool first = true;
    for (int node : boundary) {
        if (!first) cout << " ";
        cout << node;
        first = false;
    }
    cout << endl;

    return 0;
}
```

---



## **Объяснение алгоритма**

### **Что такое граница дерева?**

Вершина `v` на границе, если:
1. **`v` — лист** (нет детей).
2. **`v` — самая левая** вершина на своём уровне (расстоянии от корня).
3. **`v` — самая правая** вершина на своём уровне.

### **Подход BFS (первое решение)**

Проходим по дереву **уровнями** (BFS):
- Для каждого уровня запоминаем первую и последнюю вершину → они граничные.
- Дополнительно проходим по всем вершинам и добавляем листья.

**Плюсы:** просто, интуитивно.
**Минусы:** нужен дополнительный проход для листьев.

### **Подход DFS (второе решение)**

Классический способ обхода границы дерева:
1. **Левая граница** — идём от корня вниз, всегда сначала влево (если нет — вправо). Добавляем вершины **сверху вниз**, кроме листьев.
2. **Листья** — обходим всё дерево, добавляем все листья **слева направо**.
3. **Правая граница** — идём от корня вниз, всегда сначала вправо (если нет — влево). Добавляем вершины **снизу вверх**, кроме листьев.

Важно: **не дублировать** вершины (например, корень может быть и на левой, и на правой границе).

---

## **Разбор на примере**

**Дерево:**
```
        1
       / \
      2   3
     / \   \
    4   5   6
       / \
      7   8
```

**Уровни (BFS):**
- Уровень 0: [1] → граница: 1 (и левая, и правая — один элемент)
- Уровень 1: [2, 3] → граница: 2 (левая), 3 (правая)
- Уровень 2: [4, 5, 6] → граница: 4 (левая), 6 (правая)
- Уровень 3: [7, 8] → граница: 7 (левая), 8 (правая)

**Листья:** 4, 7, 8, 6.

**Граница:** {1, 2, 3, 4, 6, 7, 8}.

**Проверка:** вершина 5 **не** на границе — она не лист и не крайняя на своём уровне.

---

## **Важные моменты**

### 1. **Корень всегда на границе**
Если у корня есть дети, он — единственная вершина на уровне 0, значит он и левая, и правая граница.

### 2. **Листья не дублируются**
В DFS-подходе листья добавляются **только** в обходе листьев, чтобы не задваивать.

### 3. **Порядок вывода — любой**
Условие говорит: «в любом порядке». Можно использовать `set` (сортировка) или `vector` + `unordered_set` (без сортировки, быстрее).

### 4. **Обработка `n = 1`**
Единственная вершина — корень, он же лист. Ответ: `[root]`.

### 5. **Гарантия корректности**
Входные данные корректны, значит:
- `root` существует,
- все `id` в диапазоне,
- дерево связное.

---

## **Версия с `unordered_set` для скорости**

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, root;
    cin >> n >> root;

    vector<int> left_child(n, -1), right_child(n, -1);
    for (int i = 0; i < n; i++) {
        cin >> left_child[i] >> right_child[i];
    }

    unordered_set<int> boundary;
    boundary.reserve(n * 2);

    // BFS по уровням
    queue<int> q;
    q.push(root);

    while (!q.empty()) {
        int level_size = q.size();
        int first = -1, last = -1;

        for (int i = 0; i < level_size; i++) {
            int node = q.front();
            q.pop();

            if (i == 0) first = node;
            if (i == level_size - 1) last = node;

            if (left_child[node] != -1) q.push(left_child[node]);
            if (right_child[node] != -1) q.push(right_child[node]);
        }

        boundary.insert(first);
        boundary.insert(last);
    }

    // Листья
    for (int i = 0; i < n; i++) {
        if (left_child[i] == -1 && right_child[i] == -1) {
            boundary.insert(i);
        }
    }

    // Вывод
    bool first = true;
    for (int node : boundary) {
        if (!first) cout << " ";
        cout << node;
        first = false;
    }
    cout << endl;

    return 0;
}
```

---

## **Сложность**

| Подход | Время | Память |
|--------|-------|--------|
| **BFS + листья** | O(n) | O(n) |
| **DFS (3 обхода)** | O(n) | O(h) — стек рекурсии |

Оба подхода работают за **линейное время** O(n), что оптимально для n ≤ 2·10^5.

---

## **Тестирование**

**Тест 1:**
```
Ввод:
3 0
1 2
-1 -1
-1 -1

Дерево:
    0
   / \
  1   2

Граница: 0, 1, 2
Вывод: 0 1 2
```

**Тест 2:**
```
Ввод:
1 0
-1 -1

Граница: 0
Вывод: 0
```

**Тест 3:**
```
Ввод:
5 0
1 2
3 -1
4 -1
-1 -1
-1 -1

Дерево:
      0
     / \
    1   2
   /   /
  3   4

Уровни:
  0: [0]
  1: [1, 2]
  2: [3, 4]

Граница: 0, 1, 2, 3, 4
Вывод: 0 1 2 3 4
```

---

## **Финальное решение (рекомендуемое — BFS)**

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, root;
    cin >> n >> root;

    vector<int> left_child(n, -1), right_child(n, -1);
    for (int i = 0; i < n; i++) {
        cin >> left_child[i] >> right_child[i];
    }

    unordered_set<int> boundary;

    // BFS по уровням: крайние вершины каждого уровня
    queue<int> q;
    q.push(root);

    while (!q.empty()) {
        int level_size = q.size();
        int first = -1, last = -1;

        for (int i = 0; i < level_size; i++) {
            int node = q.front();
            q.pop();

            if (i == 0) first = node;
            if (i == level_size - 1) last = node;

            if (left_child[node] != -1) q.push(left_child[node]);
            if (right_child[node] != -1) q.push(right_child[node]);
        }

        boundary.insert(first);
        boundary.insert(last);
    }

    // Листья
    for (int i = 0; i < n; i++) {
        if (left_child[i] == -1 && right_child[i] == -1) {
            boundary.insert(i);
        }
    }

    // Вывод
    bool first = true;
    for (int node : boundary) {
        if (!first) cout << " ";
        cout << node;
        first = false;
    }
    cout << "\n";

    return 0;
}
```

Это решение:
- ✅ Работает за O(n)
- ✅ Не использует рекурсию (безопасно при n = 2·10^5)
- ✅ Корректно обрабатывает все крайние случаи
- ✅ Выводит вершины без дубликатов
