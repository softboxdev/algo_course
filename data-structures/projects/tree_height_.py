import sys
sys.setrecursionlimit(10**6)

# 0-based: вершины 0..5
# Дерево:
#       0
#      / \
#     1   2
#    / \   \
#   3   4   5
children = [[1, 2], [3, 4], [5], [], [], []]
# children[0] = [1, 2] — дети вершины 0
# children[1] = [3, 4] — дети вершины 1
# children[2] = [5]    — дети вершины 2
# children[3] = []     — лист
# children[4] = []     — лист
# children[5] = []     — лист

n = 6
size = [0] * n        # индексы 0..5
height = [0] * n      # индексы 0..5

def dfs(v):
    size[v] = 1
    max_child_height = 0

    for child in children[v]:
        dfs(child)
        size[v] += size[child]
        max_child_height = max(max_child_height, height[child])

    height[v] = max_child_height + 1

dfs(0)

for i in range(n):
    print(f"Вершина {i}: размер={size[i]}, высота={height[i]}")
