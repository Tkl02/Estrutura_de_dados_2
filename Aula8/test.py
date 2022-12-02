import random
from tree import BinarySearchTree

random.seed(77)

def random_tree(size=20):
    values = random.sample(range(0, 100), 20)
    tree = BinarySearchTree()
    for v in values:
        tree.insert(v)
    return tree


bst = random_tree()
bst.inorder_traversal()

# testar remoção da árvore

print('\n------------------')
v = 49
bst.remove(v)
print("Após remover {}".format(v))
bst.inorder_traversal()
print('\n')
bst.levelorder_traversal()

print("\n------------------")
print("Máximo:", bst.max())
print("Mínimo:", bst.min())
print("\n------------------")