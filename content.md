
---

# 📊 ПОЛНЫЙ ПЛАН ПОДГОТОВКИ К СОБЕСЕДОВАНИЮ ПО C++

## ЧАСТЬ 1: СТРУКТУРЫ ДАННЫХ

| Тема | Подтемы | Что нужно знать | Как решать задачи |
|------|---------|-----------------|-------------------|
| **1. Массивы и строки** | • Динамические массивы (vector)<br>• Двумерные массивы<br>• Строки (string)<br>• Sliding Window<br>• Two Pointers | • Вставка/удаление O(1) в конце, O(n) в середине<br>• Доступ по индексу O(1)<br>• SSO (Small String Optimization)<br>• Конкатенация строк | • Sliding Window: расширяем правый, сужаем левый<br>• Two Pointers: с двух концов или быстрый/медленный<br>• Prefix Sum для быстрых запросов суммы |
| **2. Связные списки** | • Односвязные<br>• Двусвязные<br>• Разворот списка<br>• Обнаружение цикла<br>• Слияние списков | • Вставка/удаление O(1) если есть указатель<br>• Доступ по индексу O(n)<br>• fakehead — главный паттерн<br>• Хранить next перед изменением | • Использовать fakehead для упрощения<br>• Сохранять next перед изменением указателей<br>• Fast/slow pointers для циклов<br>• Рекурсия для разворота |
| **3. Стек** | • LIFO<br>• std::stack<br>• Монотонный стек<br>• RPN (обратная польская запись) | • push/pop/top O(1)<br>• Адаптер над deque/vector<br>• Проверка empty() перед top()<br>• Идеален для вложенных структур | • Скобки: кладём открывающие, проверяем закрывающие<br>• Монотонный стек: поддерживаем возрастание/убывание<br>• RPN: операнды в стек, операции применяем к двум верхним |
| **4. Очередь** | • FIFO<br>• std::queue<br>• std::deque<br>• BFS | • push/pop/front/back O(1)<br>• deque — двухсторонняя очередь<br>• BFS: кладём старт, обрабатываем по уровням | • BFS: queue + visited<br>• Дек для Sliding Window Maximum<br>• Очередь задач (Task Queue) |
| **5. Хеш-таблицы** | • std::unordered_map<br>• std::unordered_set<br>• Коллизии (chaining)<br>• Хеш-функции<br>• Итераторы | • Вставка/поиск/удаление O(1) сред.<br>• Нет порядка<br>• Хорошая хеш-функция — ключ к успеху<br>• Rehash при переполнении | • Подсчёт частот (word count)<br>• Проверка существования (visited)<br>• Группировка (анаграммы)<br>• Кэширование (memoization) |
| **6. Куча** | • Бинарная куча<br>• std::priority_queue<br>• Max-heap vs Min-heap<br>• Heapify<br>• Heap Sort | • Полное бинарное дерево в массиве<br>• push/pop O(log n)<br>• top O(1)<br>• Массив: left=2i+1, right=2i+2, parent=(i-1)/2 | • K-й наибольший: min-heap размера K<br>• Слияние K списков: кладём первые элементы<br>• Дейкстра: извлекаем min, обновляем соседей<br>• Heap Sort: строим кучу, извлекаем элементы |
| **7. Двоичное дерево поиска** | • BST свойства<br>• std::set / std::multiset<br>• std::map / std::multimap<br>• Балансировка (AVL, Red-Black)<br>• Обходы (in-order, pre-order, post-order) | • Поиск/вставка/удаление O(log n)<br>• In-order обход даёт отсортированный порядок<br>• Следующий/предыдущий O(1) амортиз.<br>• lower_bound/upper_bound для диапазонов | • Медиана в окне: два дерева (lower/upper)<br>• Валидация BST: проверка диапазона<br>• K-я порядковая статистика: храним размер поддеревьев<br>• Поиск в диапазоне: lower_bound/upper_bound |

---

## ЧАСТЬ 2: АЛГОРИТМЫ

