class Student:
    institute = "WAC"
    def __init__(self, first, last, enroll):
        self.fname = first
        self.lname = last
        self.roll = enroll

    def fullname(self):
        return self.fname + " " + self.lname

    @classmethod
    def fromstring(cls, string):
        fname, lname, roll = string.split(" ")
        return cls(fname, lname, roll)

string = "Abhishek joshi 45"


st2 = Student.fromstring(string)





