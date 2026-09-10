"По ip вычислю" без использования регулярных выражений:

## **Решение на C++**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Проверка, является ли символ цифрой
bool isDigit(char c) {
    return c >= '0' && c <= '9';
}

// Проверка, является ли символ hex-цифрой
bool isHexDigit(char c) {
    return (c >= '0' && c <= '9') ||
           (c >= 'a' && c <= 'f') ||
           (c >= 'A' && c <= 'F');
}

// Проверка IPv4
bool isIPv4(const string& s) {
    // Разбиваем по точкам
    vector<string> parts;
    string current;

    for (char c : s) {
        if (c == '.') {
            parts.push_back(current);
            current.clear();
        } else {
            current += c;
        }
    }
    parts.push_back(current);

    // Должно быть ровно 4 части
    if (parts.size() != 4) return false;

    for (const string& part : parts) {
        // Часть не может быть пустой
        if (part.empty()) return false;

        // Только цифры
        for (char c : part) {
            if (!isDigit(c)) return false;
        }

        // Нет лидирующих нулей (кроме самого "0")
        if (part.size() > 1 && part[0] == '0') return false;

        // Длина не больше 3
        if (part.size() > 3) return false;

        // Значение от 0 до 255
        int value = 0;
        for (char c : part) {
            value = value * 10 + (c - '0');
        }
        if (value > 255) return false;
    }

    return true;
}

// Проверка IPv6
bool isIPv6(const string& s) {
    // Разбиваем по двоеточиям
    vector<string> parts;
    string current;

    for (char c : s) {
        if (c == ':') {
            parts.push_back(current);
            current.clear();
        } else {
            current += c;
        }
    }
    parts.push_back(current);

    // Должно быть ровно 8 частей
    if (parts.size() != 8) return false;

    for (const string& part : parts) {
        // Часть не может быть пустой
        if (part.empty()) return false;

        // Длина не больше 4
        if (part.size() > 4) return false;

        // Только hex-цифры
        for (char c : part) {
            if (!isHexDigit(c)) return false;
        }
    }

    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string s;
    cin >> s;

    // Проверяем: IPv4, IPv6 или ошибка
    // Важно: строка не может быть одновременно IPv4 и IPv6,
    // так как IPv4 содержит точки, IPv6 — двоеточия

    bool hasDot = false, hasColon = false;
    for (char c : s) {
        if (c == '.') hasDot = true;
        if (c == ':') hasColon = true;
    }

    if (hasDot && hasColon) {
        cout << "Error" << endl;
        return 0;
    }

    if (hasDot) {
        cout << (isIPv4(s) ? "IPv4" : "Error") << endl;
    } else if (hasColon) {
        cout << (isIPv6(s) ? "IPv6" : "Error") << endl;
    } else {
        cout << "Error" << endl;
    }

    return 0;
}
```

---

## **Альтернативное решение (более компактное)**

```cpp
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

bool isIPv4(const string& s) {
    int partCount = 0;
    int i = 0;
    int n = s.size();

    while (i < n) {
        // Считываем часть до точки
        int start = i;
        while (i < n && s[i] != '.') i++;

        string part = s.substr(start, i - start);

        // Проверки
        if (part.empty()) return false;
        if (part.size() > 3) return false;
        if (part.size() > 1 && part[0] == '0') return false;

        int value = 0;
        for (char c : part) {
            if (c < '0' || c > '9') return false;
            value = value * 10 + (c - '0');
        }
        if (value > 255) return false;

        partCount++;

        if (i < n) i++;  // пропускаем точку
    }

    return partCount == 4;
}

