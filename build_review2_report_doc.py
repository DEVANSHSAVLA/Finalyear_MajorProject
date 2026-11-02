import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

from report_helpers import set_cell_margins, set_cell_background, set_table_borders

def create_report():
    doc = docx.Document()

    # Page Margins (SAKEC Standard: Left=3.5cm, Right=2.0cm, Top=2.5cm, Bottom=2.5cm)
    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(3.5)
        section.right_margin = Cm(2.0)
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)

    # Styles
    COLOR_NAVY = RGBColor(20, 43, 78)
    COLOR_TEAL = RGBColor(24, 125, 125)
    COLOR_BODY = RGBColor(30, 38, 48)

    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Times New Roman'
    style_normal.font.size = Pt(12)
    style_normal.font.color.rgb = COLOR_BODY
    style_normal.paragraph_format.line_spacing = 1.5
    style_normal.paragraph_format.space_after = Pt(6)
    style_normal.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    def add_p(text, bold=False, italic=False, size=12, color=COLOR_BODY, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=6, line_spacing=1.5):
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

    def add_chapter_heading(num_str, title_str):
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

    def add_sec_heading(title_str):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run(title_str)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)
        run.font.color.rgb = COLOR_NAVY

    def add_subsec_heading(title_str):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        run = p.add_run(title_str)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(13)
        run.font.color.rgb = COLOR_TEAL

    def add_subsubsec_heading(title_str):
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

    def add_figure(img_path, caption_str, width_in=5.5):
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

    # =========================================================================
    # FRONT MATTER
    # =========================================================================
    # 1. TITLE PAGE
    add_p("CIVICSPHERE AI: EVIDENCE-GROUNDED CIVIC INTELLIGENCE PLATFORM", bold=True, size=18, color=COLOR_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=4)
    add_p("An Agentic AI-Powered Citizen Intelligence Platform for Legal Guidance, Government Services, and Regulatory Support", bold=True, size=13, color=COLOR_TEAL, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    
    add_p("A PROJECT REPORT (REVIEW 2)", bold=True, size=13, color=COLOR_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p("Submitted in Partial Fulfillment of the Requirements for the Award of the Degree of", italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p("BACHELOR OF TECHNOLOGY IN COMPUTER ENGINEERING", bold=True, size=13, color=COLOR_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)

    add_p("Submitted by", italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
    add_p("Khushbu Chheda (Roll No: 23UF17711CM132)\nDevansh Savla (Roll No: 23UF18356CM172)\nAnushka Adsul (Roll No: 124BTCM2002)\nRahul Singh (Roll No: 23UF18562CM189)", bold=True, size=12, color=COLOR_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18, line_spacing=1.3)

    add_p("Under the Esteemed Guidance of", italic=True, size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_p("Mrs. Shahzia Sayyad", bold=True, size=14, color=COLOR_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p("Assistant Professor, Department of Computer Engineering", size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)

    sakec_logo_path = r"docs\review-2-submission\latex-source\images\SAKEC_logo.png"
    if os.path.exists(sakec_logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(6)
        p_logo.paragraph_format.space_after = Pt(12)
        p_logo.add_run().add_picture(sakec_logo_path, width=Inches(1.5))

    add_p("DEPARTMENT OF COMPUTER ENGINEERING\nSHAH & ANCHOR KUTCHHI ENGINEERING COLLEGE", bold=True, size=13, color=COLOR_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p("(An Autonomous Institute Affiliated to the University of Mumbai)", size=10.5, italic=True, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p("MUMBAI -- 400 088, MAHARASHTRA, INDIA\nACADEMIC YEAR: 2026--2027", bold=True, size=11, color=COLOR_BODY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    # 2. CERTIFICATE PAGE
    doc.add_page_break()
    add_p("SHAH & ANCHOR KUTCHHI ENGINEERING COLLEGE", bold=True, size=14, color=COLOR_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p("(An Autonomous Institute Affiliated to University of Mumbai)", italic=True, size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
    add_p("Mumbai -- 400 088, Maharashtra, India", size=10, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)

    add_p("CERTIFICATE", bold=True, size=16, color=COLOR_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=12)
    
    cert_text = (
        "This is to certify that the project entitled \"CIVICSPHERE AI: EVIDENCE-GROUNDED CIVIC INTELLIGENCE PLATFORM\" "
        "is a bona fide record of work carried out by Khushbu Chheda (23UF17711CM132), Devansh Savla (23UF18356CM172), "
        "Anushka Adsul (124BTCM2002), and Rahul Singh (23UF18562CM189) under my supervision and guidance, in partial fulfillment "
        "of the requirements for the award of the degree of Bachelor of Technology in Computer Engineering by Shah & Anchor Kutchhi "
        "Engineering College (Autonomous), affiliated to the University of Mumbai, during the academic year 2026--2027.\n\n"
        "It is further certified that the students have satisfied all the academic requirements for Major Project Review 2 and that "
        "their work represents an authentic, demonstrable software engineering implementation of high academic and industrial quality."
    )
    add_p(cert_text, space_after=24)

    add_p("Mrs. Shahzia Sayyad\nProject Guide & Assistant Professor\nDepartment of Computer Engineering", bold=True, size=11, space_after=24)
    add_p("The Oral Examination for B.Tech Major Project Review 2 has been conducted on: .......................................", size=11, space_after=36)

    # Signatures table
    sig_table = doc.add_table(rows=2, cols=3)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r_idx, row in enumerate(sig_table.rows):
        for c_idx, cell in enumerate(row.cells):
            set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
    sig_table.cell(0, 0).paragraphs[0].text = "Internal Examiner"
    sig_table.cell(0, 1).paragraphs[0].text = "External Examiner"
    sig_table.cell(0, 2).paragraphs[0].text = "Mrs. Shahzia Sayyad\n(Project Guide)"
    sig_table.cell(1, 0).paragraphs[0].text = "Dr. Vidyullata Devmane\n(Head of Department)"
    sig_table.cell(1, 1).paragraphs[0].text = "Dr. Bhavesh Patel\n(Principal)"
    sig_table.cell(1, 2).paragraphs[0].text = "College Seal"
    for row in sig_table.rows:
        for cell in row.cells:
            for p in cell.paragraphs:
                p.runs[0].font.bold = True
                p.runs[0].font.size = Pt(10)
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # 3. CANDIDATE'S DECLARATION
    doc.add_page_break()
    add_p("CANDIDATE'S DECLARATION", bold=True, size=16, color=COLOR_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    decl_text = (
        "We, the undersigned students of the Department of Computer Engineering, Shah & Anchor Kutchhi Engineering College, "
        "hereby declare that the project work entitled \"CIVICSPHERE AI: EVIDENCE-GROUNDED CIVIC INTELLIGENCE PLATFORM\" "
        "is an authentic record of our own research, design, implementation, and empirical testing carried out under the guidance of "
        "Mrs. Shahzia Sayyad during the academic year 2026--2027.\n\n"
        "We affirm that the matter embodied in this report has not been submitted by us or by any other team to any other university "
        "or institution for the award of any degree or diploma. All sources of literature, open-source libraries, statutory frameworks, "
        "and published benchmarks have been duly cited and acknowledged in the bibliography."
    )
    add_p(decl_text, space_after=24)

    dec_tbl = doc.add_table(rows=5, cols=3)
    dec_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    dec_tbl.cell(0, 0).paragraphs[0].text = "Student Name"
    dec_tbl.cell(0, 1).paragraphs[0].text = "Roll Number"
    dec_tbl.cell(0, 2).paragraphs[0].text = "Signature"
    students = [
        ("Khushbu Chheda", "23UF17711CM132"),
        ("Devansh Savla", "23UF18356CM172"),
        ("Anushka Adsul", "124BTCM2002"),
        ("Rahul Singh", "23UF18562CM189")
    ]
    for idx, (s_name, r_no) in enumerate(students):
        dec_tbl.cell(idx+1, 0).paragraphs[0].text = s_name
        dec_tbl.cell(idx+1, 1).paragraphs[0].text = r_no
        dec_tbl.cell(idx+1, 2).paragraphs[0].text = "........................................"
    set_table_borders(dec_tbl)
    for r_idx, row in enumerate(dec_tbl.rows):
        for c_idx, cell in enumerate(row.cells):
            set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
            if r_idx == 0:
                set_cell_background(cell, "142B4E")
                p = cell.paragraphs[0]
                p.runs[0].font.bold = True
                p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
            else:
                cell.paragraphs[0].runs[0].font.size = Pt(11)

    add_p("\nDate: .......................................\nPlace: Mumbai", size=11, space_before=18)

    # 4. CERTIFICATE OF PLAGIARISM CHECK
    doc.add_page_break()
    add_p("CERTIFICATE OF PLAGIARISM CHECK", bold=True, size=16, color=COLOR_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    
    plag_tbl = doc.add_table(rows=9, cols=2)
    plag_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    plag_data = [
        ("Title of the Project Report", "CIVICSPHERE AI: EVIDENCE-GROUNDED CIVIC INTELLIGENCE PLATFORM"),
        ("Name of the Students", "Khushbu Chheda, Devansh Savla, Anushka Adsul, Rahul Singh"),
        ("Name of the Guide", "Mrs. Shahzia Sayyad (Assistant Professor)"),
        ("Department", "Department of Computer Engineering, SAKEC"),
        ("Plagiarism Detection Tool", "Turnitin Similarity Engine"),
        ("Similar Content (%) Identified", "[INSTITUTIONAL TURNITIN RUN REQUIRED: Target <= 10%]"),
        ("Acceptable Maximum Limit", "10% (As per University of Mumbai & SAKEC Academic Integrity Norms)"),
        ("Date of Plagiarism Verification", "......................................."),
        ("Department Academic Integrity Panel (DAIP)", "Name & Sign: ....................................................................")
    ]
    for idx, (k, v) in enumerate(plag_data):
        plag_tbl.cell(idx, 0).paragraphs[0].text = k
        plag_tbl.cell(idx, 1).paragraphs[0].text = v
    set_table_borders(plag_tbl)
    for r_idx, row in enumerate(plag_tbl.rows):
        for c_idx, cell in enumerate(row.cells):
            set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
            p = cell.paragraphs[0]
            if c_idx == 0:
                p.runs[0].font.bold = True
                p.runs[0].font.size = Pt(11)
                p.runs[0].font.color.rgb = COLOR_NAVY
                set_cell_background(cell, "F5F7F9")
            else:
                p.runs[0].font.size = Pt(11)

    add_p("\n\nSignature of Students: .....................................................................................................", size=11, space_after=12)
    add_p("Signature of Project Guide (Mrs. Shahzia Sayyad): ..................................................................", size=11)

    # 5. ACKNOWLEDGEMENTS
    doc.add_page_break()
    add_p("ACKNOWLEDGEMENTS", bold=True, size=16, color=COLOR_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    ack_text = (
        "We take immense pride in expressing our profound gratitude and heartfelt indebtedness to our esteemed project guide, "
        "Mrs. Shahzia Sayyad, Assistant Professor, Department of Computer Engineering, for her inspiring mentorship, unwavering guidance, "
        "and intellectual stimulation throughout the conception, development, and evaluation of CivicSphere AI. Her demanding academic "
        "standards, continuous constructive critique, and deep insights into software architecture and AI trust were pivotal in transforming "
        "our initial ideas into a robust, evidence-grounded production platform.\n\n"
        "We are profoundly indebted to Dr. Vidyullata Devmane, Head of the Department of Computer Engineering, for her steadfast administrative "
        "support, departmental facilities, and for fostering a rigorous research culture that inspired our pursuit of software excellence.\n\n"
        "Our sincere thanks are due to Dr. Bhavesh Patel, Principal of Shah \& Anchor Kutchhi Engineering College, for providing state-of-the-art "
        "computational infrastructure and creating an environment where undergraduate students are empowered to engineer socially meaningful "
        "technological solutions.\n\n"
        "We also acknowledge the valuable feedback received from our departmental project reviewers, faculty members, and laboratory staff. "
        "Finally, we express our boundless gratitude to our parents and families for their sacrifices, continuous encouragement, and moral support, "
        "which served as our greatest source of strength throughout this intensive engineering endeavor."
    )
    add_p(ack_text, space_after=24)
    add_p("Khushbu Chheda (23UF17711CM132)\nDevansh Savla (23UF18356CM172)\nAnushka Adsul (124BTCM2002)\nRahul Singh (23UF18562CM189)", bold=True, size=11, space_after=12)
    add_p("Shah & Anchor Kutchhi Engineering College, Mumbai", italic=True, size=10.5)

    # 6. ABSTRACT
    doc.add_page_break()
    add_p("ABSTRACT", bold=True, size=16, color=COLOR_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    abs_text = (
        "In democratic societies such as India, equal access to justice, statutory clarity, and transparent public welfare distribution "
        "represent foundational constitutional ideals under Articles 14, 21, and 39A of the Constitution of India. However, in practice, "
        "citizens face severe systemic friction arising from bureaucratic fragmentation across disconnected digital portals, dense statutory "
        "legalese, opaque welfare eligibility criteria, and prohibitive private legal consultation fees. While modern generative AI models "
        "offer conversational accessibility, their unconstrained deployment in legal and civic domains presents grave risks of legal prejudice "
        "due to pervasive hallucinations, fabricated case citations, and temporal invalidation of superseded statutes.\n\n"
        "This project presents CivicSphere AI, an agentic, evidence-grounded civic intelligence platform engineered specifically for the Indian "
        "socio-legal ecosystem. CivicSphere AI unifies four intelligent modules within a modular monolithic architecture: (i) an Evidence-Grounded "
        "Legal Guidance Engine covering eight core statutory Acts (including the Bharatiya Nyaya Sanhita 2023, Bharatiya Nagarik Suraksha Sanhita 2023, "
        "Consumer Protection Act 2019, and RTI Act 2005) with a strict Gate 2 circuit breaker that switches to deterministic synthesis whenever citation "
        "grounding falls below confidence thresholds; (ii) a Government Service Navigator incorporating a catalog of 12 Central and State welfare "
        "schemes with dynamic, rule-based eligibility evaluation; (iii) a Civic Knowledge and Agentic Graph executing multi-hop relational reasoning "
        "across a 40+ node NetworkX multigraph combined with Reciprocal Rank Fusion (RRF) hybrid retrieval (BM25 sparse + dense cosine embeddings); "
        "and (iv) an Intelligent Document Processing Pipeline featuring sub-2.0 second heuristic regex extraction of notices and summons, coupled "
        "with durable, serverless-compatible Supabase S3 cloud persistence and strict Digital Personal Data Protection (DPDP) Act 2023 cascade purge compliance.\n\n"
        "Empirical verification on live Vercel production demonstrates a 100% pass rate across 129 backend automated tests (124 functional/regression "
        "tests and 5 server-side authorization enforcement tests), error-free static prerendering of 31 Next.js 14 frontend routes, 20/20 live HTTP API "
        "endpoints returning 200 OK, and byte-exact roundtrip cloud storage persistence. By translating abstract statutory rights into plain-language, "
        "verifiable procedural roadmaps, CivicSphere AI advances UN Sustainable Development Goal 16 (Target 16.3: Equal Access to Justice) while maintaining "
        "rigorous privacy and green computational efficiency."
    )
    add_p(abs_text, space_after=18)
    add_p("Keywords: Civic Intelligence, Legal NLP, Retrieval-Augmented Generation, Reciprocal Rank Fusion, Knowledge Graphs, Citation Verification, DPDP Act 2023, Multi-Agent Systems, E-Governance, Access to Justice.", bold=True, size=11, color=COLOR_NAVY)

    # 7. TABLE OF CONTENTS SUMMARY
    doc.add_page_break()
    add_p("TABLE OF CONTENTS", bold=True, size=16, color=COLOR_NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=18)
    
    toc_items = [
        ("Certificate", "ii"),
        ("Candidate's Declaration", "iii"),
        ("Certificate of Plagiarism Check", "iv"),
        ("Acknowledgements", "v"),
        ("Abstract", "vi"),
        ("Table of Contents", "vii"),
        ("List of Figures", "ix"),
        ("List of Tables", "x"),
        ("Chapter 1: Problem Identification", "1"),
        ("    1.1 Background and Industrial Context", "1"),
        ("    1.2 The Existing Citizen Problem & Seven Core Pain Points", "2"),
        ("    1.3 Why Current Approaches Are Inadequate", "4"),
        ("    1.4 Motivation for an Evidence-Grounded Civic Platform", "5"),
        ("Chapter 2: Literature Survey and Gap Analysis", "7"),
        ("    2.1 Introduction & Selection Criteria", "7"),
        ("    2.2 Thematic Literature Survey (7 Core Themes)", "8"),
        ("    2.3 Thirty-Paper Comparative Literature Survey Matrix", "15"),
        ("    2.4 Critical Analysis of Existing Systems (Nyaya Setu, India Code, myScheme)", "19"),
        ("    2.5 Identified Research & Technical Gaps (G1--G7)", "22"),
        ("    2.6 Research Gap to Technical Solution Translation", "24"),
        ("Chapter 3: Problem Statement", "26"),
        ("    3.1 Formal Problem Formulation", "26"),
        ("    3.2 Logical Connection: From Problem to Solution", "27"),
        ("    3.3 Research and Engineering Questions (RQ1--RQ5)", "28"),
        ("    3.4 Stakeholder Personas and Explicit Non-Goals", "29"),
        ("Chapter 4: Project Objectives", "32"),
        ("    4.1 Primary Project Objective", "32"),
        ("    4.2 Specific Measurable Engineering Objectives (O1--O10)", "32"),
        ("    4.3 Success Criteria and Acceptance Metrics", "36"),
        ("Chapter 5: Sustainable Development Goals (SDG) Mapping", "38"),
        ("    5.1 Introduction to UN SDGs in Public Sector AI", "38"),
        ("    5.2 Identified SDGs and Alignment Matrix", "39"),
        ("    5.3 Detailed Reasoning (SDG 16, 10, 9, 17)", "40"),
        ("    5.4 Honest Environmental Assessment & Green AI Compute", "42"),
        ("Chapter 6: Methodology and Design Approach", "45"),
        ("    6.1 Architectural Overview: 5-Tier Modular Monolith", "45"),
        ("    6.2 Detailed Module Workflows (Modules A, B, C, D)", "47"),
        ("    6.3 14-Step End-to-End Processing Workflow", "51"),
        ("    6.4 Evidence-Grounded Synthesis & Gate 2 Circuit Breaker", "53"),
        ("Chapter 7: Tools and Technology", "56"),
        ("    7.1 Categorized Technology Stack", "56"),
        ("    7.2 Detailed Role of Key Frameworks (Next.js, FastAPI, Supabase)", "57"),
        ("    7.3 Architectural Justification of Selected Technologies", "59"),
        ("Chapter 8: Review 2 Implementation and Empirical Results", "61"),
        ("    8.1 Truthful Review 2 Implementation Status", "61"),
        ("    8.2 Module A Implementation: 8 Statutory Acts & Chunking", "62"),
        ("    8.3 Module B Implementation: 12 Welfare Schemes & Eligibility", "65"),
        ("    8.4 Module C Implementation: 40+ Node NetworkX Graph & RRF", "68"),
        ("    8.5 Module D Implementation: Heuristic Regex Triage & Cloud Storage", "71"),
        ("    8.6 Authentic Live System Prototype Showcase", "74"),
        ("    8.7 Comprehensive Empirical Test Results (129 Tests, 31 Routes)", "78"),
        ("Chapter 9: Teamwork and Collaboration Reflections", "82"),
        ("    9.1 Team Organization and Agile Dynamics", "82"),
        ("    9.2 RACI Responsibility Assignment Matrix", "83"),
        ("    9.3 Engineering Case Study: Resolving Serverless Cold Starts", "84"),
        ("    9.4 Individual In-Depth Student Reflections (Devansh, Khushbu, Anushka, Rahul)", "86"),
        ("    9.5 External Engagement & Industry Exposure Profiles", "90"),
        ("Chapter 10: Implementation Plan for Semester 8", "92"),
        ("    10.1 Review 2 Milestone Completion Summary", "92"),
        ("    10.2 Practical 5-Phase Semester 8 Delivery Plan", "93"),
        ("    10.3 Risk Assessment and Mitigation Strategies", "95"),
        ("Chapter 11: Summary and Conclusions", "97"),
        ("    11.1 Summary of Research and Engineering Achievements", "97"),
        ("    11.2 Main Technical and Empirical Findings", "98"),
        ("    11.3 Contributions to Knowledge and Public Sector AI", "99"),
        ("    11.4 Practical Implications for Citizens and Legal Aid", "100"),
        ("    11.5 Final Thoughts and Academic Defense Readiness", "101"),
        ("Bibliography", "103"),
        ("Appendix A: Production Route Inventory", "108"),
        ("Appendix B: Core API Data Transfer Objects (Pydantic)", "110"),
        ("Appendix C: Academic Integrity and Verification Statement", "112")
    ]

    toc_tbl = doc.add_table(rows=len(toc_items), cols=2)
    toc_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, (title, page_no) in enumerate(toc_items):
        cell_t = toc_tbl.cell(idx, 0)
        cell_p = toc_tbl.cell(idx, 1)
        cell_t.paragraphs[0].text = title
        cell_p.paragraphs[0].text = page_no
        cell_p.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_t = cell_t.paragraphs[0]
        p_p = cell_p.paragraphs[0]
        if "Chapter" in title or title in ["Certificate", "Candidate's Declaration", "Certificate of Plagiarism Check", "Acknowledgements", "Abstract", "Bibliography"]:
            p_t.runs[0].font.bold = True
            p_p.runs[0].font.bold = True
            p_t.runs[0].font.color.rgb = COLOR_NAVY
        p_t.runs[0].font.size = Pt(10.5)
        p_p.runs[0].font.size = Pt(10.5)
        set_cell_margins(cell_t, top=40, bottom=40, left=50, right=50)
        set_cell_margins(cell_p, top=40, bottom=40, left=50, right=50)

    # =========================================================================
    # CHAPTER 1: PROBLEM IDENTIFICATION
    # =========================================================================
    add_chapter_heading("Chapter 1", "Problem Identification")

    add_sec_heading("1.1 Background and Industrial Context")
    add_p(
        "In contemporary constitutional democracies such as the Republic of India, equal access to justice, legal transparency, "
        "and public entitlement realization represent foundational pillars of the rule of law. Over the past decade, the rapid "
        "acceleration of digital public infrastructure under the Digital India umbrella has transformed public administration. "
        "Platforms including e-Courts, India Code, the National Government Services Portal, myScheme, e-Daakhil, and CPGRAMS "
        "have made millions of statutes, court cause lists, welfare notifications, and grievance workflows available online. "
        "Yet, despite this digital ubiquity, a profound structural chasm remains between raw data availability and actionable "
        "citizen empowerment.\n\n"
        "The Indian socio-legal ecosystem is characterized by extraordinary polycentric complexity. At the statutory level, citizens "
        "are governed by over 800 central acts, thousands of state-specific enactments, and countless subordinate rules, statutory orders, "
        "and binding judicial precedents. Compounding this challenge is the ongoing legislative transition from colonial-era legal codes "
        "to modern indigenous frameworks, notably the replacement of the Indian Penal Code (IPC 1860) and Code of Criminal Procedure "
        "(CrPC 1973) with the Bharatiya Nyaya Sanhita (BNS 2023) and Bharatiya Nagarik Suraksha Sanhita (BNSS 2023). For vulnerable, "
        "marginalized, and lower-income citizens, navigating this complex landscape without specialized counsel is nearly impossible."
    )

    add_sec_heading("1.2 The Existing Citizen Problem & Seven Core Pain Points")
    add_p(
        "Empirical investigation of citizen interaction with the Indian administrative and judicial mechanisms reveals seven persistent, "
        "systemic failure modes:"
    )
    
    pain_points = [
        ("1. Jurisdictional and Forum Ambiguity:", "Citizens cannot determine whether an issue belongs before a District Consumer Forum, a Civil Court, an Industrial Labour Tribunal, or an Executive Magistrate, frequently leading to rejected petitions, wasted filing fees, and expired limitation periods."),
        ("2. Cognitive Intimidation and Notice Panic:", "Official communications (such as show-cause notices, eviction orders, summons, or Section 138 demand notices) are written in dense, archaic legalese. Misinterpreting these notices causes citizens to miss strict statutory deadlines (often 15 to 30 days), resulting in adverse ex-parte decrees."),
        ("3. Opaque Welfare Entitlement Discovery:", "While Central and State Governments fund extensive social safety nets (e.g., PM-KISAN, Ayushman Bharat PM-JAY, PMAY, NSAP), eligible beneficiaries fail to access them due to fragmented departmental portals, opaque qualification rules, and bureaucratic gatekeeping."),
        ("4. Procedural and Documentation Friction:", "Every legal grievance and scheme claim requires strict documentary prerequisites (caste certificates, revenue records, affidavits, bank statements). Omitting a single document triggers immediate portal rejection and administrative despair."),
        ("5. Prohibitive Advisory Costs:", "Quality private legal consultations typically cost between INR 2,000 and INR 10,000 per hour, rendering professional counsel financially inaccessible for over 70% of Indian households. While legal-aid clinics exist under Article 39A, they remain severely overburdened."),
        ("6. Proliferation of Generative AI Hallucination:", "Citizens increasingly turn to commercial AI chatbots (ChatGPT/Gemini) for legal advice. However, general-purpose LLMs hallucinate non-existent statutory sections, cite repealed provisions, and fabricate court precedents at alarming rates (>35%), posing grave legal risks."),
        ("7. Architectural Silos Across Public Systems:", "Existing government digital systems operate as isolated islands. The judiciary's e-Courts system does not communicate with welfare portals (myScheme), nor with legal aid authorities (NALSA), forcing citizens to manually act as the integration glue.")
    ]
    for p_title, p_desc in pain_points:
        p = add_p(p_title + " ", bold=True, color=COLOR_NAVY)
        p.add_run(p_desc)

    add_sec_heading("1.3 Why Current Approaches Are Inadequate")
    add_p(
        "Current technological and institutional interventions fail to address these systemic problems in an integrated manner:\n\n"
        "1. Static Text Repositories: Portals such as India Code and e-Courts function purely as passive document archives. They lack conversational query understanding, automated legal reasoning, and plain-language guidance linking grievances to procedural remedies.\n\n"
        "2. Government Chatbots (Nyaya Setu): While initiatives like Nyaya Setu represent positive steps, they operate primarily as stateless, single-turn informational responders. They lack contextual session memory, provide zero integration with welfare schemes, cannot parse or triage uploaded citizen documents, and lack deterministic circuit breakers to verify factual grounding.\n\n"
        "3. Commercial Foundation Models: Commercial LLMs treat statutory interpretation as an unconstrained text generation task. Because legal advice requires absolute factual precision---where an incorrect section number or missed limitation deadline alters legal outcomes entirely---unconstrained probabilistic text generation is fundamentally dangerous in civic domains."
    )

    add_sec_heading("1.4 Motivation for an Evidence-Grounded Civic Platform")
    add_p(
        "The urgent necessity for an equitable, trustworthy civic technology platform motivates the conception and development of CivicSphere AI. "
        "Rather than viewing legal guidance, welfare navigation, and document processing as isolated technical tasks, CivicSphere AI unifies them into "
        "an integrated, evidence-grounded agentic workflow.\n\n"
        "The core motivation is governed by three foundational design principles:\n"
        "• Zero-Hallucination Evidence Grounding: The platform must never generate a statutory assertion, procedural deadline, or rights claim without explicitly linking that claim to a verified, authoritative statutory section chunk or official government notification. Where evidence is ambiguous or confidence is low, the system must trigger deterministic circuit breakers rather than hallucinating.\n"
        "• Cross-Domain Contextual Synergy: A citizen's real-world problem does not conform to departmental boundaries. A labourer facing unlawful wage withholding requires employment law guidance, welfare entitlement discovery (e.g., e-Shram relief), and document extraction from their employment letter simultaneously. CivicSphere AI bridges these domains seamlessly.\n"
        "• Privacy by Design and Democratic Trust: In strict compliance with the Digital Personal Data Protection (DPDP) Act 2023, the platform must guarantee that citizen queries, uploaded notices, and personal identifying documents are treated with utmost confidentiality, stored in private encrypted object buckets, and purged permanently upon user request, while retaining immutable audit trails for transparent system governance."
    )

    # Save document checkpoint
    doc.save(r"docs\review-2-submission\CivicSphere_AI_Review_2_Report.docx")
    print("Checkpoint 1: Front Matter + Chapter 1 written.")

if __name__ == "__main__":
    create_report()
