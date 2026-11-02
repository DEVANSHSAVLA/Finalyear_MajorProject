import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

from report_helpers import set_cell_margins, set_cell_background, set_table_borders
from report_chapters_builder import (
    COLOR_NAVY, COLOR_TEAL, COLOR_BODY,
    add_p, add_chapter_heading, add_sec_heading, add_subsec_heading, add_subsubsec_heading
)

def add_rubric_audit():
    doc = docx.Document(r"docs\review-2-submission\CivicSphere_AI_Review_2_Report.docx")

    doc.add_page_break()
    add_p(doc, "APPENDIX F: SAKEC MAJOR PROJECT RUBRIC COMPLIANCE AUDIT", bold=True, size=14, color=COLOR_NAVY, space_after=12)
    add_p(doc,
        "Table F.1 presents the team's self-evaluation matrix against the official B.Tech Major Project marking rubric, "
        "demonstrating Level 4 (Exemplary) alignment across all academic criteria."
    )

    rubric_data = [
        ["Rubric Criterion", "Weight", "Level 4 (Exemplary) Descriptor", "CivicSphere AI Implementation & Evidence", "Self-Score"],
        ["Criterion 1: Problem Definition", "12%", "Specific, technically significant problem; explicit scope & non-goals; measurable objectives.", "Chapter 1 & 3: 7 citizen pain points; formal math bounds; 10 measurable objectives O1-O10.", "4 / 4 (Exemplary)"],
        ["Criterion 2: Literature Review", "20%", "Systematic review of >= 8 sources; critical comparative analysis; clear technical gap.", "Chapter 2: 30 peer-reviewed papers mapped across 7 themes; Nyaya Setu critique; 7 research gaps.", "4 / 4 (Exemplary)"],
        ["Criterion 3: SDG & Societal Impact", "8%", "Primary SDG alignment with explicit targets; evidence-based impact; honest environmental review.", "Chapter 5: Primary SDG 16 (Target 16.3/16.10), SDG 10, SDG 9; Green AI compute profiling.", "4 / 4 (Exemplary)"],
        ["Criterion 4: System Architecture", "15%", "Modular system design; clear API contracts; hybrid retrieval; durable cloud persistence.", "Chapter 6 & 7: 5-Tier Modular Monolith; Gate 2 circuit breaker; Supabase private S3 storage.", "4 / 4 (Exemplary)"],
        ["Criterion 5: Implementation & Testing", "20%", "Operational implementation across all core modules; reproducible automated tests; live deployment.", "Chapter 8: 129 passed tests; 31 prerendered routes; 20 live API probes 200 OK; byte-exact persistence.", "4 / 4 (Exemplary)"],
        ["Criterion 6: Teamwork & Reflections", "10%", "Clear RACI matrix; authentic engineering case study; individual deep learning reflections.", "Chapter 9: Squad RACI matrix; serverless cold start case study; 180-240 word individual reflections.", "4 / 4 (Exemplary)"],
        ["Criterion 7: Future Planning", "8%", "Practical, phased roadmap; risk mitigation protocols; well-defined final defense milestones.", "Chapter 10: 5-phase Semester 8 delivery roadmap; risk mitigation; load testing.", "4 / 4 (Exemplary)"],
        ["Criterion 8: Presentation & Report", "7%", "Professional typography; SAKEC formatting; complete front matter; comprehensive documentation.", "Strict adherence to SAKEC margins, Times New Roman 12pt, 1.5 line spacing, 75+ page thesis.", "4 / 4 (Exemplary)"]
    ]

    t_rub = doc.add_table(rows=len(rubric_data), cols=5)
    t_rub.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_rub)
    for r_idx, row in enumerate(rubric_data):
        for c_idx, val in enumerate(row):
            cell = t_rub.cell(r_idx, c_idx)
            set_cell_margins(cell, top=50, bottom=50, left=60, right=60)
            cell.paragraphs[0].text = val
            p = cell.paragraphs[0]
            if r_idx == 0:
                set_cell_background(cell, "142B4E")
                p.runs[0].font.bold = True
                p.runs[0].font.size = Pt(8.5)
                p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
            else:
                p.runs[0].font.size = Pt(8.0)
                if r_idx % 2 == 1:
                    set_cell_background(cell, "F5F7F9")

    add_p(doc, "\n\nEnd of CivicSphere AI Review 2 Comprehensive Project Report.", italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24)

    doc_out = r"docs\review-2-submission\CivicSphere_AI_Review_2_Report.docx"
    doc.save(doc_out)
    print("Rubric audit appended successfully!")

if __name__ == "__main__":
    add_rubric_audit()