bool isIPv6(const string& s) {
    int partCount = 0;
    int i = 0;
    int n = s.size();

    while (i < n) {
        int start = i;
        while (i < n && s[i] != ':') i++;

        string part = s.substr(start, i - start);

        if (part.empty()) return false;
        if (part.size() > 4) return false;

        for (char c : part) {
            bool ok = (c >= '0' && c <= '9') ||
                      (c >= 'a' && c <= 'f') ||
                      (c >= 'A' && c <= 'F');
            if (!ok) return false;
        }

        partCount++;

        if (i < n) i++;
    }

    return partCount == 8;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string s;
    cin >> s;

    bool hasDot = s.find('.') != string::npos;
    bool hasColon = s.find(':') != string::npos;

    if (hasDot && hasColon) {
        cout << "Error" << endl;
    } else if (hasDot) {
        cout << (isIPv4(s) ? "IPv4" : "Error") << endl;
    } else if (hasColon) {
        cout << (isIPv6(s) ? "IPv6" : "Error") << endl;
    } else {
        cout << "Error" << endl;
    }

    return 0;
}
```

---

## **Объяснение алгоритма**

### **Общая структура**

1. Определяем, содержит ли строка точки или двоеточия.
2. Если и то, и другое — **Error** (адрес не может быть смешанным).
3. Если только точки — проверяем как IPv4.
4. Если только двоеточия — проверяем как IPv6.
5. Если ни того, ни другого — **Error**.

### **Проверка IPv4**

1. Разбиваем строку по `.` — должно быть **ровно 4 части**.
2. Каждая часть:
   - **Не пустая**.
   - Состоит **только из цифр**.
   - **Нет лидирующих нулей** (кроме `"0"`).
   - **Длина ≤ 3**.
   - **Значение ≤ 255**.

### **Проверка IPv6**

1. Разбиваем строку по `:` — должно быть **ровно 8 частей**.
2. Каждая часть:
   - **Не пустая**.
   - **Длина ≤ 4**.
   - Состоит **только из hex-цифр** (`0-9`, `a-f`, `A-F`).
   - Лидирующие нули **разрешены**.

---

## **Ключевые моменты**

### 1. **Разбиение строки**

Используем ручное разбиение (без `stringstream`), чтобы контролировать пустые части.
Пример: строка `"1..2.3"` — при разбиении по `.` получим `["1", "", "2", "3"]` — есть пустая часть → Error.

### 2. **Лидирующие нули в IPv4**

Число `"01"` — **невалидно** (лидирующий ноль).
Число `"0"` — **валидно**.
Проверка: `part.size() > 1 && part[0] == '0'` → невалидно.

### 3. **Значение ≤ 255**

Вычисляем вручную, избегая `stoi` (который может кинуть исключение).

### 4. **IPv6: лидирующие нули разрешены**

`"0001"` и `"1"` — оба валидны для IPv6.

### 5. **Пустые части**

`"1:2::3"` — содержит пустую часть → Error (в нашей упрощённой задаче `::` не разрешено).

### 6. **Смешанный формат**

`"1.2.3.4:5"` — содержит и точки, и двоеточия → Error.

---

## **Примеры**

### IPv4

| Ввод | Ответ | Причина |
|------|-------|---------|
| `0.0.0.0` | IPv4 | ✅ |
| `192.168.1.1` | IPv4 | ✅ |
| `255.255.255.255` | IPv4 | ✅ |
| `256.1.1.1` | Error | 256 > 255 |
| `01.2.3.4` | Error | лидирующий ноль |
| `1.2.3` | Error | только 3 части |
| `1.2.3.4.5` | Error | 5 частей |
| `1.2.3.` | Error | пустая часть |

### IPv6

| Ввод | Ответ | Причина |
|------|-------|---------|
| `0:0:0:0:0:0:0:0` | IPv6 | ✅ |
| `ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff` | IPv6 | ✅ |
| `2001:0db8:0000:0000:0000:ff00:0042:8329` | IPv6 | ✅ (лидирующие нули ок) |
| `1:2:3:4:5:6:7` | Error | только 7 частей |
| `1:2:3:4:5:6:7:8:9` | Error | 9 частей |
| `1:2:3:4:5:6:7:g` | Error | 'g' — не hex |
| `1:2:3:4:5:6:7:12345` | Error | длина > 4 |

### Прочее

| Ввод | Ответ |
|------|-------|
| `abc` | Error |
| `1.2.3.4:5` | Error |
| `...` | Error |

---

## **Сложность**

- **Время**: O(|s|) — один проход по строке.
- **Память**: O(|s|) — для хранения частей.

При |s| ≤ 100 — работает мгновенно.

---

## **Финальное решение**

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool isDigit(char c) {
    return c >= '0' && c <= '9';
}

bool isHexDigit(char c) {
    return (c >= '0' && c <= '9') ||
           (c >= 'a' && c <= 'f') ||
           (c >= 'A' && c <= 'F');
}

vector<string> split(const string& s, char delim) {
    vector<string> parts;
    string current;
    for (char c : s) {
        if (c == delim) {
            parts.push_back(current);
            current.clear();
        } else {
            current += c;
        }
    }
    parts.push_back(current);
    return parts;
}

bool isIPv4(const string& s) {
    vector<string> parts = split(s, '.');
    if (parts.size() != 4) return false;

    for (const string& part : parts) {
        if (part.empty() || part.size() > 3) return false;
        if (part.size() > 1 && part[0] == '0') return false;

        int value = 0;
        for (char c : part) {
            if (!isDigit(c)) return false;
            value = value * 10 + (c - '0');
        }
        if (value > 255) return false;
    }
    return true;
}

bool isIPv6(const string& s) {
    vector<string> parts = split(s, ':');
    if (parts.size() != 8) return false;

    for (const string& part : parts) {
        if (part.empty() || part.size() > 4) return false;
        for (char c : part) {
            if (!isHexDigit(c)) return false;
        }
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    string s;
    cin >> s;

    bool hasDot = s.find('.') != string::npos;
    bool hasColon = s.find(':') != string::npos;

    if (hasDot && hasColon) {
        cout << "Error\n";
    } else if (hasDot) {
        cout << (isIPv4(s) ? "IPv4" : "Error") << "\n";
    } else if (hasColon) {
        cout << (isIPv6(s) ? "IPv6" : "Error") << "\n";
    } else {
        cout << "Error\n";
    }

    return 0;
}
```

Это решение корректно обрабатывает все крайние случаи и работает за O(|s|).
