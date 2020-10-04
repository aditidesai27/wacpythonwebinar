class Student:
    def __init__(self, first, last, marks):
        self.fname = first
        self.lname = last
        self.marks = marks

    def __add__(self, obj):
        if(isinstance(obj, Student)):
            return self.marks + obj.marks
        else:
            return "error"

    # def __sub__(self,obj)
    # def __mul__(self,obj)
    # def __div__(self,obj)
    # def __gt__()
    # def __st__()
    # def __ge__()

    
st1 = Student("Abhishek", "mishra", 23)
st2 = Student("Aniket", "mishra", 25)

# print(st1+st2)

print(st1+2)


