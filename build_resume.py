"""Generate resume.docx — 2-page clinical resume with links to the clinical site."""

from resume_style import (
    bullets, footer_block, header_block, heading, link_para, new_document, para, role,
    subheading,
)

BASE_URL = "https://customercaresolutions.github.io/dr-sherine/versions/current"

doc = new_document()

# === HEADER ===
header_block(
    doc,
    "DR. SHERINE MARINA D'SOUZA BRAGANZA",
    "Senior Consultant & Head, Vitreoretinal Services | Narayana Nethralaya II",
    "drsherine@gmail.com | +91 98453 66008 | KMC: 37,292",
    f"{BASE_URL}/",
    "Full Online Resume",
)

# === PROFESSIONAL SUMMARY ===
heading(doc, "PROFESSIONAL SUMMARY")
para(
    doc,
    "25+ years in surgical retina and ROP. Expert in complex VR surgery, ROP treatment, "
    "tele-ophthalmology, EMR design, infection control, and AI-driven healthcare. Strong "
    "background in postgraduate teaching and clinical research.",
    size=9, after=4,
)

# === CORE EXPERTISE ===
heading(doc, "CORE EXPERTISE")
bullets(doc, [
    "Complex VR surgery (RD, VH, complicated detachments) • ROP screening & laser treatment",
    "Medical retina: FA/ICG, OCT/OCTA, ultrasonography • Tele-ophthalmology (KIDROP)",
    "AI & data science in ophthalmology • EMR design & health system innovation",
    "Postgraduate teaching & DNB/NBE examining • Hospital infection control & NABH auditing",
])

# === CLINICAL EXPERIENCE ===
heading(doc, "CLINICAL EXPERIENCE")
bullets(doc, [
    "Advanced vitreoretinal surgery — scleral buckling, vitrectomy (including 23g), complex and "
    "complicated retinal detachments, vitreous haemorrhage, and pars plana lensectomy with "
    "scleral-fixated IOL",
    "Paediatric retina surgery, including management of complex paediatric vitreoretinal pathology",
    "Retinopathy of prematurity — screening, treatment, laser photocoagulation and cryotherapy in "
    "newborns, including Zone-I and aggressive posterior ROP (APROP)",
])

# === PROFESSIONAL EXPERIENCE ===
heading(doc, "PROFESSIONAL EXPERIENCE")
role(
    doc, "Narayana Nethralaya — Vitreoretinal Surgeon", "Nov 2006 – Present",
    "Head of VR services (NN2). Complex retinal detachments, ROP screening/treatment, advanced "
    "imaging. Training fellows.",
)
role(
    doc, "Lion's Eye Hospital — Consultant VR Surgeon", "Dec 2003 – Nov 2006",
    "Retinal detachment surgeries, vitrectomies, medical retina with lasers.",
)
role(
    doc, "Prathima Institute — Assistant Professor", "Feb 2002 – Present",
    "Teaching and clinical duties in tertiary care (MCI recognized).",
)

# === EDUCATION & CREDENTIALS ===
heading(doc, "EDUCATION & CREDENTIALS")
bullets(doc, [
    "MS Ophthalmology — Gold Medal (Rajiv Gandhi Univ. of Health Sciences, 1999)",
    "Fellowship in Retina & Vitreous — Retina Foundation, Ahmedabad • International Council of "
    "Ophthalmology, Edinburgh",
    "Medical Council: KMC 37,292 • DNB/NBE examiner • NABH Internal Auditor",
    "Languages: English, Hindi, Konkani, Kannada, Telugu, Tamil",
])

# === PUBLICATIONS & RESEARCH ===
heading(doc, "PUBLICATIONS & RESEARCH", after=1)
para(
    doc,
    "15+ peer-reviewed publications (IOVS, Ophthalmology, AJO, RETINA, Graefe's). ROP, OCTA, "
    "genetic counseling, tele-ophthalmology.",
    size=8.5, after=2,
)
link_para(doc, f"{BASE_URL}/publications.html", "View all peer-reviewed publications")

