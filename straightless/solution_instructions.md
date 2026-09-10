"Прямота" с проверкой коллинеарности через векторное произведение:

## **Решение на C++**

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Point {
    long long x, y;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<Point> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].x >> points[i].y;
    }

    // Находим первую точку, отличную от points[0]
    int idx = 1;
    while (idx < n && points[idx].x == points[0].x && points[idx].y == points[0].y) {
        idx++;
    }

    // Если все точки совпадают — они на одной прямой
    if (idx == n) {
        cout << "YES" << endl;
        return 0;
    }

    // Вектор направления от points[0] к points[idx]
    long long dx = points[idx].x - points[0].x;
    long long dy = points[idx].y - points[0].y;

    // Проверяем все остальные точки на коллинеарность
    for (int i = 0; i < n; i++) {
        // Вектор от points[0] к points[i]
        long long vx = points[i].x - points[0].x;
        long long vy = points[i].y - points[0].y;

        // Векторное произведение должно быть 0 для коллинеарных векторов
        // dx * vy - dy * vx == 0
        if (dx * vy - dy * vx != 0) {
            cout << "NO" << endl;
            return 0;
        }
    }

    cout << "YES" << endl;
    return 0;
}
```

---

## **Объяснение алгоритма**

### **Идея: векторное произведение**

Три точки `A`, `B`, `C` лежат на одной прямой **тогда и только тогда**, когда векторы `AB` и `AC` **коллинеарны**.

Для двух векторов `(dx1, dy1)` и `(dx2, dy2)` условие коллинеарности:
```
dx1 * dy2 - dy1 * dx2 == 0
```

Это **векторное произведение** (cross product) в 2D, которое равно нулю для коллинеарных векторов.

### **Пошаговый алгоритм**

1. **Выбираем базовую точку** — `points[0]`.
2. **Находим вторую точку**, отличную от первой: `points[idx]`.
   - Если все точки совпадают — ответ `YES` (все на одной прямой, тривиально).
3. **Строим вектор направления** `(dx, dy) = points[idx] - points[0]`.
4. **Проверяем каждую точку** `points[i]`:
   - Строим вектор `(vx, vy) = points[i] - points[0]`.
   - Если `dx * vy - dy * vx != 0` — точка не на прямой → `NO`.
5. Если все точки прошли проверку → `YES`.

---

## **Почему нельзя делить на `dx` или `dy`?**

Наивный подход: проверить `(y_i - y_0) / (x_i - x_0) == dy / dx`.
**Проблема:** деление на ноль (вертикальная прямая) и **потеря точности** при работе с большими числами.

Векторное произведение работает с **целыми числами** и корректно обрабатывает вертикальные прямые.

---

## **Важно: тип данных**

Координаты до `10^12`, значит:
- `dx, dy` до `2 * 10^12`
- `dx * vy` до `4 * 10^24` — **не помещается** в `long long` (макс ~9.2 * 10^18)

**Решение:** использовать `__int128` (GCC/Clang) для произведения.

### **Исправленное решение с `__int128`**

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Point {
    long long x, y;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<Point> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].x >> points[i].y;
    }

    // Находим первую точку, отличную от points[0]
    int idx = 1;
    while (idx < n && points[idx].x == points[0].x && points[idx].y == points[0].y) {
        idx++;
    }

    if (idx == n) {
        cout << "YES" << endl;
        return 0;
    }

    long long dx = points[idx].x - points[0].x;
    long long dy = points[idx].y - points[0].y;

    for (int i = 0; i < n; i++) {
        long long vx = points[i].x - points[0].x;
        long long vy = points[i].y - points[0].y;

        // Используем __int128 для избежания переполнения
        __int128 cross = (__int128)dx * vy - (__int128)dy * vx;

        if (cross != 0) {
            cout << "NO" << endl;
            return 0;
        }
    }

    cout << "YES" << endl;
    return 0;
}
```

---

## **Альтернатива без `__int128`: нормализация вектора**

Можно сократить вектор `(dx, dy)` на НОД и проверять коллинеарность через нормализованные векторы:

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <cstdlib>
using namespace std;

