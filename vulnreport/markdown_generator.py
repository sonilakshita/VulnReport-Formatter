from jinja2 import Template
import os

def generate_markdown(data, template_path="vulnreport/templates/report_template.md"):
    """
    Renders a markdown vulnerability report from a Jinja2 template.

    Args:
        data (dict): Dictionary containing vulnerability details.
        template_path (str): Path to the markdown Jinja2 template file.

    Returns:
        str: Rendered markdown string.
    """
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file not found: {template_path}")

    try:
        with open(template_path, "r", encoding="utf-8") as template_file:
            template_content = template_file.read()
            template = Template(template_content)

        markdown_output = template.render(**data)
        return markdown_output

    except Exception as e:
        print(f"[!] Failed to render markdown: {e}")
        raise

