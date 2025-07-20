import markdown2
import pdfkit

def markdown_to_pdf(markdown_text, output_path="report.pdf"):
    html = markdown2.markdown(markdown_text)
    pdfkit.from_string(html, output_path)
