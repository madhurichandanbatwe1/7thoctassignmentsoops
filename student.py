class student:
    def __init__(self,id,name):
        self.id=id
        self.name=name 
        self.grade=[]
    def add_grade(self,grade):
        self.grade.append(grade)
        return self.grade
    def average_grade(self):
        if len(self.grade)>0:
            self.avg=sum(self.grade)/len(self.grade)
        return self.avg
    def display_details(self):
        print(f'Student info is {self.name},{self.id},{self.grade},{self.avg}')
        
nishi=student(10,'nishi')
nishi.add_grade(45)
nishi.add_grade(50)
nishi.add_grade(49)

nishi.average_grade()
nishi.display_details()
   