# === CONFERENCE PRESENTATIONS ===
heading(doc, "CONFERENCE PRESENTATIONS (Selected)", after=1)
bullets(doc, [
    "AAO Chicago (2010): ROP safety net in India",
    "WOC Berlin (2010): Tele-ROP: India Experience",
    "APAO (2021): OCTA changes in RVO",
    "AIOS New Delhi (2025): Hodgkin's lymphoma causing CRAO",
    "Retina Summit Goa (2024): Speaker",
    "AIOS Jaipur (2026): Instructor — SSTC/DSTC courses",
    "AIOC Ahmedabad (March 2027): “The fluid that was not meant to be”",
    "“Multiple peripapillary membranes in Vogt-Koyanagi-Harada syndrome”",
    "“Foveal herniation in a child presenting with high myopia and nystagmus”",
])
link_para(doc, f"{BASE_URL}/presentations.html", "View all 120+ conference presentations", after=4)

para(doc)

# === LEADERSHIP & SERVICE ===
heading(doc, "LEADERSHIP & SERVICE")
subheading(doc, "Hospital Infection Control & NABH")
bullets(doc, [
    "NABH internal auditor; inter-departmental audits",
    "Secretary, Hospital Infection Control (HIC) committee",
    "Retina department clinical audits and KPI reporting",
    "HIC manual aligned to NABH 5th edition standards",
], after=0.5)
subheading(doc, "Teaching & Examining")
bullets(doc, [
    "DNB/NBE examiner and assessor",
    "Fellow mentoring in VR surgery",
    "Instruction courses: DME, ROP, laser/indirect ophthalmoscopy",
    "Registered for AI in Medical Education (NBE, Jan 2026)",
], after=0.5)

# === AWARDS & RECOGNITION ===
heading(doc, "AWARDS & RECOGNITION", after=1)
para(doc, "Academic Awards", style="List Bullet", size=9, bold=True, after=0.5)
for item in [
    "Gold Medal in MS Ophthalmology (Rajiv Gandhi Univ., 1999)",
    "Best PG Paper Award (KOS, 1998)",
    "H.J. Mehta Award — best research work",
]:
    para(doc, item, size=8.5, after=0.5)
para(doc, "Professional Awards", style="List Bullet", size=9, bold=True, after=0.5)
for item in [
    "Best Pediatric Ophthalmology paper — APROP study",
    "Innovative healthcare through PPP (KIDROP, 2012)",
    "Best poster — KOS 2018 (Terson syndrome)",
    "Best ROP paper — BOS 2022",
]:
    para(doc, item, size=8.5, after=0.5)
link_para(doc, f"{BASE_URL}/awards.html", "View all 11 awards & recognition")

# === THESIS SUPERVISION ===
heading(doc, "THESIS SUPERVISION (Selected)", after=1)
bullets(doc, [
    "ROP spectrum and treatment — DNB (2011)",
    "Dexamethasone implant effect on macular perfusion (OCTA) in RVO — DNB (2021)",
    "Retinal microvasculature abnormalities in CKD on dialysis — DNB (2021)",
    "ROP trends: rural vs. urban in Karnataka — DNB (2021)",
    "OCTA changes in sleep apnea syndrome — DNB (2025)",
], after=0.5)
link_para(doc, f"{BASE_URL}/theses.html", "View all 18 theses supervised")

# === INSTRUCTION COURSES ===
heading(doc, "INSTRUCTION COURSES", after=1)
bullets(doc, [
    "Management of diabetic macular edema — Co-instructor",
    "ROP: Update for general ophthalmologist — Co-instructor",
    "Hands-on indirect ophthalmoscopy and retinal lasers — TRUE-D (2014)",
    "ROP instruction course — KOS (2010)",
    "Anti-VEGF's in DME — KOS (2010)",
    "PG update courses (2018–2019)",
], after=0.5)
link_para(doc, f"{BASE_URL}/courses.html", "View full instruction courses & workshops", after=4)

# === FOOTER ===
footer_block(doc, f"{BASE_URL}/", "Full Online Resume", "drsherine@gmail.com | +91 98453 66008")

doc.save("resume.docx")
print("Wrote resume.docx")
