# Example Input: {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
# Example Output: {"a": 1, "b.c": 2, "b.d.e": 3}
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