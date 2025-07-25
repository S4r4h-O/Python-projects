from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")


def generate_receipt_pdf(product, price):
    pdf.add_page()
    pdf.set_font(family="Times", size=12)
    pdf.cell(w=50, h=8, txt="Receipt nr 101", ln=1)
    pdf.cell(w=12, h=12, txt=f"Article: {product}", ln=1)
    pdf.cell(w=12, h=12, txt=f"Price: {price}", ln=1)
    pdf.output("receipt.pdf")
