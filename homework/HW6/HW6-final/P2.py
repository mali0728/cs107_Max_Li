# Problem 2 -- Heaps -- for Homework 6 of CS107
# Extended by: Max Li


from math import floor
from typing import List


class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array)
        self.build_heap()

    def left(self, idx: int) -> int:
        return 2 * idx + 1

    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
            if self.size == 0:
                return '\\--'
            elif idx < self.size:
                buf = prefix
                if left:
                    buf = buf + "|-- "
                else:
                    buf = buf + "\\-- "
                #buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
                buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

                new_prefix = prefix
                if left:
                    new_prefix = new_prefix + "|   "
                else:
                    new_prefix = new_prefix + "    "

                return buf + \
                        self.to_string(new_prefix, self.left(idx), True) + \
                        self.to_string(new_prefix, self.right(idx), False)
            else:
                return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> str:
        return self.size

    # TODO: override this in your dervied classes
    def compare(self, a: int, b: int) -> bool:
        
        raise NotImplementedError


    def heapify(self, idx: int) -> None:
        # TODO: your solution from the previous question can go here
        # but remember to use your new "self.compare(a, b)" instead
        # of raw comparisons
        current_idx = idx
        left_idx = self.left(idx)
        right_idx = self.right(idx)

        if left_idx < self.size and self.compare(self.elements[current_idx], self.elements[left_idx]):
            current_idx = left_idx
        if right_idx < self.size and self.compare(self.elements[current_idx], self.elements[right_idx]):
            current_idx = right_idx
        if current_idx != idx:
            self.swap(idx, current_idx)
            self.heapify(current_idx)

    def build_heap(self) -> None:
        
        for i in range(floor(self.size/2), -1, -1):
            self.heapify(i)

    def heappush(self, key: int) -> None:
        # TODO: your solution from the previous question can go here
        # but remember to use your new "self.compare(a, b)" instead
        # of raw comparisons
        self.elements.append(key)
        current_idx = self.size
        self.size += 1
        while self.parent(current_idx)>=0 and self.compare(self.elements[self.parent(current_idx)], self.elements[current_idx]):
            self.swap(current_idx, self.parent(current_idx))
            current_idx = self.parent(current_idx)

    def heappop(self) -> int:
        # TODO: your solution from the previous question can go here
        if self.size == 0:
            raise IndexError()

        root = self.elements[0]
        self.elements[0] = self.elements[-1]
        self.elements.pop()
        self.size -= 1    
        self.heapify(0)    

        return root


class MinHeap(Heap):
    # TODO: complete implementation
    def __init__(self, array: List[int]) -> None:
        super().__init__(array)

    def compare(self, a: int, b: int) -> bool:
        return a > b


class MaxHeap(Heap):
    # TODO: complete implementation
    def __init__(self, array: List[int]) -> None:
        super().__init__(array)
        
    def compare(self, a: int, b: int) -> bool:
        return a < b


'''
if __name__ == "__main__":
    print("<<<<<<<<<<<<<<part A>>>>>>>>>>>>>>")
    h1 = MinHeap([-1,0,0,15,23,1,2,3]) # The heap tree will be built during initialization
    print(h1)

    h2 = MinHeap([5,3,2,7,4,1,9,3]) # The heap tree will be built during initialization
    print(h2)

    print("<<<<<<<<<<<<<<part B>>>>>>>>>>>>>>")

    h1.heappush(6)
    print("push 6: \n", h1)
    
    h1.heappush(19)
    print("push 19: \n",h1)    

    h1.heappop()
    print("pop :\n", h1)
    h1.heappop()

    print("pop :\n", h1)

    print("<<<<<<<<<<<<<<part C>>>>>>>>>>>>>>")

    mn = MinHeap([1,2,3,4,5])
    mx = MaxHeap([1,2,3,4,5])

    print("minheap:\n",mn)
    print("maxheap:\n",mx)
'''