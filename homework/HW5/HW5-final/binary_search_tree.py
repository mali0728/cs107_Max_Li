# Problem 3 -- Binary Search Tree -- for Homework 5 of CS107
# Author: Max Li

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
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
        if node == None:
            node = BSTNode(key, val)
            return node
        
        else:                
            if key < node.key:
                node.size += 1
                if node.left == None:
                    node.left = BSTNode(key, val)
                    return self._root
                    
                else:
                    return self._put(node.left, key, val)
            
            elif key > node.key:
                node.size += 1
                if node.right == None:
                    node.right = BSTNode(key, val)
                    return self._root
                        
                else:
                    return self._put(node.right, key, val)
            
            elif key == node.key:
                node.val = val
                return self._root
    
    def _get(self, node, key):
        if node == None:
            raise KeyError
        elif node.key == key:
            return node.val
        elif key > node.key:
            return self._get(node.right, key)
        elif key < node.key:
            return self._get(node.left, key)

    @staticmethod
    def _size(node):
        return node.size if node else 0
    
'''    
if __name__ == "__main__":  
    
    
    greektoroman = BSTTable()
    greektoroman.put('Athena',    'Minerva')
    greektoroman.put('Eros',      'Cupid')
    greektoroman.put('Aphrodite', 'Venus')
    greektoroman.put('Zeus', 'Jupiter')
    greektoroman.put('Ares', 'Mars')
    print(greektoroman)
    
    print(greektoroman.get('Zeus'))
    
    greektoroman = BSTTable()
    number = [13,7,19,17,3,29,5,31,2,11]
    
    for i in number:
        greektoroman.put(i, i)
        
        
    print(greektoroman.get(31))
    print(greektoroman.get(11))
    print(greektoroman.get(21))
    '''