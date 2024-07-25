class bank_account:
    def __init__(self,acc_no,name,bal):
        self.acc_no=acc_no
        self.name=name
        self.bal=bal
        
        
    def deposit(self,amt):
        self.amt=amt
        self.bal=self.bal+self.amt
        return self.bal
    
    def withdraw(self,amt):
        self.amt=amt
        self.bal=self.bal-self.amt
        return self.bal
    
bc=bank_account(101,'madhuri',5000)
print(bc.deposit(100))
print(bc.withdraw(100))

