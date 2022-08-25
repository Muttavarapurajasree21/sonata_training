class Leave:
    def __init__(self, empID, name, lbal):
        self.Employeeid = empID
        self.Name = name
        self.LeaveBalance = lbal

    def applyleave(self):
        return self.Employeeid, self.Name, self.LeaveBalance