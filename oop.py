class computer:

    def __init__(self,ram,cpu):
        # print(id(self))
        print(type(self).__name__)
        self.cpu=cpu
        self.ram=ram


com1 = computer("i5",8)
com2 = computer('i7',16)

print(type(computer).__name__)
print(type(com1).__name__)
print(type(com2).__name__)

# class var with class methods and instance with instance method

# Varables(class vs instance)******
# instance variable vs class var(static) : instance initilize in _init_ &property of an object and on the other hand clss var declaired and initilized out side the methods of all type and property of class remain same for all the objects

# Methods instance(instance)***
# instance method vs class metods : if method take parameter self it refers to instance b/c it takes object
# Accessor vs Mutator methods : if it fatch only result e.g avg()/get() or valye it is accessor and if it modifies values is mutator e.g update/set()
# no self no cls its static method

# class method and static method *****
#     class mehtod declaired with @classmethod and pass cls insted of seld
#     static method declaired with @staticmehtod and no pass of self or cls



class Student:
    # class variable same for all objects
    school = "Technical school of science green town "

    # instance variable dif for all objects
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    #  instace method call only by the object of the class
    def avg(self):
        return (self.m1+self.m2+self.m3)/3


    #  clss method any one can call
    @classmethod
    def getSchool(cls):
        return cls.school


    #  static method any one can call object and class var
    @staticmethod
    def info():
        print("this method retuen static and procide info only")



print("\n\nall in one ***************\n")
s1 = Student(2,22,222)
s2 = Student(3,33,333)

print("student1 average marks :: ",s1.avg())
print("student2 average marks :: ",Student.avg(s2))
print(Student.getSchool())
Student.info()








# inner class

class member:

    def __init__(self,name,rollno):
        self.name   = name
        self.rollno = rollno
        self.lap    = self.computerStu()

    def show(self):
        print(self.rollno, self.name)


    # object of inner class remain different  for both both with class name or with object of class
    class computerStu:

        def __init__(self):
            self.name = "Hp"
            self.cpu = "i5"

        def setName(self,name):
            self.name=name
        def getName(self):
            # print(self.name)
            return  self.name


        def setCpu(self,cpu):
            self.cpu=cpu
        def getCpu(self):
            # print(self.cpu)\
            return self.cpu
        def show(self):
            print(self.getName(), self.getCpu())

# clss obj
print("\n\ninner class*************")
s1 = member("Ahsan",78)
s2 = member("chudry" , 12)

s1.show()
s2.show()

# way 1 on object of inner class
lap = member.computerStu()
lap.setName("DELL")
lap.setCpu("i7")
lap.show()
print(id(lap.name))
print(id(lap))

# way 2 of access of inner class
    # s1.lap.show() #works
lap1 = s1.lap
lap1.setName("Accer")
lap1.setCpu("i3")
print(id(lap1))
print(id(lap1.name))
lap1.show()












# Iinheritancel sigle/mutiple/multilevel

# sigle level
#   if child calss dont have init then it will call the init of parent automatically . if has then it call its own e.g B




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





print("\n\n****************inheritance****************")

# SINGLE LEVEL
print("********single ************")
b = B()
b.feature1()
print(b.var1)


# MULTI-LEVEL
print("********multi-level************")

d= D()
# d.feature1()
# d.feature3()
# d.feature5()
# d.feature7()
# print(d.var3)













# class A:
#     def __init__(self):
#         print("-> A")
#         super(A, self).__init__()
#         print("<- A")
#
# class B:
#     def __init__(self):
#         print("-> B")
#         super(B, self).__init__()
#         print("<- B")
#
# class C(A, B):
#     def __init__(self):
#         print("-> C")
#         # Use super here, instead of explicit calls to __init__
#         super(C, self).__init__()
#         print("<- C")
#
# c=C()
