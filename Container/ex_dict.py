movie = {'name':'Burning', 'type':'movie', 'year':2018}

for key in movie:
    print(key, movie[key])

for key, value in movie.items():
    print(key, value)

try:
    rating = movie['rating']
except KeyError:
    rating = 0
print(rating)

print(movie.get('rating',0))

movie.setdefault("actors", []).append("bob")
movie.setdefault('actors',[]).append("mary")

for key, value in movie.items():
    print(key, value)

movie.pop('actors', None)

d1 = {'foo': 3, 'bar': 4}
var = {key: value * 10 for key, value in d1.items() if key == 'foo'}