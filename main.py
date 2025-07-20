import json
import os
from vulnreport.markdown_generator import generate_markdown
from vulnreport.pdf_generator import markdown_to_pdf

def main():
    input_path = "examples/sample_input.json"
    markdown_path = "report.md"
    pdf_path = "report.pdf"

    if not os.path.exists(input_path):
        print(f"❌ Input file not found: {input_path}")
        return

    try:
    
        with open(input_path, "r") as file:
            vulnerability_data = json.load(file)
        markdown_content = generate_markdown(vulnerability_data)
        with open(markdown_path, "w") as md_file:
            md_file.write(markdown_content)
        markdown_to_pdf(markdown_content, output_path=pdf_path)

        print(f"✅ Report generated:\n- Markdown: {markdown_path}\n- PDF: {pdf_path}")

    except json.JSONDecodeError:
        print("❌ Failed to parse JSON. Please check the format.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
