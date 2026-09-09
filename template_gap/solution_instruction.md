Решение задачи "Разрыв шаблона" с использованием динамического программирования:

## **Решение на C++ (DP)**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool matchPattern(const string& pattern, const string& text) {
    int n = pattern.size();
    int m = text.size();

    // dp[i][j] = можно ли сопоставить первые i символов шаблона с первыми j символами строки
    vector<vector<bool>> dp(n + 1, vector<bool>(m + 1, false));
    dp[0][0] = true;  // Пустой шаблон соответствует пустой строке

    // Обработка шаблона, состоящего только из '*'
    for (int i = 1; i <= n; i++) {
        if (pattern[i - 1] == '*') {
            dp[i][0] = dp[i - 1][0];
        }
    }

    // Заполнение таблицы DP
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            char p = pattern[i - 1];
            char t = text[j - 1];

            if (p == '*') {
                // '*' может соответствовать пустой строке или одному или более символам
                dp[i][j] = dp[i - 1][j]   // '*' соответствует пустой строке
                        || dp[i][j - 1];  // '*' соответствует одному символу
            } else if (p == '?' || p == t) {
                // '?' или точное совпадение
                dp[i][j] = dp[i - 1][j - 1];
            }
            // Иначе dp[i][j] остается false
        }
    }

    return dp[n][m];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string pattern, text;
    cin >> pattern >> text;

    cout << (matchPattern(pattern, text) ? "YES" : "NO") << endl;

    return 0;
}
```

---

## **Оптимизированное решение с одномерным DP**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool matchPattern(const string& pattern, const string& text) {
    int n = pattern.size();
    int m = text.size();

    // Используем одномерный массив для экономии памяти
    vector<bool> dp(m + 1, false);
    vector<bool> prev(m + 1, false);

    prev[0] = true;

    for (int i = 1; i <= n; i++) {
        char p = pattern[i - 1];
        dp[0] = (p == '*') && prev[0];  // '*' может соответствовать пустой строке

        for (int j = 1; j <= m; j++) {
            char t = text[j - 1];

            if (p == '*') {
                dp[j] = prev[j] || dp[j - 1];
            } else if (p == '?' || p == t) {
                dp[j] = prev[j - 1];
            } else {
                dp[j] = false;
            }
        }

        swap(dp, prev);
        fill(dp.begin(), dp.end(), false);
    }

    return prev[m];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string pattern, text;
    cin >> pattern >> text;

    cout << (matchPattern(pattern, text) ? "YES" : "NO") << endl;

    return 0;
}
```

---

## **Объяснение алгоритма**

### **Основная идея (DP)**

Используем динамическое программирование:
- `dp[i][j]` = true, если первые `i` символов шаблона соответствуют первым `j` символам строки

### **Переходы**

1. **Если `pattern[i-1] == '*'`**:
   - `dp[i][j] = dp[i-1][j]` — '*' соответствует пустой строке
   - `dp[i][j] = dp[i][j-1]` — '*' соответствует одному символу

2. **Если `pattern[i-1] == '?'`**:
   - `dp[i][j] = dp[i-1][j-1]` — '?' соответствует любому одному символу

3. **Если `pattern[i-1] == text[j-1]`**:
   - `dp[i][j] = dp[i-1][j-1]` — точное совпадение

### **Пример работы**

**Шаблон:** `a*b`
**Строка:** `acb`

| | 0 | a | c | b |
|---|---|---|---|---|
| **0** | T | F | F | F |
| **a** | F | T | F | F |
| ***** | T | T | T | T |
| **b** | F | F | F | T |

Ответ: YES

---

## **Вариант с рекурсией и мемоизацией**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string pattern, text;
vector<vector<int>> memo;  // -1 не посещено, 0 false, 1 true

bool dfs(int i, int j) {
    // Базовые случаи
    if (i == pattern.size() && j == text.size()) return true;
    if (i == pattern.size()) return false;
    if (j == text.size()) {
        // Шаблон должен состоять только из '*'
        while (i < pattern.size() && pattern[i] == '*') i++;
        return i == pattern.size();
    }

    if (memo[i][j] != -1) return memo[i][j];

    bool result = false;

    if (pattern[i] == '*') {
        // '*' может соответствовать пустой строке или одному символу
        result = dfs(i + 1, j) || dfs(i, j + 1);
    } else if (pattern[i] == '?' || pattern[i] == text[j]) {
        result = dfs(i + 1, j + 1);
    }

    memo[i][j] = result ? 1 : 0;
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> pattern >> text;

    memo.assign(pattern.size(), vector<int>(text.size(), -1));

    cout << (dfs(0, 0) ? "YES" : "NO") << endl;

    return 0;
}
```

---

## **Сравнение подходов**

| Подход | Время | Память | Сложность кода | Когда использовать |
|--------|-------|--------|----------------|-------------------|
| **2D DP** | O(n*m) | O(n*m) | ⭐⭐⭐ | n,m ≤ 2000 |
| **1D DP** | O(n*m) | O(m) | ⭐⭐⭐⭐ | n,m ≤ 2000 (экономия памяти) |
| **Двухстороннее сканирование** | O(n+m) | O(1) | ⭐⭐⭐⭐⭐ | Только если одна '*' |
| **Рекурсия с мемоизацией** | O(n*m) | O(n*m) | ⭐⭐ | Простота понимания |

---

## **Важные моменты**

1. **Обработка '*'**:
   - Может соответствовать **пустой строке**
   - Может соответствовать **одному или более символам**

2. **Крайние случаи**:
   - `"*"` и `""` → YES (пустая строка)
   - `"*"` и `"abc"` → YES
   - `"a*"` и `""` → NO
   - `"a*"` и `"a"` → YES

3. **Оптимизации**:
   - Можно сжать несколько подряд идущих `*` в один
   - Можно использовать двухстороннее сканирование для одного `*`

---

## **Тестирование**

```cpp
// Тест 1
pattern = "a?b"
text = "acb"
Ответ: YES

// Тест 2
pattern = "a*b"
text = "ab"
Ответ: YES

// Тест 3
pattern = "a*b"
text = "acb"
Ответ: YES

// Тест 4
pattern = "a*b"
text = "abc"
Ответ: NO

// Тест 5
pattern = "*"
text = "hello"
Ответ: YES

// Тест 6
pattern = "*a*b"
text = "acb"
Ответ: YES (a и b есть)
```

Рекомендую использовать **1D DP** как хороший баланс между производительностью и читаемостью кода.
