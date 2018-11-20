
Нужно использовать скобки c object.

class MyClass(object):
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
        


def __init__(self):
    self.data = []
    
  
def __init__(self, realpart, imagpart):
    self.r = realpart
    self.i = imagpart
    
    
    
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        
        
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
 
# Наследование        
        
сlass DerivedClassName(modname.BaseClassName):

# Множественное наследование

lass DerivedClassName(Base1, Base2, Base3):

# Приватные члены 

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
        


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method
    __str = 'Hello'
    
m = Mapping([2,2])
print m.__str
#m.update([1,2,3])
print m.items_list


    def f(self):
        super(Mapping,self).f()
        
        

from abc import ABCMeta, abstractmethod
class Abstract:
    __metaclass__ = ABCMeta

    @abstractmethod
    def foo(self):
        pass
        
#a = Abstract()



class Geterseter(object):
    __name = None
    
    def __init__(self,name):
        self.__name = name  
    
    @property
    def name(self):
        print 'Get value %s' % self.__name
        return self.__name
        
      
        
    @name.setter
    def name(self,value):
        print 'Set value %s' % value
        self.__name = value
        
        
    def __setattr__(self, attrname, val):
        print '__setattr___'
        super(Geterseter, self).__setattr__(attrname, val)



    def __getattr__(self, attrname):
        print '___getattr___'
        return super(MyModel, self).__getattr__(attrname)      
        
        

   
