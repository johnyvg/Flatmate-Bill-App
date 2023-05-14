import webbrowser

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

        #Add icon
        pdf.image ("house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        #Insert Period lable and value
        pdf.set_font(family ="Times", size=14, style= "B")
        pdf.cell(w=100, h=40, txt="Period", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        #Insert name and due amount of the first flatemate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=0, ln=1)

        #Insert name and due amount of the first flatemate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=0, ln=1)



        pdf.output(self.filename)
        webbrowser.open(self.filename)
amount = float (input("Hey user, enter a bill amount"))
period = str(input ("What is a bill period"))

name1 =input ("What is your name" )
days_in_house1 = int(input (f"How many days did {name1} stay in the house"))

name2=input ("What is the name of the secend flatmate" )
days_in_house2 = int(input (f"How many days did {name2} stay in the house"))

the_bill = Bill (amount = amount, period = period)
flatmate1 = Flatmate (name1,days_in_house1)
flatmate2= Flatmate (name2 , days_in_house2)

print (f"{flatmate1.name1} pays", flatmate1.pays(the_bill,flatmate2))
print (f"{flatmate2.name2} pays", flatmate2.pays(the_bill,flatmate1))


pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)