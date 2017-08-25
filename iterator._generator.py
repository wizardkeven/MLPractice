class Fibs:

    def __init__(self):
        self.a = 0
        self.b = 1

            
    def __iter__(self):
        return self
    
    def __next__(self):# in python 2 use: next(self)
        self.a, self.b = self.b, self.a+self.b
        if self.a > 1000:
            raise StopIteration
        else:
            return self.a

# generator with recurrence for unknown nested layers data and string supported
def flatten(nested):
    try:
        try:
            nested+''
        except TypeError:
            pass;
        else: raise TypeError('element can not be string')

        
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested

nested = [[1,2], [3,4,[5,[6,7]]],[8,'I love china']]
#nested = 'I love china'
#lst = list(flatten(nested))
#print(lst)
for num in flatten(nested = nested):
    print(num)


#fibs = Fibs()
#for f in fibs:
#    print(f)
