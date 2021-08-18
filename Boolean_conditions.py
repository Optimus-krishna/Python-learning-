#Boolean is like telling  Python to do something based on conditions:
 #if this is true, do this; else do something different.

#conditional logic in Python is written  using booleans (True and False), along with if statements.

user = 'James Bond'
if user == 'James Bond':
    print('Awesome!')
elif user == 'Ethan Hunt':
    print('Cool!')
else:
    print('Nope!')

#Python also allows you to use words like 'or', 'and', and 'not' for comparison

if 30 > 40 or 40 > 30:
    print("yeah!")

if 1 == 1 and 2 == 2:
    print("hmmm!")

if not False:
    print("not False is oviously True ")

# inequalities  can be represented together without using the 'and' keyword:


if 30 < 40 and 40 < 50:
    print("this is ok")

if 30 < 40 < 50:
    print("this is better!")



print("""Python does not require parenthesis around conditions,
 but each condition must end with a :.
If you forget the colon , you'll get a SyntaxError.""")