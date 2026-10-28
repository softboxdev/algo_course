import sys
sys.setrecursionlimit(10**6)

children = [[1, 2], [3, 4], [5], [], [], []]
# children — список детей (0-based)
# children[0] = [2, 3] — дети вершины 1 (индекс 0)
# ... — остальные

n = 6
# n — количество вершин

size = [0] * n
# size — массив размеров поддеревьев
# = — присваивание
# [0] * n — список из n нулей

height = [0] * n
# height — массив высот
# = — присваивание
# [0] * n — список из n нулей

def dfs(v):
# def — определение функции
# dfs — имя функции
# (v) — параметр (вершина, 0-based)
# : — двоеточие

    size[v] = 1
    # size[v] = 1 — сама вершина

    max_child_height = 0
    # max_child_height — максимальная высота среди детей
    # = — присваивание
    # 0 — начальное значение

    for child in children[v]:
    # for — цикл по детям
    # child — текущий ребёнок
    # in children[v] — по списку детей
    # : — двоеточие

        dfs(child)
        # dfs(child) — рекурсивный вызов

        size[v] += size[child]
        # size[v] += size[child] — прибавление размера поддерева ребёнка

        max_child_height = max(max_child_height, height[child])
        # max(...) — максимум из двух
        # height[child] — высота поддерева ребёнка

    height[v] = max_child_height + 1
    # height[v] = ... — высота вершины = макс. высота ребёнка + 1

dfs(0)
# dfs(0) — запуск с корня (индекс 0)

for i in range(n):
# for — цикл по вершинам
# i — индекс
# in range(n) — от 0 до n-1
# : — двоеточие

    print(f"Вершина {i}: размер={size[i]}, высота={height[i]}")
    # print — функция вывода
    # f"..." — f-строка
    # {i + 1} — номер вершины (1-based)
    # {size[i]} — размер
    # {height[i]} — высота
