Решение задачи Сизиф. Это классическая задача на **оптимальное объединение камней** (аналог задачи Хаффмана). Нужно использовать **приоритетную очередь** (min-heap).

## **Решение на C++**

```cpp
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    // Минимальная куча (priority_queue по умолчанию - max-heap)
    // Используем greater<int> для min-heap
    priority_queue<long long, vector<long long>, greater<long long>> pq;

    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        pq.push(x);
    }

    long long total_energy = 0;

    // Пока есть хотя бы две кучки
    while (pq.size() > 1) {
        // Берём две самые маленькие кучки
        long long a = pq.top();
        pq.pop();
        long long b = pq.top();
        pq.pop();

        // Объединяем их
        long long sum = a + b;
        total_energy += sum;

        // Кладём объединённую кучку обратно
        pq.push(sum);
    }

    cout << total_energy << endl;

    return 0;
}
```

---

## **Альтернативное решение с вектором и сортировкой**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    priority_queue<long long, vector<long long>, greater<long long>> pq;

    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        pq.push(x);
    }

    long long total_energy = 0;

    while (pq.size() > 1) {
        long long a = pq.top();
        pq.pop();
        long long b = pq.top();
        pq.pop();

        long long new_pile = a + b;
        total_energy += new_pile;
        pq.push(new_pile);
    }

    cout << total_energy << endl;

    return 0;
}
```

---

## **Решение с использованием multiset (альтернативный подход)**

```cpp
#include <iostream>
#include <set>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    multiset<long long> ms;

    for (int i = 0; i < n; i++) {
        long long x;
        cin >> x;
        ms.insert(x);
    }

    long long total_energy = 0;

    while (ms.size() > 1) {
        // Берём два наименьших элемента
        auto it1 = ms.begin();
        long long a = *it1;
        ms.erase(it1);

        auto it2 = ms.begin();
        long long b = *it2;
        ms.erase(it2);

        long long sum = a + b;
        total_energy += sum;
        ms.insert(sum);
    }

    cout << total_energy << endl;

    return 0;
}
```

---

## **Объяснение алгоритма**

### **Почему нужно брать две самые маленькие кучки?**

Это оптимальная стратегия, аналогичная **алгоритму Хаффмана**:

1. **Жадный подход**: На каждом шаге объединяем две **самые маленькие** кучки.
2. **Доказательство**: Если есть две кучки `a ≤ b` и мы не объединяем их вместе, а объединяем `a` с другой кучкой `c` (где `c ≥ b`), то можно улучшить результат, поменяв местами.

### **Пример работы**

**Вход:**
```
5
1 2 3 4 5
```

**Пошагово:**
1. Берём 1 и 2 → сумма = 3, энергия = 3
   - Кучки: 3, 3, 4, 5
2. Берём 3 и 3 → сумма = 6, энергия = 3 + 6 = 9
   - Кучки: 4, 5, 6
3. Берём 4 и 5 → сумма = 9, энергия = 9 + 9 = 18
   - Кучки: 6, 9
4. Берём 6 и 9 → сумма = 15, энергия = 18 + 15 = 33

**Ответ: 33**

---

## **Важные моменты**

1. **Тип данных**: Используем `long long`, так как:
   - Максимальное значение: `n * max_weight = 10^5 * 10^6 = 10^11`
   - Это выходит за пределы `int` (2^31 - 1 ≈ 2.1 * 10^9)

2. **Приоритетная очередь**:
   - `priority_queue<long long, vector<long long>, greater<long long>>` — это **min-heap**
   - Без `greater` это был бы max-heap, что не подходит

3. **Сложность**:
   - Время: O(n log n) — каждое объединение требует O(log n)
   - Память: O(n)

4. **Крайние случаи**:
   - `n = 1`: ответ 0 (не нужно объединять)
   - Все веса одинаковые: работает корректно

---

## **Сравнение подходов**

| Подход | Преимущества | Недостатки |
|--------|--------------|------------|
| **priority_queue** | • Быстрый доступ к минимуму<br>• Стандартное решение | • Нужно запомнить синтаксис min-heap |
| **multiset** | • Простой синтаксис<br>• Легко понять | • Медленнее (но всё равно O(log n))<br>• Больше памяти |
| **sort + deque** | • Можно для маленьких n | • Не подходит для n = 10^5 |

---

## **Почему это похоже на "Сизиф"?**

Название отсылает к мифу о Сизифе, который вечно вкатывает камень на гору. Здесь мы "перекатываем" камни, объединяя их, и каждый раз тратим энергию, равную весу новой кучки.

Чем больше камней мы объединяем, тем больше энергии тратится, поэтому оптимально сначала объединять самые лёгкие камни, чтобы тяжёлые камни "поднимались" (объединялись) как можно меньше раз.
