class bank_acc:
    def __init__(self,acc_holder_name,acc_no,balance):
        self.acc_holder_name=acc_holder_name
        self.acc_no=acc_no
        self.balance=balance
    def check_balance(self):
         return  self.balance
    def withdrawl(self,amount):
        if amount>self.balance:
            return "insufficient balance"
        else:
           self.balance-=amount
           return f"withdral success \n available balance is {self.balance}"
    def deposite(self,dip_amount):
        self.balance+=dip_amount
        return f"current available balance is {self.balance}"
        
    

s=bank_acc("nigam",123,1000)
print(s.withdrawl(500))
print(s.deposite(200))



