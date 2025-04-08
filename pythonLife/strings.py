str = "python programming"
# print(len(str))  O/p: 18

print(type(str))
# str

print(str.upper())

print(str.lower())

print(str.startswith("py")) # true

print(str.endswith("p")) #false

print(str.replace('programming', 'swagath'))

print(str.index('thon')) # 2 , if not found gives value error

print(str.find('on')) # if not found gives -1

print(str.split()) # converts the string into a list => ['python', 'programming']

print(str[::-1]) # reversing a string

print(str.count('p')) #how many p's => gives the count of p's