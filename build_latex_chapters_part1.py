import os

CHAPTERS_DIR = r"docs\review-2-submission\latex-source\chapters"

# =========================================================================
# CHAPTER 1: Problem Identification
# =========================================================================
ch1_content = r"""\chapter{Problem Identification}
\label{ch:problem_identification}

\section{Background and Industrial Context}
\label{sec:background}
In contemporary democratic governance, access to justice, statutory legal clarity, and transparent public welfare distribution represent foundational pillars of the rule of law. Within the Republic of India, the digital transformation of public administrative services has accelerated significantly over the past decade under the aegis of the Digital India initiative. Government portals such as the National Government Services Portal, myScheme, e-Courts Services, e-Daakhil, and the Centralised Public Grievance Redress and Monitoring System (CPGRAMS) have made millions of statutory records, court cause lists, and welfare application forms digitally accessible to the public.

However, a profound structural disparity persists between \textit{digital availability} and \textit{actionable citizen accessibility}. The Indian legal and administrative ecosystem is characterized by extraordinary polycentric complexity. At the statutory level, citizens are governed by over 800 central acts, thousands of state-specific enactments, and countless administrative circulars, statutory orders, and judicial precedents. Compounding this structural complexity is the transition from colonial-era legal codes to modern statutory frameworks, notably the replacement of the Indian Penal Code (IPC 1860) and Code of Criminal Procedure (CrPC 1973) with the Bharatiya Nyaya Sanhita (BNS 2023) and Bharatiya Nagarik Suraksha Sanhita (BNSS 2023).

For ordinary citizens---particularly those from economically weaker sections, rural agricultural backgrounds, and marginalized socio-economic strata---navigating this administrative labyrinth presents insurmountable cognitive, linguistic, and financial barriers. When confronted with an official summons, a tenancy eviction notice, an arbitrary denial of welfare benefits, or a consumer contract dispute, citizens rarely know which specific statute governs their grievance, which administrative or judicial forum possesses subject-matter jurisdiction, what strict limitation periods apply, or what documentation is mandatory for valid filing.

\section{The Existing Problem: Seven Core Citizen Pain Points}
\label{sec:pain_points}
Empirical investigation of citizen interaction with the Indian socio-legal ecosystem reveals seven persistent, systemic pain points:

\begin{enumerate}
    \item \textbf{Jurisdictional and Forum Ambiguity:} Citizens are unable to discern whether a civil dispute, consumer grievance, service deficiency, or criminal infringement falls under the jurisdiction of a District Consumer Disputes Redressal Commission, a Civil Judge (Junior Division), an Industrial Labour Tribunal, or a Sub-Divisional Magistrate. Filing in the incorrect forum results in procedural dismissal, forfeiture of filing fees, and expired limitation periods.
    \item \textbf{Cognitive Intimidation and Notice Panic:} Official communications from administrative authorities, municipal corporations, or opposing advocates (e.g., show-cause notices, Section 138 Negotiable Instruments Act demand notices, summary eviction notices) are drafted in archaic, formal legalese. Citizens frequently misinterpret these notices, missing strict statutory reply windows (often 15 to 30 days) and incurring adverse ex-parte orders.
    \item \textbf{Opaque Welfare Scheme Discovery:} The Government of India and various State Governments administer transformative social welfare schemes (e.g., PM-KISAN, Ayushman Bharat PM-JAY, Pradhan Mantri Awas Yojana, National Social Assistance Programme). However, qualifying citizens remain unaware of their entitlements due to fragmented departmental websites, siloed eligibility criteria, and lack of unified discovery engines.
    \item \textbf{Procedural and Documentation Friction:} Every legal action and welfare claim requires strict documentary prerequisites (e.g., land records, income certificates, caste affidavits, death certificates, purchase receipts). Omission of a single mandatory document causes repeated portal rejections, bureaucratic rent-seeking, and administrative despair.
    \item \textbf{Prohibitive Legal Consultation Costs:} While constitutional mandates guarantee legal aid under Article 39A of the Constitution of India, the reality is that quality legal advice from private advocates remains financially unattainable for over 70\% of the population. A single preliminary consultation often costs between INR 2,000 and INR 10,000, pricing out vulnerable citizens seeking preliminary orientation.
    \item \textbf{Proliferation of Generative Hallucination and Misinformation:} With the recent surge in consumer-grade Artificial Intelligence (AI) chatbots (such as standard ChatGPT or generic Gemini models), unguided citizens increasingly turn to conversational AI for legal queries. However, empirical studies demonstrate that general-purpose Large Language Models (LLMs) hallucinate non-existent statutory sections, fabricate Supreme Court case citations, and cite repealed laws with alarming frequency, presenting severe risks of legal prejudice.
    \item \textbf{Architectural Silos Across Public Systems:} Existing government digital public infrastructure operates in rigid silos. The judiciary's e-Courts system does not communicate with welfare portals (myScheme), and neither communicates with administrative tribunals or legal aid networks (National Legal Services Authority - NALSA). Citizens must manually act as the human integration glue across disparate state mechanisms.
\end{enumerate}

\section{Why Current Approaches Are Inadequate}
\label{sec:inadequacy}
Existing computational and institutional interventions suffer from fundamental structural limitations:

\subsection{Static Government Repositories (India Code, e-Courts, myScheme)}
Official repositories such as India Code and e-Courts function primarily as static text archives. They provide basic keyword-based indexing or full-text PDF downloads. They offer zero conversational reasoning, zero automated entity extraction, zero plain-language translation of complex legal sections, and zero contextual guidance correlating a citizen's factual grievance with applicable relief pathways.

\subsection{Government Conversational Portals (Nyaya Setu / Tele-Law)}
Initiatives such as Nyaya Setu represent commendable efforts to increase pre-litigation awareness. However, as detailed in our comparative analysis, Nyaya Setu operates largely as a single-turn, stateless query answering service. It lacks contextual citizen session memory, does not integrate with central or state welfare schemes, does not possess document intelligence to parse uploaded summons or notices, and lacks deterministic post-retrieval grounding circuits to prevent inaccurate generative assertions.

\subsection{Commercial Large Language Models}
General-purpose commercial foundation models (e.g., OpenAI GPT-4, Anthropic Claude, Google Gemini) possess vast general knowledge but lack deep domain constraints for Indian statutory jurisprudence. They treat legal interpretation as an unconstrained generative completion task. Because statutory law requires 100\% precision---where a single incorrect subsection number or missed limitation period alters the legal outcome entirely---unconstrained stochastic text generation is fundamentally dangerous in civic domains.

\section{Motivation for an Evidence-Grounded Civic Platform}
\label{sec:motivation}
The urgent necessity for an equitable, trustworthy civic technology platform motivates the conception and development of \textbf{CivicSphere AI}. Rather than viewing legal assistance, welfare navigation, and document processing as isolated technical tasks, CivicSphere AI unifies them into an integrated, evidence-grounded agentic workflow.

The core motivation is governed by three foundational design principles:
\begin{itemize}
    \item \textbf{Zero-Hallucination Evidence Grounding:} The platform must never generate a statutory assertion, procedural deadline, or rights claim without explicitly linking that claim to a verified, authoritative statutory section chunk or official government notification. Where evidence is ambiguous or confidence is low, the system must trigger deterministic circuit breakers rather than hallucinating.
    \item \textbf{Cross-Domain Contextual Synergy:} A citizen's real-world problem does not conform to departmental boundaries. A labourer facing unlawful wage withholding requires employment law guidance, welfare entitlement discovery (e.g., e-Shram relief), and document extraction from their employment letter simultaneously. CivicSphere AI bridges these domains seamlessly.
    \item \textbf{Privacy by Design and Democratic Trust:} In strict compliance with the Digital Personal Data Protection (DPDP) Act 2023, the platform must guarantee that citizen queries, uploaded notices, and personal identifying documents are treated with utmost confidentiality, stored in private encrypted object buckets, and purged permanently upon user request, while retaining immutable audit trails for transparent system governance.
\end{itemize}
"""

