import markdown
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

def generate_report(filename, summary, analysis):
    report = f"""
# Liability Analysis Report

## File: {filename}

### Summary
{summary}

### Analysis
{analysis}
    """
    return report

def save_report_as_pdf(report):
    # Convert Markdown to HTML
    html = markdown.markdown(report)
    
    # Create a BytesIO object to store the PDF in memory
    pdf_buffer = BytesIO()
    
    # Create the PDF document
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Split the HTML into lines
    lines = html.split('\n')
    
    # Create a list of flowables (paragraphs and spacers)
    flowables = []
    for line in lines:
        if line.startswith('<h1>'):
            flowables.append(Paragraph(line[4:-5], styles['Title']))
        elif line.startswith('<h2>'):
            flowables.append(Paragraph(line[4:-5], styles['Heading1']))
        elif line.startswith('<h3>'):
            flowables.append(Paragraph(line[4:-5], styles['Heading2']))
        elif line.strip():
            flowables.append(Paragraph(line, styles['BodyText']))
        else:
            flowables.append(Spacer(1, 12))
    
    # Build the PDF
    doc.build(flowables)
    
    # Move the buffer's cursor to the beginning
    pdf_buffer.seek(0)
    
    return pdf_buffer