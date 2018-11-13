##Python Lists

The most basic data structure in Python is the sequence.
The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets. 


    list1 = ['physics', 'chemistry', 1997, 2000];
    list2 = [1, 2, 3, 4, 5 ];
    list3 = ["a", "b", "c", "d"]
    lst = [i for i in range(30) if i % 3 == 0]

###Accessing Values in Lists

    print list1[0]
    print list2[1:5]


###Updating Lists

    
    list = ['physics', 'chemistry', 1997, 2000];
    print list[2] 
    list[2] = 2001;
    print list[2]

###Delete List Elements

    del list1[2];

###Basic List Operations

    
    len([1, 2, 3])	3	Length
    [1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	Concatenation
    ['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	Repetition
    3 in [1, 2, 3]	True	Membership
    for x in [1, 2, 3]: print x,	1 2 3	Iteration


###Built-in List Functions


    cmp(list1, list2)


Compares elements of both tuples.
	

    len(list)


Gives the total length of the tuple.

	
    max(list)


Returns item from the tuple with max value.
	
    min(list)


Returns item from the tuple with min value.
	
    list(seq)


###Built-in List Methods:


    list.append(obj)

Appends object obj to list.



    list.count(obj)


Returns count of how many times obj occurs in list.


    list.extend(seq)


Appends the contents of seq to list

    lst = [1,2,3]
    lst.extend([4,5,6])
    print lst
    >> [1, 2, 3, 4, 5, 6]


    list.index(obj)


Returns the lowest index in list that obj appears


    [1, 2, 3, 4, 5, 6]
    >>> print lst.index(2)
    1
    >>> print lst.index(4)
    3
    >>> print lst.index(44)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 44 is not in list


    list.insert(index, obj)


Inserts object obj into list at offset index.


    list.pop()


Removes and returns last object or obj from list.


    list.remove(obj)


Removes object obj from list.


    list.reverse()


Reverses objects of list in place.


    list.sort([func])


Sorts objects of list, use compare func if given.

    lst = [2,4,7,3,9]    

    def compare(it1,it2):
        if it1>it2:
            return 1
        else:
            return -1

    lst.sort(compare)
    print lst


Compare functions specifies a custom comparison function of two arguments (list items) which should return a negative, zero or positive number.

    [('c', 4), ('b', 2), ('a', 3)] => [('c', 4), ('a', 3), ('b', 2)]

    lst = [('c', 4), ('b', 2), ('a', 3)] 

    def letter_cmp(a, b):
        if a[1] > b[1]:
            return -1
        elif a[1] == b[1]:
            if a[0] > b[0]:
                return 1
            else:
                return -1
        else:
            return 1

    lst.sort(letter_cmp)
    print lst
    
    
# SET

    {1,2,3,4,1}
    
Единственное отличие set от frozenset заключается в том, что set - изменяемый тип данных, а frozenset - нет.


    

