"""Generate ocular-gene-therapy-resume.docx — 2-page resume tailored for ocular gene therapy & inherited retinal disorder companies, with links to the supporting site."""

from resume_style import (
    bullets, footer_block, header_block, heading, link_para, new_document, para, role,
    subheading,
)

BASE_URL = "https://customercaresolutions.github.io/dr-sherine/versions/ocular-gene-therapy"

doc = new_document()

# === HEADER ===
header_block(
    doc,
    "DR. SHERINE MARINA D'SOUZA BRAGANZA",
    "Vitreoretinal Surgeon | Inherited Retinal Disorders | Ocular Gene Therapy Readiness | Medical Retina",
    "drsherine@gmail.com | +91 98453 66008 | MS Ophthalmology (Gold Medal) | Bangalore, India",
    f"{BASE_URL}/",
    "Full Online Resume (Ocular Gene Therapy & IRD version)",
    name_size=16,
    link_bold=True,
)

# === PROFESSIONAL SUMMARY ===
heading(doc, "PROFESSIONAL SUMMARY")
para(
    doc,
    "Senior vitreoretinal surgeon and clinical strategist with 25+ years across medical retina, "
    "inherited retinal disorders (IRDs), ROP, and tertiary retinal care. Published on genotype–"
    "phenotype correlation in IRDs and on next-generation sequencing / genetic counseling in ocular "
    "disorders. Helped scale a tele-retina screening network across 50+ centers with 10,000+ patient "
    "records — the same infrastructure used to identify, refer, and follow patients eligible for "
    "advanced retinal therapies. Active physician-educator (16+ supervised DNB theses, 120+ "
    "conference talks, DNB / NBE examiner) with a deep imaging-interpretation footprint (OCT, OCTA, "
    "FAF, FA/ICG, B-scan). The bridge between cutting-edge retinal science and everyday ophthalmic "
    "practice.",
    size=9, after=4,
)

# === CORE EXPERTISE ===
heading(doc, "CORE EXPERTISE")
bullets(doc, [
    "Inherited Retinal Disorders (IRDs) • Genotype–Phenotype Correlation • Genetic Counseling",
    "Retinal Imaging Interpretation • OCT / SD-OCT / SS-OCT • OCT-Angiography • FAF • FA/ICG • B-scan",
    "Patient Identification Pathways • Referral Workflows • Disease Progression Monitoring",
    "Treatment-Center Engagement • Multi-Center Network Activation • Tele-Retina Operations",
    "Medical & Surgical Retina • ROP & Pediatric Retina • DR, RVO, AMD, Macular Edema",
    "KOL Engagement • Clinical Advisory • Physician Education (DNB / NBE examiner)",
])

# === CLINICAL EXPERIENCE ===
heading(doc, "CLINICAL EXPERIENCE")
bullets(doc, [
    "Advanced vitreoretinal surgery — scleral buckling, vitrectomy (including 23g), complex and "
    "complicated retinal detachments, vitreous haemorrhage, and pars plana lensectomy with "
    "scleral-fixated IOL",
    "Paediatric retina surgery, including management of complex paediatric vitreoretinal pathology "
    "in the multidisciplinary setting where IRD candidates are identified and followed",
    "Retinopathy of prematurity — screening, treatment, laser photocoagulation and cryotherapy in "
    "newborns, including Zone-I and aggressive posterior ROP (APROP)",
])

# === WHY THIS PROFILE FITS ===
heading(doc, "ALIGNMENT WITH OCULAR GENE THERAPY & IRD PROGRAMS")
para(
    doc,
    "Ocular gene therapy programs sit at the intersection of "
    "retinal disease, advanced therapeutics, inherited retinal disorders, physician education, and "
    "real-world clinical implementation. These roles call for senior retina specialists who "
    "understand patient identification pathways, retinal imaging interpretation, disease progression, "
    "referral workflows, treatment-center engagement, and how advanced therapies translate into "
    "actual ophthalmic practice. 25+ years in medical retina, ROP, tertiary retinal care, "
    "multidisciplinary teaching, and IRD / genetic-counseling research map directly onto those needs.",
    size=8.5, after=4,
)

