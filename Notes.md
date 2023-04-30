# To-Do
1. class diagrams
2. object diagrams
3. folder pathing
4. process diagram
4. README
    4.1 files
    4.1.1 file content
    4.2 documentation
    4.3 format file with correct syntax
5. repositories
6. templates
7. console testing
8. class behaviours
9. html templates

# README

Commands for installation
md syntax

# Testing
Check unittesting
    need different class properties?
    need more/different class functions?

# Classes
GymClass needs duration?







datetime

import datetime

string = "19 Nov 2015  18:45:00.000"
date = datetime.datetime.strptime(string, "%d %b %Y  %H:%M:%S.%f")

print date
Output would be:

2015-11-19 18:45:00
And you can access the desired values with:

>>> date.year
2015
>>> date.month
11
>>> date.day
19
>>> date.hour
18
>>> date.minute
45
>>> date.second
0