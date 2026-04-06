class bank :
    def transaction(self) :
        print("total transaction value ")
    def account_opening(self):
        print("this will show you your account open status ")
    def deposite(self):
        print("this will show your deposited amount")


class HDFC_bank:
    def hdfc_to_icici(self):
        print("this will show you all the transaction happend to icici throuhg hdfc")
    def test(self):
        print("this will show you all the transaction happened to icici through hdfc")

class ineuron_bank :
    def account_status_icici(self):
        print("print account status in icici ")

class icici(HDFC_bank, bank, ineuron_bank) :
    pass

i = icici()
i.hdfc_to_icici()
i.transaction()
i.deposite()
i.account_opening()
i.test()
i.account_status_icici()
