a = 10

if a == 1:
    print(1)
elif a == 2:
    print(2)
else:
    print("A lot")


for i in range(3):
    print(i)

for word in ('cool', 'powerful', 'readable'):
    print('Python is %s' % word)

z =  1 + 1j
while abs(z) < 100:
    if z.imag == 0:
        break
    z = z**2 + 1

a = [1, 0, 2, 4]
for element in a:
    if element == 0:
        continue
    print(1. / element)

vowels = 'aeiouy'
for i in 'powerful':
    if i in vowels:
        print(i)

message = "Hello how are you?"
message.split()
for word in message.split():
    print(word)

words = ('cool', 'powerful', 'readable')
for index, item in enumerate(words):
    print((index, item))

d = {'a':1, 'b':1.2, 'c':1j}
for key, val in sorted(d.items()):
    print('Key: %s has value: %s' % (key, val))