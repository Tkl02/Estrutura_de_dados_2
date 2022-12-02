from tree import BinaryTree, Node

# Vídeo Implementando uma árvore binária: https://youtu.be/6E169kShoNU
def inorder_example_tree():
    tree = BinaryTree()
    n1 = Node('5')
    n2 = Node('7')
    n3 = Node('14')
    n4 = Node('25')
    n5 = Node('35')
    n6 = Node('47')
    n7 = Node('58')
    n8 = Node('77')
    n9 = Node('90')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    
    tree.root = n2
    return tree
    # tree.simetric_traversal()
    # print()

    #      '+'
    #    /     \
    #  'a'      '*'
    #          /   \
    #        'b'    '-'
    #              /    \
    #            '/'    'e' 
    #           /   \
    #         'c'   'd'

    # (a + (b * ((c/d) - e)))

# Vídeo Percurso em Pós-Ordem:
def postorder_example_tree():
    tree = BinaryTree()
    n1 = Node('5')
    n2 = Node('7')
    n3 = Node('14')
    n4 = Node('25')
    n5 = Node('35')
    n6 = Node('47')
    n7 = Node('58')
    n8 = Node('77')
    n9 = Node('90')
    n0 = Node('92')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n8.right = n7

    tree.root = n0
    return tree
    
    
if __name__ == "__main__":
    print('-=-'*20)
    tree = postorder_example_tree()
    print("Percurso em pós ordem:")
    tree.postorder_traversal()
    print("Altura: ", tree.height())
    
    print('-=-'*20)
    
    tree = inorder_example_tree()
    print("Percurso em in ordem:")
    tree.inorder_traversal()
    print("Altura: ", tree.height())
    print('-=-'*20)