import sys

def add(*args, **kwarg):

    for k,v in kwarg.items():
        print k+'-'+str(v)
        
        
    sys.exit('Done')
    rez = 0
    for i in args:
        rez += i
    return rez
    
    
    
    
    
try:    
    print add(1,2,2,3,4, one=1, two=2)
except Exception, e:
    print 'Fail %s' % e   

print 'Done'
