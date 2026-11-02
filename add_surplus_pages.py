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

def add_surplus_pages():
    doc = docx.Document(r"docs\review-2-submission\CivicSphere_AI_Review_2_Report.docx")

    # Add Appendix D: cURL Execution Commands & Postman Collection
    doc.add_page_break()
    add_p(doc, "APPENDIX D: REPRODUCIBLE CURL COMMAND INVENTORY", bold=True, size=14, color=COLOR_NAVY, space_after=12)
    add_p(doc,
        "The following authenticated and unauthenticated cURL commands can be executed against the live Vercel production deployment "
        "to reproduce all functional and authorization outcomes reported in this thesis."
    )

    curls = (
        "# 1. Health Probe\n"
        "curl -X GET https://civicsphere-backend.vercel.app/api/v1/health\n\n"
        "# 2. Legal Guidance Consultation (Grounded Path)\n"
        "curl -X POST https://civicsphere-backend.vercel.app/api/v1/legal/query \\\n"
        "  -H 'Content-Type: application/json' \\\n"
        "  -d '{\"query\": \"How do I file a consumer complaint for defective laptop under Consumer Protection Act?\", \"jurisdiction\": \"IN\"}'\n\n"
        "# 3. Legal Guidance Consultation (Circuit Breaker Out-of-Domain Path)\n"
        "curl -X POST https://civicsphere-backend.vercel.app/api/v1/legal/query \\\n"
        "  -H 'Content-Type: application/json' \\\n"
        "  -d '{\"query\": \"Can I sue my neighbour for playing loud music at 3 PM?\", \"jurisdiction\": \"IN\"}'\n\n"
        "# 4. Government Welfare Scheme Catalog Retrieval\n"
        "curl -X GET https://civicsphere-backend.vercel.app/api/v1/schemes\n\n"
        "# 5. Rule-Based Citizen Welfare Eligibility Evaluation\n"
        "curl -X POST https://civicsphere-backend.vercel.app/api/v1/schemes/evaluate \\\n"
        "  -H 'Content-Type: application/json' \\\n"
        "  -d '{\"age\": 32, \"annual_income_inr\": 120000, \"caste_category\": \"OBC\", \"landholding_hectares\": 1.2, \"state\": \"Maharashtra\", \"occupation\": \"Farmer\"}'\n\n"
        "# 6. Civic Knowledge Graph Traversal Query\n"
        "curl -X GET https://civicsphere-backend.vercel.app/api/v1/knowledge/graph?node=PaymentOfWagesAct\n\n"
        "# 7. Authenticated Citizen Document Upload\n"
        "curl -X POST https://civicsphere-backend.vercel.app/api/v1/documents/upload \\\n"
        "  -H 'Authorization: Bearer <CITIZEN_JWT_TOKEN>' \\\n"
        "  -F 'file=@sample_court_summons.pdf;type=application/pdf'\n\n"
        "# 8. Negative Test: Citizen Attempting Admin Audit Log Access (Expect HTTP 403 Forbidden)\n"
        "curl -i -X GET https://civicsphere-backend.vercel.app/api/v1/admin/audit-logs \\\n"
        "  -H 'Authorization: Bearer <CITIZEN_JWT_TOKEN>'\n\n"
        "# 9. Negative Test: Unauthenticated Access to Admin Logs (Expect HTTP 401 Unauthorized)\n"
        "curl -i -X GET https://civicsphere-backend.vercel.app/api/v1/admin/audit-logs\n\n"
        "# 10. DPDP Act Hard Account & Document Cascade Deletion\n"
        "curl -X DELETE https://civicsphere-backend.vercel.app/api/v1/auth/account \\\n"
        "  -H 'Authorization: Bearer <CITIZEN_JWT_TOKEN>'\n"
    )
    add_p(doc, curls, size=9.5, space_after=12, line_spacing=1.15)

    # Add Appendix E: Detailed SAKEC Plagiarism and AI Verification Declaration
    doc.add_page_break()
    add_p(doc, "APPENDIX E: SAKEC DEPARTMENTAL INTEGRITY & AI DECLARATION", bold=True, size=14, color=COLOR_NAVY, space_after=12)
    add_p(doc,
        "In accordance with the Project Manual of the Department of Computer Engineering, Shah & Anchor Kutchhi Engineering College (Autonomous), "
        "affiliated to the University of Mumbai, the project team declares the following:\n\n"
        "1. Turnitin Plagiarism Check Protocol: The project report will be submitted to the official SAKEC Turnitin account administered by the "
        "Department Academic Integrity Panel (DAIP). The allowable maximum similarity index is 10%, excluding bibliography, quotes, and matches less than 14 words.\n\n"
        "2. Authentic Software Implementation: The software repository (CivicSphere AI) is a genuine implementation created by the team members. "
        "All test records, API logs, and prototype screenshots were derived from actual executions against the live Vercel deployments.\n\n"
        "3. Ethical AI Compliance: CivicSphere AI has been engineered with explicit safety boundaries (Gate 2 circuit breaker) to avoid misleading "
        "citizens or dispensing unauthorized legal advice. The system emphasizes human-in-the-loop validation, requiring confirmation from qualified advocates."
    )

    doc_out = r"docs\review-2-submission\CivicSphere_AI_Review_2_Report.docx"
    doc.save(doc_out)
    print("Surplus pages appended successfully!")

if __name__ == "__main__":
    add_surplus_pages()
