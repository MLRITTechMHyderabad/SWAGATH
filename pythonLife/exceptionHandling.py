a = 10
try:
    print(a)
except:
    print("error")
else:
    print("no error")
finally:
    print('finally block')



s = 100
try:
    print(s +'a')
except TypeError:
    print("got type error")

except ValueError:
    print("got value error")