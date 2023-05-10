from fpdf import FPDF

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

    def pays (self, bill,flatmate2):

        weight = self.days_in_house /(self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PdfReport():
    """
    Create Pdf-s file that contains data about the flatmate such as their names,
    their due amounts,and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate (self, flatmate1,flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2)))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1)))

        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        #Insert name and due amount of the first flatemate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=1, ln=1)

        #Insert name and due amount of the first flatemate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=1, ln=1)

        #Insert Period lable and value
        pdf.cell(w=100, h=40, txt="Period", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        pdf.output(self.filename)


the_bill = Bill (amount = 120, period = "April 2021")
John = Flatmate (name= "John",days_in_house=20)
Marry = Flatmate (name ="Marry", days_in_house =25)

print ("John pays", John.pays(bill=the_bill, flatmate2=Marry))
print ("Marry pays", Marry.pays(bill=the_bill,flatmate2=John))


pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=John, flatmate2=Marry, bill=the_bill)