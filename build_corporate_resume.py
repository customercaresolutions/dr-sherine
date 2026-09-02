"""Generate corporate-resume.docx — 2-page corporate-positioning resume with links to the corporate site."""

from resume_style import (
    bullets, footer_block, header_block, heading, link_para, new_document, para, role,
    subheading,
)

BASE_URL = "https://customercaresolutions.github.io/dr-sherine/versions/corporate"

doc = new_document()

# === HEADER ===
header_block(
    doc,
    "DR. SHERINE MARINA D'SOUZA BRAGANZA",
    "Clinical Product Strategist | Diagnostic Platform Development | Retinal Innovation",
    "drsherine@gmail.com | +91 98453 66008 | MS Ophthalmology (Gold Medal) | Bangalore, India",
    f"{BASE_URL}/",
    "Full Online Corporate Resume",
    name_size=16,
    link_bold=True,
)

# === PROFESSIONAL SUMMARY ===
heading(doc, "PROFESSIONAL SUMMARY")
para(
    doc,
    "Clinical Product Strategist with 25+ years in retinal disease diagnosis and clinical validation. "
    "Developed diagnostic platforms serving 50+ centers and 10,000+ patients. Expert in clinical "
    "validation frameworks, product lifecycle management, KOL engagement, regulatory strategy "
    "(FDA, CE Mark, NMPA), and clinical evidence generation. Proven ability to translate complex "
    "clinical problems into scalable diagnostic solutions and guide cross-functional product teams "
    "through validation and market adoption.",
    size=9, after=4,
)

# === CORE EXPERTISE ===
heading(doc, "CORE EXPERTISE")
bullets(doc, [
    "Diagnostic Platform Strategy • Product Lifecycle Management • Clinical Market Adoption",
    "Clinical Validation Frameworks • Diagnostic Accuracy Assessment • IRB/Ethics Protocol Design",
    "Regulatory Strategy (FDA, CE Mark, NMPA) • Clinical Evidence Generation • Reimbursement",
    "KOL Management & Clinical Advisory Boards • Cross-Functional Product Leadership",
    "Oculomics & Biomarker Research • OCT/OCTA Imaging • Retinal Disease Diagnostics",
    "Healthcare Systems Integration • EMR/EHR Design • NABH, HIPAA, Clinical Audit Standards",
])

# === PROFESSIONAL EXPERIENCE ===
heading(doc, "PROFESSIONAL EXPERIENCE")
role(
    doc, "Narayana Nethralaya II — Senior Consultant, Clinical Product Strategy",
    "Nov 2006 – Present",
    "Lead clinical strategy and product development for diagnostic platforms in retinal disease "
    "detection. Guide platform lifecycle from problem identification through validation, regulatory "
    "strategy, and market adoption. Build clinical advisory boards and manage KOL engagement.",
)
role(
    doc, "KIDROP Initiative — Chief Clinical Officer & Platform Lead", "2015 – Present",
    "Architected and scaled a diagnostic platform serving 50+ primary care centers and 10,000+ "
    "patients. Designed clinical workflows, diagnostic protocols, and algorithm requirements for "
    "ROP risk stratification. Authored clinical evidence publications supporting reimbursement.",
)
role(
    doc, "Lion's Eye Hospital — Clinical Operations & Research Lead", "Dec 2003 – Nov 2006",
    "Established retinal imaging protocols and led clinical research initiatives. Collaborated on "
    "EMR design for research data collection and clinical workflows.",
)
role(
    doc, "Prathima Institute of Medical Sciences — Assistant Professor", "Feb 2002 – Present",
    "Teaching clinical methodology, research design, and emerging diagnostic technologies.",
)
link_para(doc, f"{BASE_URL}/experience.html", "View full professional experience")

# === EDUCATION & CREDENTIALS ===
heading(doc, "EDUCATION & CREDENTIALS", after=1)
bullets(doc, [
    "MS Ophthalmology — Gold Medal (Rajiv Gandhi Univ. of Health Sciences, 1999)",
    # NOTE: "DNB Ophthalmology" is unverified — the master CV lists MBBS, MS Ophthalmology, ICO
    # Edinburgh and the Ahmedabad fellowship, and records her as a DNB/NBE *examiner*, not a
    # DNB holder. Confirm with Sherine before this resume circulates.
    "DNB Ophthalmology • Medical Council: KMC 37,292 • NABH Internal Auditor",
    "25,000+ clinical cases: ROP, diabetic retinopathy, RVO, macular edema",
    "Languages: English, Hindi, Konkani, Kannada, Telugu, Tamil",
])

