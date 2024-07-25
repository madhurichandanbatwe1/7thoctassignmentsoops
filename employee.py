class employee:
    def  __init__(self,emp_id,name,sal) :
        self.emp_id=emp_id
        self.name=name
        self.sal=sal
    
    def yearly_bonus(self,bonus):
        self.bonus=bonus
        return (self.sal*self.bonus)/100
    
    def  emp_details(self):
        print("emp_id",self.emp_id)
        print("name",self.name)
        print("salary",self.sal)

emp=employee(200,'rishi',160000)
print(emp.yearly_bonus(28))
print(emp.emp_details())