| Тема | Подтемы | Что нужно знать | Как решать задачи |
|------|---------|-----------------|-------------------|
| **1. Два указателя (Two Pointers)** | • С двух концов<br>• Быстрый/медленный<br>• Скользящее окно (фикс.)<br>• Скользящее окно (перем.) | • O(n) вместо O(n²)<br>• Используется на отсортированных массивах<br>• Быстрый указатель для поиска циклов | • Сумма чисел: left + right = target<br>• Удаление дубликатов: slow/fast<br>• Sliding Window: расширяем right, сужаем left |
| **2. Бинарный поиск** | • Классический<br>• Поиск границы (first/last)<br>• Поиск в матрице<br>• Поиск ответа (монотонный) | • O(log n)<br>• Работает только на отсортированных данных<br>• left + (right-left)/2 для избежания переполнения | • left = 0, right = n (полуинтервал [left, right))<br>• if (condition(mid)) right = mid else left = mid+1<br>• Поиск в матрице: как в одномерном массиве |
| **3. DFS (Поиск в глубину)** | • Рекурсивный<br>• Итеративный (стек)<br>• Backtracking<br>• Обходы дерева | • Использует стек (явный или неявный)<br>• O(V+E)<br>• Backtracking — DFS с откатом<br>• Рекурсия может переполнить стек | • Рекурсивно идём вглубь<br>• Для Backtracking: делаем, рекурсивно вызываем, отменяем<br>• Итеративный: стек + visited |
| **4. BFS (Поиск в ширину)** | • Классический<br>• По уровням<br>• Кратчайший путь в невзвеш. графе | • Использует очередь<br>• O(V+E)<br>• Даёт кратчайший путь<br>• Находит все компоненты связности | • queue + visited<br>• dist[v] = dist[u] + 1<br>• Для уровней: for (int i = queue.size(); i > 0; --i) |
| **5. Динамическое программирование** | • 1D DP (Climbing Stairs, House Robber)<br>• 2D DP (LCS, Edit Distance)<br>• Knapsack (0/1, Unbounded)<br>• DP на интервалах<br>• Bitmask DP | • 4 шага: состояние, переход, база, ответ<br>• Оптимальная подструктура + перекрывающиеся подзадачи<br>• Оптимизация памяти O(1) или O(n) | • 1D: dp[i] = f(dp[i-1], dp[i-2])<br>• 2D: dp[i][j] = f(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])<br>• Knapsack: идём от X вниз (0/1) или вверх (Unbounded)<br>• Восстановление ответа: храним parent |
| **6. Жадные алгоритмы** | • Интервалы (Meeting Rooms)<br>• Priority Queue (Huffman)<br>• Kadane (Max Subarray)<br>• Jump Game | • Локальный выбор → глобальный оптимум<br>• Не всегда работает (нужно доказать)<br>• Часто с сортировкой | • Сортировка по времени окончания<br>• Выбираем локально оптимальный шаг<br>• Пытаемся найти контрпример |
| **7. Графы** | • Представление (матрица, список)<br>• Dijkstra (кратч. путь)<br>• Topological Sort<br>• Union-Find (DSU)<br>• Kruskal (MST)<br>• Floyd-Warshall | • Dijkstra: O(E log V) с кучей<br>• Topological Sort: только DAG<br>• DSU: find O(α(n)), union O(α(n))<br>• Отрицательные веса → Bellman-Ford | • Dijkstra: priority_queue + dist<br>• Topological Sort: indegree + queue (Kahn)<br>• DSU: parent + size, find сжатие пути<br>• Обнаружение цикла в графе |

---

## ЧАСТЬ 3: ЯЗЫК C++ (ТЕХНИЧЕСКАЯ ЧАСТЬ)

