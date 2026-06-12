from reportlab.pdfgen import canvas

def create_grid_pdf():
    """Create a PDF with grid to find exact coordinates"""
    c = canvas.Canvas("grid_overlay.pdf", pagesize=(612, 792))  # Letter size
    
    # Draw grid every 20 points
    for x in range(0, 612, 20):
        c.line(x, 0, x, 792)
        if x % 50 == 0:
            c.drawString(x, 10, str(x))
    
    for y in range(0, 792, 20):
        c.line(0, y, 612, y)
        if y % 50 == 0:
            c.drawString(10, y, str(y))
    
    c.save()
    print("Created grid_overlay.pdf")
    print("Open both your PDF and grid_overlay.pdf")
    print("Note the X,Y coordinates where you want to place text")
    print("For name field, note the coordinates")

if __name__ == "__main__":
    create_grid_pdf()