##Decorators

Decorators dynamically alter the functionality of a function, method or class without having to directly use subclasses. 
This is ideal when you need to extend the functionality of functions that you don't want to modify. 




What you need to know about functions
Before diving in, there are some prerequisites [priːˈrekwəzɪt] (предпосылки) that should be clear. 


###Assign functions to variables

    def greet(name):
        return "hello "+name

    greet_someone = greet
    print greet_someone("John")

    # Outputs: hello John


###Define functions inside other functions

    def greet(name):
        def get_message():
            return "Hello "

        result = get_message()+name
        return result

    print greet("John")

    # Outputs: Hello John


###Functions can be passed as parameters to other functions


    def greet(name):
       return "Hello " + name 

    def call_func(func):
        other_name = "John"
        return func(other_name)  

    print call_func(greet)

    # Outputs: Hello John


###Functions can return other functions
In other words, functions generating other functions.



    def compose_greet_func():
        def get_message():
            return "Hello there!"

        return get_message

    greet = compose_greet_func()
    print greet()

    # Outputs: Hello there!


###Inner functions have access to the enclosing scope.

Notice how we modified the example above to read a "name" argument 
from the enclosing scope of the inner function and return the new function.


    def compose_greet_func(name):
        def get_message():
            return "Hello there "+name+"!"

        return get_message

    greet = compose_greet_func("John")
    print greet()

    # Outputs: Hello there John!



###Composition of Decorators
Putting the ideas mentioned above together, we can build a decorator.
In this example let's consider a function that wraps the string output of another function by p tags.

    def get_text(name):
       return "Hello, {0}".format(name)

    def p_decorate(func):
       def func_wrapper(name):
           return "<p>{0}</p>".format(func(name))
       return func_wrapper

    my_get_text = p_decorate(get_text)

    print my_get_text("John")

    # <p>Hello, John</p>

That was our first decorator. A function that takes another function as an argument, generates a new function, changing the work of the original function, and returning the generated function so we can use it anywhere. To have get_text itself be decorated by p_decorate, we just have to assign get_text to the result of p_decorate.
    

###Python's Decorator Syntax

    def p_decorate(func):
       def func_wrapper(name):
           return "<p>{0}</p>".format(func(name))
       return func_wrapper

    @p_decorate
    def get_text(name):
       return "lorem ipsum, {0} dolor sit amet".format(name)

    print get_text("John")

    # Outputs <p>lorem ipsum, John dolor sit amet</p>

Now let's consider we wanted to decorate our get_text function by 3 other functions.



    def p_decorate(func):
       def func_wrapper(name):
           return "<p>{0}</p>".format(func(name))
       return func_wrapper

    def strong_decorate(func):
        def func_wrapper(name):
            return "<strong>{0}</strong>".format(func(name))
        return func_wrapper

    def div_decorate(func):
        def func_wrapper(name):
            return "<div>{0}</div>".format(func(name))
        return func_wrapper

With the basic approach, decorating get_text would be along the lines of


    get_text = div_decorate(p_decorate(strong_decorate(get_text)))


With Python's decorator syntax, same thing can be achieved with much more expressive power.




    @div_decorate
    @p_decorate
    @strong_decorate
    def get_text(name):
       return "lorem ipsum, {0} dolor sit amet".format(name)

    print get_text("John")

    # Outputs <div><p><strong>lorem ipsum, John dolor sit amet</strong></p></div>


Decorator with arguments.


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













