from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4" )
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

print(df)
print(df.columns)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"],align="L", ln=1)
    for i in range(22, 288, 6):
        pdf.line(10, i, 200, i)
    print(index, row["Topic"])

    # Set footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(180, 180, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"],align="R", ln=1)


    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Set footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="B", size=10)
        pdf.set_text_color(180, 180, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)
        for i in range(22, 288, 6):
            pdf.line(10, i, 200, i)


pdf.output("output.pdf")
