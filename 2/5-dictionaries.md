##Dictionaries

    #!/usr/bin/python

    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    print dict['Name']

Each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces.


    dict = {1: 'one', 2: 'two'}
    print dict[1]
    print dict[3]

    Traceback (most recent call last):
      File "dict_ex.py", line 3, in <module>
        print dict[3]
    KeyError: 3

    print dict.get(3,'no')

###Updating Dictionary

    

    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    dict['Age'] = 8; # update existing entry
    dict['School'] = "DPS School"; # Add new entry


###Delete Dictionary Elements

    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    del dict['Name']; # remove entry with key 'Name'
    dict.clear();     # remove all entries in dict
    del dict ;        # delete entire dictionary

Keys must be immutable.


    dict = {['Name']: 'Zara', 'Age': 7}


    Traceback (most recent call last):
       File "test.py", line 3, in <module>
          dict = {['Name']: 'Zara', 'Age': 7};
    TypeError: list objects are unhashable




###Built-in List Functions


    cmp(tuple1, tuple2)


Compares elements of both tuples.
	

    len(dict)


Gives the total length of the tuple.


    str(dict)

Produces a printable string representation of a dictionary

    type(variable)

Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.

	
    dict(var)

    a = dict(one=1, two=2, three=3)

    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

    d = dict([('two', 2), ('one', 1), ('three', 3)])


    

###Built-in Dictionary Methods

    dict.clear()

Removes all elements of dictionary dict.


    dict.copy()

Returns a shallow copy of dictionary dict.
    

    dict.fromkeys(seq[, value])

Create a new dictionary with keys from seq and values set to value.

    seq = ('name', 'age', 'sex')
    val = (10,20,30)
    dict = dict.fromkeys(seq,val)
    print dict
    >> {'age': (10, 20, 30), 'name': (10, 20, 30), 'sex': (10, 20, 30)}

    dict.get(key, default=None)

For key key, returns value or default if key not in dictionary

	
    dict.has_key(key)

Returns true if key in dictionary dict, false otherwise

	
    dict.items()

Returns a list of dict's (key, value) tuple pairs


    dict = {1:'one', 2:'two'}
    print dict.items()
    >> [(1, 'one'), (2, 'two')]


    dict.keys()

Returns list of dictionary dict's keys


    dict.setdefault(key, default=None)

Similar to get(), but will set dict[key]=default if key is not already in dict

    dict = {1:'one', 2:'two'}
    print dict.setdefault(2, None)
    print dict.setdefault(3, None)
    >> two
    >> None


    dict.update(dict2)

Adds dictionary dict2's key-values pairs to dict


    dict.update({3:'thre', 4:'four'})
    print dict 

     >>   {1: 'one', 2: 'two', 3: 'thre', 4: 'four'}



    dict.values()

Returns list of dictionary dict's values
    
    >> ['one', 'two', 'thre', 'four']
    
    
    
    
    
    