# === PROFESSIONAL EXPERIENCE ===
heading(doc, "PROFESSIONAL EXPERIENCE")
role(
    doc, "Narayana Nethralaya II — Senior Consultant & Head, Vitreoretinal Services",
    "Nov 2006 – Present",
    "Tertiary medical and surgical retina in a high-volume superspeciality eye hospital. Workup and "
    "longitudinal management of inherited retinal disorders, retinal vascular and degenerative "
    "disease, ROP, and complex vitreoretinal pathology. Head of VR Services at the NN2 (Health City) "
    "branch. Lead point for international patients in retinal care. Active in the IRD and "
    "genetic-counseling clinical pathway alongside geneticists and paediatricians. Training fellows "
    "and DNB postgraduates.",
)
role(
    doc, "KIDROP Initiative — Senior Clinical Lead", "2008 – Present",
    "Helped scale a tele-retinal screening network across 50+ primary and secondary centers, with "
    "cumulative coverage of 10,000+ patient records. Designed clinical workflows, referral pathways, "
    "imaging protocols, and treatment escalation criteria — the same operational building blocks "
    "that underpin a gene-therapy treatment-center network.",
)
role(
    doc, "Lion's Eye Hospital — Consultant VR Surgeon", "Dec 2003 – Nov 2006",
    "Retinal detachment surgeries, vitrectomy (including 23g), cryopexy, medical retina and lasers, "
    "fluorescein/ICG angiography, B-scan ultrasonography, and OCT.",
)
role(
    doc, "Prathima Institute of Medical Sciences — Assistant Professor", "Feb 2002 – Present",
    "Undergraduate and postgraduate teaching within a tertiary care teaching hospital (MCI "
    "recognized); supervision of research projects and theses.",
)
link_para(doc, f"{BASE_URL}/full-resume.html", "View full professional experience")

# === EDUCATION & CREDENTIALS ===
heading(doc, "EDUCATION & CREDENTIALS", after=1)
bullets(doc, [
    "MS Ophthalmology — Gold Medal (Rajiv Gandhi Univ. of Health Sciences, 1999)",
    "MBBS — St. John's Medical College, Bangalore",
    "Fellowship in Retina & Vitreous — Retina Foundation, Ahmedabad • International Council of "
    "Ophthalmology, Edinburgh",
    "Medical Council: KMC 37,292 • DNB / NBE examiner • NABH Internal Auditor",
    "25,000+ clinical retinal cases: IRDs, ROP, DR, RVO, AMD, macular edema",
    "Languages: English, Hindi, Konkani, Kannada, Telugu, Tamil",
])

# === PUBLICATIONS MOST RELEVANT ===
heading(doc, "PUBLICATIONS — IRD & GENETICS LED", after=1)
bullets(doc, [
    "Inherited retinal disorders — genotype–phenotype correlation in an Indian cohort and "
    "the importance of genetic testing and counseling. Graefe's Archive, January 2023.",
    "Next generation sequencing and genetic counseling in ocular disorders — clinical, genetic, "
    "psychological and cultural dimensions. Indian Journal of Ophthalmology, 2026.",
    "Tele-ophthalmology and preventable childhood blindness: KIDROP experience. 2022.",
    "Clinically undetected macular changes in early ROP on SD-OCT. IOVS, 2011.",
    "Influence of foveal photoreceptor sub-elements on visual acuity in premature infants. IOVS, 2012.",
    "Outcomes of protocol-based management for Zone-I ROP. AJO, 2011.",
    "Spectral-domain OCT — Limitations and advances. Opening chapter, Elsevier \"Textbook and "
    "Atlas on OCT,\" 2013.",
])
link_para(doc, f"{BASE_URL}/publications.html", "View all peer-reviewed publications")

