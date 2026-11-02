import os
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL

from report_helpers import set_cell_margins, set_cell_background, set_table_borders

COLOR_NAVY = RGBColor(20, 43, 78)
COLOR_TEAL = RGBColor(24, 125, 125)
COLOR_BODY = RGBColor(30, 38, 48)

def add_p(doc, text, bold=False, italic=False, size=12, color=COLOR_BODY, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=6, line_spacing=1.5):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    run.font.name = 'Times New Roman'
    run.font.size = Pt(size)
    run.font.color.rgb = color
    return p

def add_chapter_heading(doc, num_str, title_str):
    doc.add_page_break()
    p_ch = doc.add_paragraph()
    p_ch.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_ch.paragraph_format.space_before = Pt(12)
    p_ch.paragraph_format.space_after = Pt(4)
    run_ch = p_ch.add_run(num_str.upper())
    run_ch.bold = True
    run_ch.font.name = 'Times New Roman'
    run_ch.font.size = Pt(14)
    run_ch.font.color.rgb = COLOR_TEAL

    p_t = doc.add_paragraph()
    p_t.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_t.paragraph_format.space_before = Pt(0)
    p_t.paragraph_format.space_after = Pt(18)
    run_t = p_t.add_run(title_str.upper())
    run_t.bold = True
    run_t.font.name = 'Times New Roman'
    run_t.font.size = Pt(18)
    run_t.font.color.rgb = COLOR_NAVY

def add_sec_heading(doc, title_str):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(title_str)
    run.bold = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(14)
    run.font.color.rgb = COLOR_NAVY

def add_subsec_heading(doc, title_str):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(title_str)
    run.bold = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13)
    run.font.color.rgb = COLOR_TEAL

def add_subsubsec_heading(doc, title_str):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(title_str)
    run.bold = True
    run.italic = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.color.rgb = COLOR_NAVY

def add_figure(doc, img_path, caption_str, width_in=5.5):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        p_img.add_run().add_picture(img_path, width=Inches(width_in))

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(12)
        run_cap = p_cap.add_run(caption_str)
        run_cap.italic = True
        run_cap.bold = True
        run_cap.font.size = Pt(10.5)
        run_cap.font.color.rgb = COLOR_NAVY

print("report_chapters_builder setup complete.")
