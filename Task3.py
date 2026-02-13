# Nested Dictionary "Flattener"
# The Challenge: Write a recursive function that takes a deeply nested dictionary and flattens it
# into a single-level dictionary where keys are concatenated with dots.
# Example Input: {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
# Example Output: {"a": 1, "b.c": 2, "b.d.e": 3}
# The Goal: Handle edge cases like empty dictionaries or lists within the values.

def flatten(data, new=""):
    result = {}
    for i in data:
        value = data[i]
        if new == "":
            key = i
        else:
            key = new + "." + i
        if type(value) == dict:
            b = flatten(value, key)
            result.update(b)
        else:
            result[key] = value
    return result


data = {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
print(flatten(data))