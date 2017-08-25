class ClassA:
    def __init__(self): #,value1 = ""
        print(type(self))
        self.name = "ClassA"
        print('this is ClassA init method')
        #print('value1 is %s'%value1)

    def say(self):
        print('I am %s'%self.name)

    def getName(self):
        return self.name


class ClassB(ClassA):
    
    def __init__(self):
        #ClassA.__init__(self)
        super(ClassB, self).__init__()
        print('this is ClassB init method')

    def say(self):
        print('I am ClassB')


a = ClassA()
a.say()
print(a.getName())

b = ClassB()
b.say()
print(b.getName())
