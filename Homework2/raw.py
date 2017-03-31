# class Sample:
# 	def __init__(self):
# 		print "Constructor"

# 	def sampleMethod(self):
# 		print "Hello There"

# 	@classmethod
# 	def sampleMethod1(self):
# 		print "Hello There"		

# if __name__ == '__main__':
# 	print "Main method"
# 	s = Sample()
# 	s.sampleMethod()
# 	Sample.sampleMethod1()


class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x    

a=A()