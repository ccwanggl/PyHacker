name = ('foo', 'bar', 'baz')
print(name)

def get_rectangle():
    width = 100
    height = 200
    return width, height

result = get_rectangle()
print(result, type(result))

results = tuple((n *100 for n in range(10) if n % 2 == 0))
print(results)

user_info = ('piglei', 'MALE', 30, True)
print(user_info[2])

from collections import namedtuple
Rectangle = namedtuple('Rectangle', 'width height')
rect = Rectangle(100, 100)
print(rect.width, rect.height)