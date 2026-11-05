# CIVICSPHERE AI — AUTHORITATIVE RELEASE MANIFEST (REVIEW 2)
**Date of Release:** November 5, 2026  
**Status:** Canonical Source of Truth for Review 2 Submission Deliverables  
**Verdict:** **READY AFTER STUDENT INPUT**

---

## 1. Release & Deployment Identity
- **Repository Branch:** `main`
- **Current Repository Commit:** `c2892aa`
- **GitHub Upstream Remote:** `https://github.com/Khushbu112005/Finalyear_MajorProject`
- **GitHub Fork Remote (Vercel-Connected):** `https://github.com/DEVANSHSAVLA/Finalyear_MajorProject`
- **Canonical Public Frontend URL:** `https://civicsphere-web.vercel.app`
- **Frontend Deployment ID:** `dpl_7xfYDbGja8ccJLM2CRjXrNUSWPUe` (Aliased from `civicsphere-rf9gxxnlm-devanshparagsavla1709-6335s-projects.vercel.app`)
- **Frontend Source SHA:** `86710f2` / `c2892aa`
- **Canonical Public Backend URL:** `https://civicsphere-backend.vercel.app`
- **Backend Deployment ID:** `dpl_2hhGayNGM4AfhvgqkayaN4SHGAzM`
- **Backend Source SHA:** `86710f2` / `c2892aa`
- **Backend Health Check:** `HTTP 200 OK` (`{"status":"HEALTHY","service":"civicsphere_unified_backend"}`)

---

## 2. Reconciled Deliverable Properties & Test Evidence
- **Academic Report Page Count:** **82 Pages** (CivicSphere_AI_Review_2_Report.pdf & .docx)
- **Defense Presentation Slide Count:** **24 Slides** (CivicSphere_AI_Review_2_Presentation.pptx & .pdf)

### Test Evidence & Counts
- **Full Backend Pytest Suite:**
  - Collected: 137 tests (+ 1 benchmark script runner item = 138 items)
  - Passed: 136 tests passed (137 passed when counting benchmark runner)
  - Skipped: 1 test skipped (`test_live_sources_smoke.py`)
  - Failed: 0
  - Execution Time: 24.32 seconds
- **PM-KISAN Regression Suite:**
  - 12 tests passed (fully integrated within the full backend suite)
  - Evaluates June 2019 expansion abolishing the 2-hectare ceiling
  - Evaluates all statutory exclusion criteria (institutional, constitutional, elected, regular government, pensioners >= 10k, tax payers, professionals)
  - Preserves Multi-Tasking Staff (MTS) / Class IV / Group D exceptions
- **Dedicated Server-Side Authorization Suite:**
  - 5 tests passed (`test_server_side_authorization.py`)
  - Evaluates RBAC, unauthenticated 401 denial, cross-user document IDOR, deletion isolation, and role spoofing
- **Frontend Build & Prerender:**
  - 31 static routes prerendered in Next.js 16.4.2 production build (`0` build errors)
- **Live Frontend Route Audit:**
  - 20 of 20 audited live frontend routes returned `HTTP 200 OK`
- **Backend Security Probes:**
  - Expected `HTTP 401 Unauthorized` / `HTTP 403 Forbidden` responses verified on protected administrative and citizen endpoints

---

## 3. Retrieval, Embeddings & Benchmark Grounding
- **Embedding Implementation:**
  - Class: `MockEmbeddingProvider`
  - Technique: Deterministic 384-dimensional token feature hashing
  - Algorithm: MD5 token hashes modulo 384, stopword filtering, L2 normalization
  - Fusion: Combined with BM25 sparse lexical ranking via Reciprocal Rank Fusion (RRF, $k=60$)
  - Note: Strictly deterministic hashing; not a pretrained dense transformer or neural sentence embedding
- **Benchmark Evaluation:**
  - Metric: Top-3 Retrieval Recall = 88.4%
  - Test Set: Internal benchmark consisting of 10 checked-in multi-split test cases (4 standard, 3 adversarial, 3 held-out in data/evaluation) evaluated against the localized 8-statute corpus
  - Gate 2 Verification Threshold: Configured consistently at `0.75`
  - Hallucination Claims: Bounded statement: *"No ungrounded statutory citations were observed in the evaluated test cases."* (No claim of universal zero-hallucination guarantee)
  - Document Processing Latency: Single measured representative test sample of 1.62 seconds

---

## 4. DPDP Act 2023 Principles Standardized Statement
Applied verbatim across all report chapters, presentation slides, and markdown files:
> *"Selected technical safeguards aligned with relevant DPDP Act 2023 principles have been implemented and tested. These include authentication, server-side authorization, private document storage, auditability and deletion workflows. Formal legal compliance certification has not been performed."*

Prohibited claims:
- No claims of "Section 12 compliant erasure" (Section 12 not operative as of November 5, 2026).
- No claims of "100% DPDP compliant" or "full/strict compliance".
- No claims of "client-side encryption" or "zero third-party telemetry" without verified evidence.

---

## 5. Research Reference Counts
- **Scholarly Research Papers:** 30 peer-reviewed research papers (indexed across IEEE, ACM, Springer, arXiv).
- **Statutory & Technical References:** Supplemented by relevant enactments (Digital Personal Data Protection Act, 2023).
- **Total Bibliography Entries:** 31 entries.

---

## 6. Official Pending Student & Institutional Inputs
1. **Student Signatures:** Pending physical signature on Declaration page.
2. **Guide & Examiner Signatures:** Pending physical sign-off on Certificate page.
3. **Turnitin Similarity Report:** Official similarity percentage and date pending from college library / DAIP coordinator.
4. **External Engagement Proofs:** The 4 individual team members' social/civic engagement certificates pending student submission.
