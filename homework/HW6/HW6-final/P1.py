# Problem 1 -- BST Extensions -- for Homework 6 of CS107
# Extended by: Max Li

from enum import Enum

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node:
            return BSTNode(key, val)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val
        
    @staticmethod
    def _size(node):
        return node.size if node else 0
        
        
    def _removemin(self, node):
        # TODO
        if node.left == None:
            return node.right
            
        else:
            node.left=self._removemin(node.left)
        
            node.size=1 + self._size(node.left) + self._size(node.right)
            return node
            

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        # TODO: Should return a subtree whose root is  but without
        #       the node whose key is
        
        if node == None:
            raise KeyError('key not found')
        
        if key > node.key:
            node.right = self._remove(node.right, key)
        
        elif key < node.key:
            node.left = self._remove(node.left, key)
            
        else:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
 
            node_t = node
            min_right_node = node.right
            while min_right_node.left != None:
                min_right_node = min_right_node.left
            node = min_right_node
            node.right = self._removemin(node_t.right)
            node.left = node_t.left
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node


class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3


class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        # TODO: implement
        self.tree = tree
        self.traversal_type = traversalType

    def __iter__(self):
        # TODO: implement
        self.iter_list = []
        
        if self.traversal_type == DFSTraversalTypes.PREORDER:
            self.preorder(self.tree)
        elif self.traversal_type == DFSTraversalTypes.INORDER:
            self.inorder(self.tree)
        else:
            self.postorder(self.tree)
        return self

    def __next__(self):
        # TODO: implement
        if len(self.iter_list) > 0:
            return self.iter_list.pop(0)
        else:
            raise StopIteration()
           
    def _inorder_traverse(self, node: BSTNode):
        if node.left:
            self._inorder_traverse(node.left)
        if node:
            self.iter_list.append(node)
        if node.right:
            self._inorder_traverse(node.right)
            
    def _preorder_traverse(self, node: BSTNode):
        if node:
            self.iter_list.append(node)
        if node.left:
            self._preorder_traverse(node.left)
        if node.right:
            self._preorder_traverse(node.right)   
            
    def _postorder_traverse(self, node: BSTNode):
        if node.left:
            self._postorder_traverse(node.left)
        if node.right:
            self._postorder_traverse(node.right)
        if node:
            self.iter_list.append(node)        
    
    def inorder(self, bst: BSTTable):
        # TODO: implement
        self._inorder_traverse(bst._root)

    def preorder(self, bst: BSTTable):
        # TODO: implement
        self._preorder_traverse(bst._root)

    def postorder(self, bst: BSTTable):
        # TODO: implement
        self._postorder_traverse(bst._root)


'''
print("-------------part A-----------------")
t = BSTTable()
t.put(5, 'a')
t.put(1, 'b')
t.put(2, 'c')
t.put(0, 'd')
print(t._root)
print(t._size(t._root))
print(t._removemin(t._root))
print(t._size(t._root))

print("-------------part B-----------------")
t = BSTTable()
t.put(5, 'a')
t.put(1, 'b')
t.put(2, 'c')
t.put(0, 'd')


print(t._root)
print(t._size(t._root))

t.remove(5)
print(t._root)
print(t._size(t._root))
t.remove(1)
print(t._root)
print(t._size(t._root))

    #print(t._remove(t._root, 10)) #return KeyNotFound?

    #part C
print("-------------part C-----------------")
input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
bst = BSTTable()
for key, val in input_array:
    bst.put(key, val)
traversal = DFSTraversal(bst, DFSTraversalTypes.POSTORDER)
for node in traversal:
    print(str(node.key) + ', ' + node.val)

'''
