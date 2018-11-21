

class Jumpable(object):
    def jump(self):
        print 'JUMP!!'


class Jumpnotable(object):
    def jump(self):
        print 'NO JUMP!!'
        

class Animal(object):
    color = 'Red'
    weight = '20 kg'
    name = None
    jump_behavior = None
    def __init__(self, name):
        print 'Initialisation'
        self.name = name
    
    def move(self):
        print 'I am moving'
        
    def  jump(self):
        self.jump_behavior.jump()    
        
    def sayname(self):
        print 'My name is %s' % self.name
   
class Dumdog(Animal,Jumpnotable):
    pass
    

            
        
class Dog(Animal):

    def __init__(self,name):
        self.jump_behavior = Jumpable()

    def display(self):
        print 'Dog display'
    
        
class Cat(Animal):

    def __init__(self,name):
        self.jump_behavior = Jumpable()

    def display(self):
        print 'Cat display'       
        
dog = Dog('Barry')
cat = Cat('Murzik')
d = Dumdog('Dum')
dog.jump()
d.jump()

