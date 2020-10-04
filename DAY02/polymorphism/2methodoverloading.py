# method overloading is not supported
class Student:
    def __init__(self, first, last, marks):
        self.fname = first
        self.lname = last
        self.marks = marks

    def add(self, m1=None, m2=None, m3=None):
        if(m1!=None and m2 !=None and m3!= None):
            return m1+m2+m3
        else:
            return m1+m2
    
st1 = Student("Abhishek", "mishra", 23)


print(st1.add(5, 4, 6))
print(st1.add(5, 4))



