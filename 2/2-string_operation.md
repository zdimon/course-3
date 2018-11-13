##String operations.

https://docs.python.org/2/library/string.html


Строка это как и все в питоне - обьект.
Обьект класса string.
Раз объект то должны быть методы.
Методы подстановки значения

### Formating

    s = 'hello %s' % 'dima'
    d = 'hello %s your number is %d' % ('dima', '4')

Форматирование
    

    '{}, {}, {}'.format('a', 'b', 'c')  # 2.7+ only
    '{0}, {1}, {2}'.format('a', 'b', 'c')
    '{2}, {1}, {0}'.format('a', 'b', 'c')

###Accessing arguments by name

    'Coordinates: {latitude}, {longitude}'.format(latitude='37.24', longitude='-115.81')

###Outputs

    'Coordinates: 37.24, -115.81'

###Alternative sintax

    coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
    print 'Coordinates: {latitude}, {longitude}'.format(**coord)

### Repr function

The repr module provides a means for producing object representations with limits on the size of the resulting strings. 
This is used in the Python debugger.


    "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
    "repr() shows quotes: 'test1'; str() doesn't: test2"


###Converting

        "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
        'int: 42;  hex: 2a;  oct: 52;  bin: 101010'


Type 	Meaning

'b' 	Binary format. Outputs the number in base 2.
'c' 	Character. Converts the integer to the corresponding unicode character before printing.
'd' 	Decimal Integer. Outputs the number in base 10.
'o' 	Octal format. Outputs the number in base 8.
'x' 	Hex format. Outputs the number in base 16, using lower- case letters for the digits above 9.
'X' 	Hex format. Outputs the number in base 16, using upper- case letters for the digits above 9.
'n' 	Number. This is the same as 'd', except that it uses the current locale setting to insert the appropriate number separator characters.


        '{:,}'.format(1234567890)
        '1,234,567,890'

###Float number formating

    points = 19.5
    total = 22
    'Correct answers: {:.2%}'.format(points/total)

###Output

    'Correct answers: 88.64%'

###Data formating

    import datetime
    d = datetime.datetime(2010, 7, 4, 12, 15, 58)
    '{:%Y-%m-%d %H:%M:%S}'.format(d)
    n = datetime.date.today()
    '{:%Y-%m-%d}'.format(n)
    n = datetime.datetime.now()
    '{:%Y-%m-%d %H:%M:%S}'.format(n)



len() - длинна
доступ по индексу s[2]

Срезы

    s[1:4]



https://docs.python.org/2/library/stdtypes.html#string-methods
    


###Разбиение 

    s = 'one,two,three'.split(',')

###Слияние

    '-'.join(s)

###Замена

    '1 2 3 abc'.replace('abc', '4')

###Search

    string.find(s)
    string.rfind(s)

Return the lowest index  where the s is found. Return -1 on failure. 
   
    string.index(s)

Like find() but raise ValueError when the substring is not found.


    string.count(s)

Return the number of occurrences of substring s in string

Register

str.capitalize() str.lower() str.upper()


###Converting

###int() float() long()


###str.translate(table[, deletechars])

 The method translate() returns a copy of the string in which all characters have been translated using table (constructed with the maketrans() function in the string module), optionally deleting all characters found in the string deletechars.

Parameters

    table -- You can use the maketrans() helper function in the string module to create a translation table.

    deletechars -- The list of characters to be removed from the source string.


    #!/usr/bin/python

    from string import maketrans   # Required to call maketrans function.

    intab = "aeiou"
    outtab = "12345"
    trantab = maketrans(intab, outtab)

    str = "this is string example....wow!!!";
    print str.translate(trantab)


###tr.strip([chars])

    Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace.



    '   spacious   '.strip()
    'spacious'
    'www.example.com'.strip('cmowz.')
    'example'







