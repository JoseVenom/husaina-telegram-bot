from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, darkblue, grey
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Try to register a Chinese font if available
def register_chinese_font():
    """Register Chinese font if available on the system"""
    try:
        # Linux (Render) - common Chinese fonts
        font_paths = [
            '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc',  # WenQuanYi Micro Hei
            '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
            '/System/Library/Fonts/PingFang.ttc',  # macOS
            'C:\\Windows\\Fonts\\msyh.ttc',  # Windows - Microsoft YaHei
            'C:\\Windows\\Fonts\\simsun.ttc',  # Windows - SimSun
        ]
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                pdfmetrics.registerFont(TTFont('ChineseFont', font_path))
                return 'ChineseFont'
        
        # Fallback to Helvetica (no Chinese support)
        return 'Helvetica'
    except:
        return 'Helvetica'

def create_pdf(filename, user_data):
    """
    Generate bilingual employment agreement PDF
    """
    
    # Register Chinese font
    chinese_font = register_chinese_font()
    
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    y = height - 50
    
    # ===== HEADER =====
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(darkblue)
    c.drawString((width - c.stringWidth("EMPLOYMENT AGREEMENT", "Helvetica-Bold", 18)) / 2, y, "EMPLOYMENT AGREEMENT")
    
    # Chinese header
    y -= 20
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 16)
    c.drawString((width - 100) / 2, y, "雇佣协议")
    
    y -= 30
    c.setFont("Helvetica", 10)
    c.setFillColor(black)
    
    # ===== COMPANY INFO =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Company Information / 公司信息")
    y -= 20
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Company Name / 公司名称: Husaina Parkson")
    y -= 20
    c.drawString(50, y, f"Project Name / 项目名称: Work From Home Project")
    y -= 20
    c.drawString(50, y, f"Supervisor / 主管: Jose")
    y -= 30
    
    # ===== EMPLOYEE DETAILS =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Employee Details / 员工信息")
    y -= 20
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Employee Name / 员工姓名: {user_data.get('name', 'N/A')}")
    y -= 20
    c.drawString(50, y, f"Passport/ID No. / 身份证或护照号码: {user_data.get('passport', 'N/A')}")
    y -= 20
    c.drawString(50, y, f"Start Date / 入职日期: {user_data.get('start_date', 'N/A')}")
    y -= 30
    
    # ===== SECTION 1 =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "1. Position and Employment Status")
    y -= 18
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "职位与雇佣状态")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "The Employee is hired by Husaina Parkson under the Work From Home Project managed by Supervisor Jose.")
    y -= 15
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "员工受聘于 Husaina Parkson 远程办公项目，由主管 Jose 负责管理。")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "The first three (3) months shall be considered a temporary/probationary period.")
    y -= 15
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "前三(3)个月为临时/试用期。")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "Upon successful completion of the probationary period, the Employee may be confirmed as a permanent employee.")
    y -= 15
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "试用期顺利完成后，员工可转为正式员工。")
    y -= 25
    
    # ===== SECTION 2 =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "2. Working Hours")
    y -= 18
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "工作时间")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "The Employee shall work twelve (12) hours per day according to the work schedule assigned by the Supervisor.")
    y -= 15
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "员工每日工作十二(12)小时，并按照主管安排的工作时间表执行。")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "All work activities shall be monitored and controlled by the Supervisor.")
    y -= 15
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "所有工作活动均由主管监督和管理。")
    y -= 25
    
    # ===== SECTION 3 =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "3. Work From Home Requirements")
    y -= 18
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "居家办公要求")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "This position is strictly work-from-home based.")
    y -= 15
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "本职位为居家远程办公岗位。")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "The Employee must arrange and maintain their own:")
    y -= 15
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "员工需自行准备并维护：")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(60, y, "- Personal Computer (PC)")
    y -= 15
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(60, y, "- 个人电脑(PC)")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(60, y, "- Stable Internet Connection")
    y -= 15
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(60, y, "- 稳定网络连接")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(60, y, "- Necessary working environment")
    y -= 15
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(60, y, "- 必要的办公环境")
    y -= 25
    
    # Continue with remaining sections (simplified for brevity - you can keep the full version)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "4. Salary and Benefits")
    y -= 18
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "薪资与福利")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "Basic Salary: 800 USDT per month during probation, 950 USDT after confirmation.")
    y -= 15
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "基本工资: 试用期每月 800 USDT，转正后每月 950 USDT")
    y -= 25
    
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "5. Resignation Policy")
    y -= 18
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "辞职规定")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "Resignation during probation period requires 500 USDT compensation fee.")
    y -= 15
    c.setFont(chinese_font if chinese_font != 'Helvetica' else "Helvetica", 10)
    c.drawString(50, y, "试用期内辞职需支付 500 USDT 补偿费用。")
    y -= 30
    
    # ===== SIGNATURES =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Signatures / 签字")
    y -= 25
    
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "Company Representative / 公司代表:")
    y -= 20
    c.drawString(70, y, "Name: Jose")
    y -= 15
    c.drawString(70, y, "Signature: ___________________")
    y -= 15
    c.drawString(70, y, f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    y -= 30
    
    c.drawString(50, y, "Employee / 员工:")
    y -= 20
    c.drawString(70, y, f"Name: {user_data.get('name', 'N/A')}")
    y -= 15
    c.drawString(70, y, "Signature: ___________________")
    y -= 15
    c.drawString(70, y, f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    
    c.save()
    return filename