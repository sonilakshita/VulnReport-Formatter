import streamlit as st
import json
import os
from vulnreport.markdown_generator import generate_markdown
from vulnreport.pdf_generator import markdown_to_pdf

# App setup
st.set_page_config(page_title="VulnReport Formatter", layout="wide")
st.title("🛡️ VulnReport Formatter")
st.markdown("Generate professional vulnerability reports from structured data.")

# Input section
st.subheader("Step 1: Paste Vulnerability JSON")

sample_data = {
    "title": "SQL Injection in login",
    "severity": "High",
    "target": "https://example.com/login",
    "description": "An SQL Injection vulnerability was found...",
    "steps_to_reproduce": [
        "Step 1: Intercept login request.",
        "Step 2: Modify username to `' OR 1=1--`",
        "Step 3: Send request and bypass login."
    ],
    "impact": "Unauthorized access to admin area.",
    "recommendation": "Use parameterized queries.",
    "screenshots": []
}

json_input = st.text_area(
    label="Paste your JSON data:",
    value=json.dumps(sample_data, indent=2),
    height=300
)

# Optional file upload
st.subheader("Step 2: Upload Screenshots (Optional)")
uploaded_images = st.file_uploader(
    "Attach screenshots (PNG, JPG, JPEG)",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

# Save uploaded images temporarily
screenshot_files = []
if uploaded_images:
    os.makedirs("uploads", exist_ok=True)
    for image in uploaded_images:
        path = os.path.join("uploads", image.name)
        with open(path, "wb") as f:
            f.write(image.read())
        screenshot_files.append(path)

# Report generation button
if st.button("📝 Generate PDF Report"):
    try:
        report_data = json.loads(json_input)
        report_data["screenshots"] = screenshot_files

        # Generate markdown from structured data
        markdown_content = generate_markdown(report_data)

        with open("report.md", "w") as md_file:
            md_file.write(markdown_content)

        # Convert markdown to PDF
        markdown_to_pdf(markdown_content, output_path="report.pdf")

        st.success("✅ Report generated successfully!")

        with open("report.pdf", "rb") as pdf_file:
            st.download_button(
                label="📥 Download Report",
                data=pdf_file,
                file_name="vuln_report.pdf",
                mime="application/pdf"
            )

    except json.JSONDecodeError:
        st.error("❌ Invalid JSON format. Please check your input.")
    except Exception as e:
        st.error(f"❌ Failed to generate report: {e}")

