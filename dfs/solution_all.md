
---

## 📋 ВАРИАНТ 1: DFS + ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ (САМЫЙ ЧИТАЕМЫЙ)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Глобальные переменные для доступа из dfs
int n, m;
vector<vector<int>> matrix;
vector<vector<int>> dp;

// Направления: вверх, вниз, влево, вправо
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int dfs(int x, int y) {
    // Если уже посчитали — возвращаем
    if (dp[x][y] != -1) {
        return dp[x][y];
    }
    
    // Минимальная длина — 1 (сама клетка)
    dp[x][y] = 1;
    
    // Проверяем всех 4 соседей
    for (int d = 0; d < 4; ++d) {
        int nx = x + dx[d];
        int ny = y + dy[d];
        
        // Проверяем границы
        if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
            continue;
        }
        
        // Идём только в бóльшую клетку (строгое возрастание)
        if (matrix[nx][ny] > matrix[x][y]) {
            dp[x][y] = max(dp[x][y], 1 + dfs(nx, ny));
        }
    }
    
    return dp[x][y];
}

int getLongestIncreasingPath(int n_, int m_, const vector<vector<int>>& matrixs) {
    n = n_;
    m = m_;
    matrix = matrixs;
    
    // Инициализируем dp значением -1 (ещё не считали)
    dp.assign(n, vector<int>(m, -1));
    
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            ans = max(ans, dfs(i, j));
        }
    }
    
    return ans;
}

int readInt() {
    int x;
    cin >> x;
    return x;
}

vector<int> readList(int n) {
    vector<int> res(n);
    for (int i = 0; i < n; i++) {
        cin >> res[i];
    }
    return res;
}

vector<vector<int>> readMatrix(int n, int m) {
    vector<vector<int>> matrix(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        matrix[i] = readList(m);
    }
    return matrix;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> matrix = readMatrix(n, m);
    cout << getLongestIncreasingPath(n, m, matrix);
}
```

---

## 📋 ВАРИАНТ 2: ВСЁ В ОДНОЙ ФУНКЦИИ (БЕЗ ГЛОБАЛЬНЫХ)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int getLongestIncreasingPath(int n, int m, const vector<vector<int>>& matrixs) {
    // Создаём копию матрицы
    vector<vector<int>> matrix = matrixs;
    
    // dp[i][j] — длина пути из клетки (i,j)
    vector<vector<int>> dp(n, vector<int>(m, -1));
    
    // Направления
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    
    // Рекурсивная функция (лямбда с захватом ссылок)
    function<int(int,int)> dfs = [&](int x, int y) -> int {
        if (dp[x][y] != -1) {
            return dp[x][y];
        }
        
        dp[x][y] = 1;
        
        for (int d = 0; d < 4; ++d) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                continue;
            }
            
            if (matrix[nx][ny] > matrix[x][y]) {
                dp[x][y] = max(dp[x][y], 1 + dfs(nx, ny));
            }
        }
        
        return dp[x][y];
    };
    
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            ans = max(ans, dfs(i, j));
        }
    }
    
    return ans;
}

int readInt() {
    int x;
    cin >> x;
    return x;
}

vector<int> readList(int n) {
    vector<int> res(n);
    for (int i = 0; i < n; i++) {
        cin >> res[i];
    }
    return res;
}

vector<vector<int>> readMatrix(int n, int m) {
    vector<vector<int>> matrix(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        matrix[i] = readList(m);
    }
    return matrix;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> matrix = readMatrix(n, m);
    cout << getLongestIncreasingPath(n, m, matrix);
}
```

---

## 📋 ВАРИАНТ 3: С СОРТИРОВКОЙ (БЕЗ РЕКУРСИИ)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Cell {
    int x, y, val;
};

int getLongestIncreasingPath(int n, int m, const vector<vector<int>>& matrixs) {
    vector<vector<int>> matrix = matrixs;
    
    // Собираем все клетки
    vector<Cell> cells;
    cells.reserve(n * m);
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cells.push_back({i, j, matrix[i][j]});
        }
    }
    
    // Сортируем по убыванию (от больших к меньшим)
    sort(cells.begin(), cells.end(), [](const Cell& a, const Cell& b) {
        return a.val > b.val;
    });
    
    // dp[i][j] = длина пути из клетки (i,j)
    vector<vector<int>> dp(n, vector<int>(m, 1));
    
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    
    int ans = 0;
    
    // Проходим от больших к меньшим
    for (const Cell& cell : cells) {
        int x = cell.x;
        int y = cell.y;
        
        for (int d = 0; d < 4; ++d) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                continue;
            }
            
            // Если сосед больше — обновляем
            if (matrix[nx][ny] > matrix[x][y]) {
                dp[x][y] = max(dp[x][y], 1 + dp[nx][ny]);
            }
        }
        
        ans = max(ans, dp[x][y]);
    }
    
    return ans;
}

