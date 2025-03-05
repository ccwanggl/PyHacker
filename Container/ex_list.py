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