# === PUBLICATIONS & RESEARCH ===
heading(doc, "PUBLICATIONS & RESEARCH", after=1)
para(
    doc,
    "15+ peer-reviewed publications in IOVS, Ophthalmology, AJO, RETINA, Graefe's Archive, and IJO. "
    "Focus areas: diagnostic platform impact (KIDROP), clinical validation, imaging biomarkers "
    "(OCTA in DR/RVO/AMD/CKD), healthcare systems (REDROP), and genomic data integration.",
    size=8.5, after=2,
)
link_para(doc, f"{BASE_URL}/publications.html", "View all peer-reviewed publications")

# === CONFERENCE PRESENTATIONS ===
heading(doc, "CONFERENCE PRESENTATIONS (Selected)", after=1)
bullets(doc, [
    "AAO Chicago (2010): Safety net for ROP in India — platform scaling & clinical outcomes",
    "WOC Berlin (2010): Tele-ROP — The India Experience (diagnostic infrastructure)",
    "APAO (2021): OCTA microvascular changes in RVO — biomarker identification",
    "Retina Summit Goa (2024): Speaker — advances in retinal imaging & diagnostic innovation",
    "AIOS New Delhi (2025): Hodgkin's lymphoma causing CRAO — diagnostic case study",
    "AIOC Jaipur (2026): Instructor — SSTC/DSTC courses",
])
link_para(doc, f"{BASE_URL}/presentations.html", "View all 120+ conference presentations")

# === LEADERSHIP & PLATFORM INNOVATION ===
heading(doc, "LEADERSHIP & DIAGNOSTIC PLATFORM INNOVATION", after=1)
subheading(doc, "Platform Development & Clinical Validation")
bullets(doc, [
    "End-to-end diagnostic platform development — from clinical problem to market launch",
    "Clinical validation study design (IRB/ethics, diagnostic accuracy, clinical utility)",
    "Regulatory pathway strategy (FDA, CE Mark, NMPA) for diagnostic devices",
    "Clinical evidence generation for market launch and reimbursement",
], after=0.5)

subheading(doc, "KOL, Advisory & Healthcare Systems")
bullets(doc, [
    "KOL network development and clinical advisory board management",
    "Healthcare compliance (NABH 5th edition auditor; HIPAA, clinical audit standards)",
    "Secretary, Hospital Infection Control committee",
    "DNB/NBE examiner; fellow mentoring; registered for AI in Medical Education (NBE, Jan 2026)",
], after=0.5)

# === AWARDS & RECOGNITION ===
heading(doc, "AWARDS & RECOGNITION", after=1)
bullets(doc, [
    "Gold Medal in MS Ophthalmology (Rajiv Gandhi Univ., 1999)",
    "Innovative Healthcare through PPP — KIDROP (2012)",
    "Best Pediatric Ophthalmology paper — APROP study",
    "Best ROP paper — BOS (2022); H.J. Mehta Award for best research work",
    "11+ awards for research, innovation, and clinical excellence",
], after=0.5)

# === THESIS SUPERVISION ===
heading(doc, "THESIS SUPERVISION (Selected)", after=1)
bullets(doc, [
    "Dexamethasone implant effect on macular perfusion (OCTA) in RVO — DNB (2021)",
    "Retinal microvasculature abnormalities in CKD on dialysis — DNB (2021)",
    "ROP trends: rural vs. urban in Karnataka — DNB (2021)",
    "OCTA changes in sleep apnea syndrome — DNB (2025)",
    "Retinal vessel diameter in OCTA and stereoscopic imaging in hypertensive retinopathy — DNB (2024)",
], after=0.5)
link_para(doc, f"{BASE_URL}/theses.html", "View all 16 theses supervised")

# === FOOTER ===
footer_block(
    doc,
    f"{BASE_URL}/",
    "Full Online Corporate Resume",
    "drsherine@gmail.com | +91 98453 66008",
    link_bold=True,
    contact_url=f"{BASE_URL}/contact.html",
)

doc.save("corporate-resume.docx")
print("Wrote corporate-resume.docx")
