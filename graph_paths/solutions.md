Решение задачи "Пути в дереве" с использованием DFS и хэш-таблицы (префиксных сумм):

## **Решение на C++**

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

long long ans = 0;
int target;
vector<vector<int>> children;
vector<int> weight;

void dfs(int node, long long current_sum, unordered_map<long long, int>& prefix_sums) {
    // Добавляем вес текущей вершины к сумме
    current_sum += weight[node];

    // Проверяем, есть ли путь с суммой target, заканчивающийся в текущей вершине
    // current_sum - target = сумма, которую мы ищем в префиксах
    if (prefix_sums.count(current_sum - target)) {
        ans += prefix_sums[current_sum - target];
    }

    // Добавляем текущую префиксную сумму в хэш-таблицу
    prefix_sums[current_sum]++;

    // Рекурсивно обрабатываем всех детей
    for (int child : children[node]) {
        dfs(child, current_sum, prefix_sums);
    }

    // Удаляем текущую префиксную сумму при возврате (backtracking)
    prefix_sums[current_sum]--;
    if (prefix_sums[current_sum] == 0) {
        prefix_sums.erase(current_sum);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n >> target;

    children.assign(n, {});
    weight.assign(n, 0);

    int root = -1;

    // Читаем вершины
    for (int i = 0; i < n; i++) {
        int parent, w;
        cin >> parent >> w;
        weight[i] = w;

        if (parent == -1) {
            root = i;
        } else {
            children[parent].push_back(i);
        }
    }

    // Хэш-таблица для хранения префиксных сумм
    unordered_map<long long, int> prefix_sums;
    // Изначально есть путь из 0 вершин с суммой 0
    prefix_sums[0] = 1;

    // Запускаем DFS от корня
    dfs(root, 0, prefix_sums);

    cout << ans << endl;

    return 0;
}
```

---

## **Альтернативное решение (более эффективное с reserve)**

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
private:
    long long ans = 0;
    int target;
    vector<vector<int>> children;
    vector<int> weight;

    void dfs(int node, long long current_sum, unordered_map<long long, int>& prefix_sums) {
        current_sum += weight[node];

        // Находим количество путей, заканчивающихся в текущей вершине
        auto it = prefix_sums.find(current_sum - target);
        if (it != prefix_sums.end()) {
            ans += it->second;
        }

        // Добавляем текущую сумму
        prefix_sums[current_sum]++;

        // Обрабатываем детей
        for (int child : children[node]) {
            dfs(child, current_sum, prefix_sums);
        }

        // Откатываем изменения
        prefix_sums[current_sum]--;
        if (prefix_sums[current_sum] == 0) {
            prefix_sums.erase(current_sum);
        }
    }

public:
    long long countPaths(int n, int x, const vector<pair<int, int>>& vertices) {
        target = x;
        children.assign(n, {});
        weight.assign(n, 0);

        int root = -1;
        for (int i = 0; i < n; i++) {
            int parent = vertices[i].first;
            int w = vertices[i].second;
            weight[i] = w;

            if (parent == -1) {
                root = i;
            } else {
                children[parent].push_back(i);
            }
        }

        unordered_map<long long, int> prefix_sums;
        prefix_sums.reserve(n * 2);  // Улучшаем производительность
        prefix_sums.max_load_factor(0.7);
        prefix_sums[0] = 1;

        dfs(root, 0, prefix_sums);
        return ans;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, x;
    cin >> n >> x;

    vector<pair<int, int>> vertices(n);
    for (int i = 0; i < n; i++) {
        cin >> vertices[i].first >> vertices[i].second;
    }

    Solution sol;
    cout << sol.countPaths(n, x, vertices) << endl;

    return 0;
}
```

---

## **Объяснение алгоритма**

### **Идея**
Используем метод **префиксных сумм** (prefix sums) на пути от корня до текущей вершины.

### **Ключевые моменты**

1. **Префиксная сумма**:
   - Для каждой вершины храним сумму весов от корня до этой вершины.
   - `current_sum` = сумма весов на пути от корня до текущей вершины.

2. **Поиск путей**:
   - Если мы хотим найти путь с суммой `target`, заканчивающийся в текущей вершине:
   - Нужно найти предыдущую вершину (или корень), где префиксная сумма была равна `current_sum - target`.
   - Количество таких вершин даст количество путей с суммой `target`.

3. **Хэш-таблица**:
   - Ключ: префиксная сумма
   - Значение: сколько раз такая сумма встречалась

4. **Backtracking**:
   - При возврате из рекурсии удаляем текущую префиксную сумму из хэш-таблицы.
   - Это нужно, чтобы не учитывать пути, которые идут в другие ветки дерева.

---

## **Пример работы**

**Входные данные:**
```
5 3
-1 1
0 2
0 1
1 -1
1 3
```

**Дерево:**
```
    0 (1)
   / \
  1(2) 2(1)
 / \
3(-1) 4(3)
```

**Пути с суммой 3:**
- Путь от 0 до 1: 1+2=3 ✓
- Путь от 0 до 4: 1+2+3=6 ❌
- Путь от 3 до 3: -1 ❌
- Путь от 1 до 4: 2+3=5 ❌
- Путь от 2 до 2: 1 ❌

**Ответ: 1**

---

## **Сложность**

- **Время:** O(N) - проходим каждую вершину один раз
- **Память:** O(N) - для хранения дерева и хэш-таблицы

---

## **Важные замечания**

1. **Тип данных**: Используем `long long` для сумм, так как веса могут быть отрицательными, а `X` до 10^9.

2. **Начальное условие**: `prefix_sums[0] = 1` - путь из 0 вершин с суммой 0 (нужен для случая, когда путь начинается от корня).

3. **Обработка отрицательных весов**: Алгоритм корректно работает с отрицательными весами.

4. **Корень**: Корень может быть не один? По условию дерево укоренённое, значит корень один.
