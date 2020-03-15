# How many Sundays fell on the first of the month 
# during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import date

counter = [0,0,0,0,0,0,0]

for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        day = date(year, month, 1)
        counter[day.weekday()] += 1

print counter[6]

# Zeller's congruence can be used to find the day of the week for any date
