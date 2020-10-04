class Student:
    def setvalue(self, first, last, enroll):
        self.fname = first
        self.lname = last
        self.roll = enroll

st1 = Student()
st2 = Student()

st1.setvalue("neeraj", "sharma", 31)



print(st1.fname)
print(st1.lname)