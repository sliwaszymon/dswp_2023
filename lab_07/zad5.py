def foo(vals: dict[str, list[int]], func) -> dict[str, list[int]]: 
    return dict(sorted(vals.items(), key=lambda x: func(x[1]), reverse=True))
    
print(foo({'Jan': [2,1,3,7], 'Justyna': [14, 12, 3], 'Czarek': [4, 20]}, max))