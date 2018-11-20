## Python Date & Time

The function time.time() returns the current system time in ticks (seconds) since 12:00am, January 1, 1970(epoch).


    #!/usr/bin/python
    import time;  # This is required to include time module.

    ticks = time.time()
    print "Number of ticks since 12:00am, January 1, 1970:", ticks
    >> Number of ticks since 12:00am, January 1, 1970: 1462365232.58


However, dates before the epoch cannot be represented in this form. Dates in the far future also cannot be represented this way - the cutoff point is sometime in 2038 for UNIX and Windows.

Many of Python's time functions handle time as a tuple of 9 numbers, as shown below.

Index	Field	Values
0	4-digit year	2008
1	Month	1 to 12
2	Day	1 to 31
3	Hour	0 to 23
4	Minute	0 to 59
5	Second	0 to 61 (60 or 61 are leap-seconds)
6	Day of Week	0 to 6 (0 is Monday)
7	Day of year	1 to 366 (Julian day)
8	Daylight savings	-1, 0, 1


To translate a time instant from a seconds since the epoch floating-point value into a time-tuple, pass the floating-point value to a function (e.g., localtime) that returns a time-tuple with all nine items valid.


    #!/usr/bin/python
    import time;

    localtime = time.localtime(time.time())
    print "Local current time :", localtime
    print "Local current year :", localtime.tm_year

    >> Local current time : time.struct_time(tm_year=2016, tm_mon=5, tm_mday=4, tm_hour=15, tm_min=42, tm_sec=55, tm_wday=2, tm_yday=125, tm_isdst=1)
    >> Local current year : 2016


###Getting formatted time

You can format any time as per your requirement, but simple method to get time in readable format is asctime()

    #!/usr/bin/python
    import time;

    localtime = time.asctime( time.localtime(time.time()) )
    print "Local current time :", localtime    
    >> Local current time : Wed May  4 15:47:03 2016

###Getting calendar for a month
The calendar module gives a wide range of methods to play with yearly and monthly calendars. Here, we print a calendar for a given month ( Jan 2008 )


    #!/usr/bin/python
    import calendar

    cal = calendar.month(2008, 1)
    print "Here is the calendar:"
    print cal


    Here is the calendar:
        January 2008
    Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6
     7  8  9 10 11 12 13
    14 15 16 17 18 19 20
    21 22 23 24 25 26 27
    28 29 30 31


