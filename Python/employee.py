from employee import Employee
from empaddress import Address

add1=Address('guntur', '52205')
add2=Address('banglore', '52205')
e1 = Employee("raja", "sree", "hyd")
e2 = Employee("raja", "sree",[add1, add2])
print(e1.fullname())
print(e1.getname())
print(e2.fullname())