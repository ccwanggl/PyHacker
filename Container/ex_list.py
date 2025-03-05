courses = ['Math', 'Physical', 'Educational']

# Index start with default
for index, s in enumerate(courses):
    print(index, s)

# index start with 'start' parameter
for index, s in enumerate(courses, start = 10):
    print(index, s)

numbers = [1, 2, 3, 4, 5]
results = [n * 100 for n in numbers if n % 2 == 0]

print(results)

# Add element to list
def add_list(in_func_obj):
    print(f'In add [before]: {in_func_obj} = "{in_func_obj}"')
    in_func_obj += ['baz']
    print(f'In add [after]: {in_func_obj} = "{in_func_obj}"')

orig_obj = ['foo', 'bar']
print(f'Outside [before]: orig_obj = "{orig_obj}"')
add_list(orig_obj)
print(f'Outside [after]: orig_obj = "{orig_obj}"')