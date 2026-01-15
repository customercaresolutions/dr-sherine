(function(){
  const yearEl = document.getElementById('year');
  if(yearEl) yearEl.textContent = new Date().getFullYear();

  // Mobile nav
  const toggle = document.querySelector('.nav-toggle');
  const menu = document.getElementById('navMenu');
  if(toggle && menu){
    toggle.addEventListener('click', () => {
      const open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    // close on click
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      menu.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }));
  }

  // Print button
  const printBtn = document.getElementById('printBtn');
  if(printBtn) printBtn.addEventListener('click', () => window.print());

  // Expand/collapse all accordions
  const acc = document.getElementById('researchAccordion');
  document.querySelectorAll('[data-expand="all"]').forEach(btn => {
    btn.addEventListener('click', () => acc?.querySelectorAll('details').forEach(d => d.open = true));
  });
  document.querySelectorAll('[data-collapse="all"]').forEach(btn => {
    btn.addEventListener('click', () => acc?.querySelectorAll('details').forEach(d => d.open = false));
  });

  // Search filter
  const searchBox = document.getElementById('searchBox');
  const searchableLists = ['publications','presentations','theses']
    .map(id => document.getElementById(id))
    .filter(Boolean);

  function normalize(s){ return (s || '').toLowerCase().trim(); }

  function filter(){
    const q = normalize(searchBox?.value);
    let hits = 0;

    searchableLists.forEach(list => {
      [...list.querySelectorAll('li')].forEach(li => {
        const hay = normalize(li.textContent + ' ' + (li.getAttribute('data-tags') || ''));
        const show = !q || hay.includes(q);
        li.style.display = show ? '' : 'none';
        if(show) hits++;
      });
    });

    // If user is searching, auto-open the accordion panels
    if(q && acc){
      acc.querySelectorAll('details').forEach(d => d.open = true);
    }

    const note = document.querySelector('.note');
    if(note){
      note.textContent = q
        ? `Showing ${hits} matching item(s). Clear search to show everything.`
        : 'For a comprehensive list, see the full CV.';
    }
  }

  if(searchBox){
    searchBox.addEventListener('input', filter);
  }

  // Contact form: mailto compose
  const form = document.getElementById('contactForm');
  const noteEl = document.getElementById('formNote');
  function setNote(msg){ if(noteEl) noteEl.textContent = msg || ''; }

  if(form){
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('fName')?.value?.trim();
      const email = document.getElementById('fEmail')?.value?.trim();
      const msg = document.getElementById('fMsg')?.value?.trim();

      if(!name || !email || !msg){
        setNote('Please complete all fields.');
        return;
      }
      const subject = encodeURIComponent(`Website inquiry from ${name}`);
      const body = encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\nMessage:\n${msg}\n`);
      window.location.href = `mailto:drsherine@gmail.com?subject=${subject}&body=${body}`;
      setNote('Opening your email client…');
    });
  }
})();