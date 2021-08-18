print("Variables store certain values that can change ")

x = 20
y = 'This is new variable'
print(x)
print(y)
x= 35
print(x)
# new value can be assigned to any variable and the newly assigned
#will be its value


a,b = 5,6

print(a,b)
#can also do multiple assignment
# with variables separated by a comma.

print("""Naming Requirements of Variables
Variables in Python are required to start with a letter or an underscore.
The rest of the name must consist of letters, numbers, or underscores
Names are case-sensitive""")

#printing multiple lines put """ lines """

print("""Naming Conventions
Most variable names should be written in lower_snake_case. This means that all words should be lowercase, and words should be separated by an underscore.
CAPITAL_SNAKE_CASE usually refers to constants
UpperCamelCase usually refers to a class (more on that later)
Variables that start and end with two underscores (called "dunder" for double underscore) are intended to be private or are builtins to the language""")

myVariable = 3.14  # more like a JavaScript variable!
my_variable = 3.14  # much better
AVOGADRO_CONSTANT = 6.022140857 * 10 ** 23  # https://en.wikipedia.org/wiki/Avogadro_constant
__no_touch__ = 3.14  # someone doesn't want you to mess with this!

#To indicate an absence of value, variable can be assigned to the value None.

nothing = None #here  variable 'nothing' doesnot have any value not even zero , 