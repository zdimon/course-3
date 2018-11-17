# Аргументы

    def add(x,y):
        print 'Result %s' % str(x+y)
        

    add(2,4)


    def add(x=1,y=4):
        print 'Result %s' % str(x+y)


    add()    
        
        
    def addAll(first,*args):
        rez = 0
        for i in args:
            rez = rez + i
        print 'Result %s' % str(rez)
        
        
    addAll(2,3,4,5,67)

    def greet_me(**kwargs):
        for key, value in kwargs.items():
            print("{0} = {1}".format(key, value))
            
            
    def universe(*args,**kwargs):
        for a in args:
            print 'List arg: %s' % a
           
        for k,v in kwargs.items():
            print 'key: %s  value: %s' % (k,v)
            
            
    universe(1,2,3,name='Dima')
