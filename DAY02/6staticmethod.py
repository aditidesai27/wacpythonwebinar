class Student:
    institute = "WAC"
    def __init__(self, first, last, enroll):
        self.fname = first
        self.lname = last
        self.roll = enroll

    def fullname(self):
        return self.fname + " " + self.lname

    @staticmethod
    def detail():
        return Student.institute





st = Student("Neeraj", "Sharma", 31)
print(st.detail())