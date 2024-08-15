values_list = [1, 'number', [1, 2, 3]]
values_list_2 = [1, 'error']
values_dict = {'a': 3, 'b': 'fiter', 'c': 124324}


def print_params(a=1, b='asus', c=True):
    print(a, b, c)

print_params()
print_params(1, 'stop')
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
