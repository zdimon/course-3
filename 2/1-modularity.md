
Issues to import.

    mylib.py

GLOBAL_DOMAIN = 'domain.com'

def getDomain():
    print 'My domain is %s' % GLOBAL_DOMAIN
    
class app():
    typeApp = 'angular+python'
    author = 'Dimitry'
    def getBody(self):
        html = '<body> this is %s application of %s</body>' % (self.typeApp, self.author)
        return html  
        

myapp.py

    import mylib
    import mypackage.mylib
    from mylib import GLOBAL_DOMAIN
    from mylib import GLOBAL_DOMAIN as D
    from mylib import *
    from mypackage.mylib import GLOBAL_DOMAIN
    
    
__init__.py

Files named __init__.py are used to mark directories on disk as Python package directories. 
The __init__.py file is usually empty, but can be used to export selected portions of the package under more convenient name


    #__init__.py
    
    from mylib import app
    myapp = app()
    
    # test.py
    
    from mypackage import myapp
    print myapp.getBody()    
