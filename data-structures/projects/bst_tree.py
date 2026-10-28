class Node:
# class — ключевое слово определения класса
# Node — имя класса
# : — двоеточие

    def __init__(self, value):
    # def — определение метода
    # __init__ — конструктор (вызывается при создании)
    # (self, value) — параметры: self (экземпляр), value (значение)
    # : — двоеточие

        self.value = value
        # self.value — атрибут экземпляра
        # = — присваивание
        # value — значение

        self.left = None
        # self.left — левый ребёнок
        # = — присваивание
        # None — пусто

        self.right = None
        # self.right — правый ребёнок
        # = — присваивание
        # None — пусто

class BST:
# class — определение класса
# BST — имя класса (Binary Search Tree)
# : — двоеточие

    def __init__(self):
    # def — конструктор
    # (self) — параметр
    # : — двоеточие

        self.root = None
        # self.root — корень дерева
        # = — присваивание
        # None — пустое дерево

    def insert(self, value):
    # def — метод вставки
    # (self, value) — параметры
    # : — двоеточие

        if self.root is None:
        # if — условный оператор
        # self.root is None — дерево пустое
        # : — двоеточие

            self.root = Node(value)
            # self.root = Node(value) — создание корня
            # return — выход

            return

        current = self.root
        # current — текущая вершина
        # = — присваивание
        # self.root — корень

        while True:
        # while — цикл
        # True — бесконечный цикл
        # : — двоеточие

            if value < current.value:
            # if — условный оператор
            # value < current.value — идём влево
            # : — двоеточие

                if current.left is None:
                # if — левого ребёнка нет
                # : — двоеточие

                    current.left = Node(value)
                    # current.left = Node(value) — создание левого ребёнка

                    break
                    # break — выход из цикла

                current = current.left
                # current = current.left — переход влево

            else:
            # else — иначе (идём вправо)
            # : — двоеточие

                if current.right is None:
                # if — правого ребёнка нет
                # : — двоеточие

                    current.right = Node(value)
                    # current.right = Node(value) — создание правого ребёнка

                    break
                    # break — выход

                current = current.right
                # current = current.right — переход вправо

    def search(self, value):
    # def — метод поиска
    # (self, value) — параметры
    # : — двоеточие

        current = self.root
        # current — текущая вершина
        # = — присваивание
        # self.root — корень

        while current is not None:
        # while — цикл, пока не дошли до None
        # : — двоеточие

            if value == current.value:
            # if — нашли
            # : — двоеточие

                return True
                # return True — найдено

            elif value < current.value:
            # elif — иначе если
            # value < current.value — идём влево
            # : — двоеточие

                current = current.left
                # current = current.left — переход влево

            else:
            # else — иначе (вправо)
            # : — двоеточие

                current = current.right
                # current = current.right — переход вправо

        return False
        # return False — не найдено

    def inorder(self):
    # def — метод симметричного обхода
    # (self, node=None) — параметры
    # : — двоеточие
        self._inorder(self.root)
        # self.inorder(self.root) — обход корня
    def _inorder(self, node):
        if node is None:
            return
        self._inorder(node.left)
        print(node.value, end=" ")
        self._inorder(node.right)

# Пример
bst = BST()
# bst — экземпляр класса BST
# = — присваивание
# BST() — вызов конструктора

for x in [50, 30, 70, 20, 40, 60, 80]:
# for — цикл
# x — текущее значение
# in [50, 30, ...] — по списку
# : — двоеточие

    bst.insert(x)
    # bst.insert(x) — вставка

print("Inorder (отсортировано):", end=" ")
# print — функция вывода

bst.inorder()
# bst.inorder() — обход

print()
# print() — перевод строки

print("Поиск 40:", bst.search(40))
# print — функция вывода
# "Поиск 40:" — текст
# bst.search(40) — поиск

print("Поиск 55:", bst.search(55))
# print — функция вывода
