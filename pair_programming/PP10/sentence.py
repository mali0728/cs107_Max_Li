#Collaborators: Max Li, Yujie Cai, Gabin Ryu, ChunChao Tseng

class Sentence: # An iterable
    def __init__(self, text): 
        self.text = text
        self.words = text.split()

    def __iter__(self):
        for word in self.words:
            yield word

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


if __name__ == "__main__":
    s = Sentence("1 2 3 4 5")
    print(list(iter(s)))
    for word in s:
        print(word)
        