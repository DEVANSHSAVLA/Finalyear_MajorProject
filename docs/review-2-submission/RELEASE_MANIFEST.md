# CIVICSPHERE AI — AUTHORITATIVE RELEASE MANIFEST (REVIEW 2)
**Date of Release:** November 6, 2026  
**Status:** Canonical Single Source of Truth for Review 2 Submission Deliverables  
**Verdict:** **READY AFTER STUDENT INPUT**

---

## 1. Release & Deployment Identity
- **Repository Branch:** `main`
- **Current Repository Documentation Commit:** Synchronized with latest documentation and evidence pass on branch `main` (Documentation, manifest, presentation, and evidence synchronization)
- **GitHub Upstream Remote:** `https://github.com/Khushbu112005/Finalyear_MajorProject`
- **GitHub Fork Remote (Vercel-Connected):** `https://github.com/DEVANSHSAVLA/Finalyear_MajorProject`
- **Canonical Public Frontend URL:** `https://civicsphere-web.vercel.app`
- **Frontend Deployment ID:** `dpl_HcSLpzgFmXku1VkAtYHZzYGzudFG` (Aliased from `civicsphere-d290yeyh6-devanshparagsavla1709-6335s-projects.vercel.app`)
- **Frontend Source SHA:** `c2abd5d`
- **Canonical Public Backend URL:** `https://civicsphere-backend.vercel.app`
- **Backend Deployment ID:** `dpl_2hhGayNGM4AfhvgqkayaN4SHGAzM`
- **Backend Deployed Source SHA:** `86710f2`
- **Backend Deployment Justification:** Commit `86710f2` represents the complete, verified, and hardened backend application codebase (including the June 2019 PM-KISAN rules, professional exclusions, MTS exceptions, server-side JWT RBAC authorization, Supabase S3 cloud storage durability adapter, and audit logging). All subsequent commits are documentation, test evidence, manifest, and presentation updates under `docs/review-2-submission/`. No backend application code files under `backend/` or `packages/` have been altered, and no un-deployed backend code changes are required.
- **Backend Health Check:** `HTTP 200 OK` (`{"status":"HEALTHY","service":"civicsphere_unified_backend","timestamp":...}`)

---

## 2. Reconciled Deliverable Properties & Test Evidence
- **Academic Report Page Count:** **82 Pages** (`CivicSphere_AI_Review_2_Report.pdf` & `.docx`)
- **Defense Presentation Slide Count:** **24 Slides** (`CivicSphere_AI_Review_2_Presentation.pptx` & `.pdf`)
- **Embedded Application Screenshots:** **7 authentic application figures** (Figures 7.1–7.4 in Chapter 7; Figures B.1–B.3 in Appendix B) + **1 institutional logo (`SAKEC_logo.png`)** on Title Page.

### Reconciled Test Counts & Evidence
- **Full Backend Pytest Suite:**
  - Collected: 137 tests
  - Passed: 136 tests passed
  - Skipped: 1 test skipped (`test_real_external_source_live_smoke` in `test_live_sources_smoke.py`, guarded by `@pytest.mark.skipif(not RUN_LIVE_SMOKE)` to prevent third-party government server rate limits during offline testing)
  - Failed: 0
  - Execution Time: ~54.35s
- **PM-KISAN Statutory Regression Suite:**
  - 12 tests passed (fully integrated directly within the full backend suite)
  - Evaluates June 2019 expansion abolishing the 2-hectare ceiling
  - Evaluates all statutory exclusion criteria (institutional, constitutional, elected, regular government, pensioners >= ₹10,000, income tax payees, registered practicing professionals)
  - Preserves Multi-Tasking Staff (MTS) / Class IV / Group D exceptions
- **Dedicated Server-Side Authorization Suite:**
  - 5 tests passed (`test_server_side_authorization.py`) reported separately
  - Evaluates RBAC, unauthenticated HTTP 401 denial, cross-user document IDOR, deletion isolation, and role spoofing
- **Frontend Build & Prerender:**
  - 31 static routes prerendered in Next.js 16.4.2 production build (`0` build errors)
- **Live Frontend Route Audit:**
  - 27 of 27 audited live routes returned `HTTP 200 OK` directly on `https://civicsphere-web.vercel.app`
- **Backend Security Probes:**
  - Expected `HTTP 401 Unauthorized` / `HTTP 403 Forbidden` responses verified on protected administrative and citizen endpoints

---

## 3. Retrieval, Embeddings & Benchmark Grounding
- **Embedding Implementation:**
  - Class: `MockEmbeddingProvider`
  - Technique: Deterministic 384-dimensional token feature hashing
  - Algorithm: MD5 token hashes modulo 384, stopword filtering, L2 normalization
  - Fusion: Combined with BM25 sparse lexical ranking via Reciprocal Rank Fusion (RRF, $k=60$)
  - Standard Implementation Disclosure: *"Hybrid retrieval combines BM25 lexical ranking with deterministic 384-dimensional token feature-hashing vectors using Reciprocal Rank Fusion (RRF, k=60). This vectorizer is deterministic and is not a pretrained neural sentence-embedding model."*
- **Benchmark Evaluation:**
  - Test Set: Evaluated over 10 checked-in multi-split test cases (`data/evaluation`: 4 standard, 3 adversarial, 3 held-out)
  - Pass Rate: 100.0% (10/10 passed)
  - Mean MRR: **1.0000** (every target statutory section retrieved at Rank 1)
  - Mean P@3 (Precision@3): 0.4286
  - Adversarial Block Rate: 100.0% (3/3 prompt injection / exfiltration attacks neutralized)
  - Average Retrieval Latency: 3.58 ms
  - Gate 2 Circuit Breaker Threshold: Configured at `0.75` claim-to-evidence text overlap ratio (distinct operational threshold used at runtime for deterministic synthesis fallback; conceptually separate from the offline MRR ranking metric)
  - Bounded Statutory Citation Statement: *"No ungrounded statutory citations were observed in the evaluated test cases."* (No universal zero-hallucination guarantee)
  - Document Processing Latency: Single measured representative test sample of 1.62 seconds

---

## 4. DPDP Act 2023 Principles Standardized Statement
Applied verbatim across all report chapters, presentation slides, and markdown files:
> *"Selected technical safeguards aligned with relevant DPDP Act 2023 principles have been implemented and tested. These include authentication, server-side authorization, private document storage, auditability and deletion workflows. Formal legal compliance certification has not been performed."*

Prohibited claims eliminated:
- No claims of "Section 12 compliant erasure" (Section 12 not operative as of November 6, 2026).
- No claims of "100% DPDP compliant" or "full/strict compliance".
- No claims of "client-side encryption" or "zero third-party telemetry" without verified evidence.
- No unsupported carbon emissions metrics.

---

## 5. Research Reference Counts
- **Scholarly Research Papers:** 30 peer-reviewed research papers (indexed across IEEE, ACM, Springer, ACL, ICLR).
- **Statutory & Technical References:** Supplemented by relevant enactments (Digital Personal Data Protection Act, 2023).
- **Total Bibliography Entries:** 31 entries.

---

## 6. Official Pending Student & Institutional Inputs
1. **Student Signatures:** Pending physical signatures on Candidate's Declaration page.
2. **Guide & Examiner Signatures:** Pending physical sign-off on Certificate page.
3. **Turnitin Similarity Report:** Official similarity percentage and date pending from college library / DAIP coordinator.
4. **External Engagement Proofs:** The 4 individual team members' documentary training/internship certificates pending student submission.
