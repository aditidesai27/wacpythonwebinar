class Student:
    institute = "WAC"
    def __init__(self, first, last, enroll):
        self.fname = first
        self.lname = last
        self.roll = enroll

    def fullname(self):
        return self.fname + " " + self.lname


class Sci_student(Student):
    def __init__(self, first, last, enroll, lab):
        super().__init__(first, last, enroll)
        self.lab = lab
        


st1 = Sci_student("Neeraj", "Sharma", 31, ["chemistry", "physics", "biology"])
st2 = Student("Test", "User", 41)
# print(isinstance(st1, Sci_student))
# print(isinstance(st1, Student))


print(isinstance(st2, Sci_student))
print(isinstance(st2, Student))
