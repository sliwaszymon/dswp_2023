def foo(mieszana):
    ans = {}
    for x in mieszana:
        try:
            ans[str(type(x)).replace("<class '", "").replace("'>", "")].append(x)
        except KeyError:
            ans[str(type(x)).replace("<class '", "").replace("'>", "")] = [x]
    return ans

mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
print(foo(mieszana))