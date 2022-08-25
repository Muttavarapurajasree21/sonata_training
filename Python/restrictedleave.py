from leave import Leave
class RestrictedLeave(Leave):
    def __init__(self,empID, name,dob):
        super().__init__(empID, name, dob)
        self.dob=dob

    def ApplyLeave(self):
        return self.dob