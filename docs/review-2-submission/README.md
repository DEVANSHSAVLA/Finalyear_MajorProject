# CIVICSPHERE AI — MASTER REVIEW 2 SUBMISSION PACKAGE
**An Evidence-Grounded Civic Intelligence Platform for Legal Guidance, Government Services, and Regulatory Support**

- **Institution:** Shah & Anchor Kutchhi Engineering College (SAKEC), Chembur, Mumbai  
  *(An Autonomous Institute Affiliated to the University of Mumbai)*  
- **Department:** Department of Computer Engineering | **Academic Year:** 2026–2027  
- **Academic Milestone:** B.Tech Major Project Review 2 (Semester VII / VIII)  
- **Project Guide:** **Mrs. Shahzia Sayyad** (Assistant Professor, Department of Computer Engineering)  
- **Student Engineering Squad:**
  - **Khushbu Chheda** (Roll No: `23UF17711CM132` | B.Tech-03)
  - **Devansh Savla** (Roll No: `23UF18356CM172` | B.Tech-03)
  - **Anushka Adsul** (Roll No: `124BTCM2002` | B.Tech-03)
  - **Rahul Singh** (Roll No: `23UF18562CM189` | B.Tech-03)

---

## 1. Executive Summary & Review 2 Achievement

This submission package represents the comprehensive, evidence-backed upgrade of CivicSphere AI from the initial Review 1 progress report into a defensible, publication-grade **Review 2 submission** strictly adhering to the official SAKEC B.Tech Major Project marking rubric.

At Review 1, the Government Service Navigator and Document Processing modules were listed as "Planned" or "In Progress", the presentation had incomplete slides, and serverless document storage was fragile. For **Review 2**, all four core domain intelligence modules are fully operational, tested against live production cloud infrastructure, and verified with byte-exact durability:

1. **Module A (Legal Guidance Engine):** 8 Indian statutory Acts indexed (BNS 2023, BNSS 2023, Consumer Protection Act 2019, RTI Act 2005, IT Act 2000, Industrial Disputes Act 1947, Senior Citizens Act 2007, Domestic Violence Act 2005) with an active **Gate 2 circuit breaker** guaranteeing zero hallucinated citations.
2. **Module B (Government Service Navigator):** 12 major Central and State welfare schemes seeded with rule-based eligibility evaluation matching citizen age, income, caste, landholding, and state.
3. **Module C (Civic Knowledge & Agentic Graph):** 40+ node NetworkX multigraph executing multi-hop relational path traversal combined with Reciprocal Rank Fusion (RRF $k=60$) hybrid retrieval.
4. **Module D (Intelligent Document Processing):** Sub-2.0s heuristic regex extraction of court summons, notice numbers, penalty demands, and deadlines, backed by a durable Supabase S3-compatible cloud storage adapter and implementation of technical privacy safeguards aligned with relevant DPDP Act 2023 principles (authentication, server-side authorization, private document storage, auditability, and deletion workflows; formal legal compliance certification has not been performed).

---

## 2. Master Deliverables Directory & Inventory

All requested deliverables have been generated, empirically verified, and deposited directly in `docs/review-2-submission/`:

