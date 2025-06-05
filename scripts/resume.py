""" import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


# set font
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'
status = ["Graduate Electronics Engineer at Mercedes AMG High Performance Powertrain"]
fig, ax = plt.subplots(figsize=(8.5, 11))

# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300)
plt.axhline(y=.8, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# set background color
ax.set_facecolor('white')

IDx = 50
IDy = 50
IDimg = Image.open('staticFiles/Images/ID.jpg')
IDimgs = IDimg.resize((IDx, IDy))
print(IDimg.size)
print(IDimgs.size)
IDimgs.save('staticFiles/Images/ID'+str(IDx)+'.jpg')
IDimgs = np.asarray(IDimg)



# remove axes
plt.axis('off')

# add text
plt.annotate(status, (.02,.98), weight='regular', fontsize=8, alpha=.6)
plt.imshow(IDimgs, interpolation="none")

plt.savefig('staticFiles/resume.pdf', dpi=300, bbox_inches='tight')
 """
"""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.units import inch, mm

# Define the filename for the PDF
filename = "staticFiles/resume.pdf"

# Create a PDF document
pdf = SimpleDocTemplate(filename, pagesize=letter)

# Get a set of predefined styles
styles = getSampleStyleSheet()

# Create a list to hold the flowable objects
flowables = []

# Add name and contact information with an image at the top right
header = []
profile_image = "staticFiles/Images/ID.jpg"  # Path to the profile picture

# Create an Image object
img = Image(profile_image)
img.drawHeight = 35 * mm
img.drawWidth = 33 * mm

# Define the contact information
contact_info = [
    Paragraph("John Doe", styles['Title']),
    Paragraph("123 Main Street, City, Country", styles['Normal']),
    Paragraph("Email: john.doe@example.com", styles['Normal']),
    Paragraph("Phone: +1234567890", styles['Normal'])
]
# Create a table with the image in the first cell and contact information in the second cell
header_table = Table([
    [img, contact_info]
], colWidths=[1.75 * inch, 5.75 * inch])

header_table.setStyle(TableStyle([
    ('VALIGN', (0, 0), (0, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (0, 0), 0),
    ('LEFTPADDING', (1, 0), (1, 0), 12)
]))

# Add the header table to the flowables
flowables.append(header_table)
flowables.append(Spacer(1, 24))

# Add section for Objective
flowables.append(Paragraph("Objective", styles['Heading2']))
flowables.append(Paragraph(
    "A highly motivated and experienced professional seeking a position in Software Development to leverage my skills in Python and software engineering.", 
    styles['Normal']
))
flowables.append(Spacer(1, 12))

# Add section for Experience
flowables.append(Paragraph("Experience", styles['Heading2']))
data = [
    ['Job Title', 'Company Name', 'Duration'],
    ['Software Developer', 'Tech Solutions Inc.', 'Jan 2020 - Present'],
    ['Junior Developer', 'Web Services LLC', 'Jun 2018 - Dec 2019']
]
table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))
flowables.append(table)
flowables.append(Spacer(1, 12))

# Add section for Education
flowables.append(Paragraph("Education", styles['Heading2']))
flowables.append(Paragraph("Bachelor of Science in Computer Science", styles['Normal']))
flowables.append(Paragraph("University of Example, 2014 - 2018", styles['Normal']))
flowables.append(Spacer(1, 12))

# Add section for Skills
flowables.append(Paragraph("Skills", styles['Heading2']))
skills = ["Python", "Java", "JavaScript", "HTML/CSS", "SQL", "Git"]
flowables.append(Paragraph(", ".join(skills), styles['Normal']))

# Build the PDF
pdf.build(flowables)"""


from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Frame, PageTemplate

# Custom function to draw background and image on the canvas
def draw_background(canvas, doc):
    # Draw green background on the right 1/4 of the page
    canvas.setFillColor(colors.green)
    canvas.rect(3 * letter[0] / 4, 0, letter[0] / 4, letter[1], fill=1, stroke=0)

    # Draw the image on the right side (top right corner)
    img_path = "staticFiles/Images/ID.jpg"  # Path to the profile picture
    img_width = 1 * inch
    img_height = 1 * inch
    canvas.drawImage(
        img_path,
        3 * letter[0] / 4 + (letter[0] / 4 - img_width) / 2,
        letter[1] - img_height - 0.5 * inch,
        img_width,
        img_height
    )

# Define the filename for the PDF
filename = "staticFiles/resume.pdf"

# Create a PDF document
pdf = SimpleDocTemplate(filename, pagesize=letter)

# Get a set of predefined styles
styles = getSampleStyleSheet()

# Create frames for the two-column layout
frame1 = Frame(
    0, 0, 3 * letter[0] / 4, letter[1], id='left_frame', showBoundary=0
)
frame2 = Frame(
    3 * letter[0] / 4, 0, letter[0] / 4, letter[1], id='right_frame', showBoundary=0
)

# Create flowables for the main content
left_flowables = []
right_flowables = []

# Add name and contact information to the left column
left_flowables.append(Spacer(1, 72))
left_flowables.append(Paragraph("John Doe", styles['Title']))
left_flowables.append(Paragraph("123 Main Street, City, Country", styles['Normal']))
left_flowables.append(Paragraph("Email: john.doe@example.com", styles['Normal']))
left_flowables.append(Paragraph("Phone: +1234567890", styles['Normal']))
left_flowables.append(Spacer(1, 12))

# Add section for Objective to the left column
left_flowables.append(Paragraph("Objective", styles['Heading2']))
left_flowables.append(Paragraph(
    "A highly motivated and experienced professional seeking a position in Software Development to leverage my skills in Python and software engineering.", 
    styles['Normal']
))
left_flowables.append(Spacer(1, 12))

# Add section for Experience to the left column
left_flowables.append(Paragraph("Experience", styles['Heading2']))
data = [
    ['Job Title', 'Company Name', 'Duration'],
    ['Software Developer', 'Tech Solutions Inc.', 'Jan 2020 - Present'],
    ['Junior Developer', 'Web Services LLC', 'Jun 2018 - Dec 2019']
]
table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))
left_flowables.append(table)
left_flowables.append(Spacer(1, 12))

# Add section for Education to the left column
left_flowables.append(Paragraph("Education", styles['Heading2']))
left_flowables.append(Paragraph("Bachelor of Science in Computer Science", styles['Normal']))
left_flowables.append(Paragraph("University of Example, 2014 - 2018", styles['Normal']))
left_flowables.append(Spacer(1, 12))

# Add section for Skills to the right column
right_flowables.append(Spacer(1, 72))  # Ensure it starts at the same height
right_flowables.append(Paragraph("Skills", styles['Heading2']))
skills = ["Python", "Java", "JavaScript", "HTML/CSS", "SQL", "Git"]
right_flowables.append(Paragraph(", ".join(skills), styles['Normal']))

# Combine flowables for each frame
left_frame_content = left_flowables
right_frame_content = right_flowables

# Create a PageTemplate with the defined frames
page_template = PageTemplate(id='two_columns', frames=[frame1, frame2], onPage=draw_background)

# Add the PageTemplate to the document
pdf.addPageTemplates([page_template])

# Build the PDF
pdf.build(left_frame_content + right_frame_content)

print(f"Resume created: {filename}")