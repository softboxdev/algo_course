"XORошая задача" с использованием бинарного бора (trie):

## **Решение на C++ (бинарный бор / trie)**

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct TrieNode {
    int child[2];  // 0 и 1
    TrieNode() {
        child[0] = child[1] = -1;
    }
};

vector<TrieNode> trie;

void insert(int num) {
    int node = 0;
    for (int bit = 30; bit >= 0; bit--) {
        int b = (num >> bit) & 1;
        if (trie[node].child[b] == -1) {
            trie[node].child[b] = trie.size();
            trie.emplace_back();
        }
        node = trie[node].child[b];
    }
}

int query(int num) {
    int node = 0;
    int result = 0;
    for (int bit = 30; bit >= 0; bit--) {
        int b = (num >> bit) & 1;
        int want = 1 - b;  // хотим противоположный бит для максимума XOR
        if (trie[node].child[want] != -1) {
            result |= (1 << bit);
            node = trie[node].child[want];
        } else {
            node = trie[node].child[b];
        }
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Резервируем память: n * 31 узлов максимум
    trie.reserve(n * 31 + 1);
    trie.emplace_back();  // корень

    int maxXor = 0;

    // Сначала вставляем первый элемент
    insert(a[0]);

    // Для каждого следующего элемента ищем максимальный XOR с уже вставленными
    for (int i = 1; i < n; i++) {
        maxXor = max(maxXor, query(a[i]));
        insert(a[i]);
    }

    cout << maxXor << endl;

    return 0;
}
```

---

## **Объяснение алгоритма**

### **Идея: бинарный бор (trie)**

Бор — это дерево, где каждый путь от корня соответствует числу в двоичном виде.
Мы строим бор из чисел массива, а затем для каждого числа ищем **противоположные биты** — это даёт максимальный XOR.

### **Как работает XOR**

XOR двух битов равен 1, если биты **разные**:
- `0 ⊕ 0 = 0`
- `0 ⊕ 1 = 1`
- `1 ⊕ 0 = 1`
- `1 ⊕ 1 = 0`

Значит, чтобы максимизировать XOR, нужно, чтобы биты чисел **отличались**.
Чем **старше** бит, тем он **важнее** (вклад `2^bit`).

### **Жадная стратегия**

Идём от старшего бита (30) к младшему (0):
- Если у текущего числа бит `b`, хотим найти в боре число с битом `1-b`.
- Если такой путь есть — идём по нему и добавляем `2^bit` к результату.
- Иначе идём по тому же биту `b`.

### **Почему 30 бит?**

`x_i ≤ 2^31 - 1`, значит биты от 0 до 30 включительно (31 бит).
Начинаем с бита 30 (самый старший).

---

## **Пример работы**

**Массив:** `[3, 10, 5, 25, 2, 8]`

**Двоичные представления:**
```
3  = 00011
10 = 01010
5  = 00101
25 = 11001
2  = 00010
8  = 01000
```

**Пошагово:**

1. Вставляем `3` в бор.
2. Число `10`: ищем противоположные биты к `01010`.
   - Бит 4: `0` → хотим `1`. Есть? У `3` бит 4 = 0 → нет, идём по 0.
   - Бит 3: `1` → хотим `0`. У `3` бит 3 = 0 → есть! Результат += 8.
   - Бит 2: `0` → хотим `1`. У `3` бит 2 = 0 → нет.
   - Бит 1: `1` → хотим `0`. У `3` бит 1 = 1 → нет.
   - Бит 0: `0` → хотим `1`. У `3` бит 0 = 1 → есть! Результат += 1.
   - XOR(10, 3) = 8 + 1 = 9. Проверка: `10 ⊕ 3 = 9` ✅
3. Вставляем `10`.
4. Число `5`: ищем лучшее.
   - XOR(5, 3) = 6
   - XOR(5, 10) = 15 ← лучше!
   - Результат: 15.
5. ... и так далее.

**Максимум:** XOR(5, 25) = 28 или XOR(10, 25) = 19...
Проверим все: `3⊕10=9`, `3⊕5=6`, `3⊕25=26`, `3⊕2=1`, `3⊕8=11`, `10⊕5=15`, `10⊕25=19`, `10⊕2=8`, `10⊕8=2`, `5⊕25=28`, `5⊕2=7`, `5⊕8=13`, `25⊕2=27`, `25⊕8=17`, `2⊕8=10`.

**Максимум: 28** (5 ⊕ 25).

---

## **Альтернатива: вставка всех чисел сразу**

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct TrieNode {
    int child[2];
    TrieNode() { child[0] = child[1] = -1; }
};

vector<TrieNode> trie;

void insert(int num) {
    int node = 0;
    for (int bit = 30; bit >= 0; bit--) {
        int b = (num >> bit) & 1;
        if (trie[node].child[b] == -1) {
            trie[node].child[b] = trie.size();
            trie.emplace_back();
        }
        node = trie[node].child[b];
    }
}

int query(int num) {
    int node = 0, result = 0;
    for (int bit = 30; bit >= 0; bit--) {
        int b = (num >> bit) & 1;
        int want = 1 - b;
        if (trie[node].child[want] != -1) {
            result |= (1 << bit);
            node = trie[node].child[want];
        } else {
            node = trie[node].child[b];
        }
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    trie.reserve(n * 31 + 1);
    trie.emplace_back();

    // Вставляем все числа
    for (int x : a) insert(x);

    // Ищем максимум
    int maxXor = 0;
    for (int x : a) {
        maxXor = max(maxXor, query(x));
    }

    cout << maxXor << endl;
    return 0;
}
```

⚠️ Здесь `query(x)` может вернуть `x ⊕ x = 0`, если в боре только `x`. Но так как чисел ≥ 1 и мы ищем максимум, это не проблема при `n ≥ 2`. Для `n = 1` ответ 0 (XOR числа с самим собой).

---

## **Обработка `n = 1`**

Если `n = 1`, то `i = j = 1`, и `x_i ⊕ x_j = x_1 ⊕ x_1 = 0`.
Ответ: **0**.

В первом решении (вставка + запрос по одному) это обрабатывается автоматически: цикл начинается с `i = 1`, и если `n = 1`, он не выполняется, `maxXor = 0`.

---

## **Сложность**

- **Время**: O(n · 31) = O(n) — для каждого числа проходим 31 бит.
- **Память**: O(n · 31) — максимум `n · 31` узлов бора.

Для `n = 10^5`: `10^5 · 31 = 3.1 · 10^6` узлов — укладывается в 256 Мб.

---

## **Почему не работает перебор?**

Перебор всех пар — O(n²) = 10^10 операций при n = 10^5 — **слишком долго**.

Бор даёт O(n) — оптимально.

---

## **Альтернатива: сортировка + жадный поиск**

Можно отсортировать числа и искать XOR только среди «соседних» в определённом смысле, но это сложнее и не всегда корректно. **Бор — стандартное и надёжное решение.**

---

## **Финальное решение**

```cpp
#include <iostream>
#include <vector>
using namespace std;

struct TrieNode {
    int child[2];
    TrieNode() { child[0] = child[1] = -1; }
};

vector<TrieNode> trie;

void insert(int num) {
    int node = 0;
    for (int bit = 30; bit >= 0; bit--) {
        int b = (num >> bit) & 1;
        if (trie[node].child[b] == -1) {
            trie[node].child[b] = trie.size();
            trie.emplace_back();
        }
        node = trie[node].child[b];
    }
}

int query(int num) {
    int node = 0, result = 0;
    for (int bit = 30; bit >= 0; bit--) {
        int b = (num >> bit) & 1;
        int want = 1 - b;
        if (trie[node].child[want] != -1) {
            result |= (1 << bit);
            node = trie[node].child[want];
        } else {
            node = trie[node].child[b];
        }
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    trie.reserve(n * 31 + 1);
    trie.emplace_back();

    int maxXor = 0;
    insert(a[0]);

    for (int i = 1; i < n; i++) {
        maxXor = max(maxXor, query(a[i]));
        insert(a[i]);
    }

    cout << maxXor << endl;
    return 0;
}
```

Это решение:
- ✅ Работает за O(n)
- ✅ Использует бинарный бор (trie) для жадного поиска
- ✅ Корректно обрабатывает `n = 1` (ответ 0)
- ✅ Эффективно по памяти (reserve + emplace_back)
