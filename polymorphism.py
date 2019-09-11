# ploly = many ... morphism = form
# used in ***
#     1)loose coupling,2)Dependency injection. 3)interfaces

# 4 ways to implement
#  1) Duck Tuping
#  2) operator overloading
#  3) Method overloading
#  3) Method overriding




# 1) Duck Tuping
'''
duck typing is same as pasing object in java but in java we specify  the object type
but in pyton pading object is dynamic means pass any object referance
but passing object have same behaviour that specify in the place where we use
e.g
we use execute method from the referance object and no matter which class referance it is what must it pass referance hace execute method thats all
'''


class pycharem :

    def execute(self):
        print("can able ro do ")
        print("compile")
        print("run")
class notepad:

    def execute(self):
        print("simple Editor")
        print("no editng ")
        print("no compiling")

class pyPizza:

    def execute(self):
        print("compiling")
        print("running")
        print("debuging")
        print("code folding")


class Editor:
    def codeEditor(self,ide):
        ide.execute()
pc = pycharem()
np = notepad()
pp = pyPizza()

edit = Editor()
edit2 = Editor()
edit3 = Editor()
edit.codeEditor(pc)
print("note pad *******")
edit2.codeEditor(np)
print("pypizza ********")
edit3.codeEditor(pp)














class A:
    def __init__(self):
        self.var1 = "A call var"
        print("calss A init")
    def feature1(self):
        print("feature A-1")
    def feature2(self):
        print("feature A-2")




class B(A):

    def __init__(self):
        super().__init__()
        print("class B init")
        super(A, self).__init__()
        self.var2 = "B class var"

    def feature3(self):
        print("feature B-1")
    def feature4(self):
        print("feature B-2")




class C:
    def __init__(self):
        self.var3="C class var"
        print("class C init")
    def feature5(self):
        print("feature C-1")
    def feature6(self):
        print("feature C-2")




# multiple Inheritance
#     MRO=> method resolutoin order .. will call first its left class init
class D(B,C):
    def __init__(self):
        super(D,self).__init__()# or old method B.__init__(self)
        # B.__init__(self) # B call its grand parent
        # C.__init__(self)
        print("class D init")
        self.var4="D class var"
    def feature7(self):
        print("feature D-1")
    def feature8(self):
        print("feature D-2")




# 2) operator over loading
'''
operator is same but operator is going to change 
e.d 2+2 = 4 , "2"+"2"="22"

'''
# Python Program to perform addition
# of two complex numbers using binary
# + operator overloading.

class complex:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	# adding two objects
	def __add__(self, other):
		return self.a + other.a, self.b + other.b

	def __str__(self):
		return self.a, self.b

Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2     # it treated as complex.__add__(ob1,ob2)
print(Ob3)









# 2) Method over riding and overloading
'''
==> overloading is not supported/present in py but some how we manage it indirect logically
==> overRiding same as uses parent method and change behaviour 
 


'''


# over loading
class stu:
    def __init__(self,m,mm):
        self.m = m
        self.mm = mm
    def sum(self,a=None, b=None, c=None):#if a=None it will not consider as parameter until caller pass the value
        s=0
        if a != None and b !=None and c != None:
            s=a+b+c
        elif a != None and b !=None:
            s = a + b
        else:
            s = a

        return s

# objects
s = stu(20,30)
print("method over loading solution, max argument 3 minimum1 :::",s.sum(1,2))


# overRiding
class A:
    def show(self):
        print("in parent show")
class B(A):
    def show(self):
        print("in child show changed ")
b= B()
b.show()










# iterator
#     n = [1,5,6,9,8,7,4]
#     it = iter(n)
#     print(it.__next__())
#     print(it.__next__())
#
#     class topTen:
#
#         def __init__(self):
#             self.num = 1
#         def __iter__(self):
#             return self
#         def __next__(self):
#             if self.num <= 0 :
#                 val = self.num
#                 self.num += 1
#                 return val
#             else:
#                 raise StopIteration
#
#     v= topTen()
#     print(next(v))
#     for i in v:
#         print(i)

# generator
#     # A Python program to demonstrate use of
#     # generator object with next()
#
#     # A generator function
#     def simpleGeneratorFun():
#         yield 1
#         yield 2
#         yield 3
#
#
#     # x is a generator object
#     x = simpleGeneratorFun()
#
#     # Iterating over the generator object using next
#     print(x.next());  # In Python 3, __next__()
#     print(x.next());
#     print(x.next());