class Test(object):

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

t1 = Test("foo", 42)
t2 = Test("foo", 42)
t3 = Test("bar", 42)

print t1, t2, t3
print t1 == t2
print t2 == t3




taking log in java
reading a file and store in hashmap
count dirs under certain folder

return max from 2 numbers
returninfg an object
