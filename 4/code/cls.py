"help help"

class MyClass(object):
    """A simple example class"""
    i = 12345
    
    def f(self):
        print 'hello world'
        


class Mapping(MyClass):
    ''' ed wed we wedwe '''
    mv = 123
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        "updating ...."
        for item in iterable:
            self.items_list.append(item)
            
    def f(self):
        super(Mapping,self).f()
        
    @staticmethod
    def st():
        print 'Static method'
        
    @property
    def name(self):
        return self.__str+' Dima'
        
    def __call__(self):
        print 'I was called as func'
        
    def __str__(self):
        return 'My class'
       
    def __getattribute__(self,s):
        print 'Getting %s' % s
        x = super(Mapping,self).__getattribute__(s)
        return x

    __update = update   # private copy of original update() method
    __str = 'Hello'
    
    
m = Mapping([2,2])

mm = Mapping([2,2])
#print m.__str
Mapping.st()
m.st()
print m.name

print m


#import pdb; pdb.set_trace()

#m.update([1,2,3])
print m.items_list







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
        
        
ss = Geterseter('Dima')

import pdb; pdb.set_trace()


    




    
    
