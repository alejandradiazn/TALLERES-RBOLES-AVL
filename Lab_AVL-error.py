
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y

class AVLTree:
    def _init_(self):
        self.root = None  

    
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    
    def _insert_recursive(self, node, value):
        # Caso base: inserta el nuevo nodo
        if not node:
            return Node(value)

        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node  

        
        updateHeight(node)
        balance = getBalance(node)

        # Rebalanceo según los 4 casos posibles

        # Caso Izquierda-Izquierda
        if balance > 1 and value < node.left.value:
            return rotate_right(node)

        # Caso Izquierda-Derecha
        if balance > 1 and value > node.left.value:
            node.left = rotate_left(node.left)
            return rotate_right(node)

        # Caso Derecha-Derecha
        if balance < -1 and value > node.right.value:
            return rotate_left(node)

        # Caso Derecha-Izquierda
        if balance < -1 and value < node.right.value:
            node.right = rotate_right(node.right)
            return rotate_left(node)

        return node  # Retorna el nodo balanceado

    # Elimina un valor del árbol
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    # Función recursiva para eliminar un nodo
    def _delete_recursive(self, node, value):
        if not node:
            return node  # Valor no encontrado

        # Buscar el nodo a eliminar
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Caso 1: nodo sin hijos o con un hijo
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Caso 2: nodo con dos hijos
            temp = self._get_min_value_node(node.right)  # Nodo más pequeño en subárbol derecho
            node.value = temp.value  # Copia el valor
            node.right = self._delete_recursive(node.right, temp.value)  # Elimina duplicado

        # Actualizar altura y rebalancear
        updateHeight(node)
        balance = getBalance(node)

        # Rebalanceo después de eliminación

        
        if balance > 1 and getBalance(node.left) >= 0:
            return rotate_right(node)

        
        if balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            return rotate_right(node)

        
        if balance < -1 and getBalance(node.right) <= 0:
            return rotate_left(node)

        
        if balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            return rotate_left(node)

        return node  

    
    def _get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    
    def inorder_traversal(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if not node:
            return []
        return self._inorder_recursive(node.left) + [node.value] + self._inorder_recursive(node.right)

    
    def print_tree(self, node=None, level=0, label="Root"):
        if node is None:
            node = self.root
        if node.right:
            self.print_tree(node.right, level + 1, "R")
        print("   " * level + f"{label}: ({node.value}, h={node.height})")
        if node.left:
            self.print_tree(node.left, level + 1, "L")