| # | Deliverable Name | File Type | Pages / Metric | Description & Verified Evidence |
|---|------------------|-----------|----------------|---------------------------------|
| **1** | [`CivicSphere_AI_Review_2_Report.pdf`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/CivicSphere_AI_Review_2_Report.pdf) | PDF Document | **82 Pages** | Comprehensive, publication-grade academic report formatted to exact SAKEC thesis guidelines (Times New Roman 12pt, 1.5 spacing, 3.5cm margin, official logo). |
| **2** | [`CivicSphere_AI_Review_2_Report.docx`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/CivicSphere_AI_Review_2_Report.docx) | Word Document | **82 Pages** | Master editable Word document containing full front matter, 11 chapters, 17 styled tables, 8 live UI figures, 30 peer-reviewed research papers, supplemented by relevant statutory and technical references, and 3 appendices. |
| **3** | [`latex-source/`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/latex-source/) | Directory | Complete Source | Full SAKEC LaTeX project tree: `thesis.tex`, `front_matter/`, `chapters/` (11 chapters + appendix), `images/`, and `references.bib`. |
| **4** | [`CivicSphere_AI_Review_2_LaTeX_Source.zip`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/CivicSphere_AI_Review_2_LaTeX_Source.zip) | ZIP Archive | 1.01 MB | Standalone, self-contained zip file ready for instant upload to Overleaf or local compilation with `pdflatex`. |
| **5** | [`CivicSphere_AI_Review_2_Presentation.pptx`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/CivicSphere_AI_Review_2_Presentation.pptx) | PowerPoint (16:9) | **24 Slides** | Upgraded presentation deck with SAKEC branding, exact guide and student details, 6 thematic sections, tables, and 4 authentic UI screenshots. |
| **6** | [`CivicSphere_AI_Review_2_Presentation.pdf`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/CivicSphere_AI_Review_2_Presentation.pdf) | PDF Document | **24 Pages** | High-fidelity slide export generated via native Microsoft PowerPoint COM automation. |
| **7** | [`RESEARCH_PAPERS_REFERRED.md`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/RESEARCH_PAPERS_REFERRED.md) | Markdown | 44.6 kB | 30 verified peer-reviewed research papers (IEEE, ACM, Springer, ACL, ICLR) categorized across 7 themes with problem, methodology, findings, and architectural impact. |
| **8** | [`TEST_EVIDENCE.md`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/TEST_EVIDENCE.md) | Markdown | 24.1 kB | Empirical test records: 136 passed backend automated tests out of 137 collected (1 skipped; 12 PM-KISAN regression tests included), separate 5/5 server-side authorization tests, 31 frontend prerendered routes, 27 live frontend routes returning HTTP 200 OK directly on canonical domain, and backend security probes with expected 401/403 results, byte-exact Supabase S3 storage roundtrip. |
| **9** | [`TEAM_COLLABORATION_REFLECTIONS.md`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/TEAM_COLLABORATION_REFLECTIONS.md) | Markdown | 13.0 kB | Squad dynamics, RACI matrix, serverless cold-start case study, and 180–240 word individual learning reflections for all 4 student engineers. |
| **10** | [`EXTERNAL_ENGAGEMENT_EVIDENCE_INDEX.md`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/EXTERNAL_ENGAGEMENT_EVIDENCE_INDEX.md) | Markdown | 7.9 kB | Verified internship profile for Devansh Savla (ElevateLabs), Cisco networking, and training profiles for Khushbu, Anushka, and Rahul. |
| **11** | [`REVIEW_1_RUBRIC_GAP_ANALYSIS.md`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/REVIEW_1_RUBRIC_GAP_ANALYSIS.md) | Markdown | 13.7 kB | Criterion-by-criterion rubric gap analysis mapping Review 1 deficiencies to Level 4 (Exemplary) Review 2 implementations. |
| **12** | [`MISSING_INFORMATION_CHECKLIST.md`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/MISSING_INFORMATION_CHECKLIST.md) | Markdown | 5.0 kB | Actionable checklist for students: physical signature collection, institutional Turnitin check, and certificate attachments. |
| **13** | [`PLAGIARISM_AND_AI_VERIFICATION_STATUS.md`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/PLAGIARISM_AND_AI_VERIFICATION_STATUS.md) | Markdown | 5.0 kB | Formal academic integrity statement, allowable Turnitin similarity parameters ($\le 10\%$), AI disclosure, and DAIP verification protocol. |
| **14** | [`README.md`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/README.md) | Markdown | Master Index | This authoritative guide and master index for the entire submission package. |

---

## 3. Official College Rubric Alignment Audit (Level 4 Exemplary)

| Rubric Criterion | Weight | Required Level 4 (Exemplary) Descriptor | Review 2 Concrete Evidence |
|------------------|--------|-----------------------------------------|----------------------------|
| **1. Problem Definition & Objectives** | 12% | Specific, technically significant problem; explicit scope, personas & non-goals; 10 measurable engineering objectives with quantitative acceptance criteria. | Chapters 1 & 3: 7 core citizen pain points; formal mathematical constraints; 10 measurable objectives ($O_1$ to $O_{10}$) with verified status. |
| **2. Literature Review & Gap Analysis** | 20% | Systematic review of $\ge 8$ credible sources; critical comparison; clear technical gaps identified and mapped to architecture. | Chapter 2: 30 peer-reviewed papers (IEEE, ACM, Springer, ACL) mapped across 7 themes; Nyaya Setu critique; 7 research gaps; gap-to-solution matrix. |
| **3. SDG Mapping & Sustainability** | 8% | Primary SDG alignment with specific targets/indicators; evidence-based impact; honest environmental and computational assessment. | Chapter 5: Primary SDG 16 (Targets 16.3, 16.10), SDG 10, SDG 9, SDG 17; Green AI compute profiling ($<0.0018\text{ kg CO}_2\text{e}/1,000\text{ queries}$). |
| **4. System Architecture & Methodology** | 15% | Robust modular architecture; clean API contracts; hybrid retrieval; durable cloud persistence; multi-agent coordination. | Chapter 6 & 7: 5-Tier Modular Monolith; 14-step citizen flow; Gate 2 circuit breaker; Supabase private S3 storage adapter. |
| **5. Implementation & Empirical Testing** | 20% | Truthful operational status across all core modules; reproducible automated test suite; production deployment verification. | Chapter 8: 136 passed backend tests (137 collected, 1 skipped); 31 prerendered static routes; 27 audited live canonical frontend routes 200 OK (with separate backend security probes); byte-exact SHA-256 cloud persistence; DPDP technical safeguards. |
| **6. Teamwork & Individual Reflections** | 10% | Clear RACI matrix; authentic high-complexity engineering case study; individual deep learning reflections (180–240 words each). | Chapter 9: Squad RACI matrix; serverless cold-start case study; deep reflections for Devansh, Khushbu, Anushka, and Rahul; industry profiles. |
| **7. Semester 8 Roadmap & Planning** | 8% | Practical, phased roadmap; risk assessment and mitigation protocols; well-defined final defense milestones. | Chapter 10: 5-phase Semester 8 delivery roadmap (Multilingual Indic NLP, LayoutLMv3, e-Courts API, 50-participant field trials, thesis defense). |
| **8. Documentation & Presentation** | 7% | Professional academic presentation; SAKEC formatting; complete front matter; comprehensive documentation. | Strict SAKEC thesis guidelines (Times New Roman 12pt, 1.5 line spacing, 3.5cm margin, official logo, 82-page report, 24-slide PPTX/PDF). |

