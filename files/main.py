class Bill ():
    """
    Object that cointains data aobut a bill, 
    such as a total amount and period of the bill 
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate():
    """
    Create flatmate person who lives in flate and pay a share of the bills
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays (self, bill):
        return bill.amount/2

class PdfReport():
    """
    Create Pdf-s file that contains data about the flatmate such as their names,
    their due amounts,and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate (self, flatmate1, flatmate2, bill):
        pass
        #self.flatmate1 = flatmate1
        #self.flatmate2 = flatmate2
        #self.bill = bill

the_bill = Bill (amount = 120, period = "March 2021")
John = Flatmate (name= "John", days_in_house =120)
Marry = Flatmate (name ="Marry", days_in_house =25)

print (John.pays(bill=the_bill))