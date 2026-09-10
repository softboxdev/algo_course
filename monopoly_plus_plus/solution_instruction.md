"Монополия++" с использованием жадного алгоритма и приоритетной очереди:

## **Решение на C++**

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct Building {
    long long cost;    // c_i — требуемый капитал
    long long profit;  // p_i — прибавка к капиталу
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    vector<Building> buildings(n);
    for (int i = 0; i < n; i++) {
        cin >> buildings[i].cost >> buildings[i].profit;
    }

    long long M;
    cin >> M;

    // Сортируем здания по требуемому капиталу (по возрастанию)
    sort(buildings.begin(), buildings.end(),
         [](const Building& a, const Building& b) {
             return a.cost < b.cost;
         });

    // Max-heap для прибылей доступных зданий
    priority_queue<long long> available;

    long long capital = M;
    int bought = 0;
    int i = 0;  // указатель на следующее нерассмотренное здание

    while (bought < k) {
        // Добавляем все здания, которые теперь доступны
        while (i < n && buildings[i].cost <= capital) {
            available.push(buildings[i].profit);
            i++;
        }

        // Если нет доступных зданий — дальше двигаться не можем
        if (available.empty()) {
            break;
        }

        // Берём здание с максимальной прибылью
        long long best_profit = available.top();
        available.pop();

        capital += best_profit;
        bought++;
    }

    cout << capital << endl;

    return 0;
}
```

---

## **Объяснение алгоритма**

### **Идея (жадный подход)**

На каждом шаге:
1. Из **всех доступных** зданий (тех, чья стоимость `c_i ≤ текущий капитал`) выбираем то, у которого **максимальная прибыль** `p_i`.
2. Покупаем его, увеличивая капитал.
3. Повторяем, пока не купим `k` зданий или пока нет доступных.

### **Почему это оптимально?**

- Покупка здания **никогда не уменьшает** капитал (`p_i ≥ 0`), поэтому покупать выгодно всегда.
- Чем больше капитал — тем больше зданий становится доступно.
- Выбирая **максимальную прибыль** среди доступных, мы максимизируем рост капитала на каждом шаге, что открывает больше возможностей в будущем.

Это классическая **жадная стратегия с приоритетной очередью**.

---

### **Пошаговая работа**

**Пример:**
```
n = 4, k = 2
Здания: (c, p)
  (5, 10)
  (3, 5)
  (8, 20)
  (2, 1)
M = 3
```

**Сортируем по `c`:**
```
(2, 1), (3, 5), (5, 10), (8, 20)
```

**Шаг 1:** капитал = 3
- Добавляем все здания с `c ≤ 3`: (2,1), (3,5)
- Очередь прибылей: [5, 1]
- Берём максимум: 5 → капитал = 3 + 5 = 8
- Куплено: 1

**Шаг 2:** капитал = 8
- Добавляем здания с `c ≤ 8`: (5,10), (8,20)
- Очередь: [20, 10, 1]
- Берём максимум: 20 → капитал = 8 + 20 = 28
- Куплено: 2

**Ответ: 28**

---

## **Почему нельзя просто отсортировать по прибыли?**

Рассмотрим контрпример:
```
k = 2, M = 0
Здания:
  (0, 1)    — доступно сразу
  (100, 100) — недоступно
  (1, 1)    — доступно после первого
```

Если бы мы сортировали по прибыли: (100,100), (0,1), (1,1).
Первое здание (100,100) недоступно, значит берём (0,1) → капитал = 1.
Теперь доступно (1,1) → капитал = 2. Итог: 2.

Если бы мы взяли (0,1), потом (1,1): капитал = 2. Тот же результат.

Но если прибыль у первого здания маленькая, а у второго большое — жадный по прибыли **среди доступных** даёт оптимум.

---

## **Сложность**

- **Сортировка**: O(n log n)
- **Основной цикл**: каждое здание добавляется в очередь один раз → O(n log n)
- **Итого**: O(n log n)
- **Память**: O(n)

---

## **Альтернативное решение с multiset**

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

struct Building {
    long long cost;
    long long profit;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    vector<Building> buildings(n);
    for (int i = 0; i < n; i++) {
        cin >> buildings[i].cost >> buildings[i].profit;
    }

    long long M;
    cin >> M;

    sort(buildings.begin(), buildings.end(),
         [](const Building& a, const Building& b) {
             return a.cost < b.cost;
         });

    // multiset для доступных прибылей (упорядочен по возрастанию)
    multiset<long long> available;

    long long capital = M;
    int bought = 0;
    int i = 0;

    while (bought < k) {
        while (i < n && buildings[i].cost <= capital) {
            available.insert(buildings[i].profit);
            i++;
        }

        if (available.empty()) break;

        // Берём максимальный элемент (последний в multiset)
        auto it = prev(available.end());
        capital += *it;
        available.erase(it);
        bought++;
    }

    cout << capital << endl;

    return 0;
}
```

---

## **Крайние случаи**

### 1. **Все здания недоступны сразу**
```
k = 3, M = 0
Здания: (5,10), (7,20), (10,30)
```
Ответ: `0` — ни одно здание нельзя купить.

### 2. **`k = n` (можно купить все)**
```
k = 3, M = 0
Здания: (0,5), (5,5), (10,5)
```
- Купим (0,5) → капитал 5
- Купим (5,5) → капитал 10
- Купим (10,5) → капитал 15

Ответ: 15.

### 3. **Одинаковые прибыли**
Работает корректно — берём любое.

### 4. **Большие числа**
Используем `long long`, так как:
- капитал может достигать `M + k * max(p) = 10^9 + 10^5 * 10^9 ≈ 10^14`
- выходит за пределы `int`.

---

## **Проверка на примере**

**Ввод:**
```
4 2
5 10
3 5
8 20
2 1
3
```

**Выполнение:**
1. Сортировка: (2,1), (3,5), (5,10), (8,20)
2. Капитал = 3, добавляем (2,1), (3,5) → очередь [5,1]
3. Берём 5 → капитал = 8, куплено 1
4. Добавляем (5,10), (8,20) → очередь [20,10,1]
5. Берём 20 → капитал = 28, куплено 2
6. Стоп (k=2)

**Вывод:** `28` ✅

---

## **Финальный ответ**

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

struct Building {
    long long cost;
    long long profit;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    vector<Building> buildings(n);
    for (int i = 0; i < n; i++) {
        cin >> buildings[i].cost >> buildings[i].profit;
    }

    long long M;
    cin >> M;

    sort(buildings.begin(), buildings.end(),
         [](const Building& a, const Building& b) {
             return a.cost < b.cost;
         });

    priority_queue<long long> available;
    long long capital = M;
    int bought = 0;
    int i = 0;

    while (bought < k) {
        while (i < n && buildings[i].cost <= capital) {
            available.push(buildings[i].profit);
            i++;
        }

        if (available.empty()) break;

        capital += available.top();
        available.pop();
        bought++;
    }

    cout << capital << endl;

    return 0;
}
```

Это решение эффективно работает за O(n log n) и корректно обрабатывает все крайние случаи.
