from datetime import datetime
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
import os

def create_filled_pdf(template_path, output_path, user_data):
    """
    Fill the PDF template with user data
    """
    # Create an overlay with the user's data
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    
    # Set font
    c.setFont("Helvetica", 11)
    
    # ===== COORDINATES FOR YOUR PDF (LETTER SIZE: 612 x 792) =====
    # Y=0 is bottom, Y=792 is top of page
    
    # Page 1 - Employee details (top section, right side)
    # Adjust these coordinates as needed
    c.drawString(350, 710, user_data.get('name', '_________________'))      # Employee Name
    c.drawString(350, 685, user_data.get('passport', '_________________'))   # Passport/ID
    c.drawString(300, 660, user_data.get('start_date', '_________________')) # Start Date
    
    # Page 3 - Signatures (bottom of last page)
    c.drawString(150, 250, user_data.get('name', '_________________'))       # Employee Name (signature)
    c.drawString(150, 230, datetime.now().strftime('%Y-%m-%d'))              # Date
    
    c.save()
    packet.seek(0)
    
    # Read the template
    template = PdfReader(open(template_path, 'rb'))
    writer = PdfWriter()
    
    # Merge overlay onto first page
    overlay_pdf = PdfReader(packet)
    page1 = template.pages[0]
    page1.merge_page(overlay_pdf.pages[0])
    writer.add_page(page1)
    
    # Add remaining pages without changes
    for i in range(1, len(template.pages)):
        writer.add_page(template.pages[i])
    
    # Write the output
    with open(output_path, 'wb') as output:
        writer.write(output)
    
    return output_path

def create_simple_pdf(filename, user_data):
    """Fallback: Create a simple PDF if template not found"""
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "EMPLOYMENT AGREEMENT")
    
    y -= 40
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Company: Husaina Parkson")
    y -= 25
    c.drawString(50, y, f"Project: Work From Home Project")
    y -= 25
    c.drawString(50, y, f"Supervisor: Jose")
    
    y -= 40
    c.drawString(50, y, f"Employee Name: {user_data.get('name', '_____________')}")
    y -= 25
    c.drawString(50, y, f"Passport/ID: {user_data.get('passport', '_____________')}")
    y -= 25
    c.drawString(50, y, f"Start Date: {user_data.get('start_date', '_____________')}")
    
    y -= 50
    c.drawString(50, y, "Signature: ___________________")
    y -= 20
    c.drawString(50, y, f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    
    c.save()
    return filename

def create_pdf(filename, user_data):
    """
    Main function - fills the existing PDF template with user data
    """
    template_path = "EMPLOYMENTAGREEMENT.pdf"
    
    # Check if template exists
    if os.path.exists(template_path):
        try:
            return create_filled_pdf(template_path, filename, user_data)
        except Exception as e:
            print(f"Error filling PDF: {e}")
            return create_simple_pdf(filename, user_data)
    else:
        print(f"Template {template_path} not found, using simple PDF")
        return create_simple_pdf(filename, user_data)