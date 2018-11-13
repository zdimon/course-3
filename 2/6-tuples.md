##Tuple operations

A tuple is a sequence of immutable Python objects. 

    tup1 = ('physics', 'chemistry', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5 )
    tup3 = "a", "b", "c", "d

To write a tuple containing a single value you have to include a comma.

    tup1 = (50,)


###Accessing Values in Tuples:

    print tup1[0]
    print tup2[1:5]


Tuples are immutable which means you cannot update or change the values of tuple elements. 
You are able to take portions of existing tuples to create new tuples as the following example.


    #!/usr/bin/python

    tup1 = (12, 34.56);
    tup2 = ('abc', 'xyz');

    # Following action is not valid for tuples
    # tup1[0] = 100;

    # So let's create a new tuple as follows
    tup3 = tup1 + tup2;
    print tup3

###Delete Tuple Elements

Removing individual tuple elements is not possible.


To explicitly remove an entire tuple, just use the del statement.


    tup = ('physics', 'chemistry', 1997, 2000);
    del tup;

###Basic Tuples Operations

Tuples respond to the + and * operators much like strings.


len((1, 2, 3))	3	Length
(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	Concatenation
('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	Repetition
3 in (1, 2, 3)	True	Membership
for x in (1, 2, 3): print x,	1 2 3	Iteration


###Built-in Tuple Functions
	
    cmp(tuple1, tuple2)


Compares elements of both tuples.
	

    len(tuple)


Gives the total length of the tuple.

	
    max(tuple)


Returns item from the tuple with max value.
	
    min(tuple)


Returns item from the tuple with min value.
	
    tuple(seq)


Converts a list into tuple.









