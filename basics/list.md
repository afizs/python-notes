## Python List functions with examples: 

Function Name | Function Description | Function Example (Input) | Function Example (Output)
--- | --- | --- | ---
`append()` | Adds an element to the end of the list. | `my_list = [1, 2, 3]`<br>`my_list.append(4)` | `[1, 2, 3, 4]`
`extend()` | Adds elements from another iterable to the end of the list. | `my_list = [1, 2, 3]`<br>`my_list.extend([4, 5, 6])` | `[1, 2, 3, 4, 5, 6]`
`insert()` | Inserts an element at a specific index. | `my_list = [1, 2, 4, 5]`<br>`my_list.insert(2, 3)` | `[1, 2, 3, 4, 5]`
`remove()` | Removes the first occurrence of an element from the list. | `my_list = [1, 2, 3, 2]`<br>`my_list.remove(2)` | `[1, 3, 2]`
`pop()` | Removes and returns an element at a specific index (default is the last element). | `my_list = [1, 2, 3]`<br>`my_list.pop(1)` | `[1, 3]`
`index()` | Returns the index of the first occurrence of an element in the list. | `my_list = [1, 2, 3]`<br>`my_list.index(2)` | `1`
`count()` | Returns the number of times an element appears in the list. | `my_list = [1, 2, 2, 3]`<br>`my_list.count(2)` | `2`
`sort()` | Sorts the elements in the list. | `my_list = [3, 1, 2]`<br>`my_list.sort()` | `[1, 2, 3]`
`reverse()` | Reverses the order of the elements in the list. | `my_list = [1, 2, 3]`<br>`my_list.reverse()` | `[3, 2, 1]`
`copy()` | Returns a copy of the list. | `my_list = [1, 2, 3]`<br>`new_list = my_list.copy()` | `[1, 2, 3]` (in `new_list`)
