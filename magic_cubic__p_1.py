class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def checkIndex(self,key):
        if not isinstance(key, int):
            raise TypeError
        if key < 0:
            raise IndexError

    def __getitem__(self, item):
        print('getItem be called')
        self.checkIndex(item)
        try:
            return self.changed[item]
        except KeyError:
            return self.start+self.step*item

    def __setitem__(self,key,value):
        print('setItem be called')
        self.checkIndex(key)
        self.changed[key] = value

s = ArithmeticSequence()
print(s[6])
s[3] = 'hello'
print(s[3])
del s[3]