struct Point {
    long long x, y;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<Point> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].x >> points[i].y;
    }

    int idx = 1;
    while (idx < n && points[idx].x == points[0].x && points[idx].y == points[0].y) {
        idx++;
    }

    if (idx == n) {
        cout << "YES" << endl;
        return 0;
    }

    long long dx = points[idx].x - points[0].x;
    long long dy = points[idx].y - points[0].y;

    // Нормализуем вектор направления
    long long g = gcd(abs(dx), abs(dy));
    dx /= g;
    dy /= g;

    // Приводим знак: делаем dx > 0 или (dx == 0 и dy > 0)
    if (dx < 0 || (dx == 0 && dy < 0)) {
        dx = -dx;
        dy = -dy;
    }

    for (int i = 0; i < n; i++) {
        long long vx = points[i].x - points[0].x;
        long long vy = points[i].y - points[0].y;

        if (vx == 0 && vy == 0) continue;  // совпадает с базовой

        long long g2 = gcd(abs(vx), abs(vy));
        vx /= g2;
        vy /= g2;

        if (vx < 0 || (vx == 0 && vy < 0)) {
            vx = -vx;
            vy = -vy;
        }

        if (vx != dx || vy != dy) {
            cout << "NO" << endl;
            return 0;
        }
    }

    cout << "YES" << endl;
    return 0;
}
```

⚠️ **Минус:** медленнее из-за GCD на каждой итерации. O(n log C).

---

## **Сложность**

| Подход | Время | Память |
|--------|-------|--------|
| **Векторное произведение + `__int128`** | O(n) | O(n) |
| **Нормализация через GCD** | O(n log C) | O(n) |

Первый подход быстрее — **O(n)**.

---

## **Примеры**

### Пример 1
```
Ввод:
3
0 0
1 1
2 2

Вывод: YES
```
Все точки на прямой `y = x`.

### Пример 2
```
Ввод:
3
0 0
1 1
2 3

Вывод: NO
```
Точка `(2,3)` не на прямой `y = x`.

### Пример 3 (все точки совпадают)
```
Ввод:
3
5 5
5 5
5 5

Вывод: YES
```
Тривиальный случай.

### Пример 4 (вертикальная прямая)
```
Ввод:
3
1 0
1 5
1 100

Вывод: YES
```
Все точки на прямой `x = 1`.

### Пример 5 (совпадающие + на прямой)
```
Ввод:
4
0 0
0 0
1 1
2 2

Вывод: YES
```

---

## **Крайние случаи**

1. **`n = 2`** — всегда `YES` (любые две точки лежат на одной прямой).

2. **Все точки совпадают** — `YES`.

3. **Вертикальная прямая** — `dx = 0`, `dy ≠ 0`.
   Векторное произведение: `0 * vy - dy * vx = -dy * vx`.
   Равно нулю только если `vx = 0`, т.е. все точки имеют одинаковый `x`. ✅

4. **Горизонтальная прямая** — `dy = 0`, `dx ≠ 0`.
   Аналогично работает.

5. **Первая и вторая точки совпадают** — ищем следующую отличную.

---

## **Финальное решение**

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct Point {
    long long x, y;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<Point> points(n);
    for (int i = 0; i < n; i++) {
        cin >> points[i].x >> points[i].y;
    }

    // Ищем первую точку, отличную от points[0]
    int idx = 1;
    while (idx < n && points[idx].x == points[0].x && points[idx].y == points[0].y) {
        idx++;
    }

    // Все точки совпадают
    if (idx == n) {
        cout << "YES\n";
        return 0;
    }

    long long dx = points[idx].x - points[0].x;
    long long dy = points[idx].y - points[0].y;

    for (int i = 0; i < n; i++) {
        long long vx = points[i].x - points[0].x;
        long long vy = points[i].y - points[0].y;

        __int128 cross = (__int128)dx * vy - (__int128)dy * vx;

        if (cross != 0) {
            cout << "NO\n";
            return 0;
        }
    }

    cout << "YES\n";
    return 0;
}
```

Это решение:
- ✅ Работает за O(n)
- ✅ Корректно обрабатывает большие координаты (до 10^12)
- ✅ Работает с совпадающими точками
- ✅ Работает с вертикальными и горизонтальными прямыми
- ✅ Не использует деление (нет проблем с точностью)
