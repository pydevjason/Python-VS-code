# this is known as an anti-pattern among Python developers because of increasing chances of name collision especially among larger code bases 

from calculator import *

print(developer)
print(add(10, 10))
print(subtract(3, 5))

# any variable preceded by an underscore _ will not be exported out of a module and will not be able to be pulled in using asterisk * syntax

