class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        total=sum(self.marks)
        count=0
        for i in self.marks:
            count+=1
        avg=total/count
        print(avg)
s1=Student("Mannat",[99,90,93])
print(s1.name)
s1.get_avg()
a=input("ENTER NAME OF THE STUDENT: ")
b=tuple(int(input("ENTER MARKS OF THE STUDENT: ")))
s2=Student(a,b)
print(s2.name)
s2.get_avg()