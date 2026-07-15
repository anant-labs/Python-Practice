class Employee :
    num_of_emps = 0 
    raise_pay = 1.05

    def __init__ (self,first,last,pay):
        self.first = first 
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@employeenetwork.com'

        Employee.num_of_emps += 1 

    def fullname (self) :
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_pay)
    
emp_1 = Employee('Madhavi','Sharma',98000)
emp_2 = Employee('Raj','Yadav', 58000)
emp_3 = Employee('Harshit','Singhal',90000)

print(emp_1.fullname())
print(emp_2.fullname())
print(emp_3.fullname())

print(emp_1.email)
print(emp_2.email)
print(emp_3.email)

emp_1.raise_pay = 1.08

emp_1.apply_raise()
print("emp_1 pay", emp_1.raise_pay , emp_1.pay)

emp_2.apply_raise()
print("emp_2 pay", emp_2.raise_pay , emp_2.pay)

emp_3.apply_raise()
print("emp_3 pay", emp_3.raise_pay , emp_3.pay)

print(Employee.num_of_emps)




