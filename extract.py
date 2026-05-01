import pypdf

reader = pypdf.PdfReader("Resume.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
    if "/Annots" in page:
        for annot in page["/Annots"]:
            annot_obj = annot.get_object()
            if "/A" in annot_obj and "/URI" in annot_obj["/A"]:
                print("URI:", annot_obj["/A"]["/URI"])

print("--- TEXT ---")
print(text)
