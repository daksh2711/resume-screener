from app.services.pdf_parser import extract_text_from_pdf

pdf_path = "C:/Users/daksh.dayal/Desktop/resume-screener/data/sample_resumes/Stockholm-Resume-Template-Simple.pdf"

print("Running PDF parser...\n")

text = extract_text_from_pdf(pdf_path)

print("Length of text:", len(text))
print("\nPreview:\n")
print(text[:500])