| Тема | Подтемы | Что нужно знать | Как отвечать на собеседовании |
|------|---------|-----------------|-------------------------------|
| **1. ООП** | • Классы и объекты<br>• Наследование<br>• Полиморфизм<br>• Инкапсуляция<br>• Абстракция | • virtual функции для динамического полиморфизма<br>• Виртуальный деструктор обязателен в базовом классе<br>• override, final (C++11)<br>• private/protected/public | • Рассказать про статический и динамический полиморфизм<br>• Объяснить, зачем виртуальный деструктор<br>• Показать пример с наследованием |
| **2. RAII и умные указатели** | • RAII принцип<br>• std::unique_ptr<br>• std::shared_ptr<br>• std::weak_ptr<br>• std::make_unique/make_shared | • RAII — ресурсы в конструкторе, освобождение в деструкторе<br>• unique_ptr — эксклюзивное владение<br>• shared_ptr — счётчик ссылок<br>• weak_ptr — для разрыва циклических ссылок | • Объяснить, как умные указатели упрощают управление памятью<br>• Сказать, что new/delete почти не используется<br>• Показать, как избежать утечек |
| **3. Move-семантика** | • rvalue-ссылки (&&)<br>• std::move<br>• std::forward<br>• Move-конструктор<br>• Move-присваивание | • std::move — кастует к rvalue<br>• std::forward — perfect forwarding<br>• Правило пяти (Rule of Five)<br>• noexcept для move-операций | • Объяснить разницу между копированием и перемещением<br>• Показать пример с vector и перемещением<br>• Рассказать про SSO в std::string |
| **4. Шаблоны (Templates)** | • Функциональные шаблоны<br>• Классовые шаблоны<br>• Специализация<br>• SFINAE<br>• Concepts (C++20)<br>• Variadic templates | • Шаблоны компилируются в момент инстанцирования<br>• SFINAE — подстановка не удалась, не ошибка<br>• Concepts — ограничения для шаблонов<br>• auto, decltype, type traits | • Показать пример шаблонной функции<br>• Объяснить, как работают type traits<br>• Сказать, что шаблоны — это compile-time полиморфизм |
| **5. STL** | • Контейнеры (vector, list, deque, map, set)<br>• Алгоритмы (sort, find, binary_search)<br>• Итераторы<br>• Аллокаторы<br>• Адаптеры (stack, queue) | • Итераторы — обобщённые указатели<br>• Алгоритмы работают с итераторами<br>• Контейнеры делятся на последовательные и ассоциативные<br>• Аллокаторы для кастомного управления памятью | • Сравнить vector vs list<br>• Объяснить, когда использовать map vs unordered_map<br>• Рассказать про итераторы (input, output, forward, bidirectional, random access) |
| **6. Многопоточность** | • std::thread<br>• std::mutex<br>• std::lock_guard<br>• std::unique_lock<br>• std::atomic<br>• std::condition_variable<br>• Модели памяти | • data race — UB<br>• lock_guard — RAII для мьютекса<br>• atomic — lock-free операции<br>• memory_order (relaxed, acquire, release, seq_cst)<br>• Deadlock — два мьютекса в разных порядках | • Объяснить, как избежать deadlock (lock в одном порядке)<br>• Показать пример потокобезопасного счётчика<br>• Рассказать про false sharing (выравнивание 64 байта) |
| **7. Управление памятью** | • Стек vs куча<br>• new/delete vs malloc/free<br>• placement new<br>• Аллокаторы<br>• Memory pooling<br>• Утечки памяти | • new вызывает конструктор, malloc — нет<br>• Стек — автоматическое управление, куча — ручное<br>• Утечка — потеря указателя на память<br>• Аллокатор — стратегия выделения памяти | • Объяснить, как работает память в C++<br>• Рассказать про SSO в std::string<br>• Показать, как писать кастомный аллокатор |
| **8. Константность** | • const<br>• constexpr<br>• consteval (C++20)<br>• mutable<br>• const-correctness | • const — неизменяемость во время выполнения<br>• constexpr — вычисление на этапе компиляции<br>• mutable — поле, изменяемое в const-объекте<br>• const-методы — не меняют объект | • Всегда помечать методы const, если они не меняют объект<br>• Использовать constexpr для констант и функций<br>• Объяснить разницу между const int*, int* const, const int* const |

---

## ЧАСТЬ 4: ПАТТЕРНЫ РЕШЕНИЯ ЗАДАЧ

| Паттерн | Описание | Когда использовать | Пример задачи |
|---------|----------|-------------------|---------------|
| **Two Pointers** | Два указателя для обхода массива | Сумма чисел, удаление дубликатов, палиндромы | Two Sum, Container With Most Water |
| **Sliding Window** | Окно, которое двигается по массиву | Подмассивы, строки с условием | Longest Substring Without Repeating |
| **Binary Search** | Деление пополам на отсортированных данных | Поиск, поиск ответа (монотонный) | First Bad Version, Search in Rotated Array |
| **BFS/DFS** | Обход графа/дерева | Поиск пути, компоненты связности | Number of Islands, Clone Graph |
| **DP (Tabulation)** | Итеративное заполнение таблицы | Оптимизация, подсчёт способов | Climbing Stairs, Knapsack |
| **DP (Memoization)** | Рекурсия + кэширование | Когда естественно рекурсивное решение | Fibonacci, Word Break |
| **Greedy** | Локально оптимальный выбор | Интервалы, задачи с жадным выбором | Meeting Rooms, Jump Game |
| **Backtracking** | Перебор с откатом | Комбинации, перестановки, судоку | N-Queens, Generate Parentheses |
| **Union-Find** | Объединение компонент | Связность, циклы в графе | Number of Islands (DSU), Redundant Connection |
| **Dijkstra** | Кратчайший путь | Графы с положительными весами | Network Delay Time, Path With Minimum Effort |

---

## ЧАСТЬ 5: ЧАСТЫЕ ЗАДАЧИ ПО КАТЕГОРИЯМ

