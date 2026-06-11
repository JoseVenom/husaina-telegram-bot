
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(path, d):
    doc = SimpleDocTemplate(path)
    s = getSampleStyleSheet()
    c = []
    c.append(Paragraph("HUSAINA PARKSON", s["Title"]))
    c.append(Paragraph("雇佣协议 / Employment Agreement", s["Heading2"]))
    c.append(Paragraph(f"Employee: {d['full_name']}", s["Normal"]))
    c.append(Paragraph(f"Passport/ID: {d['passport']}", s["Normal"]))
    c.append(Paragraph(f"Nationality: {d['nationality']}", s["Normal"]))
    c.append(Paragraph(f"Recruiter: {d['recruiter']}", s["Normal"]))
    c.append(Spacer(1,12))
    text = """
    Work From Home Project. Supervisor: Jose.<br/>
    Working Hours: 12 hours per day.<br/>
    Employee must arrange PC and internet connection.<br/>
    First 3 months are probationary/temporary.<br/>
    Salary: 800 USDT + incentives + attendance bonus.<br/>
    After 3 months: 950 USDT basic salary.<br/>
    One day leave per week according to roster.<br/>
    Holiday requests available after 3 months and require 72 hours notice.<br/>
    Employee must inform management before resignation.<br/>
    Rewards and disciplinary actions apply according to company policy.<br/><br/>
    Employee Signature: ______________________<br/>
    Company Signature: ______________________
    """
    c.append(Paragraph(text, s["BodyText"]))
    doc.build(c)
