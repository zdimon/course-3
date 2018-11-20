

def maindecorator(tags,tage):
    def realdecorator(func): 
        def wrapper(name):
           return tags+ func(name) +tage      
        return wrapper
    return realdecorator
    
   
    
    

@maindecorator('<div>','</div>')
def getName(name):
    return name
    


       

#two = one    
    
######################
#r = one(getName)
#print r('Hello')
print getName('Dima')
#two()   
