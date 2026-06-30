class payment:
    def __init__(self,amount):
        self.amount=amount

    def pay(self):
        print ("You payment is prcessing...",self.amount)


class Credit_card_payment(payment):  #inherited from payment class
    def pay(self):
        print("Credit carad payment of",self.amount,":+2.5%  charge ")
class Upi_payment(payment):
   def pay(self):
        print("UPI  payment of",self.amount,"No fee applicable ")
        
card_payment=Credit_card_payment(500)
card_payment.pay()
    
upi=Upi_payment(20000)
upi.pay()