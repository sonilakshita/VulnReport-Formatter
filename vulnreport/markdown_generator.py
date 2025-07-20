from jinja2 import Template
import os

def generate_markdown(data):
    with open("vulnreport/templates/report_template.md", "r") as f:
        template = Template(f.read())

    markdown = template.render(**data)
    return markdown

from jinja2 import Template

def generate_markdown(data):
    with open("vulnreport/templates/report_template.md", "r") as f:
        template = Template(f.read())

    return template.render(**data)
