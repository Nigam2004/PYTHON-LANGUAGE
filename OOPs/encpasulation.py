class bank_acc:
    def __init__(self,acc_holder_name,acc_no,balance):
        self.acc_holder_name=acc_holder_name
        self.acc_no=acc_no
        self.__balance=balance  #private variable
        # self.balance= -->public variavle
        # self._balance= -->protected variable
        # self.__balance= -->private variable
    def check_balance(self):
         return  self.__balance
    def withdrawl(self,amount):
        if amount>self.__balance:
            return "insufficient balance"
        else:
           self.__balance-=amount
           return f"withdral success \n available balance is {self.__balance}"
    def deposite(self,dip_amount):
        self.__balance+=dip_amount
        return f"current available balance is {self.__balance}"
        
    

acc1=bank_acc("nigam",123,1000)
acc1.balance=5000   
print(acc1.withdrawl(500))
print(acc1.deposite(200))



