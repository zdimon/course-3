class Myiter:

    _list = []

    def add(self, node):
        self._list.append(node)

    def __iter__(self):
        print 'Calling iter()'
        return iter(self._list)
        
if __name__ == '__main__':
    root = Myiter()
    root.add('hello')
    root.add('world')
    for ch in root:
        print(ch)
