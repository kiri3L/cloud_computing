def my_sum(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    return arr[0] + my_sum(arr[1:])


print('Практика 1 задание 1')
print(my_sum([]))
print(my_sum([0]))
print(my_sum([0, 0]))
print(my_sum([1, 2, 3, 4]))
print(my_sum(['1', '2', '3', '4']))


def my_alpha_counter(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return {arr[0][0]: len(arr[0])}
    d = my_alpha_counter(arr[1:])
    d[arr[0][0]] = max(d.get(arr[0][0]) or 0, len(arr[0]))
    return d


print('Практика 1 задание 2')
l = ['a'*7, 'b'*3, 'b', 'b', 'd', 'a'*3, 'c'*9, 'a'*6, 'q'*17, 'q']
print(my_alpha_counter(l))
