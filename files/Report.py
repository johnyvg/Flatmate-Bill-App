import os
import webbrowser
import os
from fpdf import FPDF


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
        pdf.image ("files/house.png", w=30, h=30)

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

        # Change the directory to files, generate and open the PDF
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
