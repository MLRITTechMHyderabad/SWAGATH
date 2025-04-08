d = {1: 'abc', 'x': 69, 999:'omkar_annaya'}

print(d.get(999))
print(d['x'])

print(d.keys())

print(d.values())

print(d.items())

#update

d.update({'e': 00})
print(d)

for i,j in d.items():
    print(i,j)