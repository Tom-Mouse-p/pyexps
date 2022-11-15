class College:
    def __init__(self, cname):
        self.cname = cname

    def read(self):
        print("College : ", self.cname)


class Teacher(College):
    def __init__(self, tname, cname):
        super().__init__(cname)
        self.tname = tname

    def read(self):
        print("College : ", self.cname)
        print("Teacher : ", self.tname)


class Principal(College):
    def __init__(self, pname, cname):
        super().__init__(cname)
        self.pname = pname

    def read(self):
        print("College : ", self.cname)
        print("Principal : ", self.pname)


class Student(Teacher, Principal):

    def __init__(self, sname):
        Teacher.__init__(cname=cname, tname=tname)
        Principal.__init__(pname=pname, cname=cname)
        self.sname = sname

    def read(self):
        print("College : ", self.cname)
        print("Teacher : ", self.tname)
        print("Principal : ", self.pname)
        print("Student : ", self.sname)


print("College Object : ")
c = College(cname="Pillai College of Engineering")
c.read()
print()
print("Teacher Object : ")
t = Teacher(cname="Pillai", tname="Leenata")
t.read()
print()
print("Principal Object : ")
p = Principal(cname="PCE", pname="Sameer Shahi")
p.read()
print()
print("Student Object : ")
s = Student(cname="Pillai College", pname="Sandeep Joshi", sname="Pranav Rajeevan", tname="Leenata Parab")
# print(t.cname, t.tname)
