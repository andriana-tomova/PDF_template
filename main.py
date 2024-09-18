from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4" )

df = pd.read_csv("topics.csv")

print(df)
print(df.columns)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"],align="L", ln=1)
    pdf.line(10, 22, 200, 22)
    print(index, row["Topic"])

pdf.output("output.pdf")
