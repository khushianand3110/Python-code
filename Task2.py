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