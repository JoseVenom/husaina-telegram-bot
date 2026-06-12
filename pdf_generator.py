import os
from datetime import datetime
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def create_filled_pdf(template_path, output_path, user_data):
    """
    Fill the PDF template with user data
    """
    # Create an overlay with the user data
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    
    # Set font
    c.setFont("Helvetica", 11)
    
    # === POSITION COORDINATES (X, Y) ===
    # These coordinates need to be adjusted based on your PDF
    # Y=0 is bottom of page, Y=792 is top of page (Letter size)
    
    # Page 1 - Employee details (around top section)
    # Based on your PDF, these are approximate positions
    c.drawString(350, 710, user_data.get('name', '_________________'))  # Employee Name
    c.drawString(350, 685, user_data.get('passport', '_________________'))  # Passport ID
    c.drawString(300, 660, user_data.get('start_date', '_________________'))  # Start Date
    
    # Page 1 - Supervisor signature area (bottom of page 1)
    # Adjust these coordinates
    c.drawString(400, 200, "Jose")  # Supervisor Name
    c.drawString(400, 180, datetime.now().strftime('%Y-%m-%d'))  # Date
    
    # Save the overlay
    c.save()
    packet.seek(0)
    overlay_pdf = PdfReader(packet)
    
    # Read the template
    template = PdfReader(open(template_path, 'rb'))
    writer = PdfWriter()
    
    # Merge overlay onto first page
    page = template.pages[0]
    page.merge_page(overlay_pdf.pages[0])
    writer.add_page(page)
    
    # Add remaining pages without changes
    for i in range(1, len(template.pages)):
        writer.add_page(template.pages[i])
    
    # Write the output
    with open(output_path, 'wb') as output:
        writer.write(output)
    
    return output_path

def create_pdf(filename, user_data):
    """
    Main function to create filled PDF
    """
    template_path = "EMPLOYMENTAGREEMENT.pdf"
    
    # Check if template exists
    if not os.path.exists(template_path):
        # If template not found, create a simple backup
        return create_simple_pdf(filename, user_data)
    
    return create_filled_pdf(template_path, filename, user_data)

def create_simple_pdf(filename, user_data):
    """
    Fallback: Create simple PDF if template not found
    """
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    y = height - 50
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "EMPLOYMENT AGREEMENT")
    
    y -= 40
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Employee Name: {user_data.get('name', '_____________')}")
    y -= 25
    c.drawString(50, y, f"Passport/ID: {user_data.get('passport', '_____________')}")
    y -= 25
    c.drawString(50, y, f"Start Date: {user_data.get('start_date', '_____________')}")
    y -= 25
    c.drawString(50, y, f"Agreement Date: {datetime.now().strftime('%Y-%m-%d')}")
    
    y -= 50
    c.drawString(50, y, "Signature: ___________________")
    c.save()
    return filename