from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, darkblue, grey
from reportlab.pdfgen import canvas

def create_pdf(filename, user_data):
    """
    Generate bilingual employment agreement PDF
    
    user_data = {
        'name': 'John Doe',
        'passport': '123456789',
        'nationality': 'Sri Lanka',
        'start_date': '2026-03-26'
    }
    """
    
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    y = height - 50
    
    # ===== HEADER =====
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(darkblue)
    c.drawString((width - c.stringWidth("EMPLOYMENT AGREEMENT / 雇佣协议", "Helvetica-Bold", 18)) / 2, y, "EMPLOYMENT AGREEMENT / 雇佣协议")
    
    y -= 30
    c.setFont("Helvetica", 10)
    c.setFillColor(black)
    
    # ===== COMPANY INFO =====
    c.setFont("Helvetica", 11)
    c.drawString(50, y, f"Company Name / 公司名称: Husaina Parkson")
    y -= 20
    c.drawString(50, y, f"Project Name / 项目名称: Work From Home Project")
    y -= 20
    c.drawString(50, y, f"Supervisor / 主管: Jose")
    y -= 30
    
    # ===== EMPLOYEE DETAILS =====
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
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "职位与雇佣状态")
    y -= 18
    c.drawString(50, y, "The Employee is hired by Husaina Parkson under the Work From Home Project managed by Supervisor Jose.")
    y -= 15
    c.drawString(50, y, "员工受聘于 Husaina Parkson 远程办公项目，由主管 Jose 负责管理。")
    y -= 18
    c.drawString(50, y, "The first three (3) months shall be considered a temporary/probationary period.")
    y -= 15
    c.drawString(50, y, "前三（3）个月为临时/试用期。")
    y -= 18
    c.drawString(50, y, "Upon successful completion of the probationary period, the Employee may be confirmed as a permanent employee.")
    y -= 15
    c.drawString(50, y, "试用期顺利完成后，员工可转为正式员工。")
    y -= 25
    
    # ===== SECTION 2 =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "2. Working Hours")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "工作时间")
    y -= 18
    c.drawString(50, y, "The Employee shall work twelve (12) hours per day according to the work schedule assigned by the Supervisor.")
    y -= 15
    c.drawString(50, y, "员工每日工作十二（12）小时，并按照主管安排的工作时间表执行。")
    y -= 18
    c.drawString(50, y, "All work activities shall be monitored and controlled by the Supervisor.")
    y -= 15
    c.drawString(50, y, "所有工作活动均由主管监督和管理。")
    y -= 25
    
    # ===== SECTION 3 =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "3. Work From Home Requirements")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "居家办公要求")
    y -= 18
    c.drawString(50, y, "This position is strictly work-from-home based.")
    y -= 15
    c.drawString(50, y, "本职位为居家远程办公岗位。")
    y -= 18
    c.drawString(50, y, "The Employee must arrange and maintain their own:")
    y -= 15
    c.drawString(50, y, "员工需自行准备并维护：")
    y -= 18
    c.drawString(60, y, "• Personal Computer (PC)")
    y -= 15
    c.drawString(60, y, "• 个人电脑（PC）")
    y -= 18
    c.drawString(60, y, "• Stable Internet Connection")
    y -= 15
    c.drawString(60, y, "• 稳定网络连接")
    y -= 18
    c.drawString(60, y, "• Necessary working environment")
    y -= 15
    c.drawString(60, y, "• 必要的办公环境")
    y -= 25
    
    # ===== SECTION 4 =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "4. Salary and Benefits")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "薪资与福利")
    y -= 18
    c.drawString(50, y, "During the probationary period:")
    y -= 15
    c.drawString(50, y, "试用期间：")
    y -= 18
    c.drawString(60, y, "• Basic Salary: 800 USDT per month")
    y -= 15
    c.drawString(60, y, "• 基本工资：每月 800 USDT")
    y -= 18
    c.drawString(60, y, "• Performance Incentives: Based on performance")
    y -= 15
    c.drawString(60, y, "• 绩效奖金：根据工作表现发放")
    y -= 18
    c.drawString(60, y, "• Attendance Bonus: Available according to attendance records")
    y -= 15
    c.drawString(60, y, "• 出勤奖金：根据出勤情况发放")
    y -= 22
    
    c.drawString(50, y, "After successful completion of three (3) months:")
    y -= 15
    c.drawString(50, y, "成功完成三个月试用期后：")
    y -= 18
    c.drawString(60, y, "• Basic Salary will increase to 950 USDT per month")
    y -= 15
    c.drawString(60, y, "• 基本工资调整为 950 USDT/月")
    y -= 18
    c.drawString(60, y, "• Additional rewards may be granted based on outstanding performance.")
    y -= 15
    c.drawString(60, y, "• 表现优异者可获得额外奖励。")
    y -= 25
    
    # ===== SECTION 5 =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "5. Leave and Holidays")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "请假与休假")
    y -= 18
    c.drawString(50, y, "The Employee is entitled to one (1) day off per week.")
    y -= 15
    c.drawString(50, y, "员工每周享有一天休息日。")
    y -= 18
    c.drawString(50, y, "The weekly off-day shall be determined according to the roster prepared by management.")
    y -= 15
    c.drawString(50, y, "每周休息日将根据公司排班安排决定。")
    y -= 18
    c.drawString(50, y, "Holiday leave requests will only be considered after completion of the first three (3) months of employment.")
    y -= 15
    c.drawString(50, y, "员工完成前三个月工作后方可申请假期。")
    y -= 18
    c.drawString(50, y, "Any leave request must be submitted at least seventy-two (72) hours in advance.")
    y -= 15
    c.drawString(50, y, "所有请假申请必须提前七十二（72）小时提交。")
    y -= 25
    
    # ===== SECTION 6 =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "6. Resignation Policy")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "辞职规定")
    y -= 18
    c.drawString(50, y, "The Employee must provide prior notice before resignation.")
    y -= 15
    c.drawString(50, y, "员工辞职前必须提前通知公司。")
    y -= 18
    c.drawString(50, y, "If the Employee resigns during the probationary period (within the first three months),")
    y -= 15
    c.drawString(50, y, "the Employee agrees to pay a compensation fee of 500 USDT to the Company.")
    y -= 15
    c.drawString(50, y, "如员工在试用期（三个月内）提出辞职，员工同意向公司支付 500 USDT 的补偿费用。")
    y -= 18
    c.drawString(50, y, "The Employee must complete all handover procedures before leaving the position.")
    y -= 15
    c.drawString(50, y, "员工离职前必须完成所有工作交接手续。")
    y -= 25
    
    # ===== SECTION 7 =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "7. Unauthorized Absence")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "擅自离职")
    y -= 18
    c.drawString(50, y, "Failure to report to work without notification or abandonment of duties without resignation")
    y -= 15
    c.drawString(50, y, "notice shall be considered a serious violation of company regulations.")
    y -= 15
    c.drawString(50, y, "未经通知缺勤或未办理辞职手续擅自离职，将被视为严重违反公司规定。")
    y -= 18
    c.drawString(50, y, "The Company reserves the right to impose disciplinary actions and penalties according to")
    y -= 15
    c.drawString(50, y, "company policy.")
    y -= 15
    c.drawString(50, y, "公司有权根据公司政策采取纪律处分及相应处罚措施。")
    y -= 25
    
    # ===== SECTION 8 =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "8. Rewards and Penalties")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "奖励与处罚")
    y -= 18
    c.drawString(50, y, "The Company maintains a reward and penalty system.")
    y -= 15
    c.drawString(50, y, "公司实行奖励与处罚制度。")
    y -= 18
    c.drawString(50, y, "Employees demonstrating excellent performance, attendance, and compliance may receive")
    y -= 15
    c.drawString(50, y, "incentives and bonuses.")
    y -= 15
    c.drawString(50, y, "表现优秀、出勤良好及遵守规定的员工可获得奖金及奖励。")
    y -= 18
    c.drawString(50, y, "Employees violating company policies may be subject to warnings, penalties, or")
    y -= 15
    c.drawString(50, y, "disciplinary action.")
    y -= 15
    c.drawString(50, y, "违反公司规定的员工可能受到警告、处罚或纪律处分。")
    y -= 25
    
    # ===== SECTION 9 =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "9. Acceptance")
    y -= 18
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "协议确认")
    y -= 18
    c.drawString(50, y, "By signing this Agreement, both parties acknowledge that they have read, understood,")
    y -= 15
    c.drawString(50, y, "and agreed to all terms and conditions stated herein.")
    y -= 15
    c.drawString(50, y, "双方签署本协议即表示已阅读、理解并同意本协议全部条款与条件。")
    y -= 35
    
    # ===== SIGNATURES =====
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Company Representative / 公司代表")
    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(50, y, "Name: Jose")
    y -= 15
    c.drawString(50, y, "Signature: ___________________")
    y -= 15
    c.drawString(50, y, f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    y -= 40
    
    c.setFont("Helvetica-Bold", 11)
    c.drawString(50, y, "Employee / 员工")
    y -= 20
    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Name: {user_data.get('name', 'N/A')}")
    y -= 15
    c.drawString(50, y, "Signature: ___________________")
    y -= 15
    c.drawString(50, y, f"Date: {datetime.now().strftime('%Y-%m-%d')}")
    y -= 40
    
    # ===== NOTE/REMINDER =====
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(grey)
    c.drawString(50, y, "Note / 备注: Before using this agreement, it is advisable to have a local legal professional")
    y -= 12
    c.drawString(50, y, "review it, especially the 500 USDT resignation fee and penalty clauses, as employment laws")
    y -= 12
    c.drawString(50, y, "vary by country and some provisions may not be enforceable in certain jurisdictions.")
    
    c.save()
    return filename