int readInt() {
    int x;
    cin >> x;
    return x;
}

vector<int> readList(int n) {
    vector<int> res(n);
    for (int i = 0; i < n; i++) {
        cin >> res[i];
    }
    return res;
}

vector<vector<int>> readMatrix(int n, int m) {
    vector<vector<int>> matrix(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        matrix[i] = readList(m);
    }
    return matrix;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> matrix = readMatrix(n, m);
    cout << getLongestIncreasingPath(n, m, matrix);
}
```

---

## 📋 ВАРИАНТ 4: САМЫЙ КОРОТКИЙ

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int dp[205][205];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int getLongestIncreasingPath(int n, int m, const vector<vector<int>>& matrixs) {
    vector<vector<int>> matrix = matrixs;
    
    // Обнуляем dp
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            dp[i][j] = 0;
        }
    }
    
    // Лямбда с захватом всех переменных
    function<int(int,int)> dfs = [&](int x, int y) -> int {
        if (dp[x][y]) return dp[x][y];
        dp[x][y] = 1;
        
        for (int d = 0; d < 4; ++d) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                continue;
            }
            
            if (matrix[nx][ny] > matrix[x][y]) {
                dp[x][y] = max(dp[x][y], 1 + dfs(nx, ny));
            }
        }
        
        return dp[x][y];
    };
    
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            ans = max(ans, dfs(i, j));
        }
    }
    
    return ans;
}

int readInt() {
    int x;
    cin >> x;
    return x;
}

vector<int> readList(int n) {
    vector<int> res(n);
    for (int i = 0; i < n; i++) {
        cin >> res[i];
    }
    return res;
}

vector<vector<int>> readMatrix(int n, int m) {
    vector<vector<int>> matrix(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        matrix[i] = readList(m);
    }
    return matrix;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> matrix = readMatrix(n, m);
    cout << getLongestIncreasingPath(n, m, matrix);
}
```

---

## 📊 СРАВНЕНИЕ ВАРИАНТОВ

| Вариант | Рекурсия | Код | Сложность |
|---------|----------|-----|-----------|
| **1. Глобальные переменные** | ✅ Да | ⭐⭐ | O(n·m) |
| **2. В одной функции** | ✅ Да | ⭐⭐⭐ | O(n·m) |
| **3. Сортировка** | ❌ Нет | ⭐⭐⭐⭐ | O(n·m·log(n·m)) |
| **4. Самый короткий** | ✅ Да | ⭐ | O(n·m) |

---

## 🎯 РЕКОМЕНДАЦИЯ

**Используйте ВАРИАНТ 1 (с глобальными переменными):**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;
vector<vector<int>> matrix;
vector<vector<int>> dp;
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

int dfs(int x, int y) {
    if (dp[x][y] != -1) return dp[x][y];
    dp[x][y] = 1;
    for (int d = 0; d < 4; ++d) {
        int nx = x + dx[d], ny = y + dy[d];
        if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
        if (matrix[nx][ny] > matrix[x][y]) {
            dp[x][y] = max(dp[x][y], 1 + dfs(nx, ny));
        }
    }
    return dp[x][y];
}

int getLongestIncreasingPath(int n_, int m_, const vector<vector<int>>& matrixs) {
    n = n_; m = m_; matrix = matrixs;
    dp.assign(n, vector<int>(m, -1));
    int ans = 0;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            ans = max(ans, dfs(i, j));
    return ans;
}

int readInt() { int x; cin >> x; return x; }
vector<int> readList(int n) { vector<int> res(n); for (int i = 0; i < n; i++) cin >> res[i]; return res; }
vector<vector<int>> readMatrix(int n, int m) { vector<vector<int>> matrix(n, vector<int>(m)); for (int i = 0; i < n; i++) matrix[i] = readList(m); return matrix; }

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> matrix = readMatrix(n, m);
    cout << getLongestIncreasingPath(n, m, matrix);
}
```

---

**Все решения адаптированы строго под шаблон!** 🚀