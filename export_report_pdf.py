import os
import sys
import win32com.client

def export_to_pdf():
    cwd = os.getcwd()
    docx_path = os.path.abspath(os.path.join(cwd, r"docs\review-2-submission\CivicSphere_AI_Review_2_Report.docx"))
    pdf_path = os.path.abspath(os.path.join(cwd, r"docs\review-2-submission\CivicSphere_AI_Review_2_Report.pdf"))
    
    if not os.path.exists(docx_path):
        print(f"Error: {docx_path} does not exist!")
        sys.exit(1)

    print(f"Opening Word for: {docx_path}")
    word = win32com.client.Dispatch("Word.Application")
    # word.Visible = False
    
    try:
        doc = word.Documents.Open(docx_path)
        print(f"Exporting to PDF: {pdf_path}")
        # Format 17 = wdExportFormatPDF
        doc.ExportAsFixedFormat(pdf_path, 17)
        doc.Close(False)
        print(f"Successfully exported {pdf_path} (File size: {os.path.getsize(pdf_path)} bytes)")
    except Exception as e:
        print(f"Error during export: {e}")
        raise e
    finally:
        word.Quit()

if __name__ == "__main__":
    export_to_pdf()