| Категория | Задачи | Сложность | Ключевой подход |
|-----------|--------|-----------|-----------------|
| **Массивы** | Two Sum, Three Sum, Container With Most Water, Trapping Rain Water, Maximum Subarray | Easy-Medium | Two Pointers, Sliding Window, Kadane |
| **Строки** | Valid Palindrome, Longest Substring Without Repeating, Group Anagrams, Decode String | Easy-Medium | Sliding Window, Hash Table, Stack |
| **Связные списки** | Reverse Linked List, Detect Cycle, Merge Two Sorted Lists, Remove Nth Node From End | Easy-Medium | fakehead, fast/slow pointers, рекурсия |
| **Стек** | Valid Parentheses, Min Stack, Daily Temperatures, Evaluate RPN | Easy-Medium | Монотонный стек, LIFO |
| **Деревья** | Maximum Depth, Validate BST, Lowest Common Ancestor, Level Order Traversal | Easy-Medium | BFS, DFS, рекурсия |
| **Хеш-таблицы** | Two Sum, First Unique Character, Top K Frequent, Longest Consecutive Sequence | Easy-Medium | unordered_map/set |
| **Куча** | Kth Largest, Merge K Sorted Lists, Find Median from Data Stream | Medium | priority_queue, min-heap/max-heap |
| **DP** | Climbing Stairs, House Robber, Longest Increasing Subsequence, Edit Distance | Medium-Hard | 1D DP, 2D DP, Knapsack |
| **Графы** | Number of Islands, Clone Graph, Course Schedule, Network Delay Time | Medium-Hard | BFS, DFS, Topological Sort, Dijkstra |
| **Backtracking** | N-Queens, Generate Parentheses, Word Search, Subsets | Medium | DFS + откат (backtracking) |

---

## 📝 ЧЕК-ЛИСТ ПОДГОТОВКИ

### Неделя 1-2: Структуры данных
- [ ] Массивы и строки (Sliding Window, Two Pointers)
- [ ] Связные списки (fakehead, reverse, cycle detection)
- [ ] Стек и очередь (валидные скобки, BFS)
- [ ] Хеш-таблицы (Two Sum, Group Anagrams)

### Неделя 3-4: Алгоритмы
- [ ] Двоичный поиск (границы, поиск ответа)
- [ ] DFS/BFS (обход деревьев, графов)
- [ ] Рекурсия и Backtracking
- [ ] Жадные алгоритмы (интервалы, задачи выбора)

### Неделя 5-6: Сложные темы
- [ ] Динамическое программирование (1D, 2D, Knapsack)
- [ ] Графы (Dijkstra, Topological Sort, Union-Find)
- [ ] Куча и приоритетная очередь (K-й элемент, Merge K списков)
- [ ] Двоичное дерево поиска (BST, медиана в окне)

### Неделя 7-8: Язык C++
- [ ] ООП (наследование, полиморфизм, виртуальные функции)
- [ ] RAII и умные указатели (unique_ptr, shared_ptr, weak_ptr)
- [ ] Move-семантика (rvalue, move, forward)
- [ ] STL (контейнеры, алгоритмы, итераторы)
- [ ] Многопоточность (mutex, atomic, thread)

### Неделя 9-10: Практика
- [ ] 20 задач на LeetCode (Medium)
- [ ] 10 задач на собеседования (в формате интервью)
- [ ] Написание кода на бумаге/доске
- [ ] Объяснение решений вслух

---

## 🎯 СОВЕТЫ ДЛЯ УСПЕХА

1. **Практика — ключ к успеху:** Решайте минимум 2-3 задачи в день
2. **Не заучивайте код:** Понимайте идею и паттерны
3. **Объясняйте вслух:** Это важнее самого кода на собеседовании
4. **Edge cases:** Пустые массивы, один элемент, отрицательные числа
5. **Сложность:** Всегда оценивайте O(n) и говорите интервьюеру
6. **Рисуйте на доске:** Визуализация помогает найти решение
7. **Спрашивайте уточнения:** Лучше переспросить, чем сделать не то

---

## 📚 РЕСУРСЫ ДЛЯ ПОДГОТОВКИ

| Ресурс | Что там | Как использовать |
|--------|---------|------------------|
| **LeetCode** | Задачи с собеседований | Решать Top Interview 150, Top 100 Liked |
| **HackerRank** | Задачи по темам | Практика по конкретным структурам данных |
| **Codeforces** | Олимпиадные задачи | Для продвинутой подготовки |
| **AlgoExpert** | Структурированный курс | Систематическое изучение тем |
| **YouTube (NeetCode)** | Разборы решений | Смотреть разборы сложных задач |
| **cppreference.com** | Документация C++ | Проверять синтаксис и методы STL |

---
