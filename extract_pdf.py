import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            
            print(f"Total pages: {num_pages}")
            
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += f"\n--- Page {page_num + 1} ---\n"
                text += page.extract_text()
                
        return text
    except Exception as e:
        return f"Error extracting text: {str(e)}"

if __name__ == "__main__":
    pdf_path = "SP2 Technical_Report_Nov2024 (1).pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    
    # Save the extracted text to a file
    with open("extracted_pdf_content.txt", "w", encoding="utf-8") as output_file:
        output_file.write(extracted_text)
    
    print("Extraction complete. Content saved to 'extracted_pdf_content.txt'") 