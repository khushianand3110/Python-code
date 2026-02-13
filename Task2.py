# The Advanced Inversion (One-to-Many)
# In the real world, dictionaries often have duplicate values. If you use the method above on {'a':
# 1, 'b': 1}, the second '1' will overwrite the first, and you'll lose data.
# To invert correctly, you must map the value to a list of keys.

# Problem: Write a function that inverts a dictionary where the values are lists, such as {"Python":
# ["Alice", "Bob"], "Java": ["Bob", "Charlie"]}.
# Goal: The output should show which languages each person knows: {"Alice": ["Python"], "Bob":
# ["Python", "Java"], "Charlie": ["Java"]}.

a={"Python": ["Alice", "Bob"], "Java": ["Bob", "Charlie"]}
result={}
for i in a:
    for j in a[i]:
        if j not in result:
            result[j]=[]
        result[j].append(i)
print(result)