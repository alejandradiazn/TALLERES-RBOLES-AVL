import sys 

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
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
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
        
#Error: Se realiza la rotación pero no se le asigna el valor al nodo.
        if balance > 1 and getBalance(node.left) >= 0:
            return rotate_right(node) #No hay modificación de valores de nodo y por lo tanto no se modifica el árbol.
        elif balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            return rotate_right(node) #Falta la asignación del valor al nodo.
        elif balance < -1 and getBalance(node.right) <= 0:
            return rotate_left(node) #Falta la asignación del valor al nodo.
        elif balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            return rotate_left(node) #Falta la asignación del valor al nodo.
        
        return node 

def delete(self, value):
    self.root = self._delete_recursive(self.root, value)
    
def _delete_recursive(self, node, value):
    if not node:
        return node

    if value < node.value:
        node.left = self._delete_recursive(node.left, value)
    elif value > node.value:
        node.right = self._delete_recursive(node.right, value)
    else:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left

        temp = self._get_min_value_node(node.right)
        node.value = temp.value
        node.right = self._delete_recursive(node.right, temp.value)

    updateHeight(node)
    balance = getBalance(node)

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
    current = node
    while current.left:
        current = current.left
    return current

def inorder_traversal(self, node=None, result=None):
    if result is None:
        result = []
    if node is None:
        node = self.root
    if node.left:
        self.inorder_traversal(node.left, result)
    result.append(node.value)
    if node.right:
        self.inorder_traversal(node.right, result)
    return result

def print_tree(self, node=None, level=0, prefix="Root: "):
        if node is None:
            node = self.root
        if node:
            print(" " * (level * 4) + prefix + f"{node.value} (H={node.height}, B={getBalance(node)})")
            if node.left:
                self.print_tree(node.left, level + 1, "L--- ")
            if node.right:
                self.print_tree(node.right, level + 1, "R--- ")


avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50, 25]
print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

print("\n--- Árbol después de inserciones ---")
avl.print_tree()

print("\nRecorrido in-order:", avl.inorder_traversal())

# Prueba de eliminación
avl.delete(40)
print("\n--- Árbol después de eliminar 40 ---")
avl.print_tree()
print("\nRecorrido in-order:", avl.inorder_traversal())
