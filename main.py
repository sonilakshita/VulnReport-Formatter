import json
from vulnreport.markdown_generator import generate_markdown
from vulnreport.pdf_generator import markdown_to_pdf

def main():
    with open("examples/sample_input.json", "r") as f:
        data = json.load(f)

    markdown_report = generate_markdown(data)

    with open("report.md", "w") as f:
        f.write(markdown_report)

    markdown_to_pdf(markdown_report, "report.pdf")
    print("✅ Report generated: report.md and report.pdf")

if __name__ == "__main__":
    main()
