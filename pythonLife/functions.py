def f_name(a,b):
    print("swag", a,b)
f_name(1,2)

def fun(a,b):
    return a+b
print(fun(10,20))

def func(*a): #gives output in the form of tuple
    print("hai",a)
func(1,2,3) 

def outer(a,b):
    print(a+b)
    def inner(a,b):
        print(a-b)
    inner(20,10)
outer(10,20)