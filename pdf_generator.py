from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import black, darkblue
from reportlab.pdfgen import canvas
import os

def create_pdf(filename, user_data):
    """
    Generate a clean PDF agreement with user data
    """
    try:
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        
        y = height - 50
        
        # Title
        c.setFont("Helvetica-Bold", 18)
        c.setFillColor(darkblue)
        c.drawString((width - c.stringWidth("EMPLOYMENT AGREEMENT", "Helvetica-Bold", 18)) / 2, y, "EMPLOYMENT AGREEMENT")
        
        y -= 45
        c.setFont("Helvetica", 11)
        c.setFillColor(black)
        
        # Company Info
        c.drawString(50, y, "Company Name: Husaina Parkson")
        y -= 20
        c.drawString(50, y, "Project Name: Work From Home Project")
        y -= 20
        c.drawString(50, y, "Supervisor: Jose")
        
        y -= 30
        
        # Employee Details
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "Employee Details:")
        y -= 20
        c.setFont("Helvetica", 11)
        c.drawString(70, y, f"Employee Name: {user_data.get('name', '_________________')}")
        y -= 18
        c.drawString(70, y, f"Passport/ID No.: {user_data.get('passport', '_________________')}")
        y -= 18
        c.drawString(70, y, f"Nationality: {user_data.get('nationality', '_________________')}")
        y -= 18
        c.drawString(70, y, f"Start Date: {user_data.get('start_date', '_________________')}")
        
        y -= 35
        
        # Section 1
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "1. Position and Employment Status")
        y -= 20
        c.setFont("Helvetica", 10)
        c.drawString(50, y, "The Employee is hired by Husaina Parkson under the Work From Home Project managed by Supervisor Jose.")
        y -= 16
        c.drawString(50, y, "The first three (3) months shall be considered a temporary/probationary period.")
        y -= 16
        c.drawString(50, y, "Upon successful completion, the Employee may be confirmed as a permanent employee.")
        
        y -= 30
        
        # Section 2
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "2. Working Hours")
        y -= 20
        c.setFont("Helvetica", 10)
        c.drawString(50, y, "The Employee shall work twelve (12) hours per day according to the schedule assigned.")
        y -= 16
        c.drawString(50, y, "All work activities shall be monitored and controlled by the Supervisor.")
        
        y -= 30
        
        # Section 3
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "3. Work From Home Requirements")
        y -= 20
        c.setFont("Helvetica", 10)
        c.drawString(50, y, "The Employee must arrange and maintain:")
        y -= 16
        c.drawString(65, y, "- Personal Computer (PC)")
        y -= 14
        c.drawString(65, y, "- Stable Internet Connection")
        y -= 14
        c.drawString(65, y, "- Necessary working environment")
        
        y -= 30
        
        # Section 4
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "4. Salary and Benefits")
        y -= 20
        c.setFont("Helvetica", 10)
        c.drawString(50, y, "During probationary period: Basic Salary 800 USDT per month")
        y -= 16
        c.drawString(50, y, "After completion: Basic Salary increases to 950 USDT per month")
        y -= 16
        c.drawString(50, y, "Additional performance-based incentives available.")
        
        y -= 30
        
        # Section 5
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "5. Resignation Policy")
        y -= 20
        c.setFont("Helvetica", 10)
        c.drawString(50, y, "If the Employee resigns during the probationary period, a compensation fee of")
        y -= 16
        c.drawString(50, y, "500 USDT shall be paid to the Company.")
        
        y -= 35
        
        # Signatures
        c.line(60, y, 250, y)
        c.drawString(60, y - 12, "Employee Signature")
        c.line(310, y, 500, y)
        c.drawString(310, y - 12, "Supervisor Signature")
        
        y -= 30
        c.drawString(60, y, f"Date: {datetime.now().strftime('%Y-%m-%d')}")
        
        c.save()
        
        if os.path.exists(filename):
            return filename
        return None
        
    except Exception as e:
        print(f"Error creating PDF: {e}")
        return None