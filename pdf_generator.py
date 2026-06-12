from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, darkblue, grey, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
import os

def register_chinese_font():
    """Register Chinese font if available on the system"""
    try:
        # Common Chinese font paths for different systems
        font_paths = [
            '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',  # Linux/Render
            '/System/Library/Fonts/PingFang.ttc',  # macOS
            'C:\\Windows\\Fonts\\msyh.ttc',  # Windows - Microsoft YaHei
            'C:\\Windows\\Fonts\\simsun.ttc',  # Windows - SimSun
        ]
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                pdfmetrics.registerFont(TTFont('ChineseFont', font_path))
                return 'ChineseFont'
        return 'Helvetica'
    except:
        return 'Helvetica'

def create_pdf(filename, user_data):
    """
    Generate bilingual employment agreement PDF
    """
    chinese_font = register_chinese_font()
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    # Title
    y = height - 50
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(darkblue)
    c.drawString((width - c.stringWidth("EMPLOYMENT AGREEMENT", "Helvetica-Bold", 22)) / 2, y, "EMPLOYMENT AGREEMENT")
    
    y -= 25
    c.setFont("Helvetica-Bold", 16)
    c.drawString((width - c.stringWidth("雇佣协议", "Helvetica-Bold", 16)) / 2, y, "雇佣协议")
    
    y -= 40
    c.setFont("Helvetica", 10)
    c.setFillColor(black)
    
    # Line separator
    c.setStrokeColor(grey)
    c.line(50, y + 5, width - 50, y + 5)
    
    # Company Information Section
    y -= 15
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(darkblue)
    c.drawString(50, y, "Company Information")
    y -= 18
    c.setFont(chinese_font, 12)
    c.drawString(50, y, "公司信息")
    
    y -= 22
    c.setFont("Helvetica", 11)
    c.setFillColor(black)
    c.drawString(50, y, f"Company Name / 公司名称: Husaina Parkson")
    y -= 20
    c.drawString(50, y, f"Project Name / 项目名称: Work From Home Project")
    y -= 20
    c.drawString(50, y, f"Supervisor / 主管: Jose")
    
    y -= 30
    
    # Employee Details Section
    c.setFont("Helvetica-Bold", 13)
    c.setFillColor(darkblue)
    c.drawString(50, y, "Employee Details")
    y -= 18
    c.setFont(chinese_font, 12)
    c.drawString(50, y, "员工信息")
    
    y -= 22
    c.setFont("Helvetica", 11)
    c.setFillColor(black)
    c.drawString(50, y, f"Employee Name / 员工姓名: {user_data.get('name', 'N/A')}")
    y -= 20
    c.drawString(50, y, f"Passport/ID No. / 身份证或护照号码: {user_data.get('passport', 'N/A')}")
    y -= 20
    c.drawString(50, y, f"Start Date / 入职日期: {user_data.get('start_date', 'N/A')}")
    
    y -= 35
    
    # Section 1
    c.line(50, y + 8, width - 50, y + 8)
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(black)
    c.drawString(50, y, "1. Position and Employment Status")
    y -= 18
    c.setFont(chinese_font, 11)
    c.drawString(50, y, "职位与雇佣状态")
    
    y -= 22
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "The Employee is hired by Husaina Parkson under the Work From Home Project managed by Supervisor Jose.")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(50, y, "员工受聘于 Husaina Parkson 远程办公项目，由主管 Jose 负责管理。")
    
    y -= 22
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "The first three (3) months shall be considered a temporary/probationary period.")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(50, y, "前三(3)个月为临时/试用期。")
    
    y -= 22
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "Upon successful completion of the probationary period, the Employee may be confirmed as a permanent employee.")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(50, y, "试用期顺利完成后，员工可转为正式员工。")
    
    y -= 30
    
    # Section 2
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "2. Working Hours")
    y -= 18
    c.setFont(chinese_font, 11)
    c.drawString(50, y, "工作时间")
    
    y -= 22
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "The Employee shall work twelve (12) hours per day according to the work schedule assigned by the Supervisor.")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(50, y, "员工每日工作十二(12)小时，并按照主管安排的工作时间表执行。")
    
    y -= 22
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "All work activities shall be monitored and controlled by the Supervisor.")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(50, y, "所有工作活动均由主管监督和管理。")
    
    y -= 30
    
    # Section 3
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "3. Work From Home Requirements")
    y -= 18
    c.setFont(chinese_font, 11)
    c.drawString(50, y, "居家办公要求")
    
    y -= 22
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "This position is strictly work-from-home based.")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(50, y, "本职位为居家远程办公岗位。")
    
    y -= 22
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "The Employee must arrange and maintain their own:")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(50, y, "员工需自行准备并维护：")
    
    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(60, y, "- Personal Computer (PC)")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(60, y, "- 个人电脑(PC)")
    
    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(60, y, "- Stable Internet Connection")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(60, y, "- 稳定网络连接")
    
    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(60, y, "- Necessary working environment")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(60, y, "- 必要的办公环境")
    
    y -= 35
    
    # Section 4
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "4. Salary and Benefits")
    y -= 18
    c.setFont(chinese_font, 11)
    c.drawString(50, y, "薪资与福利")
    
    y -= 22
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "During the probationary period:")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(50, y, "试用期间：")
    
    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(60, y, "- Basic Salary: 800 USDT per month")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(60, y, "- 基本工资：每月 800 USDT")
    
    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(60, y, "- Performance Incentives: Based on performance")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(60, y, "- 绩效奖金：根据工作表现发放")
    
    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(60, y, "- Attendance Bonus: Available according to attendance records")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(60, y, "- 出勤奖金：根据出勤情况发放")
    
    y -= 25
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "After successful completion of three (3) months:")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(50, y, "成功完成三个月试用期后：")
    
    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(60, y, "- Basic Salary will increase to 950 USDT per month")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(60, y, "- 基本工资调整为 950 USDT/月")
    
    y -= 25
    
    # Section 5 - Resignation Policy
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "5. Resignation Policy")
    y -= 18
    c.setFont(chinese_font, 11)
    c.drawString(50, y, "辞职规定")
    
    y -= 22
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "If the Employee resigns during the probationary period, the Employee agrees to pay")
    y -= 16
    c.drawString(50, y, "a compensation fee of 500 USDT to the Company.")
    y -= 16
    c.setFont(chinese_font, 10)
    c.drawString(50, y, "如员工在试用期提出辞职，员工同意向公司支付 500 USDT 的补偿费用。")
    
    y -= 35
    
    # Signatures
    c.line(50, y + 8, width - 50, y + 8)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Signatures")
    y -= 18
    c.setFont(chinese_font, 11)
    c.drawString(50, y, "签字")
    
    y -= 30
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Company Representative / 公司代表:")
    y -= 22
    c.setFont("Helvetica", 10)
    c.drawString(70, y, f"Name / 姓名: Jose")
    y -= 18
    c.drawString(70, y, "Signature / 签字: ___________________")
    y -= 18
    c.drawString(70, y, f"Date / 日期: {datetime.now().strftime('%Y-%m-%d')}")
    
    y -= 40
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Employee / 员工:")
    y -= 22
    c.setFont("Helvetica", 10)
    c.drawString(70, y, f"Name / 姓名: {user_data.get('name', 'N/A')}")
    y -= 18
    c.drawString(70, y, "Signature / 签字: ___________________")
    y -= 18
    c.drawString(70, y, f"Date / 日期: {datetime.now().strftime('%Y-%m-%d')}")
    
    y -= 40
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(grey)
    c.drawString(50, y, "Note: This agreement is legally binding upon signature.")
    y -= 12
    c.setFont(chinese_font, 9)
    c.drawString(50, y, "备注：本协议一经签字即具有法律效力。")
    
    c.save()
    return filename