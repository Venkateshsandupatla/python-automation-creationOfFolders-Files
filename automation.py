import os
import shutil
from datetime import datetime
from docx import Document  # install with: pip install python-docx

# Constants
BASE_DIR = r"C:\Users\venka\OneDrive\Documents\2025\Applications"
BASE_RESUME = os.path.join(BASE_DIR, "AAAVenkateshSandupatla-Resume.docx")

def create_empty_docx(filepath):
    doc = Document()
    doc.save(filepath)

def create_job_folder(company_name):
    year = datetime.now().year
    folder_name = f"{company_name}_{year}"
    folder_path = os.path.join(BASE_DIR, folder_name)

    # Create the job folder
    os.makedirs(folder_path, exist_ok=True)

    # Resume destination
    resume_dest = os.path.join(folder_path, "venkatesh_sandupatla_resume.docx")

    # Copy resume
    if os.path.exists(BASE_RESUME):
        shutil.copy(BASE_RESUME, resume_dest)
        print(f"✅ Copied resume to: {resume_dest}")
    else:
        create_empty_docx(resume_dest)
        print(f"⚠️ Resume not found — created empty file: {resume_dest}")

    # Job description and cover letter filenames
    job_desc_path = os.path.join(folder_path, f"{company_name.lower()}_job_description.docx")
    cover_letter_path = os.path.join(folder_path, f"cover_letter_{company_name.lower()}.docx")

    # Create empty .docx files
    create_empty_docx(job_desc_path)
    create_empty_docx(cover_letter_path)

    print(f"📁 Folder created: {folder_path}")
    print("📝 Created empty job description and cover letter .docx files.")

# Run
if __name__ == "__main__":
    company = input("Enter the company name: ").strip().title().replace(" ", "")
    create_job_folder(company)
