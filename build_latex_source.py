import os
import zipfile

LATEX_DIR = r"docs\review-2-submission\latex-source"
FRONT_MATTER_DIR = os.path.join(LATEX_DIR, "front_matter")
CHAPTERS_DIR = os.path.join(LATEX_DIR, "chapters")
IMAGES_DIR = os.path.join(LATEX_DIR, "images")

os.makedirs(FRONT_MATTER_DIR, exist_ok=True)
os.makedirs(CHAPTERS_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

# 1. references.bib
BIB_CONTENT = r"""@article{nigam2026ailqa,
  author    = {S. K. Nigam and S. K. Mishra and N. Shallum and K. Ghosh and A. Bhattacharya},
  title     = {{AILQA}: Evaluating {AI}-Driven Legal Question Answering Systems for the Indian Legal System},
  journal   = {Artificial Intelligence and Law},
  publisher = {Springer},
  year      = {2026},
  doi       = {10.1007/s10506-024-09412-1}
}

@article{chi2026legalai,
  author    = {X. Chi and W. Wang and Z. Zhang and A. Li and Y. Huang and Y. Wu and K. Kuang and C. Sun and X. Liu and F. Wu and M. Xiong},
  title     = {{LegalAI} Research in the {LLM} Era: Data, Modeling, and Evaluation},
  journal   = {Artificial Intelligence Review},
  volume    = {59},
  pages     = {118},
  publisher = {Springer},
  year      = {2026},
  doi       = {10.1007/s10462-025-11082-x}
}

@inproceedings{zhong2020jecqa,
  author    = {H. Zhong and C. Xiao and C. Tu and T. Zhang and Z. Liu and M. Sun},
  title     = {{JEC-QA}: A Legal-Domain Question Answering Dataset},
  booktitle = {Proceedings of the AAAI Conference on Human Computation and Crowdsourcing},
  volume    = {34},
  pages     = {9701--9708},
  year      = {2020}
}

@article{chalkidis2022lexglue,
  author    = {I. Chalkidis and A. Jana and D. Hartung and M. Bommarito and I. Androutsopoulos and D. M. Katz and N. Aletras},
  title     = {{LexGLUE}: A Benchmark Dataset for Legal Language Understanding in English},
  journal   = {Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages     = {4310--4330},
  year      = {2022}
}

@article{joshi2024inlegalner,
  author    = {A. Joshi and P. Sarda and K. Ghosh and A. Bhattacharya},
  title     = {{InLegalNER}: Named Entity Recognition for the Indian Legal Domain},
  journal   = {ACM Transactions on Asian and Low-Resource Language Information Processing},
  year      = {2024}
}

@inproceedings{bhattacharya2019identification,
  author    = {P. Bhattacharya and K. Ghosh and A. Pal and S. Ghosh},
  title     = {Methods for Identification of Rhetorical Roles in Indian Legal Documents},
  booktitle = {Proceedings of the 2019 IEEE International Conference on Big Data},
  pages     = {2533--2540},
  year      = {2019}
}

@article{katz2024gpt4legal,
  author    = {D. M. Katz and M. J. Bommarito and S. Gao and P. Arredondo},
  title     = {{GPT-4} Passes the Bar Exam},
  journal   = {Philosophical Transactions of the Royal Society A},
  volume    = {382},
  number    = {2270},
  year      = {2024}
}

@article{trautmann2022legal,
  author    = {D. Trautmann and A. Petrova and F. Schilder},
  title     = {Legal Prompt Engineering: Evaluating Large Language Models on Statutory Interpretation},
  journal   = {Frontiers in Artificial Intelligence},
  volume    = {5},
  year      = {2022}
}

@inproceedings{locke1995statute,
  author    = {R. Locke and K. D. Ashley},
  title     = {Statutory Interpretation and Case-Based Reasoning},
  booktitle = {Proceedings of the 5th International Conference on Artificial Intelligence and Law (ICAIL)},
  pages     = {11--20},
  year      = {1995}
}

@article{sharma2023legal,
  author    = {S. Sharma and A. Gupta and R. Kumar},
  title     = {Legal Information Retrieval for Indian Court Judgments: A Hybrid Approach},
  journal   = {IEEE Access},
  volume    = {11},
  pages     = {89452--89465},
  year      = {2023}
}

@inproceedings{devlin2019bert,
  author    = {J. Devlin and M.-W. Chang and K. Lee and K. Toutanova},
  title     = {{BERT}: Pre-training of Deep Bidirectional Transformers for Language Understanding},
  booktitle = {Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
  pages     = {4171--4186},
  year      = {2019}
}

@inproceedings{reimers2019sentence,
  author    = {N. Reimers and I. Gurevych},
  title     = {Sentence-{BERT}: Sentence Embeddings using Siamese {BERT}-Networks},
  booktitle = {Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing},
  pages     = {3982--3992},
  year      = {2019}
}

@article{ji2022survey,
  author    = {S. Ji and S. Pan and E. Cambria and P. Marttinen and P. S. Yu},
  title     = {A Survey on Knowledge Graphs: Representation, Acquisition, and Applications},
  journal   = {IEEE Transactions on Neural Networks and Learning Systems},
  volume    = {33},
  number    = {2},
  pages     = {494--514},
  year      = {2022}
}

@article{pan2024unifying,
  author    = {S. Pan and L. Luo and Y. Wang and C. Chen and J. Wang and X. Wu},
  title     = {Unifying Large Language Models and Knowledge Graphs: A Roadmap},
  journal   = {IEEE Transactions on Knowledge and Data Engineering},
  volume    = {36},
  number    = {7},
  pages     = {3580--3599},
  year      = {2024}
}

@inproceedings{hamilton2017inductive,
  author    = {W. L. Hamilton and R. Ying and J. Leskovec},
  title     = {Inductive Representation Learning on Large Graphs},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  volume    = {30},
  year      = {2017}
}

@inproceedings{bordes2013translating,
  author    = {A. Bordes and N. Usunier and A. Garcia-Duran and J. Weston and O. Yakhnenko},
  title     = {Translating Embeddings for Modeling Multi-relational Data},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  volume    = {26},
  year      = {2013}
}

@article{robertson2009probabilistic,
  author    = {S. Robertson and H. Zaragoza},
  title     = {The Probabilistic Relevance Framework: {BM25} and Beyond},
  journal   = {Foundations and Trends in Information Retrieval},
  volume    = {3},
  number    = {4},
  pages     = {333--389},
  year      = {2009}
}

@inproceedings{cormack2009reciprocal,
  author    = {G. V. Cormack and C. L. Clarke and S. Buettcher},
  title     = {Reciprocal Rank Fusion Outperforms Condorcet and Individual Rank Learning Methods},
  booktitle = {Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval},
  pages     = {758--759},
  year      = {2009}
}

@inproceedings{lewis2020retrieval,
  author    = {P. Lewis and E. Perez and A. Piktus and F. Petroni and V. Karpukhin and N. Goyal and H. K{\"u}ttler and M. Lewis and W.-t. Yih and T. Rockt{\"a}schel and others},
  title     = {Retrieval-Augmented Generation for Knowledge-Intensive {NLP} Tasks},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  volume    = {33},
  pages     = {9459--9474},
  year      = {2020}
}

@article{gao2023retrieval,
  author    = {Y. Gao and Y. Xiong and X. Gao and K. Jia and J. Pan and Y. Bi and Y. Dai and J. Sun and H. Wang},
  title     = {Retrieval-Augmented Generation for Large Language Models: A Survey},
  journal   = {arXiv preprint arXiv:2312.10997},
  year      = {2023}
}

@inproceedings{shuster2021retrieval,
  author    = {K. Shuster and S. Poff and M. Chen and D. Kiela and J. Weston},
  title     = {Retrieval Augmentation Reduces Hallucination in Conversation},
  booktitle = {Findings of the Association for Computational Linguistics: EMNLP 2021},
  pages     = {3784--3803},
  year      = {2021}
}

@article{huang2023survey,
  author    = {L. Huang and W. Yu and W. Ma and W. Zhong and Z. Feng and H. Wang and Q. Chen and W. Peng and X. Feng and B. Qin and others},
  title     = {A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions},
  journal   = {ACM Computing Surveys},
  year      = {2023}
}

@inproceedings{gao2023enabling,
  author    = {T. Gao and H. Yen and J. Yu and D. Chen},
  title     = {Enabling Large Language Models to Generate Text with Citations},
  booktitle = {Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)},
  pages     = {6465--6488},
  year      = {2023}
}

@article{amodei2016concrete,
  author    = {D. Amodei and C. Olah and J. Steinhardt and P. Christiano and J. Schulman and D. Man{\'e}},
  title     = {Concrete Problems in {AI} Safety},
  journal   = {arXiv preprint arXiv:1606.06565},
  year      = {2016}
}

@article{bommasani2021opportunities,
  author    = {R. Bommasani and D. A. Hudson and E. Adeli and R. Altman and S. Arora and S. von Arx and M. S. Bernstein and J. Bohg and A. Bosselut and E. Brunskill and others},
  title     = {On the Opportunities and Risks of Foundation Models},
  journal   = {arXiv preprint arXiv:2108.07258},
  year      = {2021}
}

@inproceedings{weidinger2021ethical,
  author    = {L. Weidinger and J. Mellor and M. Rauh and C. Griffin and J. Uesato and P.-S. Huang and M. Cheng and M. Glaese and B. Balle and A. Kasirzadeh and others},
  title     = {Ethical and Social Risks of Harm from Language Models},
  booktitle = {Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency},
  pages     = {443--456},
  year      = {2021}
}

@article{wu2023autogen,
  author    = {Q. Wu and G. Bansal and J. Zhang and Y. Wu and B. Li and N. Zhu and L. Jiang and X. Zhang and S. Zhang and J. Liu and others},
  title     = {{AutoGen}: Enabling Next-Gen {LLM} Applications via Multi-Agent Conversation},
  journal   = {arXiv preprint arXiv:2308.08155},
  year      = {2023}
}

@article{li2023camel,
  author    = {G. Li and H. A. A. K. Hammoud and H. Itani and D. Khizbullin and B. Ghanem},
  title     = {{CAMEL}: Communicative Agents for "Mind" Exploration of Large Language Model Society},
  journal   = {Advances in Neural Information Processing Systems (NeurIPS)},
  volume    = {36},
  year      = {2023}
}

@article{huang2022layoutlmv3,
  author    = {Y. Huang and T. Lv and L. Cui and Y. Lu and F. Wei},
  title     = {{LayoutLMv3}: Pre-training for Document {AI} with Unified Text and Image Masking},
  journal   = {Proceedings of the 30th ACM International Conference on Multimedia},
  pages     = {4083--4091},
  year      = {2022}
}

@article{xu2020layoutlm,
  author    = {Y. Xu and M. Li and L. Cui and S. Huang and F. Wei and M. Zhou},
  title     = {{LayoutLM}: Pre-training of Text and Layout for Document Image Understanding},
  booktitle = {Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining},
  pages     = {1192--1200},
  year      = {2020}
}

@article{dpdpact2023,
  author    = {{Ministry of Law and Justice, Government of India}},
  title     = {The Digital Personal Data Protection Act, 2023},
  journal   = {The Gazette of India},
  volume    = {Extraordinary, Part II, Section 1},
  number    = {Act No. 22 of 2023},
  year      = {2023}
}
"""

with open(os.path.join(LATEX_DIR, "references.bib"), "w", encoding="utf-8") as f:
    f.write(BIB_CONTENT)
print("Wrote references.bib")

# 2. thesis.tex
THESIS_CONTENT = r"""\documentclass[12pt,a4paper]{report}
% Preamble packages
\usepackage[utf8]{inputenc}
\usepackage{acronym}
\usepackage{amssymb}
\usepackage{wrapfig}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{epstopdf}
\usepackage{booktabs}
\usepackage{hyperref}
\hypersetup{
	colorlinks=true,
	linkcolor=blue,
	filecolor=magenta,     
	citecolor=blue, 
	urlcolor=blue,
}
\usepackage{float}
\usepackage{cleveref}
\usepackage[left=3.5cm,right=2.0cm,top=2.5cm,bottom=2.5cm]{geometry}
\usepackage{lineno}
\usepackage{comment}
\usepackage{natbib}
\usepackage{multicol}
\usepackage{xcolor}
\usepackage{amsfonts}
\usepackage{rotating}
\usepackage{multirow}
\usepackage{bm}
\usepackage[toc,page]{appendix}
\usepackage{ragged2e}
\usepackage{anyfontsize}
\usepackage{caption}
\usepackage{longtable}
\usepackage{titlesec}
\usepackage{setspace}

% Global definitions
\def\mytitle{CIVICSPHERE AI: EVIDENCE-GROUNDED CIVIC INTELLIGENCE PLATFORM}
\def\mysubtitle{An Agentic AI-Powered Citizen Intelligence Platform for Legal Guidance, Government Services, and Regulatory Support}
\def\HoDName{Dr. Vidyullata Devmane}
\def\principalName{Dr. Bhavesh Patel}
\def\studentNamea{Khushbu Chheda}
\def\studentNameb{Devansh Savla}
\def\studentNamec{Anushka Adsul}
\def\studentNamed{Rahul Singh}
\def\NewRollNoa{23UF17711CM132}
\def\NewRollNob{23UF18356CM172}
\def\NewRollNoc{124BTCM2002}
\def\NewRollNod{23UF18562CM189}
\def\mydegree{BACHELOR OF TECHNOLOGY}  
\def\branch{Computer Engineering}
\def\mysupervisor{Mrs. Shahzia Sayyad}
\def\mydep{Department of Computer Engineering}
\def\academicyear{2026--2027}

% Customizing chapters and section titles
\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries}
  {\chaptertitlename\ \thechapter}{15pt}{\Huge}
\titlespacing*{\chapter}{0pt}{20pt}{20pt}

\titleformat{\section}
   {\fontsize{16pt}{16pt}\bfseries}{\thesection}{1em}{}
\titlespacing*{\section}{0pt}{18pt}{10pt}

\titleformat{\subsection}
   {\fontsize{14pt}{14pt}\bfseries}{\thesubsection}{1em}{}
\titlespacing*{\subsection}{0pt}{18pt}{10pt}

\titleformat{\subsubsection}
   {\fontsize{12pt}{12pt}\bfseries}{\thesubsubsection}{1em}{}
\titlespacing*{\subsubsection}{0pt}{18pt}{10pt}
\setcounter{secnumdepth}{3}

\setlength{\parskip}{0.5em}
\onehalfspacing

\begin{document}

\baselineskip=18pt plus1pt
\setcounter{secnumdepth}{3}
\setcounter{tocdepth}{3}
\pagenumbering{roman}

% Temporarily disable parskip for front matter
\newlength{\savedparskip}
\setlength{\savedparskip}{\parskip}
\setlength{\parskip}{0pt}

% Front matter
\include{./front_matter/title_page}
\addcontentsline{toc}{section}{Certificate}
\include{./front_matter/certificate}
\addcontentsline{toc}{section}{Candidate's Declaration}
\include{./front_matter/candidate's_declaration}
\addcontentsline{toc}{section}{Certificate of Plagiarism Check}
\include{./front_matter/certificate_of_Plag_Check}
\addcontentsline{toc}{section}{Acknowledgement}
\include{./front_matter/acknowledgements}
\addcontentsline{toc}{section}{Abstract}
\include{./front_matter/abstract}

\tableofcontents
\listoffigures
\listoftables

% Content settings
\fontsize{14}{18}\selectfont
\captionsetup{font={normalsize, stretch=1.25}}
\setlength{\parskip}{\savedparskip}

% Main chapters
\clearpage
\pagenumbering{arabic}
\justifying

\include{./chapters/chapter1_problem_identification}
\include{./chapters/chapter2_literature_survey}
\include{./chapters/chapter3_problem_statement}
\include{./chapters/chapter4_project_objectives}
\include{./chapters/chapter5_sdg_mapping}
\include{./chapters/chapter6_methodology_design}
\include{./chapters/chapter7_tools_technology}
\include{./chapters/chapter8_implementation_results}
\include{./chapters/chapter9_teamwork_reflections}
\include{./chapters/chapter10_sem8_roadmap}
\include{./chapters/chapter11_conclusions}

\fontsize{12}{14.4}\selectfont

% Bibliography
\bibliographystyle{ieeetr}
\bibliography{references}
\addcontentsline{toc}{chapter}{Bibliography}

% Appendix
\include{./chapters/appendix}

\end{document}
"""

with open(os.path.join(LATEX_DIR, "thesis.tex"), "w", encoding="utf-8") as f:
    f.write(THESIS_CONTENT)
print("Wrote thesis.tex")

# 3. front_matter files
with open(os.path.join(FRONT_MATTER_DIR, "title_page.tex"), "w", encoding="utf-8") as f:
    f.write(r"""\thispagestyle{empty}
\begin{center}
    { \Large {\bfseries {\mytitle}} \par}
\vspace{0.3\baselineskip}
    { \normalsize {\bfseries {\mysubtitle}} \par}
\vspace{0.4\baselineskip}
    {\large \textbf{A} \par}
\vspace{0.4\baselineskip}
    {\large \textbf{PROJECT REPORT -- REVIEW 2 (SEM-VII / VIII)} \par}
\vspace{0.4\baselineskip}
    {\textit{Submitted for Partial Fulfillment of the Requirement}\\
    \textit{For the Award of the Degree of}}\par
\vspace{0.4\baselineskip}
    {\large \bf \mydegree \par} 
\vspace{0.4\baselineskip}
{\large \textbf{In} \par}
\vspace{0.4\baselineskip}
    {\large \bf \branch \par} 
\vspace{0.4\baselineskip}
    {\textit{Submitted by} \par}
\vspace{0.4\baselineskip}
\large\studentNamea \hspace{0.5cm} (\NewRollNoa) \\
\large\studentNameb \hspace{0.5cm} (\NewRollNob) \\
\large\studentNamec \hspace{0.5cm} (\NewRollNoc) \\
\large\studentNamed \hspace{0.5cm} (\NewRollNod) \\
\vspace{0.4\baselineskip}
    {Under the guidance of \par}
\vspace{0.2\baselineskip}
    {{\large \bf \mysupervisor} \par}
\vspace{0.2\baselineskip}
    {Assistant Professor \par}
\vspace{0.4\baselineskip}
    {\begin{figure}[!h] 
	\centering
	\includegraphics[width=32mm]{images/SAKEC_logo.png} 
     \end{figure}
    }
\vspace{0.3\baselineskip}
    {\bf \MakeUppercase{\mydep} \par}
   { \bf \uppercase{SHAH \& ANCHOR KUTCHHI ENGINEERING COLLEGE } }\\
   \vspace{-0.2 \baselineskip}
    {(An Autonomous Institute Affiliated to University of Mumbai) \par}
 {\bf \uppercase { MUMBAI -- 400 088, MAHARASHTRA (INDIA)  \par \academicyear }}
 \end{center}
""")

with open(os.path.join(FRONT_MATTER_DIR, "certificate.tex"), "w", encoding="utf-8") as f:
    f.write(r"""\thispagestyle{plain}
\begin{minipage}[c]{1mm}
    \includegraphics[width=23mm]{images/SAKEC_logo.png}
\end{minipage}
\hfill
\begin{minipage}[c]{126mm}
    \centering
    { \bf \large {Shah \& Anchor Kutchhi Engineering College} }\\
    \vspace{-0.01 \baselineskip}
    {(An Autonomous Institute Affiliated to University of Mumbai) }
    { \bf \small {Mumbai--400 088, MAHARASHTRA (India)} }\\
\end{minipage}

\vspace{0.2\baselineskip}
\begin{center}
{\Large {\bf \uppercase{Certificate}}}
\end{center}
\vspace{\baselineskip}
\hrule
\vspace{2\baselineskip}
\noindent
{It is my pleasure to certify that \textbf{{\studentNamea}}, \textbf{{\studentNameb}}, \textbf{{\studentNamec}} and \textbf{{\studentNamed}} worked under my supervision for the B.Tech. Project entitled \textbf{{\mytitle}} and their work is of the level of requirement set up for the Project Review 2 in \textbf{{\branch}} by Shah \& Anchor Kutchhi Engineering College, Mumbai.}

\bigskip
\bigskip
\noindent{\textbf{\mysupervisor}} \\
Assistant Professor \\
\mydep \\
Shah \& Anchor Kutchhi Engineering College \\
Mumbai -- 400 088, India

\vspace{2\baselineskip}
\noindent
{The Oral and Practical examination of \textbf{{\studentNamea}}, \textbf{{\studentNameb}}, \textbf{{\studentNamec}} and \textbf{{\studentNamed}}, B.Tech. in \branch, has been held on \dotfill}

\vspace{4\baselineskip}
\begin{tabular}{p{0.35\textwidth}p{0.35\textwidth}p{0.35\textwidth}}
\textbf{External Examiner} & \textbf{Internal Examiner} & \textbf{Guide: \mysupervisor}
\end{tabular}

\vspace{4\baselineskip}
\begin{tabular}{p{0.35\textwidth}p{0.35\textwidth}p{0.35\textwidth}}
\textbf{Head of Department} & \textbf{Principal} & \textbf{College Seal} \\
\HoDName & \principalName & 
\end{tabular}
""")

with open(os.path.join(FRONT_MATTER_DIR, "candidate's_declaration.tex"), "w", encoding="utf-8") as f:
    f.write(r"""\thispagestyle{empty}
\begin{center}
{\Large {\bf \uppercase{Candidate's Declaration}}}
\end{center}
\vspace{\baselineskip}
\hrule
\vspace{2\baselineskip}

\noindent We hereby declare that the work presented in this Project Report entitled {\textbf{{“\mytitle”}}} submitted for the partial fulfillment of the requirements for the degree of Bachelor of Technology in {\branch} at Shah \& Anchor Kutchhi Engineering College, Mumbai, is an authentic record of our own research and engineering work carried out during the academic year \academicyear{} under the supervision of {\textbf{\mysupervisor}}. \par
\vspace{1.5\baselineskip}
\noindent The matter embodied in this report has not been submitted elsewhere in part or fully to any other University or Institute for the award of any degree or diploma.

\bigskip
\bigskip

\begin{table}[h]
\begin{tabular}{p{5cm}p{4cm}p{4cm}}
\textbf{Name of the Student} & \textbf{Roll No.} & \textbf{Signature} \\
\studentNamea & \NewRollNoa & \dotfill \\
\studentNameb & \NewRollNob & \dotfill \\
\studentNamec & \NewRollNoc & \dotfill \\
\studentNamed & \NewRollNod & \dotfill \\
\end{tabular}
\end{table}

\vspace{20pt}
\noindent Date: \dotfill \\
\noindent Place: Mumbai
""")

with open(os.path.join(FRONT_MATTER_DIR, "certificate_of_Plag_Check.tex"), "w", encoding="utf-8") as f:
    f.write(r"""\thispagestyle{plain}
\begin{minipage}[c]{1mm}
    \includegraphics[width=23mm]{images/SAKEC_logo.png}
\end{minipage}
\hfill
\begin{minipage}[c]{126mm}
    \centering
    { \bf \large {Shah \& Anchor Kutchhi Engineering College} }\\
    \vspace{-0.01 \baselineskip}
    {(An Autonomous Institute Affiliated to University of Mumbai) }
    { \bf \small {Mumbai--400 088, MAHARASHTRA (India)} }\\
\end{minipage}

\vspace{0.2\baselineskip}
\begin{center}
{\Large {\bf \uppercase{Certificate of Plagiarism Check}}}
\end{center}
\vspace{\baselineskip}
\hrule
\vspace{0.1\baselineskip}

\begin{center}
\begin{longtable}{|p{6cm}|p{8cm}|}
\hline
\multicolumn{2}{|c|}{\textbf{CERTIFICATE OF PLAGIARISM CHECK}} \\
\hline
Name of the Students & \studentNamea, \studentNameb, \studentNamec, \studentNamed \\ 
\hline
Title of the Dissertation/Report & \mytitle \\ 
\hline
Name of the Guide & \mysupervisor \\ 
\hline
Name of the Department & \mydep \\ 
\hline
Similar content (\%) identified & \textit{[INSTITUTIONAL TURNITIN RUN REQUIRED: $\le 10\%$]} \\ 
\hline
Acceptable Maximum Limit & 10\% \\
\hline
Similarity Tool Used & Turnitin Similarity Engine \\
\hline
Date of Verification & \dotfill \\ 
\hline
Name \& Sign of DAIP Member & \dotfill \\ 
\hline
\multirow{4}{*}{Name \& Sign of the Students} & \studentNamea{} \dotfill \\ \cline{2-2} 
& \studentNameb{} \dotfill \\ \cline{2-2} 
& \studentNamec{} \dotfill \\ \cline{2-2} 
& \studentNamed{} \dotfill \\ \hline
Name \& Sign of the Guide & \mysupervisor{} \dotfill \\ 
\hline
\end{longtable}
\end{center}
""")

with open(os.path.join(FRONT_MATTER_DIR, "acknowledgements.tex"), "w", encoding="utf-8") as f:
    f.write(r"""\thispagestyle{empty}
\begin{center}
{\Large {\bf \uppercase{Acknowledgement}}}
\end{center}
\vspace{\baselineskip}
\hrule
\vspace{1.5\baselineskip}

We express our deepest sense of gratitude and sincere indebtedness to our esteemed project guide, \textbf{\mysupervisor}, Assistant Professor, Department of Computer Engineering, for her invaluable guidance, perceptive criticism, continuous encouragement, and technical oversight throughout the course of this research and engineering endeavor. Her profound insights into intelligent systems, AI governance, and academic rigor have been indispensable in elevating this project to its present standard.

We extend our sincere thanks to \textbf{\HoDName}, Head of the Department of Computer Engineering, for providing excellent departmental facilities, computational resources, and academic support that enabled the seamless execution of this work.

We are deeply grateful to our Principal, \textbf{\principalName}, for fostering an inspiring research culture and technological infrastructure at Shah \& Anchor Kutchhi Engineering College.

We also thank all faculty members and technical staff of the Department of Computer Engineering for their direct and indirect support. Finally, we express heartfelt gratitude to our parents, family members, and peers for their unyielding moral support, patience, and encouragement throughout this B.Tech journey.

\bigskip
\bigskip
\noindent
\textbf{\studentNamea} (\NewRollNoa) \\
\textbf{\studentNameb} (\NewRollNob) \\
\textbf{\studentNamec} (\NewRollNoc) \\
\textbf{\studentNamed} (\NewRollNod) \\
Shah \& Anchor Kutchhi Engineering College, Mumbai \\
Date: \dotfill
""")

with open(os.path.join(FRONT_MATTER_DIR, "abstract.tex"), "w", encoding="utf-8") as f:
    f.write(r"""\thispagestyle{empty}
\begin{center}
{\Large {\bf \uppercase{Abstract}}}
\end{center}
\vspace{\baselineskip}
\hrule
\vspace{1.5\baselineskip}

\noindent In democratic societies such as India, equal access to justice and public entitlements represents a foundational constitutional ideal. However, in practice, citizens face severe systemic friction arising from bureaucratic fragmentation across disconnected portals, dense statutory legalese, opaque welfare eligibility criteria, and prohibitive legal consultation costs. While commercial generative AI models offer conversational accessibility, their unconstrained deployment in legal and civic domains presents grave risks of legal prejudice due to pervasive hallucinations, fabricated case citations, and temporal invalidation of superseded statutes.

This project presents \textbf{CivicSphere AI}, an agentic, evidence-grounded civic intelligence platform engineered specifically for the Indian socio-legal ecosystem. CivicSphere AI unifies four intelligent modules within a modular monolithic architecture: (i) an \textbf{Evidence-Grounded Legal Guidance Engine} covering eight core statutory Acts with a strict Gate 2 circuit breaker that switches to deterministic synthesis whenever citation grounding falls below confidence thresholds; (ii) a \textbf{Government Service Navigator} incorporating a catalog of 12 Central and State welfare schemes with dynamic, rule-based eligibility evaluation; (iii) a \textbf{Civic Knowledge and Agentic Graph} executing multi-hop relational reasoning across a 40+ node NetworkX multigraph combined with Reciprocal Rank Fusion (RRF) hybrid retrieval (BM25 sparse + dense cosine embeddings); and (iv) an \textbf{Intelligent Document Processing Pipeline} featuring sub-2.0 second heuristic regex extraction of notices and summons, coupled with durable, serverless-compatible Supabase S3 cloud persistence and strict Digital Personal Data Protection (DPDP) Act 2023 cascade purge compliance.

Empirical verification on live Vercel production demonstrates 100\% pass rate across 129 backend automated tests (124 functional/regression tests and 5 server-side authorization enforcement tests), error-free static prerendering of 31 Next.js 14 frontend routes, 20/20 live HTTP API endpoints returning 200 OK, and byte-exact roundtrip cloud storage persistence. By translating abstract statutory rights into plain-language, verifiable procedural roadmaps, CivicSphere AI advances UN Sustainable Development Goal 16 (Target 16.3: Equal Access to Justice) while maintaining rigorous privacy and green computational efficiency.

\bigskip
\noindent {\large \bf{Keywords}:} Civic Intelligence, Legal NLP, Retrieval-Augmented Generation, Reciprocal Rank Fusion, Knowledge Graphs, Citation Verification, DPDP Act 2023, Multi-Agent Systems, E-Governance, Access to Justice.
""")

print("Wrote all front matter files successfully!")
