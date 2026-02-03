class bank :
    def transaction(self) :
        print("total transaction value ")
    def account_opening(self):
        print("this will show you your account open status ")
    def deposite(self):
        print("this will show your deposited amount")

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print("this will show you all the transaction happend to icici throuhg hdfc")

class icici(HDFC_bank):
    pass

i = icici()
i.hdfc_to_icici()
i.deposite()
i.account_opening()
i.transaction()