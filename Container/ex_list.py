colors = ['red', 'blue', 'green', 'black', 'white']
colors.append('pink')
colors.pop()
colors.extend(['pink', 'purple'])
# slicing
# colors[start:stop:stride]
# start <= i < stop, colors[start:stop] has (stop - start) elements

rcolors = colors[::-1]
rcolors2 = list(colors)                     # new object that is a copy of colors in a different memory area
rcolors2.reverse()                          # in-place; reversing rcolors2 does not affect colors

courses = ['Math', 'Physical', 'Educational']

# Index start with default and get index of the list
for index, s in enumerate(courses):
    print(index, s)

# index start with 'start' parameter
for index, s in enumerate(courses, start = 10):
    print(index, s)

numbers = [1, 2, 3, 4, 5]
print("Deal list element with list comprehension")
results = [n * 100 for n in numbers if n % 2 == 0]
print(results)

def remove_odd_mul_100(numbers:list[int]) -> list[int]:
    results :list[int] = []
    for number in numbers:
        if number % 2 == 1:
            continue
        results.append(number * 100)
    return results

print("Deal list element with function remove_odd_mul_100()")
print(remove_odd_mul_100(numbers))

# Add element to list
def add_list(in_func_obj :list[str]):
    print(f'In add [before]: {in_func_obj} = "{in_func_obj}"')
    in_func_obj += ['baz']
    print(f'In add [after]: {in_func_obj} = "{in_func_obj}"')

orig_obj = ['foo', 'bar']
print(f'Outside [before]: orig_obj = "{orig_obj}"')
add_list(orig_obj)
print(f'Outside [after]: orig_obj = "{orig_obj}"')
