#create an empty set
s = set()

#Add some elements to the sets
s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)
#cannot add duplicate member to the set
s.add(3)
print(s)

s.remove(2)
print(s)

print(f"The set has {len(s)} elements.")