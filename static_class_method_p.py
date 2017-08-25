class MyClass:
    @staticmethod
    def method1():
        print('this is a static method')

    @classmethod
    def method2(cls):
        print('this is a class method of ',cls)


MyClass.method1()
MyClass.method2()
