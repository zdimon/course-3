




def decorator(opentag,closetag):

    def real_decorator(decfunc):
    
        def wrapper(name):
            
            return opentag+' '+ decfunc(name) +' '+closetag
            
        return wrapper
        
    
    return real_decorator
   
@decorator('<h1>','</h1>') 
def myf(name):
    return name
    
    
print myf('Dima')
