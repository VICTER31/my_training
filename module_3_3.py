def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [23, "лист", False]
values_dict = {'a' : 12, 'b' : 'словарь', 'c' : True}
values_list2 = [ 56, False]
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, 42)