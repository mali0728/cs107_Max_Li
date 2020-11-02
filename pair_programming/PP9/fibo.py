"""
PP9

Collaborators: Max Li, Tale Lokvenec

"""

class Fibonacci: # An iterable b/c it has __iter__
    def __init__(self, val): 
        self.val = val

    def __iter__(self):
        return FibonacciIterator(self.val) # Returns an instance of the iterator

class FibonacciIterator: # has __next__ and __iter__
    def __init__(self, val): 
        self.index = 0
        self.val = val 
        self.previous = 1
        self.previous_previous = 0

    def __next__(self): 
        if self.index < self.val:
            next_value = self.previous + self.previous_previous
            self.previous_previous = self.previous
            self.previous = next_value
            self.index += 1
            return next_value
        else:
            raise StopIteration()            

    def __iter__(self):
        return self # Allows iterators to be used where an iterable is expected



if __name__ == "__main__":
    fib = Fibonacci(10)
    print(list(iter(fib)))

    fib2 = Fibonacci(2)
    print(list(iter(fib2)))