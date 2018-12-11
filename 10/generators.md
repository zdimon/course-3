##Generators iterators

### Iterators


We use for statement for looping over a list.

    for i in [1, 2, 3, 4]:
        print i,

over string

    for c in "python":
        print c

over file

    for line in open("a.txt"):
        print line,



Problem

You need to process items in an iterable, but for whatever reason, you can’t or don’t want to use a for loop.

    with open('/etc/passwd') as f:
        try:
            while True:
                line = next(f)
                print(line)
        except StopIteration:
            pass


    with open('/etc/passwd') as f:
         while True:
             line = next(f, None)
             if line is None:
                 break
             print(line)

The following interactive example illustrates the basic mechanics of what happens during iteration:

    >>> items = [1, 2, 3]
    >>> # Get the iterator
    >>> it = iter(items)     # Invokes items.__iter__()
    >>> # Run the iterator
    >>> next(it)             # Invokes it.__next__()
    1
    >>> next(it)
    2
    >>> next(it)
    3
    >>> next(it)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration
    >>>    


Python’s iterator protocol requires __iter__() to return a special iterator object that implements a __next__() method to carry out the actual iteration. If all you are doing is iterating over the contents of another container, you don’t really need to worry about the underlying details of how it works. All you need to do is to forward the iteration request along.
    


class Myiter:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# Example
if __name__ == '__main__':
    root = Myiter(0)
    root.add_child('hello')
    root.add_child('world')
    for ch in root:
        print(ch)
# Outputs hello world


Containers 
Containers are data structures holding elements.
Most containers are iterable.


>>> x = [1, 2, 3]
>>> y = iter(x)
>>> z = iter(x)
>>> next(y)
1
>>> next(y)
2
>>> next(z)
1
>>> type(x)
<class 'list'>
>>> type(y)
<class 'list_iterator'>


##Creating New Iteration Patterns with Generators



You want to implement a custom iteration pattern that’s different than the usual built-in functions (e.g., range(), reversed(), etc.).





    def frange(start, stop, increment):
        x = start
        while x < stop:
            yield x
            x += increment




http://nvie.com/posts/iterators-vs-generators/
http://anandology.com/python-practice-book/iterators.html
http://chimera.labs.oreilly.com/books/1230000000393/ch04.html

