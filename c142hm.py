def linear_search(arr, target):
    iterations = 0
    for i in range(len(arr)):
        iterations +=1
        if arr[i] == target:
            print(f'--> found{target} at index{i} in {iterations} iteration(s) \n)')
            return i
    print(f'-->{target} not found after {iterations} iteration (s) \n')
    return -1
data = [10,20,30,40,50]
print('array:',data)
# best case target is in the beginning 0(1)
best_target =   10
best_index = linear_search(data,best_target)
print(f'best case -> searching {best_target}: found at index{best_index}')
# average case target is somewhere in the middle O(n)
avg_target = 30
avg_index = linear_search(data,avg_target)
print(f'average case -> searching {avg_target}: found in index{avg_index}')
# worst case target is at the end O(n)
worst_target = 50
worst_index = linear_search(data,worst_target)
print(f'worst case -> searching {worst_target}: found in index{worst_index}')