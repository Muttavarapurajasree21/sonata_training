from leave import Leave
class BasketOfLeave(Leave):
    def __init__(self, empID, name, lbal , applyleave):
        super().__init__(empID, name, lbal)
        self.Applyingleave=applyleave

    def applyleave(self):
        return self.applyleave