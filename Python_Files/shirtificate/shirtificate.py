from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("Times","BI", 50)
        self._pdf.set_fill_color(255, 255, 255)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(35)
        self._pdf.set_text_color(255,255,255)
        self._pdf.set_fill_color(240, 160, 70)
        self._pdf.text(x=60, y=150, txt = f"{name} took CS50")

    def save(self, name):
        self._pdf.output(name)

name = input("Please, enter your name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")