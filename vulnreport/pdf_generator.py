import markdown2
import pdfkit
import os

def markdown_to_pdf(markdown_text, output_path="report.pdf", css_path=None):
    """
    Converts Markdown text to a styled PDF file.
    """
    try:
        # Convert markdown to HTML
        html_content = markdown2.markdown(markdown_text)

        # PDF generation options
        options = {
            "page-size": "A4",
            "margin-top": "0.75in",
            "margin-right": "0.75in",
            "margin-bottom": "0.75in",
            "margin-left": "0.75in",
            "encoding": "UTF-8"
        }

        # Check if CSS is provided and valid
        if css_path and os.path.exists(css_path):
            pdfkit.from_string(html_content, output_path, options=options, css=css_path)
        else:
            pdfkit.from_string(html_content, output_path, options=options)

        print(f"[+] PDF generated successfully: {output_path}")

    except Exception as e:
        print(f"[!] Failed to generate PDF: {e}")
        raise
