from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas

def create_invoice(filename, invoice_data):
    c = canvas.Canvas(filename, pagesize=LETTER)

    c.drawString(50,750,"Invoice: #{invoice_number}")
    c.drawString(50, 730, f"Customer: {invoice_data['customername']}")

    c.save()

invoiceNumber = 1

if invoiceNumber < 10:
    invoiceNumber = f"00{invoiceNumber}"
elif invoiceNumber < 100:
    invoiceNumber = f"0{invoiceNumber}"
else:
    invoiceNumber = str(invoiceNumber)

create_invoice(f"invoice{invoiceNumber}.pdf", invoice_data)