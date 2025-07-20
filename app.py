import streamlit as st
import json
import os
from vulnreport.markdown_generator import generate_markdown
from vulnreport.pdf_generator import markdown_to_pdf

st.set_page_config(page_title="VulnReport Formatter", layout="wide")

st.title("🛡️ VulnReport Formatter")
st.markdown("Turn raw bug bounty findings into clean PDF reports.")

st.subheader("Step 1: Enter Vulnerability Data")

default_json = {
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

input_text = st.text_area("Paste your JSON here:", json.dumps(default_json, indent=2), height=300)

st.subheader("Step 2: Upload Screenshots (Optional)")
uploaded_files = st.file_uploader("Upload PoC screenshots", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

# Save screenshots to a temp folder
screenshot_paths = []
if uploaded_files:
    os.makedirs("uploads", exist_ok=True)
    for file in uploaded_files:
        file_path = os.path.join("uploads", file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())
        screenshot_paths.append(file_path)

if st.button("📝 Generate Report"):
    try:
        data = json.loads(input_text)
        data["screenshots"] = screenshot_paths

        markdown = generate_markdown(data)

        with open("report.md", "w") as f:
            f.write(markdown)

        markdown_to_pdf(markdown, "report.pdf")

        st.success("✅ Report generated!")

        with open("report.pdf", "rb") as f:
            st.download_button("📥 Download PDF Report", f, file_name="vuln_report.pdf", mime="application/pdf")

    except Exception as e:
        st.error(f"❌ Error generating report: {e}")