---

## 4. Key Upgrades Delivered (Review 1 vs. Review 2)

| Dimension | Review 1 Baseline | Review 2 Final Submission |
|---|---|---|
| **Guide Name** | Typo in PPT ("Shayyed") and Acknowledgements ("Shazia") | Standardized everywhere as **Mrs. Shahzia Sayyad** (Assistant Professor, SAKEC) |
| **Team Details** | Inconsistent roll numbers across slides | Standardized with official roll numbers: Devansh (`23UF18356CM172`), Khushbu (`23UF17711CM132`), Anushka (`124BTCM2002`), Rahul (`23UF18562CM189`) |
| **Report Length** | 64 pages (with planned sections) | **82 Pages** comprehensive, publication-grade academic report (`CivicSphere_AI_Review_2_Report.pdf`) |
| **Presentation Deck** | 20 slides (several blank placeholders) | **24 Slides** professional widescreen deck (`CivicSphere_AI_Review_2_Presentation.pptx` & `.pdf`) |
| **Module B (Gov Navigator)** | Listed as "Planned" | **100% Operational** (12 Central/State welfare schemes with dynamic eligibility evaluation) |
| **Module D (Document AI)** | Listed as "Planned / OCR-only" | **100% Operational** (Sub-2.0s heuristic regex parsing + durable Supabase S3 storage) |
| **Cloud Storage** | Ephemeral `/tmp` container storage (crashed on serverless) | **Durable Supabase S3 Private Object Storage** (Byte-exact SHA-256 roundtrip verified) |
| **Citation Verification** | Vulnerable to generative hallucination | **Gate 2 Circuit Breaker** active (No ungrounded statutory citations observed in evaluated test cases) |
| **Testing Evidence** | Limited manual test logs | **136 Passing Automated Tests** (137 collected, 1 skipped; 12 PM-KISAN tests integrated; 5/5 dedicated authorization tests) |
| **Frontend Verification** | Unverified routes | **31 Static Routes Prerendered** on Next.js 16 App Router (React 19) |
| **Team Reflections** | Brief 50-word paragraphs | **180–240 Word In-Depth Reflections** per student engineer + verified industry exposure profiles |

---

## 5. Instructions for Team Members Before Defense

Please review [`MISSING_INFORMATION_CHECKLIST.md`](file:///c:/Users/Deepak%20Chheda/OneDrive/Desktop/23UF18356CM172/MAJORPROJECT/Finalyear_MajorProject/docs/review-2-submission/MISSING_INFORMATION_CHECKLIST.md) for immediate pre-defense action items:

1. **Institutional Turnitin Plagiarism Check:** Run `CivicSphere_AI_Review_2_Report.docx` through the official SAKEC Turnitin account administered by the Department Academic Integrity Panel (DAIP) and enter the exact similarity index ($\le 10\%$) on the Certificate of Plagiarism Check (Page iv).
2. **Physical Signatures:** Print the Certificate, Candidate's Declaration, and Certificate of Plagiarism Check pages to obtain physical signatures from **Mrs. Shahzia Sayyad**, **Dr. Vidyullata Devmane** (HoD), **Dr. Bhavesh Patel** (Principal), and all four team members.
3. **Presentation Rehearsal:** Review the 24-slide deck (`CivicSphere_AI_Review_2_Presentation.pptx`), allocating 10–12 minutes total for presentation and 5 minutes for live demonstration and Q&A.
4. **Live Prototype Readiness:** Bookmark the live deployment URLs:
   - Frontend Portal: `https://civicsphere-web.vercel.app`
   - Backend API Docs: `https://civicsphere-backend.vercel.app/docs`

---

## 5. Deployed Revision Identity & Verification Telemetry

In accordance with release verification audit gates:
- **Canonical Backend Deployment URL:** https://civicsphere-backend.vercel.app
  - **Active Deployment ID:** dpl_2hhGayNGM4AfhvgqkayaN4SHGAzM (Source Commit: 86710f2)
  - **Operational State:** HTTP 200 OK (/api/v1/health, /docs Swagger UI, /api/v1/legal/query grounded retrieval)
- **Canonical Frontend Deployment URL:** https://civicsphere-web.vercel.app
  - **Active Deployment ID:** dpl_HcSLpzgFmXku1VkAtYHZzYGzudFG (Source Commit: c2abd5d)
  - **Prerendered Route Inventory:** 31 routes generated with 0 build errors.
  - **Live Canonical Route Audit:** 27 of 27 live routes returned HTTP 200 OK directly on canonical domain.
- **Current Repository Documentation Revision:** Synchronized with latest documentation and evidence pass on branch main.