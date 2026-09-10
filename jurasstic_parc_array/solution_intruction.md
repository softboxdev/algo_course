
## **Оптимальное решение: персистентный массив с использованием "толстых" узлов**

```cpp
#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, q;
    cin >> n >> q;

    // Для каждого индекса храним историю изменений: (время, значение)
    // Время - это номер операции set (или момент, когда эра закончилась)
    vector<vector<pair<int, long long>>> history(n);

    // Для каждой эры храним время её окончания
    map<int, int> era_end_time;  // era_id -> номер операции, когда эра закончилась

    int current_era = 0;
    int set_count = 0;  // Счётчик операций set

    // Сначала прочитаем все операции и построим историю
    struct Op {
        string type;
        int index;
        long long value;
    };
    vector<Op> ops(q);

    for (int i = 0; i < q; i++) {
        cin >> ops[i].type;
        if (ops[i].type == "set") {
            cin >> ops[i].index >> ops[i].value;
        } else if (ops[i].type == "begin_new_era") {
            cin >> ops[i].value;
        } else {
            cin >> ops[i].index >> ops[i].value;
        }
    }

    // Обрабатываем операции, строим историю
    current_era = 0;
    set_count = 0;

    for (int i = 0; i < q; i++) {
        if (ops[i].type == "set") {
            int idx = ops[i].index;
            long long val = ops[i].value;
            history[idx].push_back({set_count, val});
            set_count++;
        } else if (ops[i].type == "begin_new_era") {
            // Завершаем текущую эру
            era_end_time[current_era] = set_count;  // эра закончилась после set_count операций set
            current_era = ops[i].value;
        }
    }
    era_end_time[current_era] = set_count;  // последняя эра

    // Теперь обрабатываем get запросы
    for (int i = 0; i < q; i++) {
        if (ops[i].type == "get") {
            int idx = ops[i].index;
            int era_id = ops[i].value;

            // Находим время окончания эры
            int end_time = era_end_time[era_id];

            // Ищем последнее значение в history[idx], которое было установлено до end_time
            long long result = 0;  // по умолчанию 0

            // Бинарный поиск по history[idx]
            auto& h = history[idx];
            int lo = 0, hi = h.size() - 1;
            int best = -1;

            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                if (h[mid].first < end_time) {
                    best = mid;
                    lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }

            if (best != -1) {
                result = h[best].second;
            }

            cout << result << "\n";
        }
    }

    return 0;
}
```

---

## **Объяснение оптимального решения**

### **Идея**

1. **История изменений**: Для каждого индекса массива храним список пар `(время, значение)`, где время — это порядковый номер операции `set`.

2. **Время окончания эры**: Для каждой эры запоминаем, после какого количества операций `set` она закончилась.

3. **Запрос get**:
   - Находим время окончания эры `end_time`
   - В истории изменений индекса ищем последнее значение, установленное **до** `end_time`
   - Используем бинарный поиск для эффективности

### **Пример работы**

```
n = 3, операции:
set 0 5
set 1 10
begin_new_era 1
set 0 7
begin_new_era 2
get 0 1    <- эра 1 закончилась после 2-х set
get 0 2    <- эра 2 закончилась после 3-х set
```

**История:**
- Индекс 0: [(0, 5), (2, 7)]  (set #0: 5, set #2: 7)
- Индекс 1: [(1, 10)]

**Время окончания эр:**
- Эра 0: закончилась после 2 set (begin_new_era 1)
- Эра 1: закончилась после 3 set (begin_new_era 2)
- Эра 2: закончилась после 3 set (конец)

**Запросы:**
- `get 0 1`: end_time = 3, ищем в истории индекса 0 последнее значение до времени 3 → (2, 7) → **7**
- `get 0 2`: end_time = 3, ищем в истории индекса 0 последнее значение до времени 3 → (2, 7) → **7**

---

## **Сложность**

- **Время**:
  - Построение истории: O(q)
  - Каждый get: O(log q) на бинарный поиск
  - Итого: O(q log q)
- **Память**: O(q) — храним только изменения

---

## **Важные моменты**

1. **Начальное значение**: 0 (по умолчанию)
2. **Время окончания эры**: это количество операций `set`, выполненных до начала следующей эры
3. **Бинарный поиск**: ищем последнее значение с временем `< end_time`
4. **Гарантия**: при запросе `get` эра уже закончилась

---

## **Тестирование**

```cpp
// Тест 1
n = 3
q = 6
set 0 5
set 1 10
begin_new_era 1
set 0 7
begin_new_era 2
get 0 1

// История:
// idx 0: [(0, 5), (2, 7)]
// idx 1: [(1, 10)]
// era_end_time: {0: 2, 1: 3, 2: 3}

// get 0 1: end_time=3, ищем < 3 в idx 0 → (2,7) → 7
// Вывод: 7
```

Это решение эффективно использует память и время, подходя для ограничений n, q ≤ 10^5.