with open(os.path.join(CHAPTERS_DIR, "chapter1_problem_identification.tex"), "w", encoding="utf-8") as f:
    f.write(ch1_content)
print("Wrote chapter1_problem_identification.tex")

# =========================================================================
# CHAPTER 2: Literature Survey and Gap Analysis
# =========================================================================
ch2_content = r"""\chapter{Literature Survey and Gap Analysis}
\label{ch:literature_survey}

\section{Introduction}
\label{sec:lit_intro}
Developing a high-stakes, domain-specific civic intelligence platform requires grounding in contemporary peer-reviewed scientific literature. This chapter presents a systematic review of thirty-one peer-reviewed research papers and foundational technical specifications published in premier venues including IEEE, ACM, Springer, ACL, EMNLP, ICLR, and ICML. The literature is decomposed into seven cohesive thematic categories, followed by a comparative survey matrix, a detailed critical critique of existing systems, the identification of seven technical research gaps, and a rigorous gap-to-solution translation mapping.

\section{Research Selection Criteria and Search Methodology}
\label{sec:selection_criteria}
To ensure the highest academic quality and direct relevance to CivicSphere AI, papers were selected according to strict inclusion and exclusion criteria:
\begin{itemize}
    \item \textbf{Peer-Reviewed Quality:} Published in indexed journals (IEEE Trans., ACM Computing Surveys, Springer AI \& Law) or top-tier computer science conferences (ACL, EMNLP, NeurIPS, AAAI, SIGIR).
    \item \textbf{Domain Specificity:} Explicit focus on legal Natural Language Processing (NLP), statutory reasoning, Retrieval-Augmented Generation (RAG), knowledge graph representation, intelligent document processing, or AI trust/safety.
    \item \textbf{Jurisdictional Relevance:} Strong representation of Indian legal benchmarks, multilingual processing, and low-resource governance contexts.
\end{itemize}

\section{Thematic Literature Survey}
\label{sec:thematic_survey}

\subsection{Theme 1: Legal AI, Legal Question Answering \& Indian Legal Systems}
Research in legal AI has evolved from early rule-based expert systems to neural transformer architectures. Nigam et al.~\cite{nigam2026ailqa} introduced the AILQA benchmark specifically for evaluating AI-driven legal question answering within the Indian judicial hierarchy. Their findings revealed that commercial LLMs exhibit severe hallucination rates ($>35\%$) when answering Indian legal queries, frequently citing repealed provisions of the Indian Penal Code or fabricating High Court case citations. Chi et al.~\cite{chi2026legalai} provided a comprehensive survey of LegalAI in the LLM era, establishing taxonomies for legal information extraction, legal reasoning, and judgment prediction, concluding that domain-specific grounding is indispensable. Zhong et al.~\cite{zhong2020jecqa} introduced JEC-QA, demonstrating that legal QA requires multi-step deductive reasoning over statutory conditions rather than simple semantic surface matching.

\subsection{Theme 2: Legal NLP, Benchmarks \& Rhetorical Role Extraction}
Chalkidis et al.~\cite{chalkidis2022lexglue} established LexGLUE as the authoritative benchmark for legal language understanding in English, proving that generic language models perform poorly on complex legal classification tasks without task-specific tuning. In the Indian context, Joshi et al.~\cite{joshi2024inlegalner} developed InLegalNER, a specialized Named Entity Recognition corpus identifying Indian legal entities such as petitioner, respondent, judge, statute, section, and precedent. Bhattacharya et al.~\cite{bhattacharya2019identification} investigated methods for identifying rhetorical roles in Indian court judgments, providing the foundational principles for chunking legal texts according to argumentative structure rather than arbitrary token boundaries.

\subsection{Theme 3: Legal Information Retrieval \& Entailment}
Statutory retrieval presents unique challenges distinct from general web search. Sharma et al.~\cite{sharma2023legal} demonstrated that legal information retrieval for Indian judgments requires hybrid approaches combining lexical matching and semantic dense vectors. Locke and Ashley~\cite{locke1995statute} analyzed statutory interpretation, emphasizing that statutory sections function as rigid logical rules containing conditions precedent. Standard keyword search (BM25)~\cite{robertson2009probabilistic} excels at identifying exact statutory section numbers, whereas dense semantic search (Sentence-BERT)~\cite{reimers2019sentence} captures high-level intent. Cormack et al.~\cite{cormack2009reciprocal} established Reciprocal Rank Fusion (RRF) as a robust, parameter-free algorithm to combine disparate ranking lists, outperforming individual rank learning methods.

\subsection{Theme 4: Knowledge Graphs \& Multi-Hop Relational Reasoning}
Knowledge graphs provide structured, symbolic representations of domain entities and relationships. Ji et al.~\cite{ji2022survey} surveyed knowledge graphs, highlighting their role in enhancing neural models with factual grounding. Pan et al.~\cite{pan2024unifying} provided a roadmap for unifying LLMs and Knowledge Graphs (KGs), demonstrating that bidirectional synergy---using KGs to constrain LLM generation and LLMs to extract graph triples---mitigates hallucination. Hamilton et al.~\cite{hamilton2017inductive} developed GraphSAGE for inductive node embeddings, while Bordes et al.~\cite{bordes2013translating} introduced TransE for multi-relational link prediction, enabling multi-hop path traversal between legal acts, administrative authorities, and citizen welfare schemes.

\subsection{Theme 5: Retrieval-Augmented Generation (RAG) Systems}
Lewis et al.~\cite{lewis2020retrieval} established the modern RAG paradigm, combining parametric memory (pre-trained neural weights) with non-parametric retrieval memory. Gao et al.~\cite{gao2023retrieval} surveyed advanced RAG systems, categorizing them into Naive RAG, Advanced RAG (pre-retrieval query routing, post-retrieval reranking), and Modular RAG. In civic intelligence, modular RAG is essential because the platform must route legal questions to statutory databases and welfare questions to scheme registries dynamically.

\subsection{Theme 6: Citation Verification \& Hallucination Mitigation}
Hallucination in foundation models represents the most severe bottleneck to production deployment in public domains. Huang et al.~\cite{huang2023survey} presented an exhaustive taxonomy of LLM hallucinations, distinguishing between factuality hallucinations and faithfulness hallucinations. Shuster et al.~\cite{shuster2021retrieval} proved that retrieval augmentation significantly reduces conversational hallucination. Gao et al.~\cite{gao2023enabling} proposed automated citation evaluation frameworks, demonstrating that requiring models to generate explicit citations directly linked to retrieved spans enables deterministic post-generation verification.

\subsection{Theme 7: AI Security, Privacy \& Adversarial Robustness}
Deploying AI in public governance demands enterprise-grade trust, security, and privacy. Bommasani et al.~\cite{bommasani2021opportunities} and Weidinger et al.~\cite{weidinger2021ethical} documented social risks and security vulnerabilities in foundation models, including prompt injection, privilege escalation, and unintended PII disclosure. Amodei et al.~\cite{amodei2016concrete} outlined concrete AI safety problems, advocating for deterministic guardrails. Wu et al.~\cite{wu2023autogen} and Li et al.~\cite{li2023camel} explored communicative multi-agent architectures, demonstrating that dividing tasks among role-bounded agents prevents privilege escalation. In India, statutory compliance with the Digital Personal Data Protection (DPDP) Act 2023~\cite{dpdpact2023} mandates strict purpose limitation, encrypted storage, and verifiable data erasure.

\section{Literature Survey Matrix}
\label{sec:lit_matrix}
Table~\ref{tab:lit_survey_matrix} summarizes representative foundational papers across our seven research themes, detailing their core methodology, key findings, and direct engineering impact on the CivicSphere AI platform architecture.

\begin{table}[H]
\centering
\caption{Thirty-Paper Thematic Literature Survey Matrix (Representative Sample)}
\label{tab:lit_survey_matrix}
\resizebox{\textwidth}{!}{%
\begin{tabular}{|l|l|p{4.5cm}|p{5cm}|p{4.5cm}|}
\hline
\textbf{Paper Ref.} & \textbf{Theme} & \textbf{Core Methodology} & \textbf{Key Findings} & \textbf{Impact on CivicSphere AI} \\ \hline
Nigam et al.~\cite{nigam2026ailqa} & Legal AI & Benchmark Indian legal QA against SC/HC judgments & Commercial LLMs suffer $>35\%$ hallucination on Indian law & Engineered Gate 2 statutory circuit breaker \\ \hline
Chi et al.~\cite{chi2026legalai} & Legal NLP & Taxonomy of LLM tasks in legal informatics & General models lack statutory domain constraints & Ingested 8 dedicated Indian statutory acts \\ \hline
Zhong et al.~\cite{zhong2020jecqa} & Legal QA & Multi-choice statutory QA requiring condition parsing & Surface semantic similarity fails on legal logic & Implemented condition-action rule evaluation \\ \hline
Sharma et al.~\cite{sharma2023legal} & Legal IR & Hybrid lexical + dense retrieval on Indian judgments & Exact section numbers missed by pure vector search & Adopted BM25 + dense vector hybrid search \\ \hline
Cormack et al.~\cite{cormack2009reciprocal} & Information Retrieval & Reciprocal Rank Fusion (RRF) parameter-free combination & RRF consistently outperforms individual rankers & Implemented RRF fusion with $k=60$ constant \\ \hline
Ji et al.~\cite{ji2022survey} & Knowledge Graphs & Comprehensive survey of KG representations and reasoning & Graph paths ground generative reasoning in facts & Built 40+ node NetworkX multi-relational graph \\ \hline
Lewis et al.~\cite{lewis2020retrieval} & RAG Systems & Parametric + non-parametric retrieval generation & External knowledge reduces hallucinations & Core RAG architecture for statutory guidance \\ \hline
Shuster et al.~\cite{shuster2021retrieval} & Hallucination & Retrieval augmentation in conversational systems & Grounding reduces dialogue hallucination by $>80\%$ & Structured immutable Evidence Packs \\ \hline
Gao et al.~\cite{gao2023enabling} & Citation AI & Automated citation extraction and span verification & Inline citations enable deterministic verification & Built regex citation validator \\ \hline
Wu et al.~\cite{wu2023autogen} & Multi-Agent & Multi-agent conversation and task orchestration & Specialized agents outperform single monolithic LLM & Modular orchestrator with 4 domain agents \\ \hline
Huang et al.~\cite{huang2022layoutlmv3} & Document AI & Multimodal text and layout transformer pre-training & Spatial coordinates critical for notice parsing & Structured heuristic PDF regex extractor \\ \hline
DPDP Act~\cite{dpdpact2023} & AI Governance & Statutory personal data protection mandate & Mandates hard deletion and purpose limitation & Supabase S3 private storage + cascade purge \\ \hline
\end{tabular}%
}
\end{table}

\section{Critical Analysis of Existing Systems}
\label{sec:existing_systems_critique}
A rigorous evaluation of current technological and governmental solutions underscores the gap CivicSphere AI bridges:

\subsection{Nyaya Setu Platform}
The Nyaya Setu platform is an official government-backed legal assistance initiative designed to provide conversational guidance and connect citizens to legal-aid clinics (Tele-Law and District Legal Services Authorities - DLSA).
\begin{itemize}
    \item \textbf{Strengths:} Nyaya Setu offers an accessible, public-facing portal that raises fundamental civic awareness, indexes basic legal definitions, and establishes formal institutional referral pathways.
    \item \textbf{Critical Limitations:} (i) It operates primarily as a single-turn query system without contextual session memory; (ii) It has zero integration with central or state welfare schemes, forcing citizens to consult separate platforms; (iii) It lacks intelligent document processing, preventing citizens from uploading notices or court summons for analysis; (iv) It relies on unconstrained conversational generation without deterministic statutory verification gates; and (v) It does not provide client-side case dossier workspaces for persistent document tracking.
\end{itemize}

\subsection{Static Government Portals (India Code, e-Courts, myScheme)}
India Code hosts authentic text of central and state enactments, while myScheme indexes central welfare schemes.
\begin{itemize}
    \item \textbf{Strengths:} Highly authoritative, official sources of truth with statutory validity.
    \item \textbf{Critical Limitations:} Rigid search filters require the user to already know the exact act name, department, or legal terminology. They offer no conversational assistance, no automated eligibility calculation, and zero cross-linking between a legal grievance and an applicable welfare remedy.
\end{itemize}

\subsection{Commercial Foundation Models (ChatGPT, Claude, Gemini)}
\begin{itemize}
    \item \textbf{Strengths:} High conversational fluency, multilingual translation, and broad conceptual understanding.
    \item \textbf{Critical Limitations:} High propensity for legal hallucination; failure to differentiate between current and repealed Indian statutes; lack of verifiable citation grounding; and severe data privacy concerns regarding the transmission of confidential citizen legal documents to foreign cloud servers.
\end{itemize}

\section{Identified Research and Technical Gaps}
\label{sec:research_gaps}
Our systematic survey identifies seven critical research and engineering gaps:
\begin{enumerate}
    \item \textbf{Gap 1: Cross-Domain Fragmentation:} Legal guidance, government welfare navigation, and document processing are treated as isolated computational problems rather than an integrated citizen workflow.
    \item \textbf{Gap 2: Single-Mode Retrieval Brittleness:} Dense vector embeddings fail to retrieve specific statutory subsections, while BM25 fails to understand citizen natural language queries.
    \item \textbf{Gap 3: Citation Hallucination in Civic AI:} Standard autoregressive LLMs fabricate non-existent case laws, incorrect sections, and expired administrative orders.
    \item \textbf{Gap 4: Temporal and Jurisdictional Invalidation:} Legal systems fail to account for statutory transitions (e.g., IPC to BNS 2023) and expiring welfare application deadlines.
    \item \textbf{Gap 5: Uncontrolled Autonomous Agency:} Unconstrained multi-agent architectures pose authorization, security, and prompt injection risks in public deployments.
    \item \textbf{Gap 6: OCR-Only Document Processing:} Existing document tools perform raw optical character recognition without semantic legal structuring (failing to extract notice dates, fine demands, or court dates).
    \item \textbf{Gap 7: Ephemeral Serverless Storage Vulnerabilities:} Modern serverless cloud deployments routinely fail to persist uploaded citizen documents across invocations due to reliance on ephemeral local container storage (`/tmp`).
\end{enumerate}

\section{Research Gap to Technical Solution Translation}
\label{sec:gap_to_solution}
Table~\ref{tab:gap_to_solution} articulates the direct translation from identified research gaps to our engineered technical solutions and their implementation in CivicSphere AI.

\begin{table}[H]
\centering
\caption{Research Gap to Technical Solution to Implemented Architecture Matrix}
\label{tab:gap_to_solution}
\resizebox{\textwidth}{!}{%
\begin{tabular}{|l|p{4.5cm}|p{5cm}|p{4.5cm}|}
\hline
\textbf{Gap ID} & \textbf{Identified Gap} & \textbf{Engineered Solution} & \textbf{CivicSphere Implementation} \\ \hline
\textbf{G1} & Cross-Domain Fragmentation & Unified Multi-Agent Modular Architecture & FastAPI modular monolith with shared Pydantic DTOs \\ \hline
\textbf{G2} & Retrieval Brittleness & Reciprocal Rank Fusion (RRF) Hybrid Search & BM25 sparse + dense cosine embeddings ($k=60$) \\ \hline
\textbf{G3} & Citation Hallucination & Gate 2 Statutory Circuit Breaker & Deterministic synthesis fallback with regex citation validator \\ \hline
\textbf{G4} & Temporal Invalidation & Temporal Knowledge Graph Traversal & NetworkX multigraph with \texttt{valid\_until} edge metadata \\ \hline
\textbf{G5} & Uncontrolled Agency & Strict Role-Based Access Control (RBAC) & JWT bearer dependency injection with scoped agent tools \\ \hline
\textbf{G6} & OCR-Only Processing & Heuristic Civic Entity Extractor & pdfplumber layout parser + regex legal metadata extraction \\ \hline
\textbf{G7} & Ephemeral Storage Crashes & Durable Cloud Storage Adapter & Supabase private S3 object storage with presigned tokens \\ \hline
\end{tabular}%
}
\end{table}
"""

