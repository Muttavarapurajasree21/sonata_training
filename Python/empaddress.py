class Address:
    def _init_(self,city,pincode):
        self.c=city
        self.p=pincode
    def getaddress(self):
         return self.city, self.pincode