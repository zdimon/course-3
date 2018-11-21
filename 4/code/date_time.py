#!/usr/bin/python
# -*- coding: utf-8 -*-
import time;  # This is required to include time module.

ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks

localtime = time.localtime(time.time())
print "Local current time :", localtime
print "Local current year :", localtime.tm_year

localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime 

import calendar

cal = calendar.month(2008, 1)
print "Here is the calendar:"
print cal

import datetime

print datetime.date(2012, 12, 14).year

print datetime.date.today().year

a = datetime.datetime(2017, 3, 5)
print(a) # datetime.datetime(2017, 3, 5, 0, 0)

today = datetime.date.today()
print( today.strftime("%m/%d/%Y") )



now = datetime.datetime.now()
 
then = datetime.datetime(2017, 2, 26)
 
# Кол-во времени между датами.
delta = now - then
 
print(delta.days) # 38
print(delta.seconds) # 1131

print now + datetime.timedelta(days=10)

# pip install dateutils

from dateutil.relativedelta import relativedelta

print today + relativedelta(months=1)


import time
 
for x in range(5):
    print x
    time.sleep(1)
    
    

