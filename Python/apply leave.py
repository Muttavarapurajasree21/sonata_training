from leave import Leave
from basketofleaves import BasketOfLeave
from restrictedleave import RestrictedLeave

l1=Leave(1212, "jaya", 20)
print(l1.applyleave())

l2=BasketOfLeave(2346, "rajasree", 50, "sick leave")
print(l2.applyleave())

l3=RestrictedLeave(2346, "rajasree", 2000)
print(l3.applyleave())