from fpdf import FPDF
import pandas as pd

data = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit='mm', format='a4')
pdf.set_auto_page_break(auto=False, margin=0)
for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font(family="arial", style="B", size=22)
    pdf.set_text_color(60, 60, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], border="", align="L", ln=1)

    for y in range(20, 290, 10):
        pdf.line(x1=5, y1=y, x2=205, y2=y)
    pdf.ln(270)
    pdf.set_font(family="", style="I", size=10)
    pdf.set_text_color(160, 160, 160)
    pdf.cell(w=0, h=6, txt=row["Topic"], border="", align="R")
    for page in range(row['Pages']-1):
        pdf.add_page()
        for y in range(10, 290, 10):
            pdf.line(x1=5, y1=y, x2=205, y2=y)
        pdf.ln(280)
        pdf.set_font(family="", style="I", size=10)
        pdf.set_text_color(160, 160, 160)
        pdf.cell(w=0, h=6, txt=row["Topic"], border="", align="R")
pdf.output("output.pdf")
