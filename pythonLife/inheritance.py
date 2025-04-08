# single inheritance, multiple
class parent():
    def p(self):
        print("IAM A PARENT")

class child(parent):
    def c(self):
        print("IAM A CHILD")

ch = child()
ch.p()
ch.c()

#multiple

class father():
    def f(self):
        print("am father")
class mother():
    def m(self):
        print("am mother")

class children(father, mother):
    def c1(self):
        print("am a child")

child = children()
child.f()
child.m()
child.c1()