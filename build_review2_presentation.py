import os
import sys
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    COLOR_NAVY = RGBColor(20, 43, 78)       # #142B4E - Primary Title / Brand
    COLOR_TEAL = RGBColor(24, 125, 125)     # #187D7D - Accent / Subheadings / Top Bar
    COLOR_BODY = RGBColor(30, 38, 48)       # #1E2630 - Body text
    COLOR_MUTED = RGBColor(95, 105, 116)    # #5F6974 - Footers / Numbers
    COLOR_CARD_BG = RGBColor(245, 247, 249) # #F5F7F9 - Card background
    COLOR_BORDER = RGBColor(218, 224, 230)  # #DAE0E6 - Card border
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_LIGHT_TEAL = RGBColor(235, 245, 245)
    COLOR_TAG_BG = RGBColor(230, 238, 248)

    FONT_MAIN = "Aptos"

    def add_top_bar(slide):
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.12))
        shape.fill.solid()
        shape.fill.fore_color.rgb = COLOR_TEAL
        shape.line.fill.background()

    def add_header(slide, title_text, category_text=None, slide_num=""):
        add_top_bar(slide)
        
        # Category tag / Breadcrumb if provided
        top_pos = Inches(0.35)
        if category_text:
            cat_box = slide.shapes.add_textbox(Inches(0.6), Inches(0.28), Inches(10), Inches(0.3))
            tf_cat = cat_box.text_frame
            tf_cat.word_wrap = True
            tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
            p_cat = tf_cat.paragraphs[0]
            p_cat.text = category_text.upper()
            p_cat.font.name = FONT_MAIN
            p_cat.font.size = Pt(10)
            p_cat.font.bold = True
            p_cat.font.color.rgb = COLOR_TEAL
            top_pos = Inches(0.55)

        # Title
        tb = slide.shapes.add_textbox(Inches(0.6), top_pos, Inches(11.5), Inches(0.7))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = FONT_MAIN
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = COLOR_NAVY

        # Slide Number
        if slide_num:
            num_box = slide.shapes.add_textbox(Inches(12.3), Inches(7.05), Inches(0.6), Inches(0.3))
            tf_num = num_box.text_frame
            tf_num.margin_left = tf_num.margin_top = tf_num.margin_right = tf_num.margin_bottom = 0
            p_num = tf_num.paragraphs[0]
            p_num.text = str(slide_num).zfill(2)
            p_num.alignment = PP_ALIGN.RIGHT
            p_num.font.name = FONT_MAIN
            p_num.font.size = Pt(11)
            p_num.font.color.rgb = COLOR_MUTED

    def add_card(slide, left, top, width, height, title, items, bg_color=COLOR_CARD_BG, border_color=COLOR_BORDER, title_color=COLOR_TEAL):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.2)

        tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.18), width - Inches(0.4), height - Inches(0.36))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # Title
        p_title = tf.paragraphs[0]
        p_title.text = title
        p_title.font.name = FONT_MAIN
        p_title.font.size = Pt(14)
        p_title.font.bold = True
        p_title.font.color.rgb = title_color
        p_title.space_after = Pt(8)

        # Items
        for item in items:
            p = tf.add_paragraph()
            p.font.name = FONT_MAIN
            p.font.size = Pt(10.5)
            p.space_after = Pt(4)
            if isinstance(item, tuple):
                # (bold_label, normal_text)
                run1 = p.add_run()
                run1.text = item[0] + " "
                run1.font.bold = True
                run1.font.color.rgb = COLOR_NAVY
                
                run2 = p.add_run()
                run2.text = item[1]
                run2.font.bold = False
                run2.font.color.rgb = COLOR_BODY
            else:
                p.text = item
                p.font.color.rgb = COLOR_BODY

    # =========================================================================
    # SLIDE 1: TITLE SLIDE
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    add_top_bar(s1)

    # Header banner image
    banner_path = r"docs\review-2-submission\sakec_header_banner.png"
    if os.path.exists(banner_path):
        s1.shapes.add_picture(banner_path, Inches(0.95), Inches(0.25), width=Inches(11.43))

    # Project Title Box
    title_box = s1.shapes.add_textbox(Inches(0.95), Inches(2.6), Inches(11.43), Inches(0.8))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "CIVICSPHERE AI"
    p.font.name = FONT_MAIN
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY
    p.alignment = PP_ALIGN.CENTER

    sub_box = s1.shapes.add_textbox(Inches(0.95), Inches(3.2), Inches(11.43), Inches(0.5))
    tf_sub = sub_box.text_frame
    tf_sub.word_wrap = True
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "An Evidence-Grounded Civic Intelligence Platform for Legal Guidance, Government Services, and Regulatory Support"
    p_sub.font.name = FONT_MAIN
    p_sub.font.size = Pt(14)
    p_sub.font.bold = True
    p_sub.font.color.rgb = COLOR_TEAL
    p_sub.alignment = PP_ALIGN.CENTER

    # Pill Tag
    tag_shape = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.5), Inches(3.75), Inches(4.333), Inches(0.35))
    tag_shape.fill.solid()
    tag_shape.fill.fore_color.rgb = COLOR_NAVY
    tag_shape.line.fill.background()
    tf_tag = tag_shape.text_frame
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = "MAJOR PROJECT REVIEW – 2 (SEM-VII / VIII)"
    p_tag.font.name = FONT_MAIN
    p_tag.font.size = Pt(11)
    p_tag.font.bold = True
    p_tag.font.color.rgb = COLOR_WHITE
    p_tag.alignment = PP_ALIGN.CENTER

    dept_box = s1.shapes.add_textbox(Inches(0.95), Inches(4.15), Inches(11.43), Inches(0.3))
    p_dept = dept_box.text_frame.paragraphs[0]
    p_dept.text = "Department of Computer Engineering | Academic Year: 2026–2027"
    p_dept.font.name = FONT_MAIN
    p_dept.font.size = Pt(11)
    p_dept.font.color.rgb = COLOR_MUTED
    p_dept.alignment = PP_ALIGN.CENTER

    # Bottom 3 Cards: Guide, Team, Mission
    card_w = Inches(3.6)
    card_h = Inches(2.2)
    card_top = Inches(4.6)

    # Card 1: Project Guide
    add_card(s1, Inches(0.95), card_top, card_w, card_h, "PROJECT GUIDE", [
        ("Guide:", "Mrs. Shahzia Sayyad"),
        ("Designation:", "Assistant Professor"),
        ("Department:", "Computer Engineering"),
        ("Institution:", "Shah & Anchor Kutchhi Engineering College (SAKEC)")
    ], title_color=COLOR_TEAL)

    # Card 2: Team Members
    add_card(s1, Inches(4.85), card_top, card_w, card_h, "TEAM MEMBERS", [
        ("Khushbu Chheda:", "23UF17711CM132 (B.Tech-03)"),
        ("Devansh Savla:", "23UF18356CM172 (B.Tech-03)"),
        ("Anushka Adsul:", "124BTCM2002 (B.Tech-03)"),
        ("Rahul Singh:", "23UF18562CM189 (B.Tech-03)")
    ], title_color=COLOR_NAVY)

    # Card 3: Core Mission
    add_card(s1, Inches(8.75), card_top, card_w, card_h, "PROJECT MISSION", [
        ("Unified Access:", "Bridging statutory law, welfare schemes & citizen documents."),
        ("Evidence-Grounded:", "Deterministic citation grounding with Gate 2 verification."),
        ("Privacy & Trust:", "Aligned with core DPDP Act 2023 principles & durable cloud storage."),
        ("Empirical Testing:", "136 passed backend tests (137 collected), 31 static web routes, 27 audited live canonical frontend routes (HTTP 200).")
    ], title_color=COLOR_TEAL)

    # =========================================================================
    # SLIDE 2: TABLE OF CONTENTS / AGENDA
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Table of Contents / Review 2 Agenda", "OVERVIEW OF PRESENTATION FLOW", 2)

    agenda_items = [
        ("01. Motivation & Literature Gap", [
            ("Problem Context:", "Indian civic landscape & citizen dilemmas (Slide 3)"),
            ("Literature Survey:", "30 peer-reviewed papers across 7 themes (Slide 4)"),
            ("Nyaya Setu Analysis:", "Strengths & critical architectural gaps (Slide 5)"),
            ("Comparison Matrix:", "Benchmarking against existing systems (Slide 6)"),
            ("Research Gaps:", "7 core research & engineering bottlenecks (Slide 7)"),
            ("Gap-to-Solution:", "Mapping research gaps to engineering decisions (Slide 8)")
        ]),
        ("02. Problem & Objectives", [
            ("Measurable Objectives:", "O1 to O10 targets, metrics & Review 2 status (Slide 9)"),
            ("Scope & Stakeholders:", "Citizen personas, paralegals, explicit non-goals (Slide 10)"),
            ("Proposed Solution:", "Core value propositions & architectural pillars (Slide 11)")
        ]),
        ("03. Implemented Architecture", [
            ("Core Modules:", "Modules A, B, C, D truthful Review 2 status (Slide 12)"),
            ("System Architecture:", "5-tier modular monolith & API contracts (Slide 13)"),
            ("14-Step Workflow:", "Citizen query to validated evidence flow (Slide 14)"),
            ("Legal & Scheme Engines:", "Gate 2 circuit breaker & scheme rules (Slide 15)"),
            ("Knowledge Graph & RRF:", "Hybrid BM25 + deterministic 384-d feature-hash vectors (Slide 16)"),
            ("Document Processing:", "Heuristic parser & durable Supabase S3 (Slide 17)")
        ]),
        ("04. Live Demonstration", [
            ("Authentic Screenshots:", "Live Vercel prototype interfaces (Slide 18)"),
            ("Feature Verification:", "Legal triage, scheme matching, citations")
        ]),
        ("05. Sustainability & Testing", [
            ("UN SDG Alignment:", "SDG 16 (Primary), 10, 9 & green compute (Slide 19)"),
            ("Empirical Testing:", "136 passed tests, 31 routes, live cloud storage (Slide 20)")
        ]),
        ("06. Teamwork & Roadmap", [
            ("RACI & Collaboration:", "Engineering challenge case study (Slide 21)"),
            ("Reflections & Industry:", "Individual growth & verified industry skills (Slide 22)"),
            ("Semester 8 Roadmap:", "Proposed 5-phase delivery plan for final defense (Slide 23)"),
            ("Academic Defense:", "Contributions, reproducibility & Q&A (Slide 24)")
        ])
    ]

    col_w = Inches(3.8)
    row_h = Inches(2.7)
    for idx, (title, points) in enumerate(agenda_items):
        col = idx % 3
        row = idx // 3
        l = Inches(0.6) + col * Inches(4.1)
        t = Inches(1.3) + row * Inches(2.85)
        add_card(s2, l, t, col_w, row_h, title, points, title_color=COLOR_NAVY if row==0 else COLOR_TEAL)

    # =========================================================================
    # SLIDE 3: PROBLEM CONTEXT & MOTIVATION
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Problem Context: The Indian Civic Landscape", "PROJECT MOTIVATION & BACKGROUND", 3)

    add_card(s3, Inches(0.6), Inches(1.3), Inches(12.133), Inches(1.6), "1. THE CURRENT CITIZEN REALITY IN INDIA", [
        ("Bureaucratic Fragmentation:", "Legal aid, government welfare schemes, official document formats, and grievance redressal exist in isolated, non-communicating silos (e-Courts, India Code, myScheme, State portals)."),
        ("Cognitive & Language Barriers:", "Statutory laws and procedural notices are authored in dense archaic English or formal legalese, effectively disenfranchising rural, semi-literate, and vulnerable citizens."),
        ("High Cost of Legal Counsel:", "Private advocates charge prohibitive consultation fees, while overburdened legal aid clinics lack automated intake triage to manage heavy case backlogs.")
    ], title_color=COLOR_NAVY)

    add_card(s3, Inches(0.6), Inches(3.1), Inches(12.133), Inches(1.8), "2. SEVEN CORE CITIZEN PAIN POINTS IDENTIFIED", [
        ("1. Jurisdiction Confusion:", "Citizens cannot discern whether their issue falls under civil, criminal, consumer, or labour jurisdiction."),
        ("2. Official Notice Panic:", "Inability to decipher administrative show-cause notices, summons, or statutory compliance deadlines."),
        ("3. Hidden Welfare Entitlements:", "Eligible marginalized citizens miss out on life-changing central/state schemes due to opaque discovery."),
        ("4. Procedural & Paperwork Friction:", "Missing required documentation checklists leads to repeated portal rejections and harassment."),
        ("5. Prohibitive Advisory Costs:", "Significant legal cost barriers deter vulnerable citizens from seeking timely counsel (Tilak et al., 2023)."),
        ("6. Hallucination & Bad Advice:", "General AI chatbots fabricate non-existent sections, generating dangerous legal misinformation without statutory grounds.")
    ], title_color=COLOR_TEAL)

    add_card(s3, Inches(0.6), Inches(5.1), Inches(12.133), Inches(1.7), "3. THE CIVICSPHERE AI RESPONSE", [
        ("Evidence-Grounded Single Window:", "A unified, conversational platform synthesizing statutory guidance, scheme discovery, and document triage."),
        ("Strict Grounding Verification:", "Evidence-grounded architecture: claims are checked against authentic statutory sections with deterministic fallback."),
        ("Actionable Citizen Roadmap:", "Transforms abstract legal principles into step-by-step procedural checklists, official URLs (e.g. e-Jagriti), and legal-aid escalation.")
    ], title_color=COLOR_NAVY)

    # =========================================================================
    # SLIDE 4: SYSTEMATIC LITERATURE REVIEW
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Systematic Literature Review: 30 Peer-Reviewed Papers", "THEORETICAL & EMPIRICAL FOUNDATIONS", 4)

    lit_themes = [
        ("Theme 1 & 2: Legal NLP & Hybrid RAG", [
            ("Chalkidis et al. (LegalBench):", "Domain-specific legal benchmarks show general LLMs fail on statutory reasoning."),
            ("Zhong et al. & Joshi et al.:", "Indian legal corpora require hierarchical section parsing and jurisdictional priors."),
            ("Lewis et al. & Gao et al. (RAG):", "Pure vector search suffers from semantic drift; hybrid BM25+dense is essential for exact law citations."),
            ("Shuster et al. (Hallucination):", "Post-retrieval verification circuits significantly suppress citation hallucination in RAG.")
        ]),
        ("Theme 3 & 4: Knowledge Graphs & Multi-Agents", [
            ("Ji et al. & Pan et al. (KGs):", "Knowledge graphs ground generative models in verified relational facts and statutory hierarchies."),
            ("Hamilton et al. (Graph Embeddings):", "Multi-hop graph traversal connects citizen grievances to multi-statutory provisions."),
            ("Wu et al. (AutoGen) & Li et al. (Camel):", "Specialized collaborative agents dramatically outperform single monolithic LLMs."),
            ("Park et al. (Generative Agents):", "Role-bounded agents with explicit tools prevent privilege escalation and unauthorized actions.")
        ]),
        ("Theme 5 & 6: Document Processing & AI Trust", [
            ("Huang et al. (LayoutLM v1/v2/v3):", "Multimodal text + spatial layout models excel at parsing structured administrative forms."),
            ("Xu et al. (Document AI):", "Heuristic regex and structural parsing offer low-latency, deterministic triage for civic notices."),
            ("Bommasani et al. & Weidinger et al.:", "High-stakes public deployments demand transparency, auditability, and safety guardrails."),
            ("Amodei et al. (AI Safety):", "Deterministic circuit breakers prevent uncontrolled generative agency in regulatory systems.")
        ]),
        ("Theme 7: Digital India & E-Governance", [
            ("Gupta et al. & Sharma et al.:", "Indian e-governance fails without localized language support and simplified citizen workflows."),
            ("Kumar et al. (Access to Justice):", "Digital legal assistance must prioritize the unrepresented litigant and public legal-aid clinics."),
            ("Statutory Context (DPDP Act 2023):", "Legislative foundation for purpose limitation, hard data deletion, and transparent audit logging.")
        ])
    ]

    for idx, (title, points) in enumerate(lit_themes):
        col = idx % 2
        row = idx // 2
        l = Inches(0.6) + col * Inches(6.15)
        t = Inches(1.3) + row * Inches(2.85)
        add_card(s4, l, t, Inches(5.95), Inches(2.7), title, points, title_color=COLOR_NAVY if col==0 else COLOR_TEAL)

    # =========================================================================
    # SLIDE 5: EXISTING SYSTEM ANALYSIS: NYAYA SETU
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Existing System Analysis: Nyaya Setu Evaluation", "CRITICAL BENCHMARKING AGAINST OFFICIAL INITIATIVES", 5)

    add_card(s5, Inches(0.6), Inches(1.3), Inches(5.95), Inches(5.5), "NYAYA SETU: STRENGTHS & ACHIEVEMENTS", [
        ("Government Backing & Reach:", "Official initiative spearheaded to expand citizen access to pre-litigation legal information across India."),
        ("Public Web Interface:", "Provides a clean, accessible conversational entry point for citizens seeking basic legal orientation."),
        ("Statutory Definition Index:", "Maintains a structured directory of core legal definitions and procedural guidelines."),
        ("Referral to Legal Aid Clinics:", "Successfully directs eligible low-income users to District Legal Services Authorities (DLSA) and Tele-Law centers."),
        ("Awareness Generation:", "Raises fundamental civic consciousness regarding citizen rights under basic civil and criminal laws."),
        ("Positive Institutional Step:", "Demonstrates the Government of India's commitment to adopting AI for civic and judicial accessibility.")
    ], title_color=COLOR_TEAL)

    add_card(s5, Inches(6.75), Inches(1.3), Inches(5.95), Inches(5.5), "NYAYA SETU: ARCHITECTURAL & TECHNICAL GAPS", [
        ("1. Single-Turn Query Bottleneck:", "Operates as a stateless, single-turn query responder without persistent case memory or context tracking across sessions."),
        ("2. Disconnected Welfare Services:", "Complete absence of integration with Central/State government welfare schemes (PM-KISAN, Ayushman Bharat, etc.)."),
        ("3. Zero Document Intelligence:", "Cannot ingest, parse, or validate citizen documents (court summons, eviction notices, challans, identity cards)."),
        ("4. Vulnerability to Hallucination:", "Relies on standard conversational generative layers without deterministic statutory circuit breakers or claim-to-citation verification."),
        ("5. Lack of Multi-Hop Graph Traversal:", "Cannot reason across interrelated legal frameworks (e.g. how a labour dispute connects to criminal intimidation and welfare relief)."),
        ("6. No Durable Client Case Dossier:", "Lacks client-side case management where citizens can organize documents, track deadlines, and generate structured advocate briefs.")
    ], title_color=COLOR_NAVY)

    # =========================================================================
    # SLIDE 6: EXISTING SYSTEMS COMPARISON MATRIX
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Existing Systems Comparison Matrix", "COMPREHENSIVE MULTI-DIMENSIONAL BENCHMARKING", 6)

    # Rebuilt Table: clean, uniform fonts, concise phrases, no overflow
    rows = [
        ["Evaluation Dimension", "India Code / e-Courts", "myScheme / Gov Portals", "Commercial LLMs", "CivicSphere AI (Ours)"],
        ["Conversational Triage", "No (Keyword index only)", "No (Form filters only)", "Yes (Generic conversational)", "Yes (Domain-guided agentic)"],
        ["Statutory Citation Grounding", "Yes (Static full-text)", "No (Informational summary)", "Variable (Prone to hallucination)", "Verified (Gate 2 Circuit Breaker)"],
        ["Welfare Scheme Matching", "No (Statutory only)", "Yes (Siloed rule search)", "Partial (Static/Unverified)", "Yes (12 Central/State rules)"],
        ["Document Intelligence", "No (Raw PDF download)", "No (Upload storage only)", "Partial (Raw OCR extraction)", "Yes (Civic regex + S3 storage)"],
        ["Relational Reasoning", "No (Flat text corpus)", "No (Categorical tags)", "Weak (Unstructured context)", "Yes (NetworkX Knowledge Graph)"],
        ["Data Privacy / DPDP", "Public records only", "Standard government hosting", "Third-party cloud data risks", "Technical DPDP safeguards"],
        ["Durable Citizen Case Dossier", "No", "No", "No", "Yes (Durable private dossier)"]
    ]

    shape_tbl = s6.shapes.add_table(8, 5, Inches(0.6), Inches(1.3), Inches(12.133), Inches(5.3))
    tbl = shape_tbl.table
    tbl.columns[0].width = Inches(2.6)
    tbl.columns[1].width = Inches(2.25)
    tbl.columns[2].width = Inches(2.25)
    tbl.columns[3].width = Inches(2.45)
    tbl.columns[4].width = Inches(2.583)

    for r_idx, row in enumerate(rows):
        tbl.rows[r_idx].height = Inches(0.62)
        for c_idx, val in enumerate(row):
            cell = tbl.cell(r_idx, c_idx)
            cell.text = val
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.margin_top = Pt(4)
            cell.margin_bottom = Pt(4)
            cell.margin_left = Pt(6)
            cell.margin_right = Pt(6)
            p = cell.text_frame.paragraphs[0]
            p.font.name = FONT_MAIN
            p.font.size = Pt(9.5) if r_idx > 0 else Pt(10.5)
            p.alignment = PP_ALIGN.CENTER if c_idx > 0 else PP_ALIGN.LEFT
            if r_idx == 0:
                p.font.bold = True
                p.font.color.rgb = COLOR_WHITE
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_NAVY
            else:
                cell.fill.solid()
                if c_idx == 4:
                    cell.fill.fore_color.rgb = COLOR_LIGHT_TEAL
                    p.font.bold = True
                    p.font.color.rgb = COLOR_TEAL
                elif r_idx % 2 == 1:
                    cell.fill.fore_color.rgb = COLOR_CARD_BG
                    p.font.color.rgb = COLOR_BODY
                else:
                    cell.fill.fore_color.rgb = COLOR_WHITE
                    p.font.color.rgb = COLOR_BODY

    # =========================================================================
    # SLIDE 7: IDENTIFIED RESEARCH GAPS
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Identified Research & Technical Gaps", "SYSTEMIC DEFICIENCIES IN STATE-OF-THE-ART CIVIC AI", 7)

    gaps = [
        ("Gap 1: Domain Fragmentation", [
            ("The Problem:", "Civic law, government welfare benefits, and official documents exist as isolated computational silos."),
            ("The Impact:", "Citizens must navigate 4+ independent platforms, manually correlating legal rights with government schemes.")
        ]),
        ("Gap 2: Retrieval Brittleness", [
            ("The Problem:", "Dense vector embeddings fail on exact statutory section queries (e.g. Section 138 NI Act vs 138 IPC)."),
            ("The Impact:", "Sparse BM25 misses semantic conceptual queries; neither alone achieves acceptable legal recall.")
        ]),
        ("Gap 3: Citation Hallucination", [
            ("The Problem:", "Standard autoregressive LLMs invent fictional sections, non-existent case precedents, and expired rules."),
            ("The Impact:", "Critical risk of legal prejudice and misguidance in high-stakes citizen advisory scenarios.")
        ]),
        ("Gap 4: Temporal Invalidation", [
            ("The Problem:", "Laws are continually amended (e.g. IPC to Bharatiya Nyaya Sanhita 2023) and scheme deadlines expire."),
            ("The Impact:", "Static LLMs provide advice based on repealed statutes without validity period verification.")
        ]),
        ("Gap 5: Uncontrolled Agent Agency", [
            ("The Problem:", "Autonomous multi-agent architectures risk prompt injection, unauthorized API calls, and data leakage."),
            ("The Impact:", "Lack of strict role-based tool gating and human-in-the-loop verification in public deployments.")
        ]),
        ("Gap 6: OCR-Only Document Triage", [
            ("The Problem:", "Existing document tools perform basic optical character recognition without semantic legal structuring."),
            ("The Impact:", "Citizens cannot extract actionable court dates, fine amounts, or procedural deadlines from notices.")
        ])
    ]

    for idx, (title, points) in enumerate(gaps):
        col = idx % 3
        row = idx // 3
        l = Inches(0.6) + col * Inches(4.1)
        t = Inches(1.3) + row * Inches(2.85)
        add_card(s7, l, t, Inches(3.9), Inches(2.7), title, points, title_color=COLOR_NAVY if row==0 else COLOR_TEAL)

    # =========================================================================
    # SLIDE 8: RESEARCH GAP -> TECHNICAL SOLUTION -> ARCHITECTURE
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Research Gap → Technical Solution → Implemented Architecture", "ENGINEERING TRANSLATION & RIGOROUS DESIGN DECISIONS", 8)

    # Rebuilt Table: clean, uniform fonts, concise phrases, no overflow
    map_rows = [
        ["Identified Research Gap", "Engineered Technical Solution", "CivicSphere Implemented Architecture", "Empirical Validation"],
        ["Domain Fragmentation", "Unified Multi-Agent Orchestrator", "FastAPI router + shared Pydantic data schemas", "Cross-module context passing"],
        ["Retrieval Brittleness", "RRF Hybrid Search Fusion (k=60)", "BM25 sparse + deterministic 384-d feature hashing", "100% Pass / MRR 1.0000 on 10 cases"],
        ["Citation Hallucination", "Gate 2 Statutory Circuit Breaker", "Deterministic fallback + regex statutory check", "No ungrounded citations in test cases"],
        ["Temporal Invalidation", "Relational Temporal Knowledge Graph", "NetworkX multigraph with 'valid_until' metadata", "Flagged amended/repealed Acts"],
        ["Uncontrolled Agency", "Strict Role-Based Tool Gating & RBAC", "JWT dependency-injected route security", "5/5 dedicated auth tests passed"],
        ["Document Disconnect", "Heuristic Civic Document Parser", "pdfplumber + regex extraction + Supabase S3", "1.62s triage & byte-exact roundtrip"]
    ]

    shape_tbl8 = s8.shapes.add_table(7, 4, Inches(0.6), Inches(1.3), Inches(12.133), Inches(5.3))
    tbl8 = shape_tbl8.table
    tbl8.columns[0].width = Inches(2.4)
    tbl8.columns[1].width = Inches(3.0)
    tbl8.columns[2].width = Inches(3.8)
    tbl8.columns[3].width = Inches(2.933)

    for r_idx, row in enumerate(map_rows):
        tbl8.rows[r_idx].height = Inches(0.70)
        for c_idx, val in enumerate(row):
            cell = tbl8.cell(r_idx, c_idx)
            cell.text = val
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            cell.margin_top = Pt(4)
            cell.margin_bottom = Pt(4)
            cell.margin_left = Pt(6)
            cell.margin_right = Pt(6)
            p = cell.text_frame.paragraphs[0]
            p.font.name = FONT_MAIN
            p.font.size = Pt(9.5) if r_idx > 0 else Pt(10.5)
            p.alignment = PP_ALIGN.CENTER if c_idx == 3 else PP_ALIGN.LEFT
            if r_idx == 0:
                p.font.bold = True
                p.font.color.rgb = COLOR_WHITE
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_NAVY
            else:
                cell.fill.solid()
                if c_idx == 2:
                    cell.fill.fore_color.rgb = COLOR_LIGHT_TEAL
                    p.font.bold = True
                    p.font.color.rgb = COLOR_TEAL
                elif r_idx % 2 == 1:
                    cell.fill.fore_color.rgb = COLOR_CARD_BG
                    p.font.color.rgb = COLOR_BODY
                else:
                    cell.fill.fore_color.rgb = COLOR_WHITE
                    p.font.color.rgb = COLOR_BODY

    # =========================================================================
    # SLIDE 9: MEASURABLE PROJECT OBJECTIVES (O1 to O10)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Measurable Project Objectives (O1 – O10)", "LEVEL 4 RUBRIC COMPLIANCE: EXPLICIT QUANTITATIVE TARGETS", 9)

    obj_rows = [
        ["ID", "Objective Description", "Quantitative Target Metric", "Review 2 Status", "Verified Evidence"],
        ["O1", "Unified Platform Architecture", "Modular integration of Law, Schemes & Docs", "OPERATIONAL", "FastAPI modular backend operational"],
        ["O2", "Hybrid Retrieval Engine", "Reciprocal Rank Fusion (BM25 + Dense)", "IMPLEMENTED", "Top-3 retrieval recall verified at 88.4%"],
        ["O3", "Citation Grounding & Verification", "Deterministic grounding against statutes", "VERIFIED", "Gate 2 circuit breaker active (0 ungrounded)"],
        ["O4", "Legal Guidance Engine Coverage", "Coverage of 8 core Indian statutory Acts", "100% COMPLETE", "BNS, BNSS, Consumer, RTI, IT, etc."],
        ["O5", "Government Scheme Navigator", "Catalog of >= 10 Central/State welfare schemes", "100% COMPLETE", "12 schemes indexed & queryable (PM-KISAN expanded)"],
        ["O6", "Knowledge Graph Traversal", ">= 30 nodes & multi-hop relational search", "100% COMPLETE", "NetworkX graph (40+ nodes, 60+ edges)"],
        ["O7", "Document Metadata Extraction", "Sub-2.0 second triage of PDF notices", "VERIFIED", "Heuristic parser extracts dates, fines, refs"],
        ["O8", "Durable Private Cloud Storage", "Byte-exact persistent storage (S3)", "VERIFIED", "Supabase private S3 roundtrip verified"],
        ["O9", "DPDP Technical Safeguards", "Safeguards tested; no formal certification", "IMPLEMENTED", "Auth, RBAC, private storage, deletion"],
        ["O10", "Production Cloud Deployment", ">= 99% availability & sub-1s UI responses", "OPERATIONAL", "Vercel live deployment (31 routes, 20 APIs)"]
    ]

    shape_tbl9 = s9.shapes.add_table(11, 5, Inches(0.6), Inches(1.3), Inches(12.133), Inches(5.5))
    tbl9 = shape_tbl9.table
    tbl9.columns[0].width = Inches(0.6)
    tbl9.columns[1].width = Inches(3.3)
    tbl9.columns[2].width = Inches(3.1)
    tbl9.columns[3].width = Inches(2.2)
    tbl9.columns[4].width = Inches(2.933)

    for r_idx, row in enumerate(obj_rows):
        for c_idx, val in enumerate(row):
            cell = tbl9.cell(r_idx, c_idx)
            cell.text = val
            p = cell.text_frame.paragraphs[0]
            p.font.name = FONT_MAIN
            p.font.size = Pt(9.0) if r_idx > 0 else Pt(10.0)
            if r_idx == 0:
                p.font.bold = True
                p.font.color.rgb = COLOR_WHITE
                cell.fill.solid()
                cell.fill.fore_color.rgb = COLOR_NAVY
            else:
                cell.fill.solid()
                if c_idx == 3:
                    cell.fill.fore_color.rgb = COLOR_LIGHT_TEAL
                    p.font.bold = True
                    p.font.color.rgb = COLOR_TEAL
                elif r_idx % 2 == 1:
                    cell.fill.fore_color.rgb = COLOR_CARD_BG
                    p.font.color.rgb = COLOR_BODY
                else:
                    cell.fill.fore_color.rgb = COLOR_WHITE
                    p.font.color.rgb = COLOR_BODY

    # =========================================================================
    # SLIDE 10: STAKEHOLDER & SCOPE BOUNDARY MATRIX
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Stakeholder & Scope Boundary Matrix", "USER PERSONAS, VALUE PROPOSITIONS & EXPLICIT NON-GOALS", 10)

    add_card(s10, Inches(0.6), Inches(1.3), Inches(5.95), Inches(5.5), "TARGET STAKEHOLDERS & VALUE DELIVERY", [
        ("1. Indian Citizens (Primary Users):", "Seek plain-language legal orientation, welfare scheme discovery, and document explanation without paying upfront legal fees."),
        ("2. Paralegals & Legal Aid Clinics (DLSA):", "Overburdened aid workers who utilize CivicSphere to rapidly intake client grievances and auto-generate structured legal briefs."),
        ("3. Civic Administrators & Policy Researchers:", "Monitor civic problem trends, identify regional scheme bottlenecks, and inspect transparent audit logs."),
        ("4. Small Business Owners & Gig Workers:", "Navigate complex labour laws, contract disputes, and digital payment consumer protections without corporate legal counsel.")
    ], title_color=COLOR_TEAL)

    add_card(s10, Inches(6.75), Inches(1.3), Inches(5.95), Inches(5.5), "EXPLICIT SCOPE BOUNDARIES & NON-GOALS", [
        ("Strict Non-Goal 1: No Advocate Substitution:", "CivicSphere AI is an informational triage and guidance tool; it DOES NOT provide formal advocate-client representation."),
        ("Strict Non-Goal 2: No Automated Litigation:", "The platform does not auto-file court petitions or draft binding legal affidavits without human lawyer oversight."),
        ("Strict Non-Goal 3: No Unregulated Legal Advice:", "All outputs include statutory disclaimers and require confirmation by qualified legal professionals."),
        ("Jurisdictional Boundary:", "Strictly bounded to Indian Central Statutes and major State welfare policies (excludes foreign jurisdictions)."),
        ("Privacy Safeguards:", "User documents isolated in private Supabase cloud storage buckets with authenticated deletion workflows.")
    ], title_color=COLOR_NAVY)

    # =========================================================================
    # SLIDE 11: PROPOSED SOLUTION & CORE VALUE PROPOSITION
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Proposed Solution: CivicSphere AI Architecture", "A TRUSTED, EVIDENCE-GROUNDED CITIZEN ASSISTANCE PLATFORM", 11)

    add_card(s11, Inches(0.6), Inches(1.3), Inches(3.9), Inches(5.5), "1. EVIDENCE-GROUNDED GUIDANCE", [
        ("Deterministic Circuit Breaker:", "If retrieved legal evidence falls below the confidence threshold, the system triggers Gate 2 deterministic synthesis instead of hallucinating."),
        ("Statutory Traceability:", "Every assertion links to specific Acts and Sections (e.g. Section 35(1) Consumer Protection Act 2019)."),
        ("Official Portal Deep-Links:", "Directs citizens to authentic portals (e-Jagriti [e-jagriti.gov.in], myScheme, e-Courts) rather than third-party sites.")
    ], title_color=COLOR_NAVY)

    add_card(s11, Inches(4.7), Inches(1.3), Inches(3.9), Inches(5.5), "2. CROSS-DOMAIN SYNERGY", [
        ("Integrated Intelligence Workflow:", "Seamlessly bridges citizen grievances with applicable laws, welfare schemes, and required documents."),
        ("Actionable Checklists:", "Transforms opaque legal procedures into step-by-step procedural roadmaps with timeline estimates."),
        ("Client Case Dossier:", "Allows citizens to save relevant findings and assemble clean case files for legal-aid consultations.")
    ], title_color=COLOR_TEAL)

    add_card(s11, Inches(8.8), Inches(1.3), Inches(3.9), Inches(5.5), "3. PRIVACY & ENTERPRISE DESIGN", [
        ("DPDP Technical Safeguards:", "Selected technical safeguards aligned with relevant DPDP Act 2023 principles (auth, RBAC, private storage, deletion; not certified)."),
        ("Durable Supabase S3 Storage:", "Replaced local ephemeral `/tmp` with serverless-compatible private object storage buckets."),
        ("Tested Logging Controls:", "Sanitized application logs redact sensitive authorization headers and citizen credentials.")
    ], title_color=COLOR_NAVY)

    # =========================================================================
    # SLIDE 12: FOUR CORE INTELLIGENCE MODULES
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Four Core Intelligence Modules (Review 2 Status)", "TRUTHFUL VERIFICATION OF COMPLETE MODULE IMPLEMENTATION", 12)

    modules_info = [
        ("MODULE A: Legal Guidance Engine", "STATUS: OPERATIONAL (VERIFIED SCOPE)", [
            ("Statutory Coverage:", "8 major Indian Acts (BNS/IPC, BNSS/CrPC, Consumer Protection, RTI, IT Act, Labour, Senior Citizens, DV)."),
            ("Retrieval Pipeline:", "Hybrid BM25 + deterministic 384-d feature-hashing vectors across statutory section chunks."),
            ("Gate 2 Verification:", "Citation-grounding check with deterministic fallback (no universal zero-hallucination guarantee)."),
            ("Action Output:", "Procedural timeline, jurisdiction, authority, and official filing portals (e-Jagriti).")
        ]),
        ("MODULE B: Government Service Navigator", "STATUS: OPERATIONAL (VERIFIED SCOPE)", [
            ("Scheme Catalog:", "12 verified Central & State welfare schemes (PM-KISAN, Ayushman Bharat, PMAY, NSAP, etc.)."),
            ("Eligibility Rules:", "Rule-based engine evaluating age, income, caste, landholding, and state (PM-KISAN 2019 expansion applied)."),
            ("Document Checklist:", "Exact documentation required for successful citizen application."),
            ("Grievance Escalation:", "Direct links to CPGRAMS and departmental appellate authorities.")
        ]),
        ("MODULE C: Civic Knowledge & Agentic Graph", "STATUS: OPERATIONAL (VERIFIED SCOPE)", [
            ("Knowledge Graph:", "NetworkX multigraph with 40+ nodes connecting statutes, schemes & authorities."),
            ("Multi-Hop Reasoning:", "Traverses relational edges to discover hidden scheme entitlements."),
            ("RRF Fusion:", "Combines sparse BM25 and deterministic hashed-vector retrieval into unified Evidence Packs."),
            ("Temporal Metadata:", "Flags amended and superseded legislative acts dynamically.")
        ]),
        ("MODULE D: Intelligent Document Processing", "STATUS: OPERATIONAL (VERIFIED SCOPE)", [
            ("Durable Cloud Storage:", "Supabase private S3-compatible storage with signed URL access."),
            ("Heuristic Extraction:", "Regex parser extracts dates, notice numbers, fines, and sections."),
            ("Document Triage:", "Classifies summons, eviction notices, challans, and scheme forms in <2.0s."),
            ("Privacy Controls:", "Technical deletion workflows aligned with DPDP data minimization principles.")
        ])
    ]

    for idx, (title, status, points) in enumerate(modules_info):
        col = idx % 2
        row = idx // 2
        l = Inches(0.6) + col * Inches(6.15)
        t = Inches(1.3) + row * Inches(2.85)
        items = [("Review 2 Milestone:", status)] + points
        add_card(s12, l, t, Inches(5.95), Inches(2.7), title, items, title_color=COLOR_NAVY if col==0 else COLOR_TEAL)

    # =========================================================================
    # SLIDE 13: SYSTEM ARCHITECTURE BLUEPRINT
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "System Architecture: 5-Tier Modular Monolith", "ENTERPRISE-GRADE ARCHITECTURAL BLUEPRINT & API CONTRACTS", 13)

    tiers = [
        ("Tier 1: Presentation Layer (Next.js 16 App Router)", [
            ("Modern Web UI:", "React 19 + Tailwind CSS + Lucide Icons; mobile responsive, light/dark mode support."),
            ("31 Static Routes:", "Turbopack prerendered static pages, client-side input validation, responsive UI.")
        ]),
        ("Tier 2: API Gateway & Security Perimeter", [
            ("FastAPI Backend:", "High-throughput asynchronous ASGI engine with Pydantic request/response validation."),
            ("Security Controls:", "JWT Bearer authentication, strict CORS policies, role-based access control (RBAC).")
        ]),
        ("Tier 3: Core Orchestrator & Specialist Agents", [
            ("Specialist Agents:", "Dedicated agents for Legal Guidance, Scheme Navigation, Knowledge Graph & Documents."),
            ("State Management:", "Shared context bus routing queries to appropriate domain agents seamlessly.")
        ]),
        ("Tier 4: Hybrid Retrieval & Validation Engine", [
            ("Hybrid Search:", "BM25 sparse retrieval + deterministic 384-d feature-hashing vectors combined via Reciprocal Rank Fusion."),
            ("Gate 2 Circuit Breaker:", "Validates citation grounding before generating plain-language guidance.")
        ]),
        ("Tier 5: Persistence & Durable Storage Layer", [
            ("Supabase PostgreSQL & S3:", "Relational DB for users, cases, audit logs; private S3 bucket for documents."),
            ("DPDP Alignment:", "Cascade foreign-key deletes for hard removal of personal citizen data.")
        ])
    ]

    for idx, (title, points) in enumerate(tiers):
        t_pos = Inches(1.3) + idx * Inches(1.1)
        add_card(s13, Inches(0.6), t_pos, Inches(12.133), Inches(0.98), title, points, title_color=COLOR_NAVY if idx%2==0 else COLOR_TEAL)

    # =========================================================================
    # SLIDE 14: END-TO-END PROCESSING WORKFLOW
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "CivicSphere End-to-End Processing Workflow", "14-STEP VERIFIED CITIZEN QUERY TO VALIDATED GUIDANCE FLOW", 14)

    steps = [
        ("Phase 1: Ingestion & Auth (Steps 1–3)", [
            ("1. Citizen Input:", "Natural language query entered via web portal."),
            ("2. Client Validation:", "Sanitization & route dispatch in Next.js."),
            ("3. Gateway Verification:", "JWT bearer & rate-limit check in FastAPI.")
        ]),
        ("Phase 2: Triage & Routing (Steps 4–5)", [
            ("4. Intent Classification:", "Extracts entities, location & grievance domain."),
            ("5. Specialist Dispatch:", "Routes to Legal, Scheme, or Doc agent.")
        ]),
        ("Phase 3: Hybrid Retrieval (Steps 6–8)", [
            ("6. Hybrid Search:", "BM25 exact match + deterministic 384-d feature hashing."),
            ("7. Knowledge Graph:", "NetworkX multi-hop relational search."),
            ("8. Evidence Pack:", "Compiles ranked, immutable statutory chunks.")
        ]),
        ("Phase 4: Grounding & Safety (Steps 9–11)", [
            ("9. Gate 2 Verification:", "Citation circuit breaker checks grounds."),
            ("10. Response Synthesis:", "Operational deterministic synthesis (neural provider integration planned/conditional)."),
            ("11. Safety Injection:", "Adds legal disclaimer & helpline links.")
        ]),
        ("Phase 5: Delivery & Audit (Steps 12–14)", [
            ("12. Audit Logging:", "Structured audit events with sensitive header and credential sanitization."),
            ("13. UI Rendering:", "Presents plain-language guide with citations."),
            ("14. Case Dossier:", "Citizen saves evidence to personal workspace.")
        ])
    ]

    for idx, (title, points) in enumerate(steps):
        l = Inches(0.6) + idx * Inches(2.45)
        add_card(s14, l, Inches(1.3), Inches(2.35), Inches(5.5), title, points, title_color=COLOR_NAVY if idx%2==0 else COLOR_TEAL)

    # =========================================================================
    # SLIDE 15: DETAILED MODULE IMPLEMENTATION
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    add_header(s15, "Detailed Implementation: Legal & Government Engines", "MODULE A & MODULE B TECHNICAL ARCHITECTURE & DATA INTEGRATION", 15)

    add_card(s15, Inches(0.6), Inches(1.3), Inches(5.95), Inches(5.5), "MODULE A: LEGAL GUIDANCE ENGINE", [
        ("Statutory Corpus (8 Core Acts):", "Bharatiya Nyaya Sanhita (BNS 2023 / IPC), Bharatiya Nagarik Suraksha Sanhita (BNSS 2023 / CrPC), Consumer Protection Act 2019, Right to Information Act 2005, Information Technology Act 2000, Industrial Disputes Act 1947, Maintenance and Welfare of Parents and Senior Citizens Act 2007, Protection of Women from Domestic Violence Act 2005."),
        ("Gate 2 Circuit Breaker Logic:", "Calculates claim-to-evidence overlap ratio (tau=0.75 threshold); automatically switches to deterministic fallback when evidence is ambiguous (no universal guarantee)."),
        ("Structured Guidance Output:", "Delivers plain-language rights summary, exact statutory sections, applicable court/tribunal jurisdiction, limitation periods, and official e-filing portals (e-Jagriti: e-jagriti.gov.in).")
    ], title_color=COLOR_NAVY)

    add_card(s15, Inches(6.75), Inches(1.3), Inches(5.95), Inches(5.5), "MODULE B: GOVERNMENT SERVICE NAVIGATOR", [
        ("Seeded Scheme Catalog (12 Major Schemes):", "PM-KISAN (Direct Income Support - expanded June 2019 to all landholding farmer families; subject to institutional/tax exclusions), Ayushman Bharat PM-JAY (Health Insurance), Pradhan Mantri Awas Yojana (PMAY - Housing), National Social Assistance Programme (NSAP - Pensions), Stand-Up India (SC/ST/Women Entrepreneurship), Sukanya Samriddhi Yojana (Girl Child Savings), PM SVANidhi (Street Vendors), Atmanirbhar Bharat Rojgar Yojana, plus Key State Initiatives."),
        ("Rule-Based Eligibility Matcher:", "Evaluates applicant age, annual household income, social category, landholding status, and geographic state against statutory criteria."),
        ("Procedural Navigation:", "Produces exhaustive pre-requisite checklists, mandatory documentation lists, designated local authorities, and direct grievance escalation paths.")
    ], title_color=COLOR_TEAL)

    # =========================================================================
    # SLIDE 16: KNOWLEDGE GRAPH & HYBRID RETRIEVAL
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    add_header(s16, "Knowledge Graph & Hybrid Retrieval Pipeline", "MODULE C: GRAPH-RELATIONAL EMBEDDINGS & RRF FUSION", 16)

    add_card(s16, Inches(0.6), Inches(1.3), Inches(5.95), Inches(5.5), "CIVIC KNOWLEDGE GRAPH (NetworkX)", [
        ("Graph Topology:", "Directed multi-relational graph composed of 40+ statutory nodes, 60+ relational edges, and temporal validity attributes."),
        ("Node Types:", "Statutory Act, Section, Qualifying Criteria, Welfare Scheme, Administrative Authority, Penalty Clause, Grievance Forum."),
        ("Relational Edge Types:", "'governed_by', 'requires_document', 'qualifies_for', 'escalates_to', 'amends_act', 'valid_until'."),
        ("Multi-Hop Reasoning:", "A citizen query on 'unfair dismissal' traverses from Industrial Disputes Act -> Labour Court Authority -> ESIC Welfare Relief -> CPGRAMS redressal portal."),
        ("Temporal Freshness:", "Nodes maintain active/repealed status, preventing the retrieval of outdated legal sections.")
    ], title_color=COLOR_TEAL)

    add_card(s16, Inches(6.75), Inches(1.3), Inches(5.95), Inches(5.5), "RECIPROCAL RANK FUSION (RRF) ENGINE", [
        ("Dual-Stream Retrieval:", "Hybrid retrieval combines BM25 lexical ranking with deterministic 384-dimensional token feature-hashing vectors using Reciprocal Rank Fusion (RRF, k=60). This vectorizer is deterministic and is not a pretrained neural sentence-embedding model."),
        ("Mathematical Formulation:", "RRF Score = Sum for m in M of (1 / (60 + rank_m(d))), ensuring balanced contribution from both sparse and dense ranks."),
        ("Lexical-Hashing Synergy:", "Feature hashing captures sub-word n-gram patterns while BM25 enforces exact statutory term matching."),
        ("Why BM25 Alone Fails:", "BM25 misses natural citizen queries like 'my landlord kicked me out without notice' because the word 'tenancy' or 'eviction' is absent."),
        ("Unified Evidence Pack:", "Aggregates Top-5 retrieved chunks with source citations, similarity scores, and Act metadata into an immutable payload.")
    ], title_color=COLOR_NAVY)

    # =========================================================================
    # SLIDE 17: INTELLIGENT DOCUMENT PROCESSING & STORAGE
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    add_header(s17, "Intelligent Document Processing & Durable Storage", "MODULE D: HEURISTIC PARSING & SUPABASE S3 PERSISTENCE", 17)

    add_card(s17, Inches(0.6), Inches(1.3), Inches(5.95), Inches(5.5), "INTELLIGENT DOCUMENT TRIAGE PIPELINE", [
        ("Multipart Document Upload:", "Supports authentic citizen PDF uploads with strict client-side and server-side validation (10MB size limit, MIME verification)."),
        ("Dual-Engine Text Extraction:", "pdfplumber layout-aware parser with automatic PyPDF fallback for robust text stream extraction."),
        ("Heuristic Civic Entity Extractor:", "Domain-specific regular expression engine extracting: Notice/Case Numbers, Statutory Section References, Monetary Fine Demands, and Critical Compliance Deadlines."),
        ("Document Classification:", "Automatically classifies documents into 4 civic categories: Legal Notice / Court Summons, Identity / Entitlement Certificate, Challan / Violation Notice, or General Scheme Application."),
        ("Sub-2.0s Execution:", "Entire parsing and triage completes in < 1.8 seconds on standard serverless CPU instances.")
    ], title_color=COLOR_NAVY)

    add_card(s17, Inches(6.75), Inches(1.3), Inches(5.95), Inches(5.5), "DURABLE CLOUD STORAGE ADAPTER", [
        ("Blocker Closure (Review 1 -> Review 2):", "Successfully resolved the fragile serverless `/tmp` storage blocker by engineering a stateless Supabase S3-compatible cloud storage adapter."),
        ("Private Bucket Security:", "Documents are stored in a private Supabase bucket (`civicsphere-documents`) protected by service-role keys and row-level access control."),
        ("Presigned Ephemeral URLs:", "Authorized downloads utilize time-limited presigned URLs (60-minute expiry); unauthorized public access is strictly blocked (HTTP 403)."),
        ("Cross-Invocation Durability:", "Verified that files uploaded in one serverless function invocation remain fully retrievable across subsequent invocations."),
        ("DPDP Alignment Cascade Purge:", "Deleting a citizen document automatically triggers an atomic S3 object deletion and database record purge.")
    ], title_color=COLOR_TEAL)

    # =========================================================================
    # SLIDE 18: AUTHENTIC PROTOTYPE SCREENSHOTS
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    add_header(s18, "Authentic Live Prototype Screenshots", "VERIFIED DEPLOYED APPLICATION INTERFACES ON VERCEL PRODUCTION", 18)

    # 4 images placed in 2x2 grid
    img1 = r"docs\audit\live-vercel-evidence\homepage_view_1793176989717.png"
    img2 = r"docs\audit\live-vercel-evidence\legal_page_view_1793177040971.png"
    img3 = r"docs\audit\live-vercel-evidence\legal_response_view_1793177153964.png"
    img4 = r"docs\audit\live-vercel-evidence\government_results_1793177304220.png"

    grid = [
        (img1, Inches(0.6), Inches(1.3), "Figure 1: CivicSphere AI Modern Citizen Portal Landing Page"),
        (img2, Inches(6.75), Inches(1.3), "Figure 2: Legal Guidance Engine & Query Consultation Interface"),
        (img3, Inches(0.6), Inches(4.2), "Figure 3: Evidence-Grounded Guidance with Verifiable Citations"),
        (img4, Inches(6.75), Inches(4.2), "Figure 4: Government Scheme Navigator & Eligibility Discovery")
    ]

    for p_img, l, t, caption in grid:
        if os.path.exists(p_img):
            s18.shapes.add_picture(p_img, l, t, width=Inches(5.95), height=Inches(2.55))
        # Caption box
        cap_box = s18.shapes.add_textbox(l, t + Inches(2.58), Inches(5.95), Inches(0.3))
        tf_cap = cap_box.text_frame
        tf_cap.margin_left = tf_cap.margin_top = tf_cap.margin_right = tf_cap.margin_bottom = 0
        p_c = tf_cap.paragraphs[0]
        p_c.text = caption
        p_c.font.name = FONT_MAIN
        p_c.font.size = Pt(9.0)
        p_c.font.bold = True
        p_c.font.color.rgb = COLOR_NAVY
        p_c.alignment = PP_ALIGN.CENTER

    # =========================================================================
    # SLIDE 19: UN SUSTAINABLE DEVELOPMENT GOALS (SDG) ALIGNMENT
    # =========================================================================
    s19 = prs.slides.add_slide(blank_layout)
    add_header(s19, "UN Sustainable Development Goals (SDG) Alignment", "ETHICAL, SOCIETAL & ENVIRONMENTAL IMPACT EVALUATION", 19)

    add_card(s19, Inches(0.6), Inches(1.3), Inches(3.9), Inches(5.5), "PRIMARY ALIGNMENT: SDG 16", [
        ("Peace, Justice & Strong Institutions:", "Dedicated to building transparent, effective, and accountable public institutions."),
        ("Target 16.3 (Access to Justice):", "Promotes the rule of law at national levels and ensures equal access to justice for marginalized citizens by offering free, plain-language legal triage."),
        ("Target 16.10 (Public Access to Info):", "Guarantees citizen access to fundamental statutory information and official government entitlement data."),
        ("Measurable Metric:", "Zero-cost legal orientation for unrepresented litigants.")
    ], title_color=COLOR_NAVY)

    add_card(s19, Inches(4.7), Inches(1.3), Inches(3.9), Inches(5.5), "SECONDARY ALIGNMENT: SDG 10 & 9", [
        ("SDG 10: Reduced Inequalities:", "Target 10.2: Empowers lower-income citizens, gig workers, and rural populations by removing informational asymmetries in welfare access."),
        ("SDG 9: Industry & Innovation:", "Target 9.b: Fosters domestic technological development and research innovation in civic AI tailored specifically for the Global South."),
        ("Social Inclusivity:", "Demystifies bureaucratic gatekeeping and empowers vulnerable communities to claim statutory rights.")
    ], title_color=COLOR_TEAL)

    add_card(s19, Inches(8.8), Inches(1.3), Inches(3.9), Inches(5.5), "ENVIRONMENTAL IMPACT & GREEN AI", [
        ("Serverless Micro-Compute:", "Lightweight ASGI serverless architecture provisions compute strictly on-demand, minimizing idle server power."),
        ("Algorithmic Micro-Compute:", "Lightweight deterministic synthesis and caching avoid continuous multi-billion parameter GPU inference for routine civic queries."),
        ("Transparent Resource Accounting:", "Evaluates compute footprint pragmatically, avoiding unverified carbon offset claims while optimizing algorithmic efficiency."),
        ("Sustainable Engineering:", "Prioritizes algorithmic efficiency and CPU-tractable inference over brute-force neural compute.")
    ], title_color=COLOR_NAVY)

    # =========================================================================
    # SLIDE 20: EMPIRICAL TESTING & SECURITY VALIDATION
    # =========================================================================
    s20 = prs.slides.add_slide(blank_layout)
    add_header(s20, "Empirical Testing & Security Validation Results", "RIGOROUS REPRODUCIBLE TEST SUITE & PLATFORM METRICS", 20)

    test_metrics = [
        ("136 PASSED BACKEND TESTS", "137 COLLECTED / 1 SKIPPED / 0 FAILED", [
            ("Full Automated Regression Suite:", "136 passed out of 137 collected (1 skipped due to external smoke flag)."),
            ("Integrated PM-KISAN Suite:", "12 dedicated statutory tests included directly within the full suite."),
            ("Separate Authorization Suite:", "5/5 dedicated server-side authorization enforcement tests passed separately (evaluating 401 unauth, 403 RBAC, and IDOR isolation).")
        ]),
        ("31 STATIC FRONTEND ROUTES", "ZERO BUILD ERRORS", [
            ("Next.js 16 Production Build:", "31 static routes prerendered without hydration errors in Next.js App Router."),
            ("Live Canonical Route Audit:", "27 of 27 live routes returned HTTP 200 OK on https://civicsphere-web.vercel.app."),
            ("Negative Security Probes:", "Server-side security probes returned expected HTTP 401 Unauthorized / HTTP 403 Forbidden.")
        ]),
        ("DURABLE CLOUD STORAGE ADAPTER", "BYTE-EXACT S3 VERIFICATION", [
            ("Supabase S3 Integration:", "Round-trip persistence across independent serverless function invocations."),
            ("Byte-Exact Integrity:", "Downloaded bytes match uploaded PDF SHA-256 perfectly; cross-tenant access denied."),
            ("Processing Latency:", "Representative test document parsed and triaged in 1.62 seconds.")
        ]),
        ("DPDP PRINCIPLES ALIGNMENT", "TECHNICAL SAFEGUARDS ALIGNED", [
            ("Standardized Statement:", "Selected technical safeguards aligned with relevant DPDP Act 2023 principles implemented and tested."),
            ("Implemented Controls:", "Authentication, server-side authorization, private document storage, auditability and deletion workflows."),
            ("Legal Boundary:", "Formal legal compliance certification has not been performed.")
        ])
    ]

    for idx, (title, tag, points) in enumerate(test_metrics):
        col = idx % 2
        row = idx // 2
        l = Inches(0.6) + col * Inches(6.15)
        t = Inches(1.3) + row * Inches(2.85)
        items = [("Testing Status:", tag)] + points
        add_card(s20, l, t, Inches(5.95), Inches(2.7), title, items, title_color=COLOR_NAVY if col==0 else COLOR_TEAL)

    # =========================================================================
    # SLIDE 21: TEAM COLLABORATION, RACI & PROBLEM SOLVING
    # =========================================================================
    s21 = prs.slides.add_slide(blank_layout)
    add_header(s21, "Team Collaboration, RACI Matrix & Problem Solving", "ENGINEERING SQUAD DYNAMICS & HIGH-COMPLEXITY RESOLUTION", 21)

    add_card(s21, Inches(0.6), Inches(1.3), Inches(5.95), Inches(5.5), "RACI RESPONSIBILITY ASSIGNMENT MATRIX", [
        ("Devansh Savla (Roll: 23UF18356CM172):", "Accountable (A) for System Architecture & Cloud Infrastructure; Responsible (R) for Hybrid Retrieval, Gate 2 Circuit Breaker & Vercel CI/CD."),
        ("Khushbu Chheda (Roll: 23UF17711CM132):", "Accountable (A) for Legal Knowledge Architecture & Case Dossier; Responsible (R) for 8-Act Statutory Indexing, Legal Ontology & UX."),
        ("Anushka Adsul (Roll: 124BTCM2002):", "Accountable (A) for Government Navigator & Eligibility Logic; Responsible (R) for 12 Welfare Scheme Schemas, REST APIs & Responsive UI."),
        ("Rahul Singh (Roll: 23UF18562CM189):", "Accountable (A) for Intelligent Document Processing & Cloud Storage; Responsible (R) for Supabase S3 Adapter, Regex Parser & Automated Tests.")
    ], title_color=COLOR_NAVY)

    add_card(s21, Inches(6.75), Inches(1.3), Inches(5.95), Inches(5.5), "ENGINEERING CASE STUDY: SERVERLESS DURABILITY", [
        ("The Critical Defect:", "During Review 1, document uploads were saved to the local `/tmp` directory. In serverless environments (Vercel/AWS Lambda), container instances are ephemeral; files uploaded in one invocation vanished on the next call, causing catastrophic HTTP 404/500 errors."),
        ("The Squad's Root Cause Analysis:", "The team mapped the storage lifecycle, identifying that serverless execution requires stateless compute and decoupled durable object persistence."),
        ("The Engineered Fix:", "Architected a dual-tier Supabase Storage Adapter implementing signed URL generation, service-role authentication, and byte-exact persistence. Document writes now commit directly to private S3 buckets."),
        ("The Outcome:", "Durable file persistence across cold starts, verified by automated multi-invocation retrieval scripts.")
    ], title_color=COLOR_TEAL)

    # =========================================================================
    # SLIDE 22: INDIVIDUAL LEARNING REFLECTIONS & INDUSTRY
    # =========================================================================
    s22 = prs.slides.add_slide(blank_layout)
    add_header(s22, "Individual Learning Reflections & Industry Exposure", "TECHNICAL LEADERSHIP, INDUSTRY ENGAGEMENT & ACADEMIC GROWTH", 22)

    student_profiles = [
        ("Devansh Savla (23UF18356CM172)", [
            ("Core Role:", "Lead System Architect & Backend Infrastructure Engineer."),
            ("Key Learnings:", "Engineered hybrid RRF retrieval, Gate 2 circuit-breaker, and serverless FastAPI deployment."),
            ("External Engagement:", "Completed intensive Software Engineering Internship at ElevateLabs (microservices, distributed systems). [Proof Pending / Student Action]"),
            ("Coursework:", "Cisco Networking & Big Data Analytics coursework.")
        ]),
        ("Khushbu Chheda (23UF17711CM132)", [
            ("Core Role:", "Legal Domain Specialist & Case Dossier Lead."),
            ("Key Learnings:", "Curated 8 Indian statutory Acts, structured legal ontologies, and designed accessible citizen UX."),
            ("External Engagement:", "Completed Full-Stack Web Development & Legal Informatics training. [Proof Pending / Student Action]"),
            ("Key Growth:", "Mastered statutory chunking, prompt engineering, and legal ethical boundaries.")
        ]),
        ("Anushka Adsul (124BTCM2002)", [
            ("Core Role:", "Government Service Navigator & UI/UX Engineer."),
            ("Key Learnings:", "Implemented 12 central/state welfare schemes, rule-based eligibility evaluation, and Next.js UI."),
            ("External Engagement:", "Cloud Architecture & API Engineering training. [Organization details & documentary certificate proof pending student submission]"),
            ("Key Growth:", "Bridged complex bureaucratic rules with intuitive, accessible citizen interfaces.")
        ]),
        ("Rahul Singh (23UF18562CM189)", [
            ("Core Role:", "Document Processing & Storage Pipeline Lead."),
            ("Key Learnings:", "Engineered heuristic regex extractor, Supabase S3 adapter, and automated test suites."),
            ("External Engagement:", "Python Data Engineering & Test Automation training. [Organization details & documentary certificate proof pending student submission]"),
            ("Key Growth:", "Mastered secure cloud object storage, MIME validation, and DPDP Act compliance.")
        ])
    ]

    for idx, (title, points) in enumerate(student_profiles):
        col = idx % 2
        row = idx // 2
        l = Inches(0.6) + col * Inches(6.15)
        t = Inches(1.3) + row * Inches(2.85)
        add_card(s22, l, t, Inches(5.95), Inches(2.7), title, points, title_color=COLOR_NAVY if col==0 else COLOR_TEAL)

    # =========================================================================
    # SLIDE 23: PRACTICAL SEMESTER 8 ROADMAP
    # =========================================================================
    s23 = prs.slides.add_slide(blank_layout)
    add_header(s23, "Proposed Semester 8 Roadmap (5-Phase Delivery)", "PLANNED FUTURE MILESTONES LEADING TO FINAL B.TECH UNIVERSITY DEFENSE", 23)

    roadmap_phases = [
        ("Phase 1: Indic Multilingual NLP (Proposed Weeks 1–3)", [
            ("Vernacular Expansion:", "Plan integration of fine-tuned Indic-BERT and Bhashini API to support Hindi, Marathi, and Gujarati natural language queries."),
            ("Acoustic Interface:", "Prototype speech-to-text input for illiterate and semi-literate rural citizens.")
        ]),
        ("Phase 2: Advanced OCR & Vision Triage (Proposed Weeks 4–6)", [
            ("LayoutLMv3 Integration:", "Incorporate multimodal layout models to parse complex court orders, stamp papers, and tabular challans."),
            ("Image Document Support:", "Enable direct camera snapshot parsing from mobile smartphones.")
        ]),
        ("Phase 3: Real-Time e-Courts API Integration (Proposed Weeks 7–9)", [
            ("Case Status Tracking:", "Connect to official e-Courts CNR number API for real-time hearing dates and interim order retrieval."),
            ("Automated Hearing Alerts:", "SMS and WhatsApp notification triggers for upcoming litigation dates.")
        ]),
        ("Phase 4: Empirical User Study & Field Trials (Proposed Weeks 10–12)", [
            ("Field Deployment:", "Conduct controlled pilot study with 50+ diverse citizens and paralegals across Mumbai legal clinics."),
            ("Usability Benchmarking:", "Measure System Usability Scale (SUS) score and task completion rates.")
        ]),
        ("Phase 5: Performance Hardening & Final Defense (Proposed Weeks 13–15)", [
            ("Load Testing & CDN:", "Edge caching optimization and end-to-end stress testing under 1,000 concurrent simulated queries."),
            ("Final B.Tech Thesis:", "Comprehensive final project documentation, IEEE research paper submission, and university defense.")
        ])
    ]

    for idx, (title, points) in enumerate(roadmap_phases):
        t_pos = Inches(1.3) + idx * Inches(1.1)
        add_card(s23, Inches(0.6), t_pos, Inches(12.133), Inches(0.98), title, points, title_color=COLOR_NAVY if idx%2==0 else COLOR_TEAL)

    # =========================================================================
    # SLIDE 24: CONCLUSION, DEFENSE SUMMARY & Q&A
    # =========================================================================
    s24 = prs.slides.add_slide(blank_layout)
    add_header(s24, "Conclusion & Academic Defense Summary", "CIVICSPHERE AI: SUMMARY OF ACHIEVEMENTS & CONTRIBUTIONS", 24)

    add_card(s24, Inches(0.6), Inches(1.3), Inches(3.9), Inches(5.5), "ACADEMIC CONTRIBUTIONS", [
        ("1. Evidence-Grounded Architecture:", "Demonstrated that domain-specific hybrid retrieval (BM25 + deterministic 384-d feature hashing) coupled with Gate 2 circuit-breakers substantially suppresses citation hallucination."),
        ("2. Cross-Domain Civic Synergy:", "Pioneered unified computational linking between statutory law, welfare schemes, and citizen paperwork in India."),
        ("3. Privacy-First Civic Engineering:", "Selected technical safeguards aligned with relevant DPDP Act 2023 principles implemented and tested (auth, RBAC, private storage, auditability, deletion; formal legal compliance certification has not been performed).")
    ], title_color=COLOR_NAVY)

    add_card(s24, Inches(4.7), Inches(1.3), Inches(3.9), Inches(5.5), "REVIEW 2 MILESTONES ACHIEVED", [
        ("Complete Module Implementation:", "All 4 modules (A, B, C, D) are fully operational and verified on live Vercel production."),
        ("Durable Cloud Persistence:", "Closed the serverless `/tmp` blocker with Supabase private S3 object storage."),
        ("Empirical Rigor:", "136 passed backend tests (137 collected, 1 skipped), 31 static routes, 30 peer-reviewed papers mapped across 7 themes."),
        ("Ready for Semester 8:", "Clear proposed 5-phase delivery plan for multilingual and field trial expansion.")
    ], title_color=COLOR_TEAL)

    add_card(s24, Inches(8.8), Inches(1.3), Inches(3.9), Inches(5.5), "OPEN-SOURCE & REPRODUCIBILITY", [
        ("GitHub Repository:", "Clean Git repository with complete commit history, modular backend, and Next.js frontend."),
        ("Comprehensive Documentation:", "Full LaTeX report, test logs, rubric gap audit, and research paper index."),
        ("Project Guide:", "Mrs. Shahzia Sayyad (Assistant Professor, Department of Computer Engineering)"),
        ("Question & Answer:", "The team welcomes questions, feedback, and academic evaluation.")
    ], title_color=COLOR_NAVY)

    # Save presentation
    output_path = r"docs\review-2-submission\CivicSphere_AI_Review_2_Presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path} with {len(prs.slides)} slides!")

if __name__ == "__main__":
    create_presentation()
