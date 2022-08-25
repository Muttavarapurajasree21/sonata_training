class Student:
    def __init__(self,student_id,student_name,):
        self.stdid=student_id
        self.stdname=student_name



    def getStud(self):
         return self.stdid , self.stdname

st=Student(22784, 'rajasree')
s=st.getStud();
print(s)
setattr(st,'student_class',10)
print(getattr(st,'student_class'))
delattr(st,'stdname')
print(hasattr(st,'stdname'))
setattr(st,'student_class',20)
print(getattr(st,'student_class'))