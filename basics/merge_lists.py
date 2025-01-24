def merge_lists(a: list, b:list)-> list:
    return sorted(set(a + b))


a = [1,2,3,4,2,7,5]
b = [4,1,9,8,7,6]
c = merge_lists(a, b)
print(c)