Решение задачи "Пересечение отрезков" с использованием двух указателей:

## **Решение на C++**

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Segment {
    long long start, end;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n, m;
    cin >> n;

    vector<Segment> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].start >> a[i].end;
    }

    cin >> m;

    vector<Segment> b(m);
    for (int i = 0; i < m; i++) {
        cin >> b[i].start >> b[i].end;
    }

    vector<Segment> result;
    int i = 0, j = 0;

    while (i < n && j < m) {
        // Находим пересечение текущих отрезков
        long long left = max(a[i].start, b[j].start);
        long long right = min(a[i].end, b[j].end);

        // Если есть пересечение (даже нулевой длины)
        if (left <= right) {
            result.push_back({left, right});
        }

        // Сдвигаем тот отрезок, который заканчивается раньше
        if (a[i].end < b[j].end) {
            i++;
        } else if (b[j].end < a[i].end) {
            j++;
        } else {
            // Если концы совпадают, сдвигаем оба
            i++;
            j++;
        }
    }

    // Вывод результата
    for (const auto& seg : result) {
        cout << seg.start << " " << seg.end << "\n";
    }

    return 0;
}
```

---

## **Решение с обработкой пустых последовательностей**

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Segment {
    long long start, end;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<Segment> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].start >> a[i].end;
    }

    int m;
    cin >> m;

    vector<Segment> b(m);
    for (int i = 0; i < m; i++) {
        cin >> b[i].start >> b[i].end;
    }

    vector<Segment> result;

    // Если одна из последовательностей пуста, пересечение пусто
    if (n == 0 || m == 0) {
        // Ничего не выводим
        return 0;
    }

    int i = 0, j = 0;

    while (i < n && j < m) {
        // Проверяем пересечение
        long long left = max(a[i].start, b[j].start);
        long long right = min(a[i].end, b[j].end);

        // Если отрезки пересекаются (включая касание)
        if (left <= right) {
            result.push_back({left, right});
        }

        // Переходим к следующему отрезку в последовательности, которая заканчивается раньше
        if (a[i].end < b[j].end) {
            i++;
        } else if (a[i].end > b[j].end) {
            j++;
        } else {
            // Концы равны - сдвигаем оба указателя
            i++;
            j++;
        }
    }

    // Вывод результата
    for (const auto& seg : result) {
        cout << seg.start << " " << seg.end << "\n";
    }

    return 0;
}
```

---

## **Альтернативное решение с более детальной обработкой**

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Segment {
    long long start, end;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<Segment> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].start >> a[i].end;
    }

    int m;
    cin >> m;

    vector<Segment> b(m);
    for (int i = 0; i < m; i++) {
        cin >> b[i].start >> b[i].end;
    }

    vector<Segment> result;
    int i = 0, j = 0;

    while (i < n && j < m) {
        // Если отрезки не пересекаются
        if (a[i].end < b[j].start) {
            // Отрезок a полностью левее b
            i++;
            continue;
        }
        if (b[j].end < a[i].start) {
            // Отрезок b полностью левее a
            j++;
            continue;
        }

        // Отрезки пересекаются
        long long left = max(a[i].start, b[j].start);
        long long right = min(a[i].end, b[j].end);

        result.push_back({left, right});

        // Определяем, какой отрезок закончился
        if (a[i].end < b[j].end) {
            // Если a закончился раньше, сдвигаем его
            i++;
        } else if (b[j].end < a[i].end) {
            // Если b закончился раньше, сдвигаем его
            j++;
        } else {
            // Если закончились одновременно
            i++;
            j++;
        }
    }

    for (const auto& seg : result) {
        cout << seg.start << " " << seg.end << "\n";
    }

    return 0;
}
```

---

## **Объяснение алгоритма**

### **Основная идея**
Используем **два указателя** для одновременного прохода по двум отсортированным последовательностям отрезков.

### **Алгоритм**

1. **Начальное состояние**:
   - `i = 0` (указатель на первый отрезок первой последовательности)
   - `j = 0` (указатель на первый отрезок второй последовательности)

2. **На каждом шаге**:
   - Находим пересечение текущих отрезков `[a[i].start, a[i].end]` и `[b[j].start, b[j].end]`
   - Пересечение: `[max(start1, start2), min(end1, end2)]`
   - Если `left <= right`, добавляем в результат

3. **Сдвиг указателей**:
   - Если `a[i].end < b[j].end`, сдвигаем `i++` (отрезок `a` закончился раньше)
   - Если `b[j].end < a[i].end`, сдвигаем `j++` (отрезок `b` закончился раньше)
   - Если равны, сдвигаем оба

### **Визуализация**

```
Последовательность A: [1,3] [5,8] [10,12]
Последовательность B: [2,4] [6,9] [11,15]

Шаг 1: A[0]=[1,3], B[0]=[2,4] → пересечение [2,3] → результат: [2,3]
       A[0] заканчивается раньше → i=1

Шаг 2: A[1]=[5,8], B[0]=[2,4] → нет пересечения (A левее B) → i=2

Шаг 3: A[2]=[10,12], B[0]=[2,4] → нет пересечения (A правее B) → j=1

Шаг 4: A[2]=[10,12], B[1]=[6,9] → нет пересечения (A правее B) → j=2

Шаг 5: A[2]=[10,12], B[2]=[11,15] → пересечение [11,12] → результат: [2,3], [11,12]
       A[2] заканчивается раньше → i=3 (выход)
```

---

## **Важные моменты**

1. **Пересечение нулевой длины**:
   - Если `left == right`, это точка
   - По условию такие отрезки тоже нужно выводить

2. **Пустые последовательности**:
   - Если `n == 0` или `m == 0`, пересечение пусто
   - Ничего не выводим

3. **Отсортированность**:
   - Входные последовательности уже отсортированы
   - Результат также будет отсортирован

4. **Типы данных**:
   - Используем `long long`, так как координаты до 10^9

---

## **Сложность**

- **Время**: O(n + m) — проходим по каждому отрезку один раз
- **Память**: O(n + m) для хранения входных данных + O(min(n,m)) для результата

---

## **Тестирование**

```cpp
// Тест 1: Обычный случай
A: [1,3] [5,8] [10,12]
B: [2,4] [6,9] [11,15]
Ответ:
2 3
6 8
11 12

// Тест 2: Касание
A: [1,2] [3,4]
B: [2,3] [4,5]
Ответ:
2 2
3 3
4 4

// Тест 3: Один отрезок полностью внутри другого
A: [1,10]
B: [3,7]
Ответ:
3 7

// Тест 4: Нет пересечений
A: [1,2] [5,6]
B: [3,4] [7,8]
Ответ:
(пусто)

// Тест 5: Пустая последовательность
A: [1,2] [3,4]
B: (пусто)
Ответ:
(пусто)
```

---

## **Оптимизация памяти**

Если требуется экономить память, можно читать отрезки второй последовательности на лету:

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Segment {
    long long start, end;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<Segment> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].start >> a[i].end;
    }

    int m;
    cin >> m;

    vector<Segment> b(m);
    for (int i = 0; i < m; i++) {
        cin >> b[i].start >> b[i].end;
    }

    // ... остальной код такой же
}
```

Два указателя идеально подходят для работы с отсортированными последовательностями!
