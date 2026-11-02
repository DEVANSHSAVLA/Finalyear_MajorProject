import os
import sys
import win32com.client

def export_to_pdf():
    cwd = os.getcwd()
    pptx_path = os.path.abspath(os.path.join(cwd, r"docs\review-2-submission\CivicSphere_AI_Review_2_Presentation.pptx"))
    pdf_path = os.path.abspath(os.path.join(cwd, r"docs\review-2-submission\CivicSphere_AI_Review_2_Presentation.pdf"))
    
    if not os.path.exists(pptx_path):
        print(f"Error: {pptx_path} does not exist!")
        sys.exit(1)

    print(f"Opening PowerPoint for: {pptx_path}")
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    # ppt.Visible = 1
    
    try:
        presentation = ppt.Presentations.Open(pptx_path, WithWindow=False)
        print(f"Exporting to PDF: {pdf_path}")
        # Format 32 = ppSaveAsPDF
        presentation.SaveAs(pdf_path, 32)
        presentation.Close()
        print(f"Successfully exported {pdf_path} (File size: {os.path.getsize(pdf_path)} bytes)")
    except Exception as e:
        print(f"Error during export: {e}")
        raise e
    finally:
        ppt.Quit()

if __name__ == "__main__":
    export_to_pdf()
