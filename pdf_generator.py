import os
from datetime import datetime
from pdfrw import PdfReader, PdfWriter, PageMerge
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def create_overlay(user_data):
    """Create an overlay with the user's data to place on the PDF"""
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    
    # Set font and size for the data fields
    c.setFont("Helvetica", 11)
    
    # Position these coordinates based on your PDF template
    # You'll need to adjust these X,Y coordinates to match where fields are on your PDF
    
    # Example coordinates - YOU MUST ADJUST THESE!
    # To find correct coordinates, print the PDF and measure or trial/error
    
    c.drawString(150, 650, user_data.get('name', '_________________'))
    c.drawString(150, 620, user_data.get('passport', '_________________'))
    c.drawString(150, 590, user_data.get('start_date', '_________________'))
    c.drawString(150, 560, datetime.now().strftime('%Y-%m-%d'))  # Today's date
    
    c.save()
    packet.seek(0)
    return packet

def create_pdf(filename, user_data):
    """
    Fill existing EMPLOYMENTAGREEMENT.pdf with user data
    """
    # Path to your existing PDF template
    template_path = "EMPLOYMENTAGREEMENT.pdf"
    
    if not os.path.exists(template_path):
        # If template doesn't exist, create a simple one
        return create_simple_pdf(filename, user_data)
    
    # Create overlay with user data
    overlay_packet = create_overlay(user_data)
    overlay_pdf = PdfReader(overlay_packet)
    
    # Read the template
    template_pdf = PdfReader(template_path)
    
    # Merge overlay onto each page
    writer = PdfWriter()
    for page in template_pdf.pages:
        overlay = PageMerge().add(overlay_pdf.pages[0])[0]
        PageMerge(page).add(overlay).render()
        writer.addpage(page)
    
    # Save the filled PDF
    writer.write(filename)
    return filename

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