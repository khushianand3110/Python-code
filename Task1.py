# Original: {'a': 1, 'b': 2, 'c': 3}
# Inverted: {1: 'a', 2: 'b', 3: 'c'}
a={'a': 1, 'b': 2, 'c': 3}
b={value:key for key,value in a.items()}
print (b)