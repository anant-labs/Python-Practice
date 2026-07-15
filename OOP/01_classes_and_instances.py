class Employee:
    def __init__ (self,first,last,pay) :
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'
    def fullname(self) : 
        return '{} {}' .format(self.first,self.last)

emp_1 = Employee('Anant','Mathur', 90000)
emp_2 = Employee('Rohit','Gupta', 50000)
emp_3 = Employee('Keshav','Rao', 75000)

print(emp_1.fullname())
print(emp_2.fullname())
print(emp_3.fullname())

print(emp_1.email)
print(emp_2.email)
print(emp_3.email) 



