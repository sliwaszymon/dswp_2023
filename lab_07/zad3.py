def foo(vals: list[int | str], reversed=False) -> list[int | str]:
    nums = list(filter(lambda x: isinstance(x, int), vals))
    strs = list(filter(lambda x: isinstance(x, str), vals))
    nums = list(sorted(nums))
    strs = list(sorted(strs, key=lambda x: len(x)))
    if not reversed:
        return nums+strs
    return strs[::-1] + nums[::-1]

print(foo([1,2,2135,'jaś',-1,'zupa'], True))