# === CONFERENCE PRESENTATIONS ===
heading(doc, "CONFERENCE PRESENTATIONS (Selected)", after=1)
bullets(doc, [
    "Speaker — Electrophysiology and Applied Clinical Genetics, Bangalore (Feb 2023)",
    "Homozygosity by descent of a foveal hypoplasia gene in an inbred South Indian family — AIOS Delhi (2015)",
    "“Foveal herniation in a child presenting with high myopia and nystagmus”",
    "Juvenile association of nephronophthisis with RP — AIOS Coimbatore (2017); APVRS Seoul (2018)",
    "Effect of consanguinity on retinitis pigmentosa severity — Asia ARVO Singapore (2011)",
    "BEST's vitelliform dystrophy with CNVM on SD-OCT — APAO Hyderabad (2013)",
    "\"Creating a safety net for ROP in India\" — AAO Retina Subspecialty, Chicago (2010)",
    "Speaker — Retina Summit, Goa (Feb 2024); Faculty — Retina Clinix International (2024–2025)",
    "Instructor — SSTC / DSTC courses, AIOC New Delhi (2025); AIOC Jaipur (2026)",
])
link_para(doc, f"{BASE_URL}/presentations.html", "View all 120+ conference presentations")

# === LEADERSHIP, EDUCATION, NETWORK ===
heading(doc, "LEADERSHIP, EDUCATION & NETWORK", after=1)
subheading(doc, "Patient Pathways & Treatment Centers")
bullets(doc, [
    "Multi-center retinal screening across 50+ sites and 10,000+ patient records (KIDROP)",
    "Referral workflow design, clinical protocols, treatment-center activation",
    "Imaging-based patient identification and longitudinal monitoring (OCT, OCTA, FAF)",
], after=0.5)

subheading(doc, "Physician Education & KOL")
bullets(doc, [
    "DNB / NBE examiner (clinical excellence standards in ophthalmology)",
    "16+ supervised DNB theses concentrated in retinal imaging and retinal disease",
    "120+ conference talks; faculty for AAO India Chapter, Retina Summit, Retina Clinix",
    "Hospital Infection Control committee leadership; NABH-aligned clinical governance",
], after=0.5)

# === THESIS SUPERVISION ===
heading(doc, "THESIS SUPERVISION (Selected)", after=1)
bullets(doc, [
    "Dexamethasone implant effect on macular perfusion (OCTA) in RVO — DNB (2021)",
    "Retinal microvasculature in stage-5 CKD on dialysis using SS-OCTA — DNB (2021)",
    "Longitudinal foveal morphology on SD-OCT in preterm infants with/without ROP — DNB (2012)",
    "Retinal vessel diameter in OCTA in hypertensive retinopathy — DNB (2024)",
    "OCTA changes in sleep apnea syndrome — DNB (2025)",
], after=0.5)
link_para(doc, f"{BASE_URL}/theses.html", "View all 16+ theses supervised")

# === AWARDS ===
heading(doc, "AWARDS & RECOGNITION", after=1)
bullets(doc, [
    "Gold Medal in MS Ophthalmology (Rajiv Gandhi Univ., 1999)",
    "Innovative Healthcare through PPP — KIDROP (2012)",
    "Best Pediatric Ophthalmology paper — APROP study",
    "Best ROP paper — BOS (2022); H.J. Mehta Award (best undergraduate research)",
    "11+ awards for research, innovation, and clinical excellence",
], after=0.5)

# === FOOTER ===
footer_block(
    doc,
    f"{BASE_URL}/",
    "Full Online Resume (Ocular Gene Therapy & IRD version)",
    "drsherine@gmail.com | +91 98453 66008",
    link_bold=True,
    contact_url=f"{BASE_URL}/index.html#contact",
)

doc.save("ocular-gene-therapy-resume.docx")
print("Wrote ocular-gene-therapy-resume.docx")