with open(os.path.join(CHAPTERS_DIR, "chapter2_literature_survey.tex"), "w", encoding="utf-8") as f:
    f.write(ch2_content)
print("Wrote chapter2_literature_survey.tex")

# =========================================================================
# CHAPTER 3: Problem Statement
# =========================================================================
ch3_content = r"""\chapter{Problem Statement}
\label{ch:problem_statement}

\section{Formal Problem Formulation}
\label{sec:problem_formulation}
Formally, let a citizen user $U$ interact with the public socio-legal domain through a natural language query $Q = \{w_1, w_2, \dots, w_n\}$ or an uploaded legal document $D_{in} \in \{\text{PDF, Image}\}$. The citizen's objective is to obtain an actionable, legally accurate, and plain-language guidance response $R$, accompanied by a set of verifiable statutory citations $C = \{c_1, c_2, \dots, c_k\}$, a set of qualifying government welfare schemes $S = \{s_1, s_2, \dots, s_m\}$, and an extracted document structured evidence record $E_{doc}$.

The multi-domain civic intelligence challenge can be modeled as finding an optimal mapping function $\Phi$:
\begin{equation}
\Phi: (Q, D_{in}, \mathcal{K}_{statute}, \mathcal{K}_{scheme}, \mathcal{G}_{civic}) \longrightarrow (R, C, S, E_{doc}, \mathcal{A}_{next})
\label{eq:mapping_func}
\end{equation}
subject to the following hard constraints:
\begin{enumerate}
    \item \textbf{Citation Verifiability Constraint:} $\forall c_i \in C$, $c_i$ must map directly to an authoritative statutory section in $\mathcal{K}_{statute}$ with empirical text grounding $\text{Sim}(c_i, \mathcal{K}_{statute}) \ge \tau_{threshold}$. No fabricated or hallucinated citations are permitted.
    \item \textbf{Temporal Freshness Constraint:} $\forall c_i \in C$, the statutory provision must be legally in force at timestamp $t_{query}$ (i.e., repealed provisions such as IPC sections must be mapped to their corresponding BNS 2023 equivalents).
    \item \textbf{Data Privacy and Confidentiality Constraint:} The storage of $D_{in}$ and processing of $Q$ must strictly comply with the Digital Personal Data Protection Act 2023, ensuring zero unauthorized cross-tenant data access, isolated private object storage, and immediate cascade deletion upon user request:
    \begin{equation}
    \text{Purge}(U) \Longrightarrow \forall d \in D_U, \quad \text{S3Delete}(d) \land \text{DBDelete}(d) = \text{True}
    \end{equation}
    \item \textbf{Sub-Second Computational Latency:} The triage of $Q$ and heuristic extraction of $D_{in}$ must execute within latency $\le 2.0$ seconds on serverless cloud compute infrastructure.
\end{enumerate}

\section{Logical Connection: From Problem to Solution}
\label{sec:logical_connection}
The logical progression from the identified civic failure modes to our architectural design is visualized in Figure~\ref{fig:problem_to_solution_flow}.

\begin{figure}[H]
\centering
\includegraphics[width=0.9\textwidth]{images/homepage_view.png}
\caption{Logical progression from citizen problem to evidence-grounded civic guidance.}
\label{fig:problem_to_solution_flow}
\end{figure}

The transition operates across three sequential computational layers:
\begin{itemize}
    \item \textbf{Input Disambiguation Layer:} Translates ambiguous, emotionally distressed natural language queries into normalized legal entities, statutory domains, and administrative locations.
    \item \textbf{Hybrid Knowledge Reasoning Layer:} Simultaneously interrogates lexical BM25 indices, dense semantic embedding vectors, and relational knowledge graph multigraphs to assemble a comprehensive, factual Evidence Pack.
    \item \textbf{Verification and Plain-Language Synthesis Layer:} Evaluates the assembled Evidence Pack through the Gate 2 circuit breaker. If grounded, it generates an accessible citizen action roadmap with procedural steps, limitation deadlines, and official portal links; if ungrounded, it falls back to safe deterministic guidance.
\end{itemize}

\section{Research and Engineering Questions}
\label{sec:research_questions}
To evaluate the technical viability of CivicSphere AI, the project investigates five fundamental research and engineering questions:
\begin{itemize}
    \item \textbf{RQ1 (Retrieval Precision):} Does a hybrid retrieval architecture combining BM25 sparse keyword matching and dense vector embeddings via Reciprocal Rank Fusion achieve higher recall and Mean Reciprocal Rank (MRR) on Indian statutory queries than either retrieval model independently?
    \item \textbf{RQ2 (Hallucination Elimination):} Can a deterministic post-retrieval circuit breaker (Gate 2) completely eliminate fabricated statutory section citations compared to unconstrained foundation model generation?
    \item \textbf{RQ3 (Multi-Hop Civic Reasoning):} Does traversing a relational Knowledge Graph allow a system to discover indirect government welfare schemes for which a citizen qualifies based on their underlying legal problem?
    \item \textbf{RQ4 (Document Triage Latency):} Can a lightweight, regex-based heuristic parsing engine reliably extract critical notice dates, penalty demands, and section references from uploaded civic PDFs within 2.0 seconds on commodity serverless compute?
    \item \textbf{RQ5 (Serverless Storage Durability):} How can an asynchronous cloud storage adapter be architected to eliminate ephemeral container crashes and achieve 100\% byte-exact document persistence under serverless cold-start conditions?
\end{itemize}

\section{Stakeholder Personas and Scope Boundaries}
\label{sec:scope_boundaries}

\subsection{Target Stakeholder Personas}
CivicSphere AI is engineered to deliver differentiated value across four primary stakeholder groups:
\begin{enumerate}
    \item \textbf{The Everyday Indian Citizen (Primary User):} Vulnerable, semi-literate, or middle-income citizens requiring rapid, no-cost legal triage, welfare discovery, and document explanation without paying upfront retainer fees.
    \item \textbf{Paralegals and Legal Aid Clinics (Secondary User):} District Legal Services Authority (DLSA) volunteers and paralegals who utilize the platform to rapidly intake walk-in clients, auto-extract notice deadlines, and compile structured legal briefing dossiers.
    \item \textbf{Civic Administrators and Policy Analysts:} Government officials who inspect anonymized query telemetry and audit logs to identify emerging civic grievances (e.g., localized ration distribution failures).
    \item \textbf{Micro, Small, and Medium Enterprises (MSMEs) and Gig Workers:} Independent contractors navigating contract disputes, delayed payments under the MSMED Act, and gig-platform consumer grievances.
\end{enumerate}

\subsection{Explicit Scope Boundaries and Non-Goals}
To maintain academic integrity and ethical safety, the project defines strict non-goals:
\begin{itemize}
    \item \textbf{Non-Goal 1 (No Advocate Substitution):} CivicSphere AI does \textit{not} provide formal advocate-client representation and does not dispense binding legal opinions. It functions strictly as an informational and procedural triage system.
    \item \textbf{Non-Goal 2 (No Automated Litigation Filing):} The platform does not automatically file court petitions or submit binding affidavits to judicial registries without human lawyer review.
    \item \textbf{Non-Goal 3 (Jurisdictional Scope):} The platform is bounded strictly to the Republic of India (Central Statutes and major State welfare schemes), excluding foreign legal jurisdictions.
\end{itemize}
"""

with open(os.path.join(CHAPTERS_DIR, "chapter3_problem_statement.tex"), "w", encoding="utf-8") as f:
    f.write(ch3_content)
print("Wrote chapter3_problem_statement.tex")

print("Wrote chapters 1, 2, and 3.")
